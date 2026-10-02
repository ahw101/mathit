/* Counts real printed A4 pages by generating a PDF and reading /Type /Page.
   Usage: node tools/pagecount.js                                           */
const puppeteer = require('puppeteer');

const BASE = 'http://127.0.0.1:8080';

function countPages(buf) {
  const s = Buffer.from(buf).toString('latin1');
  const m = s.match(/\/Type\s*\/Pages[^>]*?\/Count\s+(\d+)/);
  if (m) return parseInt(m[1], 10);
  return (s.match(/\/Type\s*\/Page[^s]/g) || []).length;
}

async function pdfPages(page) {
  const buf = await page.pdf({
    format: 'A4', printBackground: true, preferCSSPageSize: true,
  });
  return countPages(buf);
}

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });
  const results = [];

  async function check(label, url, prep) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
    if (prep) await prep(page);
    await new Promise((r) => setTimeout(r, 250));
    const n = await pdfPages(page);
    results.push([label, n]);
    await page.close();
  }

  const setMode = (mode) => (p) =>
    p.evaluate((m) => {
      document.documentElement.classList.remove(
        'print-worksheet', 'print-answers', 'print-both', 'print-set');
      document.documentElement.classList.add('print-' + m);
    }, mode);

  const setCount = (n, mode) => async (p) => {
    await p.evaluate((c) => {
      const S = window.MathIt.Settings;
      S.save(Object.assign(S.load(), { count: c }));
      const sel = document.querySelector('[data-setting="count"]');
      if (sel) { sel.value = String(c); sel.dispatchEvent(new Event('change', { bubbles: true })); }
    }, n);
    await new Promise((r) => setTimeout(r, 400));
    await setMode(mode)(p);
  };

  for (const n of [12, 18, 24, 36, 48, 60]) {
    await check(`practice worksheet count=${n}`, `${BASE}/practice.html`, setCount(n, 'worksheet'));
  }
  await check('practice answers (36)', `${BASE}/practice.html`, setCount(36, 'answers'));
  await check('practice both (36)', `${BASE}/practice.html`, setCount(36, 'both'));

  for (const n of [36, 60]) {
    await check(`tables worksheet count=${n}`, `${BASE}/tables.html`, setCount(n, 'worksheet'));
  }

  for (const f of ['fractions-reference-sheet', 'long-division-reference-sheet',
    'bidmas-reference-sheet', 'times-tables-grid']) {
    await check(`downloads/${f}`, `${BASE}/downloads/${f}.html`);
  }

  // --- the reference sheets are hard-clipped to one page, so also prove that
  // --- nothing actually falls outside the 281 mm content box.
  const BOX = Math.round((281 / 25.4) * 96);
  const clip = [];
  for (const f of ['fractions-reference-sheet', 'long-division-reference-sheet',
    'bidmas-reference-sheet', 'times-tables-grid']) {
    const page = await browser.newPage();
    await page.emulateMediaType('print');
    await page.setViewport({ width: Math.round((194 / 25.4) * 96), height: BOX });
    await page.goto(`${BASE}/downloads/${f}.html`, { waitUntil: 'networkidle0' });
    const lowest = await page.evaluate(() => {
      let low = 0;
      document.querySelectorAll('.sheet *').forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.height > 0 && r.bottom > low) low = r.bottom;
      });
      return Math.round(low);
    });
    clip.push([f, lowest, BOX]);
    await page.close();
  }

  await browser.close();

  let bad = 0;
  console.log('\n  pages  target  page');
  console.log('  ' + '-'.repeat(60));
  for (const [label, n] of results) {
    const target = label.startsWith('practice both') ? 2 : 1;
    const ok = n === target;
    if (!ok) bad++;
    console.log(`  ${String(n).padStart(5)}  ${String(target).padStart(6)}  ${ok ? ' ' : '<<'} ${label}`);
  }
  console.log('\n  headroom  page (content must fit the 281mm box, not just paginate)');
  console.log('  ' + '-'.repeat(60));
  for (const [f, low, box] of clip) {
    const ok = low <= box;
    if (!ok) bad++;
    console.log(`  ${String(box - low).padStart(6)}px  ${ok ? ' ' : '<<'} downloads/${f}`);
  }

  console.log('');
  console.log(bad === 0 ? 'ALL PRINT CHECKS OK' : `${bad} PRINT FAILURE(S)`);
  process.exit(bad === 0 ? 0 : 1);
})().catch((e) => { console.error(e); process.exit(2); });
