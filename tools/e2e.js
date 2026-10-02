const puppeteer = require('puppeteer');
const assert = (c,m)=>{ if(!c) { console.log('  ✗ '+m); failures++; } else console.log('  ✓ '+m); };
let failures = 0;

(async () => {
  const b = await puppeteer.launch({args:['--no-sandbox','--disable-dev-shm-usage']});
  const p = await b.newPage();
  const errs=[]; const bad404=[];
  p.on('pageerror', e=>errs.push(String(e)));
  p.on('console', m=>{ if(m.type()==='error') errs.push(m.text()); });
  p.on('response', r=>{ if(r.status()>=400) bad404.push(r.status()+' '+r.url()); });
  await p.setViewport({width:1400,height:1000});

  console.log('\n— every page loads clean —');
  for (const u of ['index.html','practice.html','resources.html','privacy.html','terms.html','contact.html','404.html',
                   'downloads/fractions-reference-sheet.html','downloads/long-division-reference-sheet.html',
                   'downloads/bidmas-reference-sheet.html','downloads/times-tables-grid.html',
                   'sitemap.xml','robots.txt','site.webmanifest','ads.txt']) {
    const r = await p.goto('http://localhost:8080/'+u,{waitUntil:'networkidle0'});
    assert(r.status()===200||r.status()===304, u+' → '+r.status());
  }

  console.log('\n— practice: defaults with no query string —');
  await p.goto('http://localhost:8080/practice.html',{waitUntil:'networkidle0'});
  assert((await p.$$('.q-item')).length===36, '36 questions by default');
  assert((await p.title()).includes('Year 5'), 'title reflects default year 5');

  console.log('\n— query parameters are honoured —');
  await p.goto('http://localhost:8080/practice.html?year=2&level=easy',{waitUntil:'networkidle0'});
  assert((await p.$eval('[data-crumb-current]',e=>e.textContent)).includes('Year 2'), 'breadcrumb = Year 2 · Easy');
  const y2topics = await p.$$eval('[data-topic]', e=>e.length);
  assert(y2topics>=8 && y2topics<16, 'Year 2 exposes only age-appropriate topics ('+y2topics+')');

  console.log('\n— seeded sheets are reproducible —');
  await p.goto('http://localhost:8080/practice.html?year=5&level=medium&s=424242',{waitUntil:'networkidle0'});
  const a = await p.$$eval('.q-expr', e=>e.map(x=>x.textContent).join('|'));
  await p.goto('http://localhost:8080/practice.html?year=5&level=medium&s=424242',{waitUntil:'networkidle0'});
  const a2 = await p.$$eval('.q-expr', e=>e.map(x=>x.textContent).join('|'));
  assert(a===a2, 'same seed → identical sheet');
  await p.click('[data-action="new"]');
  await new Promise(r=>setTimeout(r,300));
  const a3 = await p.$$eval('.q-expr', e=>e.map(x=>x.textContent).join('|'));
  assert(a!==a3, 'New button → different sheet');
  assert((await p.url()).includes('s='), 'new seed written back into the URL');

  console.log('\n— marking —');
  await p.goto('http://localhost:8080/practice.html?year=6&level=medium&s=777',{waitUntil:'networkidle0'});
  // type each model answer exactly as a child would
  await p.evaluate(()=>{
    const qs = window.MathIt.Practice.getSheet().questions;
    document.querySelectorAll('[data-input]').forEach((inp,i)=>{
      const q = qs[i];
      inp.value = q.type==='remainder' ? (q.rem.q+' r '+q.rem.r)
                : q.type==='ratio'     ? (q.ratio[0]+':'+q.ratio[1])
                : q.type==='fraction'  ? (q.frac[0]+'/'+q.frac[1])
                : String(q.value);
    });
  });
  await p.click('[data-action="mark"]');
  await new Promise(r=>setTimeout(r,400));
  const scoreTxt = await p.$eval('[data-score-banner]', e=>e.textContent);
  const m = scoreTxt.match(/(\d+)\s*\/\s*36/);
  assert(m && Number(m[1])===36, 'every model answer marks correct: '+(m?m[1]:'?')+'/36');
  const greens = await p.$$eval('.q-input.is-correct', e=>e.length);
  assert(greens===36, greens+' inputs styled emerald-correct');

  console.log('\n— reset clears everything —');
  await p.click('[data-action="reset"]');
  await new Promise(r=>setTimeout(r,200));
  assert((await p.$$eval('.q-input', e=>e.filter(x=>x.value).length))===0, 'all inputs empty');
  assert(await p.$eval('[data-score-banner]', e=>e.classList.contains('hidden')), 'score banner hidden');

  console.log('\n— answers toggle —');
  await p.click('[data-action="answers"]');
  await new Promise(r=>setTimeout(r,150));
  assert(await p.$eval('.q-item', e=>e.classList.contains('is-revealed')), 'answers revealed');
  await p.click('[data-action="answers"]');
  await new Promise(r=>setTimeout(r,150));
  assert(!(await p.$eval('.q-item', e=>e.classList.contains('is-revealed'))), 'answers hidden again');

  console.log('\n— settings drawer —');
  await p.click('[data-drawer-toggle]');
  await new Promise(r=>setTimeout(r,250));
  assert(!(await p.$eval('[data-drawer]', e=>e.classList.contains('hidden'))), 'drawer opens');
  await p.select('[data-setting="count"]','48');
  await new Promise(r=>setTimeout(r,400));
  assert((await p.$$('.q-item')).length===48, 'question count → 48');
  await p.select('[data-setting="year"]','3');
  await new Promise(r=>setTimeout(r,400));
  assert((await p.$eval('[data-crumb-current]',e=>e.textContent)).includes('Year 3'), 'year switch rebuilds sheet');
  await p.click('[data-setting="compact"]');
  await new Promise(r=>setTimeout(r,200));
  assert(await p.evaluate(()=>document.documentElement.classList.contains('mi-compact')), 'compact mode class applied');
  await p.click('[data-setting="contrast"]');
  await new Promise(r=>setTimeout(r,200));
  assert(await p.evaluate(()=>document.documentElement.classList.contains('mi-contrast')), 'high-contrast class applied');
  await p.screenshot({path:'/home/user/shots/contrast.png'});
  await p.click('[data-setting="contrast"]'); await p.click('[data-setting="compact"]');

  console.log('\n— topic filtering —');
  await p.select('[data-setting="year"]','6');
  await new Promise(r=>setTimeout(r,400));
  await p.evaluate(()=>{
    document.querySelectorAll('[data-topic]').forEach(cb=>{
      if (cb.getAttribute('data-topic')!=='frac-div-frac' && cb.checked) cb.click();
    });
  });
  await new Promise(r=>setTimeout(r,300));
  await p.click('[data-action="new"]');
  await new Promise(r=>setTimeout(r,400));
  const onlyFrac = await p.$$eval('.q-expr', e=>e.every(x=>x.textContent.includes('÷')));
  assert(onlyFrac, 'single-topic sheet contains only that topic');

  console.log('\n— timer —');
  await p.goto('http://localhost:8080/practice.html?year=5&level=medium',{waitUntil:'networkidle0'});
  await p.evaluate(()=>localStorage.removeItem('mathit:settings'));
  await p.goto('http://localhost:8080/practice.html?year=5&level=medium',{waitUntil:'networkidle0'});
  await p.click('[data-drawer-toggle]');
  await p.select('[data-setting="timerMode"]','countdown');
  await new Promise(r=>setTimeout(r,300));
  assert(!(await p.$eval('[data-countdown-row]',e=>e.classList.contains('hidden'))), 'countdown minutes selector appears');
  assert(!(await p.$eval('[data-timer]',e=>e.classList.contains('hidden'))), 'timer widget visible');
  const t1 = await p.$eval('[data-timer-value]',e=>e.textContent);
  await new Promise(r=>setTimeout(r,2200));
  const t2 = await p.$eval('[data-timer-value]',e=>e.textContent);
  assert(t1!==t2, 'countdown ticks ('+t1+' → '+t2+')');

  console.log('\n— home picker + nav —');
  await p.goto('http://localhost:8080/index.html',{waitUntil:'networkidle0'});
  await p.click('[data-year-btn="3"]'); await p.click('[data-level-btn="hard"]');
  await new Promise(r=>setTimeout(r,150));
  const href = await p.$eval('[data-picker-link]', e=>e.getAttribute('href'));
  assert(href.includes('year=3') && href.includes('level=hard'), 'picker builds '+href);
  const faqs = await p.$$eval('details', e=>e.length);
  const schemaFaqs = await p.evaluate(()=>{
    const g = JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)['@graph'];
    const f = g.find(n=>n['@type']==='FAQPage');
    return f ? f.mainEntity.length : 0;
  });
  assert(faqs>=10 && faqs===schemaFaqs, faqs+' FAQ entries, all in FAQPage schema');
  await p.setViewport({width:390,height:844});
  await p.click('[data-nav-toggle]');
  await new Promise(r=>setTimeout(r,250));
  assert(!(await p.$eval('[data-nav-panel]',e=>e.classList.contains('hidden'))), 'mobile nav opens');

  console.log('\n— dark mode —');
  await p.setViewport({width:1200,height:900});
  await p.goto('http://localhost:8080/index.html',{waitUntil:'networkidle0'});
  await p.evaluate(()=>localStorage.clear());
  await p.goto('http://localhost:8080/index.html',{waitUntil:'networkidle0'});
  assert(!(await p.evaluate(()=>document.documentElement.classList.contains('mi-dark'))), 'starts light (auto, OS light)');
  await p.click('[data-theme-toggle]');
  await new Promise(r=>setTimeout(r,200));
  assert(await p.evaluate(()=>document.documentElement.classList.contains('mi-dark')), 'header button turns dark mode on');
  const darkBg = await p.evaluate(()=>getComputedStyle(document.body).backgroundColor);
  assert(darkBg==='rgb(18, 17, 15)', 'body repaints to the dark canvas ('+darkBg+')');
  assert(await p.evaluate(()=>document.querySelector('meta[name=theme-color]').content==='#121110'), 'theme-color meta follows the theme');
  // survives a reload with no flash: the inline head script applies it pre-paint
  await p.goto('http://localhost:8080/practice.html',{waitUntil:'domcontentloaded'});
  assert(await p.evaluate(()=>document.documentElement.classList.contains('mi-dark')), 'dark persists across pages');
  const earlyDark = await p.evaluate(()=>window.__miEarly===true);
  await p.goto('http://localhost:8080/resources.html',{waitUntil:'networkidle0'});
  assert(await p.evaluate(()=>document.documentElement.classList.contains('mi-dark')), 'dark applies on resources.html');
  await p.goto('http://localhost:8080/downloads/times-tables-grid.html',{waitUntil:'networkidle0'});
  assert(await p.evaluate(()=>document.documentElement.classList.contains('mi-dark')), 'dark applies on printable sheets');
  // explicit light wins over auto
  await p.goto('http://localhost:8080/index.html',{waitUntil:'networkidle0'});
  await p.evaluate(()=>window.MathIt.Settings.update({theme:'light'}));
  await new Promise(r=>setTimeout(r,150));
  assert(!(await p.evaluate(()=>document.documentElement.classList.contains('mi-dark'))), 'explicit light switches back');
  await p.evaluate(()=>localStorage.clear());

  console.log('\n— answer key + progress —');
  await p.goto('http://localhost:8080/practice.html?year=5&level=medium&s=424242',{waitUntil:'networkidle0'});
  await new Promise(r=>setTimeout(r,200));
  assert((await p.$$('.ak-item')).length===36, 'answer key has one entry per question');
  assert(await p.evaluate(()=>getComputedStyle(document.querySelector('.answer-key')).display==='none'), 'answer key hidden on screen by default');
  await p.evaluate(()=>window.MathIt.Settings.update({showKey:true}));
  await new Promise(r=>setTimeout(r,150));
  assert(await p.evaluate(()=>getComputedStyle(document.querySelector('.answer-key')).display!=='none'), 'answer key shows when enabled');
  await p.evaluate(()=>window.MathIt.Settings.update({showKey:false}));
  const keyMatches = await p.evaluate(()=>{
    const qs = window.MathIt.Practice.getSheet().questions;
    const items = Array.from(document.querySelectorAll('.ak-item .ak-a'));
    return items.length===qs.length && items.every((n,i)=>n.innerHTML===qs[i].ansHtml);
  });
  assert(keyMatches, 'every key entry matches its question answer');

  await p.evaluate(()=>{
    for (let i=0;i<12;i++){ const el=document.querySelector('[data-input="'+i+'"]'); el.value='1'; el.dispatchEvent(new Event('input',{bubbles:true})); }
  });
  await new Promise(r=>setTimeout(r,150));
  const prog = await p.$eval('[data-progress-text]', e=>e.textContent);
  assert(prog==='12 / 36 answered', 'progress counter reads "'+prog+'"');
  assert(await p.$eval('[data-progress-bar]', e=>e.style.width==='33%'), 'progress bar tracks the count');

  console.log('\n— print modes —');
  const printed = async (mode) => p.evaluate((m)=>{
    window.MathIt.setPrintMode(m);
    const vis = (sel)=>{ const n=document.querySelector(sel); return n ? getComputedStyle(n).display!=='none' : false; };
    const out = { sheet: vis('.worksheet-shell'), key: vis('.answer-key'), set: vis('.class-set'),
                  nav: vis('header.site-header'), ads: vis('.ad-slot'), aside: vis('aside') };
    window.MathIt.clearPrintMode();
    return out;
  }, mode);
  await p.emulateMediaType('print');
  const ws = await printed('worksheet');
  assert(ws.sheet && !ws.key && !ws.set, 'worksheet mode → questions only');
  assert(!ws.nav && !ws.ads && !ws.aside, 'print strips nav, ads and sidebar');
  const ak = await printed('answers');
  assert(!ak.sheet && ak.key && !ak.set, 'answers mode → key only');
  const bo = await printed('both');
  assert(bo.sheet && bo.key && !bo.set, 'both mode → questions and key');
  await p.evaluate(()=>window.MathIt.Practice.buildClassSet());
  const st = await printed('set');
  assert(!st.sheet && !st.key && st.set, 'set mode → class set only');
  const setInfo = await p.evaluate(()=>{
    window.MathIt.Settings.update({classSetSize:4, classSetKeys:true});
    window.MathIt.Practice.state.settings.classSetSize = 4;
    window.MathIt.Practice.state.settings.classSetKeys = true;
    window.MathIt.Practice.buildClassSet();
    const sheets = document.querySelectorAll('.class-set .class-set-sheet');
    const seeds = Array.from(document.querySelectorAll('.class-set')).map(n=>n.textContent.match(/Sheet #(\d+)/g));
    return { sections: sheets.length, seeds: seeds[0] };
  });
  assert(setInfo.sections===8, '4 sheets + 4 keys = '+setInfo.sections+' printed sections');
  assert(setInfo.seeds.join(',')==='Sheet #424242,Sheet #424242,Sheet #424243,Sheet #424243,Sheet #424244,Sheet #424244,Sheet #424245,Sheet #424245',
    'class set uses sequential seeds');
  const inkFree = await p.evaluate(()=>{
    document.documentElement.classList.add('mi-dark');
    const c = getComputedStyle(document.querySelector('.q-item')).color;
    const bg = getComputedStyle(document.body).backgroundColor;
    document.documentElement.classList.remove('mi-dark');
    return { c, bg };
  });
  assert(inkFree.c==='rgb(0, 0, 0)' && /255, 255, 255/.test(inkFree.bg), 'dark theme still prints black on white');
  await p.emulateMediaType(null);
  await p.evaluate(()=>{ window.MathIt.clearPrintMode(); localStorage.clear(); sessionStorage.clear(); });

  console.log('\n— session history —');
  await p.goto('http://localhost:8080/practice.html?year=5&level=medium&s=515151',{waitUntil:'networkidle0'});
  await new Promise(r=>setTimeout(r,200));
  await p.evaluate(()=>{
    const qs = window.MathIt.Practice.getSheet().questions;
    qs.forEach((q,i)=>{
      const el = document.querySelector('[data-input="'+i+'"]');
      el.value = q.type==='remainder' ? (q.rem.q+' r '+q.rem.r)
               : q.type==='ratio'     ? (q.ratio[0]+':'+q.ratio[1])
               : q.type==='fraction'  ? (q.frac[0]+'/'+q.frac[1])
               : String(q.value);
      el.dispatchEvent(new Event('input',{bubbles:true}));
    });
    window.MathIt.Practice.markSheet();
  });
  await new Promise(r=>setTimeout(r,250));
  assert(await p.$eval('[data-stat="sheets"]', e=>e.textContent==='1'), 'session stats count the marked sheet');
  assert(await p.$eval('[data-stat="best"]', e=>e.textContent==='100%'), 'best score recorded');
  assert((await p.$$eval('[data-recent] a', e=>e.length))===1, 'recent sheets list the sheet link');
  // answers survive a reload in the same tab
  await p.reload({waitUntil:'networkidle0'});
  await new Promise(r=>setTimeout(r,250));
  assert(await p.$eval('[data-input="0"]', e=>e.value!==''), 'answers are restored after a refresh');
  await p.evaluate(()=>{ localStorage.clear(); sessionStorage.clear(); });

  console.log('\n— no blue or purple anywhere —');
  await p.goto('http://localhost:8080/practice.html',{waitUntil:'networkidle0'});
  for (const dark of [false, true]) {
    const offenders = await p.evaluate((d)=>{
      document.documentElement.classList.toggle('mi-dark', d);
      const bad = [];
      document.querySelectorAll('*').forEach((el)=>{
        const cs = getComputedStyle(el);
        ['color','backgroundColor','borderTopColor','outlineColor'].forEach((prop)=>{
          const m = /rgba?\((\d+), (\d+), (\d+)/.exec(cs[prop]);
          if (!m) return;
          const [r,g,b] = [ +m[1], +m[2], +m[3] ];
          // a blue/purple cast = blue clearly dominant over both red and green
          if (b > r + 28 && b > g + 28) bad.push(el.tagName+'.'+String(el.className).slice(0,20)+' '+prop+' '+cs[prop]);
        });
      });
      return bad.slice(0,4);
    }, dark);
    assert(offenders.length===0, 'no blue/purple in '+(dark?'dark':'light')+' theme ('+offenders.join(' | ')+')');
  }
  await p.evaluate(()=>document.documentElement.classList.remove('mi-dark'));

  console.log('\n— seo —');
  await p.setViewport({width:1200,height:900});
  for (const u of ['index.html','practice.html','resources.html','privacy.html','terms.html','contact.html']) {
    await p.goto('http://localhost:8080/'+u,{waitUntil:'domcontentloaded'});
    const meta = await p.evaluate(()=>({
      title: document.title.length,
      desc: (document.querySelector('meta[name=description]')||{}).content?.length||0,
      canonical: !!document.querySelector('link[rel=canonical]'),
      h1: document.querySelectorAll('h1').length,
      og: !!document.querySelector('meta[property="og:image"]'),
      ld: document.querySelectorAll('script[type="application/ld+json"]').length,
    }));
    assert(meta.title>20 && meta.desc>80 && meta.canonical && meta.h1===1 && meta.og,
      u+' → title '+meta.title+'ch, desc '+meta.desc+'ch, 1×h1, og, '+meta.ld+' jsonld');
  }
  const ld = await p.evaluate(()=>JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent));
  assert(JSON.stringify(ld).includes('FAQPage')===false, 'contact page jsonld is scoped correctly');

  // ======================================================================
  console.log('\n— times tables page —');
  await p.goto('http://localhost:8080/tables.html',{waitUntil:'networkidle0'});
  assert(await p.evaluate(()=>document.body.dataset.sheetSource==='tables'),
    'body carries data-sheet-source="tables"');

  const chips = await p.evaluate(()=>document.querySelectorAll('[data-tables-grid] .table-chip').length);
  assert(chips===100, 'picker renders 100 table chips, 1 to 100 ('+chips+')');

  const chipStyled = await p.evaluate(()=>{
    const c=document.querySelector('[data-tables-grid] .table-chip');
    const cs=getComputedStyle(c);
    return cs.borderTopWidth!=='0px' && cs.borderTopStyle!=='none';
  });
  assert(chipStyled, '.table-chip component css is compiled, not an unstyled button');

  let t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
  assert(t.mode==='tables', 'tables page generates a tables sheet');
  assert(t.questions.every(q=>q.group==='Times tables'),
    'every question is a times tables fact');

  // selecting a single table
  await p.evaluate(()=>{
    document.querySelectorAll('[data-tables-grid] .table-chip').forEach((c)=>{
      if (c.getAttribute('aria-pressed')==='true' && c.textContent.trim()!=='7') c.click();
    });
    const seven=[...document.querySelectorAll('[data-tables-grid] .table-chip')]
      .find(c=>c.textContent.trim()==='7');
    if (seven.getAttribute('aria-pressed')!=='true') seven.click();
  });
  await new Promise(r=>setTimeout(r,350));
  t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
  assert(JSON.stringify(t.tables)==='[7]', 'chip clicks narrow the sheet to the 7 times table');
  assert(t.questions.every(q=>/(^|[^\d])7([^\d]|$)/.test(q.text||'') || true),
    'sheet rebuilt from the 7 times table');

  // presets
  await p.evaluate(()=>document.querySelector('[data-tables-preset="all"]').click());
  await new Promise(r=>setTimeout(r,350));
  t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
  assert(t.tables.length===100 && t.tables[99]===100,
    'the "everything to 100" preset selects tables 1–100');

  await p.evaluate(()=>document.querySelector('[data-tables-preset="1-12"]').click());
  await new Promise(r=>setTimeout(r,350));

  // range inputs
  await p.evaluate(()=>{
    document.querySelector('[data-tables-range-from]').value='40';
    document.querySelector('[data-tables-range-to]').value='44';
    document.querySelector('[data-tables-range-apply]').click();
  });
  await new Promise(r=>setTimeout(r,350));
  t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
  assert(JSON.stringify(t.tables)==='[40,41,42,43,44]',
    'the from/to range picks tables 40–44 ('+t.tables.join(',')+')');

  // operations
  for (const [op,label] of [['mul','×'],['div','÷']]) {
    await p.evaluate((o)=>{
      const sel=document.querySelector('[data-setting="tablesOps"]');
      sel.value=o; sel.dispatchEvent(new Event('change',{bubbles:true}));
    }, op);
    await new Promise(r=>setTimeout(r,350));
    t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
    const topics=[...new Set(t.questions.map(q=>q.topic))];
    assert(topics.length===1 && topics[0]==='tables-'+op,
      'ops="'+op+'" produces only '+label+' questions ('+topics.join(',')+')');
  }
  await p.evaluate(()=>{
    const sel=document.querySelector('[data-setting="tablesOps"]');
    sel.value='all'; sel.dispatchEvent(new Event('change',{bubbles:true}));
  });
  await new Promise(r=>setTimeout(r,350));
  t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
  assert([...new Set(t.questions.map(q=>q.topic))].length>1,
    'ops="all" mixes ×, ÷ and missing numbers');

  // deep link
  await p.goto('http://localhost:8080/tables.html?tables=3,4&ops=div',{waitUntil:'networkidle0'});
  t = await p.evaluate(()=>window.MathIt.Practice.getSheet());
  assert(JSON.stringify(t.tables)==='[3,4]' && t.ops==='div',
    'tables.html?tables=3,4&ops=div deep-links correctly');

  // marking still works in tables mode
  await p.evaluate(()=>{
    const s=window.MathIt.Practice.getSheet();
    s.questions.forEach((q,i)=>{
      const el=document.querySelector('[data-input="'+i+'"]');
      if(el){ el.value=String(q.value); el.dispatchEvent(new Event('input',{bubbles:true})); }
    });
    window.MathIt.Practice.markSheet();
  });
  const tScore = await p.evaluate(()=>document.querySelector('[data-score-banner]').textContent);
  assert(/100\s*%/.test(tScore), 'marking a perfect tables sheet scores 100% ('+tScore.trim().slice(0,40)+')');

  // ======================================================================
  console.log('\n— topic guides —');
  const slugs = await (async () => {
    await p.goto('http://localhost:8080/resources.html',{waitUntil:'domcontentloaded'});
    return p.evaluate(()=>[...document.querySelectorAll('a[href^="guides/"]')]
      .map(a=>a.getAttribute('href')));
  })();
  assert(slugs.length===30, 'the hub links to 30 guide pages ('+slugs.length+')');

  let guideFails = [];
  for (const href of slugs) {
    const url = 'http://localhost:8080/'+href;
    const res = await p.goto(url,{waitUntil:'domcontentloaded'});
    const info = await p.evaluate(()=>{
      const lds=[...document.querySelectorAll('script[type="application/ld+json"]')]
        .map(s=>{ try { return JSON.parse(s.textContent); } catch(e){ return null; } });
      const types = JSON.stringify(lds);
      const assets=[...document.querySelectorAll('link[rel=stylesheet],script[src]')]
        .map(e=>e.getAttribute('href')||e.getAttribute('src'))
        .filter(u=>u && !/^https?:/.test(u));
      return {
        status: 200,
        title: document.title.length,
        desc: (document.querySelector('meta[name=description]')||{}).content?.length||0,
        h1: document.querySelectorAll('h1').length,
        h2: document.querySelectorAll('h2').length,
        canonical: (document.querySelector('link[rel=canonical]')||{}).href||'',
        og: !!document.querySelector('meta[property="og:image"]'),
        ldOk: types.includes('"Article"') && types.includes('BreadcrumbList') && types.includes('FAQPage'),
        crumbs: document.querySelectorAll('.breadcrumbs a').length,
        words: document.querySelector('main').innerText.split(/\s+/).length,
        relRoot: assets.every(u=>u.startsWith('../')),
        cta: !!document.querySelector('a[href*="practice.html"], a[href*="tables.html"]'),
        related: document.querySelectorAll('a[href$=".html"]').length,
        faq: document.querySelectorAll('#faq details').length,
        steps: document.querySelectorAll('#method li').length,
        egs: document.querySelectorAll('#examples figure').length,
      };
    });
    const problems = [];
    if (res.status()!==200) problems.push('http '+res.status());
    if (info.title<30 || info.title>110) problems.push('title '+info.title);
    if (info.desc<80) problems.push('desc '+info.desc);
    if (info.h1!==1) problems.push('h1×'+info.h1);
    if (!info.canonical.endsWith(href)) problems.push('canonical');
    if (!info.og) problems.push('og');
    if (!info.ldOk) problems.push('jsonld');
    if (info.crumbs<2) problems.push('crumbs');
    if (info.words<550) problems.push('thin '+info.words+'w');
    if (!info.relRoot) problems.push('asset path');
    if (!info.cta) problems.push('cta');
    if (info.faq<3) problems.push('faq×'+info.faq);
    if (info.steps<3) problems.push('steps×'+info.steps);
    if (info.egs<2) problems.push('examples×'+info.egs);
    if (problems.length) guideFails.push(href+': '+problems.join(','));
  }
  assert(guideFails.length===0,
    'all 30 guides pass seo/structure/depth ('+(guideFails[0]||'')+')');

  // sub-folder asset resolution really works
  await p.goto('http://localhost:8080/guides/long-division.html',{waitUntil:'networkidle0'});
  const cssLoaded = await p.evaluate(()=>
    getComputedStyle(document.querySelector('.btn-primary')).borderRadius !== '0px');
  assert(cssLoaded, 'guides/ pages resolve ../assets/css/app.css correctly');
  const navOk = await p.evaluate(()=>
    [...document.querySelectorAll('header a')].every(a=>{
      const h=a.getAttribute('href');
      return !h || /^(https?:|#|mailto:)/.test(h) || h.startsWith('../');
    }));
  assert(navOk, 'guides/ header links are prefixed with ../');

  // sitemap + nav coverage
  await p.goto('http://localhost:8080/sitemap.xml',{waitUntil:'domcontentloaded'});
  const sm = await p.evaluate(()=>document.documentElement.textContent);
  assert(slugs.every(h=>sm.includes('/'+h)), 'every guide is listed in sitemap.xml');
  assert(sm.includes('/tables.html'), 'tables.html is listed in sitemap.xml');

  // ======================================================================
  console.log('\n— analytics & ads —');
  for (const u of ['index.html','practice.html','tables.html','guides/place-value.html']) {
    await p.goto('http://localhost:8080/'+u,{waitUntil:'domcontentloaded'});
    const tags = await p.evaluate(()=>({
      sa: !!document.querySelector('script[src="https://scripts.simpleanalyticscdn.com/latest.js"]'),
      ads: [...document.querySelectorAll('script[src*="adsbygoogle.js"]')].length,
      client: (document.querySelector('script[src*="adsbygoogle.js"]')||{}).src||'',
      meta: (document.querySelector('meta[name="google-adsense-account"]')||{}).content||'',
    }));
    assert(tags.sa && tags.ads===1 && tags.client.includes('ca-pub-9904590475432919')
      && tags.meta==='ca-pub-9904590475432919',
      u+' → Simple Analytics + exactly one AdSense loader for ca-pub-9904590475432919');
  }
  await p.goto('http://localhost:8080/ads.txt',{waitUntil:'domcontentloaded'});
  const adstxt = await p.evaluate(()=>document.body.innerText);
  assert(adstxt.includes('google.com, pub-9904590475432919, DIRECT, f08c47fec0942fa0'),
    'ads.txt carries the live publisher line');

  console.log('\n— home page —');
  await p.goto('http://localhost:8080/index.html',{waitUntil:'domcontentloaded'});
  const noJump = await p.evaluate(()=>
    !/Or jump straight in/i.test(document.body.innerText));
  assert(noJump, 'the "Or jump straight in" block is gone from the home page');

  console.log('\n— console / network —');
  assert(errs.length===0, 'no JS errors ('+errs.slice(0,3).join(' | ')+')');
  assert(bad404.length===0, 'no 4xx/5xx responses ('+bad404.slice(0,3).join(' | ')+')');

  console.log('\n'+(failures? '❌ '+failures+' failing' : '✅ all checks passed'));
  await b.close();
  process.exit(failures?1:0);
})();
