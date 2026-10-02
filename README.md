# Math It! — mental maths worksheet platform

A production-ready, dependency-free static site that generates unlimited printable
mental-maths worksheets for **Years 2–6** (upper Key Stage 1 and Key Stage 2), built with
**Tailwind CSS** in an earthy neutral palette: warm charcoal, stone, emerald, amber and a
muted clay red. No blue or purple anywhere in the UI, in either theme.

Everything runs client-side. There is no backend, no database, no account system and no
build step required to *serve* the site — only to recompile the CSS or regenerate the HTML.

**Features at a glance**

| | |
|---|---|
| Worksheets | 34 question types, 5 year groups, 3 difficulty levels, 12–60 questions a sheet |
| Marking | Instant per-question marking, score card by topic, reveal-answers toggle |
| Answer keys | On-screen key for marking by hand, or printed on its own page |
| Printing | Questions only · answer key only · both · **class set** of up to 35 different sheets |
| Theming | Light / dark / auto, applied before first paint, plus a high-contrast mode |
| Accessibility | Three text sizes, compact density, full keyboard control, visible focus rings |
| Session | Progress counter, answer autosave, recent sheets and today's averages |
| Monetisation | AdSense-ready slots, `ads.txt`, privacy & terms pages |

---

## 1. What's in the box

```
.
├── index.html                  Home — hero, year/difficulty picker, curriculum,
│                               pedagogy, parent & teacher tips, 10-question FAQ
├── practice.html               Worksheet generator (?year=X&level=Y&config=…&s=SEED)
├── tables.html                 Times tables drill (?tables=3,7&ops=div&s=SEED) —
│                               any tables from 1 to 100, × ÷ and missing numbers
├── resources.html              Guide hub: all 30 topic guides by category,
│                               plus printables + glossary
├── privacy.html                UK GDPR / AdSense-ready privacy & cookie notice
├── terms.html                  Terms of use incl. the free classroom copying licence
├── contact.html                Contact page with a no-server (mailto) form
├── 404.html                    Friendly not-found page
│
├── guides/                     30 topic guides, one page each
│   ├── place-value.html …      Number & place value (5)
│   ├── column-addition.html …  Calculating (7)
│   ├── mental-strategies.html… Mental maths (2)
│   ├── fractions-explained.html… Fractions (7)
│   ├── decimals-explained.html…  Decimals & percentages (5)
│   └── ratio-and-proportion.html… Ratio, algebra & measures (4)
│
├── downloads/                  Four printable A4 reference sheets (1 page each)
│   ├── fractions-reference-sheet.html
│   ├── long-division-reference-sheet.html
│   ├── bidmas-reference-sheet.html
│   └── times-tables-grid.html
│
├── assets/
│   ├── css/app.css             ← compiled Tailwind (the only stylesheet)
│   ├── img/                    og-image, app icons
│   └── js/
│       ├── ads.js              ★ ADSENSE CONFIG — the only file you edit to monetise
│       ├── settings.js         Settings store: localStorage + URL + theme/modes
│       ├── generator.js        The question engine (34 topics, 5 years, 3 tiers)
│       ├── practice.js         Worksheet lifecycle: build, mark, reveal, time,
│       │                       answer key, class sets, history, print.
│       │                       Dual-mode — drives practice.html AND tables.html
│       └── site.js             Nav, theme, print modes, home picker, contact form
│
├── src/app.src.css             Tailwind source (edit this, not assets/css/app.css)
├── tailwind.config.js          Palette + design tokens
├── tools/                      Build & test scripts (not deployed)
│   ├── build.py                Regenerates every HTML page from one shared shell
│   ├── shell.py                <head>, header, footer, ad-slot helper
│   ├── content_*.py            Page content (home, practice, tables, guides,
│   │                           resources, legal, downloads)
│   ├── guides_*.py             The 30 guides as data + the shared renderer
│   ├── e2e.js                  Puppeteer end-to-end test suite
│   └── pagecount.js            Proves every worksheet and printable is 1 page
│
├── netlify.toml  vercel.json  _headers  _redirects  .nojekyll   ← host configs
├── sitemap.xml   robots.txt   ads.txt   site.webmanifest   favicon.ico
└── package.json
```

---

## 2. Running it

It is a plain static site — any web server will do.

```bash
python3 -m http.server 8080      # then open http://localhost:8080
# or
npx serve .
```

### Rebuilding

```bash
npm install                       # installs tailwindcss only
npm run build                     # CSS + HTML
npm run build:css                 # Tailwind → assets/css/app.css
npm run watch:css                 # recompile on save
npm run build:html                # python3 tools/build.py
```

Edit page copy in `tools/content_*.py` and the shared chrome in `tools/shell.py`, then
run `npm run build:html`. Never hand-edit the generated `*.html` files — they will be
overwritten.

### Testing

```bash
npm i -D puppeteer                # not a runtime dependency; test-only
npm run serve &                   # the suite drives a real browser against :8080
npm test                          # 105 end-to-end assertions
npm run test:print                # real PDF page counts — every sheet must be 1 page
```

The suite checks that every page returns 200; that worksheets build, mark and reproduce
from a seed; that the settings drawer, topic filters and timer work; that dark mode
applies before paint and survives navigation; that every print mode shows the right
sections and still prints black on white from a dark screen; that class sets use
sequential seeds; that progress, answer autosave and session history behave; that **no
computed colour anywhere resolves to blue or purple in either theme**; and that every
page has a unique title, description, canonical, single `h1`, Open Graph image and
JSON-LD block.

It also covers the times tables page end to end (the 1–100 chip picker, the five
presets, the from/to range, all five question types, deep links and marking), and walks
**all 30 guide pages** asserting status, title and description length, a single `h1`,
breadcrumbs, `../`-prefixed asset paths, a practice CTA, at least 550 words, three FAQ
entries, three method steps, two worked examples, and Article + BreadcrumbList +
FAQPage JSON-LD. Finally it verifies the Simple Analytics tag, exactly one AdSense
loader carrying the live publisher ID, and `ads.txt`.

`npm run test:print` is separate because it renders real PDFs. It asserts a one-page
count for worksheets at 12/18/24/36/48/60 questions on both generators, for the answer
key, and for all four reference sheets — then re-measures the sheets to prove the
one-page clamp is not silently cropping anything.

---

## 3. Turning on Google AdSense

The account is already wired in. `tools/shell.py` puts the loader script and the
`google-adsense-account` meta tag in the `<head>` of every page for
**`ca-pub-9904590475432919`**, and `ads.txt` carries the matching authorised-seller
line. Because the shell injects the loader, `assets/js/ads.js` has `loadScript: false`
— do not set it back to `true` or the script loads twice.

**The remaining work lives in one file: `assets/js/ads.js`.**

1. Get approved at [adsense.google.com](https://adsense.google.com) and create your ad units.
2. Open `assets/js/ads.js` and set `enabled: true` plus your real slot IDs:

```js
enabled: true,
publisherId: 'ca-pub-9904590475432919',   // already set
slots: {
  'home-leaderboard':        '1234567890',
  'home-infeed':             '2345678901',
  'practice-sidebar-top':    '3456789012',
  'practice-sidebar-bottom': '4567890123',
  'practice-footer':         '5678901234',
  'resources-inarticle':     '6789012345',
  'resources-sidebar':       '7890123456',
  'generic':                 '',
}
```

3. Put the same publisher ID in `/ads.txt` (uncomment the line and replace the zeros).

That's it. The runtime injects the `adsbygoogle.js` loader, adds the
`google-adsense-account` verification meta tag, builds each `<ins class="adsbygoogle">`
and calls `push({})` for you.

**Prefer to paste Google's raw snippet?** Any slot accepts it verbatim:

```js
'practice-sidebar-top': {
  customHtml: '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-…" …></ins>'
}
```

**Auto ads only?** Set `autoAdsOnly: true` and the manual placeholders disappear.

Until `enabled` is `true` **and** a publisher ID is present, every position renders a
neutral dashed box labelled *Advertisement* — no network requests, nothing tracked.
Ad slots are declared in the HTML as:

```html
<div class="ad-wrap" data-ad-slot-name="practice-sidebar-top"
     data-ad-size="300 × 250" data-ad-shape="box"></div>
```

Add a slot anywhere by copying that markup and adding a matching key to `slots`.

### AdSense approval checklist — already done

| Requirement | Status |
|---|---|
| Substantial original content | ✅ ~9 000 words across home, guides and legal pages |
| Clear navigation & site structure | ✅ Header, footer, breadcrumbs, sitemap |
| Privacy policy incl. cookie/third-party disclosure | ✅ `privacy.html` |
| Terms of use | ✅ `terms.html` |
| Working contact method | ✅ `contact.html` |
| Ads clearly labelled and separated from content | ✅ Dashed, labelled, never inline with questions |
| `ads.txt` present | ✅ (add your ID) |
| Mobile friendly | ✅ Responsive from 320 px |
| No prohibited content | ✅ Educational only |

---

## 4. Publishing the site

### 4.1 Before you upload

1. **Change the domain.** `SITE_URL` at the top of `tools/shell.py` (currently
   `https://www.mathit.co.uk`) feeds every canonical, Open Graph tag, JSON-LD block and
   the sitemap. Change it once, then `npm run build:html`.
2. **Change the contact address.** `CONTACT_EMAIL` in the same file.
3. **Fill in `ads.txt`** with your publisher ID, and `assets/js/ads.js` (see §3).
4. Run `npm run build` one final time and commit the generated files.

### 4.2 What actually gets deployed

Everything in the project root **except** `tools/`, `src/`, `node_modules/` and
`package*.json`. Those are build-time only; `robots.txt` already disallows `/tools/` and
`/src/` in case you upload them anyway. There is no server-side code, so any static host
works: Netlify, Vercel, Cloudflare Pages, GitHub Pages, Amazon S3 + CloudFront, or plain
Apache/nginx.

### 4.3 One-command deploys

Config files for the three most common hosts ship in the repo — nothing to write.

| Host | Command | Config used |
|---|---|---|
| **Netlify** | `npx netlify deploy --prod --dir .` (or drag the folder onto [netlify.com/drop](https://app.netlify.com/drop)) | `netlify.toml`, `_redirects`, `_headers` |
| **Vercel** | `npx vercel --prod` | `vercel.json` |
| **Cloudflare Pages** | `npx wrangler pages deploy .` | `_headers`, `_redirects` |
| **GitHub Pages** | push to `main`, enable Pages → *Deploy from branch* | `.nojekyll` |
| **Any web server** | `rsync -av --exclude node_modules --exclude tools --exclude src ./ user@host:/var/www/mathit/` | — |

All of them set the same three things: long cache lifetimes on `/assets/*`,
`must-revalidate` on HTML, and the usual security headers (`nosniff`, `SAMEORIGIN`,
`strict-origin-when-cross-origin`). They also map `/practice` → `/practice.html` so the
pretty URLs work.

### 4.4 Apache / nginx

<details>
<summary>nginx server block</summary>

```nginx
server {
  listen 443 ssl http2;
  server_name www.mathit.co.uk;
  root /var/www/mathit;
  index index.html;

  error_page 404 /404.html;

  location /assets/ { expires 1y; add_header Cache-Control "public, immutable"; }
  location ~* \.html$ { add_header Cache-Control "public, max-age=0, must-revalidate"; }

  add_header X-Content-Type-Options nosniff;
  add_header X-Frame-Options SAMEORIGIN;
  add_header Referrer-Policy strict-origin-when-cross-origin;

  location / { try_files $uri $uri.html $uri/ =404; }
  location ~ ^/(tools|src)/ { return 404; }
}
```
</details>

<details>
<summary>.htaccess for shared hosting</summary>

```apache
ErrorDocument 404 /404.html
Options -Indexes

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^\.]+)$ $1.html [NC,L]
RewriteRule ^(tools|src)/ - [F,L]

<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\.(css|js|png|ico|woff2)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
</IfModule>
```
</details>

### 4.5 After going live

1. Submit `https://your-domain/sitemap.xml` to **Google Search Console** and **Bing
   Webmaster Tools**.
2. Confirm `https://your-domain/ads.txt` loads and contains your publisher line.
3. Run [PageSpeed Insights](https://pagespeed.web.dev/) — the site ships one 50 kB
   stylesheet and ~90 kB of JS, all static, so there should be nothing to fix.
4. Only then submit the site for AdSense review (§3).

---

## 5. Printing

**Every worksheet prints on exactly one side of A4, and so does every reference
sheet.** This is enforced, not hoped for — `npm run test:print` renders real PDFs and
counts `/Type /Page`.

Worksheets fit by density band. `practice.js` writes `data-print-density` onto `<html>`
from the row count, and `@media print` tightens type, padding and column gap to match:

| Questions | Rows | Band | Row type |
|---|---|---|---|
| ≤ 36 | ≤ 18 | `normal` | 11 pt |
| 38–42 | 19–21 | `snug` | 10.5 pt |
| 44–50 | 22–25 | `tight` | 10 pt |
| 52–60 | 26–30 | `tighter` | 9 pt |

The reference sheets in `downloads/` are clamped by a fixed `height: 281mm` plus
`overflow: hidden` on `.sheet`, which makes a second page structurally impossible.
Per-sheet tightening lives in `PRINT_CSS` in `tools/content_downloads.py`; the test
re-measures each sheet against the 281 mm box so the clamp can never crop content
silently. Note that Chrome's print engine **ignores `zoom` and CSS transforms** when
paginating, so the fit has to come from real layout values.

Four print modes, all driven by a class on `<html>` and the `@media print` block in
`src/app.src.css`:

| Mode | `<html>` class | What prints |
|---|---|---|
| Questions only (default) | `print-worksheet` | The sheet with blank boxes |
| Answer key only | `print-answers` | The numbered key, four columns |
| Questions and answer key | `print-both` | Sheet, page break, key |
| Class set | `print-set` | *N* different sheets from seeds `s`, `s+1`, …, optionally each followed by its key |

The split **Print** button on `practice.html` sets the class, calls `window.print()` and
clears the class again on `afterprint`. Printing always forces black on white, so a dark
or high-contrast screen still produces an ink-friendly sheet. Navigation, the sidebar,
adverts, the toolbar, the score banner and the supporting article are all suppressed.

Call it from the console or your own script:

```js
MathIt.Practice.print('both');     // worksheet | answers | both | set
MathIt.Practice.buildClassSet();   // render the set without printing
```

---

## 6. The question engine

`assets/js/generator.js` is standalone and has no dependencies. It exposes:

```js
MathIt.Generator.buildSheet({ year: 6, level: 'hard', count: 36, topics: [...] })
MathIt.Generator.isCorrect(question, userTypedString)
MathIt.Generator.groupedTopicsForYear(5)
MathIt.Generator.TOPICS            // the full registry
```

Difficulty is a single blended scalar, `pw = (year − 2) + levelIndex`, clamped to 0–6, so
Year 4 Hard and Year 6 Easy overlap naturally rather than sitting in separate silos.
Sheets round-robin through a shuffled list of enabled topics, so every topic appears
before any topic repeats — deliberate interleaving, not random sampling.

### 34 question types

| Group | Topics |
|---|---|
| Mental arithmetic | Addition · Subtraction · Multiplication facts · Division facts · Doubling & halving · Number bonds |
| Number & place value | Place value (integers and decimals) · Rounding (integers and d.p.) |
| Written methods | Long multiplication (3-digit × 2-digit) · Short division with remainders · Long division (4-digit ÷ 2-digit) |
| Fractions | Fraction × integer · Fraction of an amount · Adding & subtracting unlike denominators · Fraction × fraction · Fraction ÷ whole number · Fraction ÷ fraction · Mixed ↔ improper · Simplifying |
| Decimals & percentages | × and ÷ by 10/100/1000 · Decimal add & subtract (mismatched places) · Decimal × · Decimal ÷ · Percentage of an amount · Fraction ↔ decimal ↔ % |
| Reasoning & algebra | Missing numbers (unknown in any position, incl. balanced equations) · BIDMAS · Linear equations · Negative numbers · Squares, cubes & roots · Ratio & proportion · Sequences |
| Measurement | Metric unit conversion · Area & perimeter |

### Accepted answer formats

| Type | Accepted |
|---|---|
| Fraction | `3/4`, any equivalent (`6/8`), or `0.75` |
| Mixed number | `2 1/4` or `9/4` |
| Remainder | `12 r 3`, `12r3`, `12 rem 3`, `12 remainder 3` |
| Ratio | `3:4` or `3 : 4` |
| Negative | `-7` or `−7` |
| Large numbers | `1560` or `1,560` |
| Units | Trailing `cm`, `kg`, `%`, `£` are ignored |

### Adding a topic

```js
topic({
  id: 'prime-numbers',
  label: 'Prime numbers',
  group: 'Number & place value',   // must match an existing GROUP_ORDER entry
  years: [5, 6],
  blurb: 'Identifying primes below 100.',
  gen(c) {                          // c = { year, level, pw }
    const n = pick([11, 13, 17, 19, 23]);
    return Object.assign({
      html: `<span class="q-prompt">Next prime after ${n}</span>`,
      equals: false,
      key: `prime-${n}`,
    }, numAns(nextPrime(n)));
  },
});
```

It appears automatically in the settings drawer, the sheet rotation and the URL config.

---

## 7. Settings & shareable links

Settings resolve in this order: **defaults → localStorage → `?config=` → explicit params.**

| Parameter | Example | Notes |
|---|---|---|
| `year` | `?year=6` | 2–6 |
| `level` | `?level=hard` | `easy` · `medium` · `hard` |
| `count` | `?count=48` | 12, 18, 24, 36, 48, 60 |
| `topics` | `?topics=bidmas,ratio` | Comma-separated topic IDs |
| `compact` / `contrast` | `?compact=1` | `1` to enable |
| `config` | `?config=eyJ…` | Base64url of everything non-default |
| `s` | `?s=418203` | **Seed** — the same seed always rebuilds the identical sheet |

The seed is what makes class sets possible: hand out one link and every child gets the
same thirty-six questions. "New" simply rolls a fresh seed and rewrites the URL.

Drawer options: year, difficulty, question count, text size (3 steps), colour theme
(auto / light / dark), timer mode (off / stopwatch / countdown with 2–20 minutes),
compact density, high contrast, on-screen answer key, question numbers,
Enter-to-advance, topic labels, per-topic checkboxes grouped by curriculum area, and a
copyable share link.

### Stored keys

| Key | Where | Contents |
|---|---|---|
| `mathit:settings` | `localStorage` | Everything above, including `theme` |
| `mathit:history` | `localStorage` | Last 12 marked sheets: seed, year, level, score, timestamp |
| `mathit:answers:<seed>` | `sessionStorage` | Typed answers, so a refresh does not lose work |

Nothing leaves the browser. Clearing site data resets all three.

---

## 8. Toolbar

| Button | Key | Behaviour |
|---|---|---|
| **New** | `N` | Fresh seed, rebuilds 36 unique questions honouring every active setting |
| **Reset** | `R` | Clears inputs and markers, keeps the questions, restarts the timer |
| **Mark** | `M` / `Ctrl`+`Enter` | Scores attempted boxes — emerald for correct, clay for incorrect with the right answer shown — and opens a score card with a percentage bar and a "revisit" list of weak topics |
| **Answers** | `A` | Toggles all solutions without scoring |
| **Print** | `P` | A4 output: no nav, no sidebar, no ads, no banner — just the title, sheet number, name/class/date/score line and two columns of questions |
| **Print ▾** | — | Questions only · answer key only · both · class set of up to 35 different sheets (see §5) |

---

## 9. Accessibility

* Skip-to-content link, semantic landmarks, one `h1` per page.
* High-contrast mode (pure black on white, heavier borders) and three text sizes,
  both persisted across pages.
* Every answer box carries an `aria-label` containing the full question.
* Revealed answers expose a plain-text `aria-label` (`3/4`, not "34").
* Score card and timer are `aria-live` regions.
* Visible emerald focus rings; the whole app is keyboard-operable.
* A proper dark theme (`auto` follows `prefers-color-scheme`), applied by an inline
  script in `<head>` so there is no white flash on load. High contrast layers on top of
  either theme.
* `prefers-reduced-motion` respected via Tailwind's transition defaults; no autoplay,
  no flashing, no motion-dependent interactions.

---

## 10. Licence & attribution

Site code and written guides © Math It!. Teachers and parents may print, photocopy and
share worksheets freely for classroom and home use — see `terms.html`.
