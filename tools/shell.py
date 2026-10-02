# -*- coding: utf-8 -*-
"""Shared HTML shell for Math It! — head, theme boot, header, footer, ad slots."""

SITE_NAME = "Math It!"
SITE_URL = "https://www.mathit.co.uk"          # ← change once, rebuild, done
SITE_TAGLINE = "Mental maths worksheets for Years 2 to 6"
CONTACT_EMAIL = "hello@mathit.co.uk"

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='14' fill='%23272420'/%3E"
    "%3Cpath d='M14 44V20h6l6 11 6-11h6v24h-6V31l-6 10-6-10v13z' fill='%23f7f6f4'/%3E"
    "%3Ccircle cx='48' cy='22' r='5' fill='%23f59e0b'/%3E"
    "%3Cpath d='M43 40h10M48 35v10' stroke='%2334d399' stroke-width='3.4' stroke-linecap='round'/%3E"
    "%3C/svg%3E"
)

# fill-* / stroke-* utilities resolve to theme tokens, so the mark inverts
# cleanly in dark mode instead of sitting as a dark square on a dark page.
LOGO_SVG = """<svg viewBox="0 0 64 64" class="h-9 w-9 shrink-0" aria-hidden="true" focusable="false">
        <rect width="64" height="64" rx="14" class="fill-strong"></rect>
        <path d="M14 44V20h6l6 11 6-11h6v24h-6V31l-6 10-6-10v13z" class="fill-canvas"></path>
        <circle cx="48" cy="22" r="5" class="fill-warn"></circle>
        <path d="M43 40h10M48 35v10" class="stroke-accent" stroke-width="3.4" stroke-linecap="round"></path>
      </svg>"""

NAV = [
    ("index.html", "Home"),
    ("practice.html", "Worksheets"),
    ("tables.html", "Times tables"),
    ("resources.html", "Guides"),
    ("contact.html", "Contact"),
]

ADSENSE_CLIENT = "ca-pub-9904590475432919"

# Google AdSense loader. Slot-level configuration lives in /assets/js/ads.js.
ADSENSE = f"""<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}"
          crossorigin="anonymous"></script>"""

# Simple Analytics — cookie-free, no personal data, no consent banner needed.
ANALYTICS = """<script async src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
  <noscript><img src="https://queue.simpleanalyticscdn.com/noscript.gif" alt="" referrerpolicy="no-referrer-when-downgrade"></noscript>"""

# Runs before first paint so a dark-mode visitor never sees a white flash.
THEME_BOOT = """<script>
  (function () {
    try {
      var d = document.documentElement, s = {};
      try { s = JSON.parse(localStorage.getItem('mathit:settings') || '{}') || {}; } catch (e) {}
      var t = s.theme || 'auto';
      var dark = t === 'dark' || (t === 'auto' &&
        window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
      d.classList.toggle('mi-dark', dark);
      if (s.contrast) d.classList.add('mi-contrast');
      if (s.compact) d.classList.add('mi-compact');
      if (s.fontScale === 'large') d.classList.add('mi-font-lg');
      if (s.fontScale === 'xlarge') d.classList.add('mi-font-xl');
      var m = document.querySelector('meta[name="theme-color"]');
      if (m) m.setAttribute('content', dark ? '#121110' : '#faf9f7');
    } catch (e) {}
  })();
  </script>"""

SUN_ICON = ('<svg data-theme-icon="light" viewBox="0 0 20 20" class="h-[18px] w-[18px]" fill="currentColor" '
            'aria-hidden="true"><path d="M10 14a4 4 0 100-8 4 4 0 000 8zm0-12a1 1 0 011 1v1.5a1 1 0 11-2 0V3a1 1 0 '
            '011-1zm0 13a1 1 0 011 1V17a1 1 0 11-2 0v-1a1 1 0 011-1zM3 9h1.5a1 1 0 110 2H3a1 1 0 110-2zm12.5 0H17a1 '
            '1 0 110 2h-1.5a1 1 0 110-2zM4.9 3.5l1.1 1.1A1 1 0 014.6 6L3.5 4.9A1 1 0 014.9 3.5zm9 9.9 1.1 1.1a1 1 0 '
            '01-1.4 1.4L12.5 14.8a1 1 0 011.4-1.4zM15.1 3.5a1 1 0 011.4 1.4L15.4 6A1 1 0 0114 4.6zM6 14.8a1 1 0 '
            '01-1.4 1.4L3.5 15.1A1 1 0 014.9 13.7z"/></svg>')

MOON_ICON = ('<svg data-theme-icon="dark" viewBox="0 0 20 20" class="hidden h-[18px] w-[18px]" fill="currentColor" '
             'aria-hidden="true"><path d="M8.3 2.2a7.8 7.8 0 109.5 9.6 6.4 6.4 0 01-9.5-9.6z"/></svg>')


def ad(slot, size="300 × 250", shape="box", extra=""):
    """Reserved advertising position. Real units are configured in /assets/js/ads.js."""
    return (
        f'<div class="ad-wrap{" " + extra if extra else ""}" data-ad-slot-name="{slot}" '
        f'data-ad-size="{size}" data-ad-shape="{shape}"></div>'
    )


def _nav_links(current, mobile=False, pre=""):
    base = "block w-full text-left nav-link" if mobile else "nav-link"
    out = []
    for href, label in NAV:
        aria = ' aria-current="page"' if href == current else ""
        out.append(f'<a href="{pre}{href}" class="{base}"{aria}>{label}</a>')
    return "\n          ".join(out)


def header(current, pre=""):
    return f"""  <header class="site-header sticky top-0 z-40 border-b border-line bg-canvas/95 backdrop-blur supports-[backdrop-filter]:bg-canvas/80">
    <div class="mx-auto flex max-w-page items-center gap-3 px-4 py-3 sm:px-6 lg:px-8">
      <a href="{pre}index.html" class="flex items-center gap-2.5 rounded-lg py-1 pr-2" aria-label="{SITE_NAME} home">
        {LOGO_SVG}
        <span class="flex flex-col leading-none">
          <span class="font-display text-xl font-bold tracking-tight text-strong">Math&nbsp;It!</span>
          <span class="mt-0.5 hidden text-[0.65rem] font-semibold uppercase tracking-[0.16em] text-faint sm:block">Years 2–6</span>
        </span>
      </a>

      <nav class="ml-auto hidden items-center gap-1 md:flex" aria-label="Primary">
          {_nav_links(current, pre=pre)}
      </nav>

      <div class="ml-auto flex items-center gap-2 md:ml-3">
        <button type="button" data-theme-toggle class="icon-btn" title="Switch between light and dark"
                aria-label="Switch between light and dark">
          {SUN_ICON}
          {MOON_ICON}
        </button>
        <a href="{pre}practice.html" class="btn btn-primary btn-sm hidden sm:inline-flex">Make a worksheet</a>

        <button type="button" data-nav-toggle aria-expanded="false" aria-controls="mobile-nav"
                class="icon-btn h-10 w-10 md:hidden">
          <span class="sr-only">Toggle navigation</span>
          <svg data-icon-open viewBox="0 0 20 20" class="h-5 w-5" fill="currentColor" aria-hidden="true"><path d="M3 5h14v2H3zM3 9h14v2H3zM3 13h14v2H3z"/></svg>
          <svg data-icon-close viewBox="0 0 20 20" class="hidden h-5 w-5" fill="currentColor" aria-hidden="true"><path d="M5.3 4 4 5.3 8.7 10 4 14.7 5.3 16 10 11.3 14.7 16 16 14.7 11.3 10 16 5.3 14.7 4 10 8.7z"/></svg>
        </button>
      </div>
    </div>

    <div id="mobile-nav" data-nav-panel class="hidden border-t border-line bg-surface px-4 py-3 md:hidden">
      <nav class="flex flex-col gap-1" aria-label="Mobile">
          {_nav_links(current, mobile=True, pre=pre)}
        <a href="{pre}practice.html" class="btn btn-primary mt-2 w-full">Make a worksheet</a>
      </nav>
    </div>
  </header>"""


def _footer_year_links(pre=""):
    return "\n            ".join(
        f'<li><a href="{pre}practice.html?year={y}&amp;level=medium" class="text-sm text-soft hover:text-accent-text">Year {y} worksheets</a></li>'
        for y in range(2, 7)
    )

THEME_PICKER = """<div class="flex flex-wrap items-center gap-2">
            <span class="label">Appearance</span>
            <div class="seg" role="group" aria-label="Colour theme">
              <button type="button" data-theme-set="auto">Auto</button>
              <button type="button" data-theme-set="light">Light</button>
              <button type="button" data-theme-set="dark">Dark</button>
            </div>
            <button type="button" data-mode-toggle="contrast" role="switch" aria-checked="false"
                    class="btn btn-ghost btn-sm">High contrast</button>
          </div>"""


def footer(pre=""):
    return f"""  <footer class="site-footer mt-16 border-t border-line bg-raise">
    <div class="mx-auto max-w-page px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid gap-10 md:grid-cols-4">
        <div class="md:col-span-1">
          <div class="flex items-center gap-2.5">
            {LOGO_SVG}
            <span class="font-display text-xl font-bold text-strong">Math&nbsp;It!</span>
          </div>
          <p class="mt-4 max-w-xs text-sm leading-relaxed text-soft">
            Free printable maths worksheets for Years 2 to 6. Pick a year group, pick a difficulty,
            print it or work through it on screen. No account, no subscription.
          </p>
          <div class="mt-5">
            {THEME_PICKER}
          </div>
        </div>

        <div>
          <h2 class="text-xs font-bold uppercase tracking-[0.16em] text-faint">Worksheets</h2>
          <ul class="mt-4 space-y-2.5">
            {_footer_year_links(pre)}
            <li><a href="{pre}tables.html" class="text-sm text-soft hover:text-accent-text">Times tables</a></li>
          </ul>
        </div>

        <div>
          <h2 class="text-xs font-bold uppercase tracking-[0.16em] text-faint">Guides</h2>
          <ul class="mt-4 space-y-2.5">
            <li><a href="{pre}resources.html#fractions" class="text-sm text-soft hover:text-accent-text">Fractions</a></li>
            <li><a href="{pre}resources.html#long-division" class="text-sm text-soft hover:text-accent-text">Long division</a></li>
            <li><a href="{pre}resources.html#order-of-operations" class="text-sm text-soft hover:text-accent-text">BIDMAS</a></li>
            <li><a href="{pre}resources.html#decimal-multiplication" class="text-sm text-soft hover:text-accent-text">Decimal multiplication</a></li>
            <li><a href="{pre}resources.html" class="text-sm text-soft hover:text-accent-text">All 30 topic guides</a></li>
            <li><a href="{pre}resources.html#downloads" class="text-sm text-soft hover:text-accent-text">Reference sheets</a></li>
          </ul>
        </div>

        <div>
          <h2 class="text-xs font-bold uppercase tracking-[0.16em] text-faint">Site</h2>
          <ul class="mt-4 space-y-2.5">
            <li><a href="{pre}contact.html" class="text-sm text-soft hover:text-accent-text">Contact</a></li>
            <li><a href="{pre}privacy.html" class="text-sm text-soft hover:text-accent-text">Privacy &amp; cookies</a></li>
            <li><a href="{pre}terms.html" class="text-sm text-soft hover:text-accent-text">Terms of use</a></li>
            <li><a href="{pre}sitemap.xml" class="text-sm text-soft hover:text-accent-text">Sitemap</a></li>
          </ul>
        </div>
      </div>

      <div class="mt-10 flex flex-col gap-3 border-t border-line pt-6 sm:flex-row sm:items-center sm:justify-between">
        <p class="text-xs text-faint">
          © <span data-current-year>2026</span> {SITE_NAME}. Made in the UK for primary classrooms.
        </p>
        <p class="max-w-xl text-xs leading-relaxed text-faint">
          An independent resource. Not affiliated with the Department for Education, Ofsted or any exam board.
        </p>
      </div>
    </div>
  </footer>"""


def page(*, filename, title, description, body, current, keywords="",
         extra_head="", extra_scripts="", jsonld="", og_type="website",
         body_attrs="", prefix=""):
    canonical = f"{SITE_URL}/{filename}"
    ba = f" {body_attrs}" if body_attrs else ""
    pre = prefix
    kw = f'\n  <meta name="keywords" content="{keywords}">' if keywords else ""
    jl = f'\n  <script type="application/ld+json">{jsonld}</script>' if jsonld else ""
    return f"""<!doctype html>
<html lang="en-GB" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">{kw}
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="theme-color" content="#faf9f7">
  <meta name="author" content="{SITE_NAME}">
  <meta name="format-detection" content="telephone=no">

  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="en_GB">
  <meta property="og:image" content="{SITE_URL}/assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE_URL}/assets/img/og-image.png">

  <link rel="icon" href="{pre}favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="{FAVICON}">
  <link rel="icon" type="image/png" sizes="192x192" href="{pre}assets/img/icon-192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{pre}assets/img/icon-180.png">
  <link rel="manifest" href="{pre}site.webmanifest">
  <link rel="stylesheet" href="{pre}assets/css/app.css">{extra_head}{jl}

  <meta name="google-adsense-account" content="{ADSENSE_CLIENT}">
  {ADSENSE}

  {THEME_BOOT}
</head>
<body class="min-h-screen"{ba}>
  <a href="#main" class="skip-link sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-invert focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-invert-fg">Skip to main content</a>

{header(current, pre)}

{body}

{footer(pre)}

  <script src="{pre}assets/js/settings.js"></script>
  <script src="{pre}assets/js/ads.js"></script>
  <script src="{pre}assets/js/site.js"></script>{extra_scripts}

  {ANALYTICS}
</body>
</html>
"""
