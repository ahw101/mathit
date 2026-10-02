# -*- coding: utf-8 -*-
"""Resource hub & topic guides for Math It!"""
from shell import ad

import re as _re
from guides_data import GUIDES, CATEGORIES


def _anchor(cat):
    return _re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")


TOC = [(_anchor(c), c) for c in CATEGORIES] + [
    ("downloads", "Printable reference sheets"),
    ("glossary", "Glossary of terms"),
]

DOWNLOADS = [
    ("fractions-reference-sheet.html", "Fractions reference sheet",
     "Every rule on one page: multiplying, dividing, adding and subtracting fractions, converting mixed numbers and simplifying.",
     "A4 · 1 page"),
    ("long-division-reference-sheet.html", "Long division reference sheet",
     "The bus stop and the long division frame side by side, with a fully worked 4-digit ÷ 2-digit example and the DMSB cycle.",
     "A4 · 1 page"),
    ("bidmas-reference-sheet.html", "BIDMAS reference sheet",
     "The correct hierarchy, the two common myths, and eight worked examples that catch the usual traps.",
     "A4 · 1 page"),
    ("times-tables-grid.html", "Times tables grid to 12 × 12",
     "A clean multiplication square plus a blank grid to fill in against the clock, and the square numbers highlighted.",
     "A4 · 1 page"),
]

GLOSSARY = [
    ("Numerator", "The number on top of a fraction. It counts how many parts you have."),
    ("Denominator", "The number underneath a fraction. It names the size of each part — how many equal parts the whole was split into."),
    ("Improper fraction", "A fraction where the numerator is larger than the denominator, such as 9/4. Sometimes called top-heavy."),
    ("Mixed number", "A whole number written alongside a proper fraction, such as 2¼."),
    ("Dividend, divisor, quotient", "In 84 ÷ 7 = 12, the 84 is the dividend, the 7 is the divisor and the 12 is the quotient."),
    ("Product", "The result of a multiplication. The product of 6 and 7 is 42."),
    ("Factor", "A whole number that divides exactly into another. The factors of 12 are 1, 2, 3, 4, 6 and 12."),
    ("Multiple", "The result of multiplying a number by a whole number. The multiples of 7 are 7, 14, 21, 28 and so on."),
    ("Common denominator", "A shared denominator used to compare, add or subtract fractions — usually the lowest common multiple of the original denominators."),
    ("Reciprocal", "The fraction turned upside down. The reciprocal of 3/4 is 4/3. Dividing by a fraction is the same as multiplying by its reciprocal."),
    ("Partition", "Splitting a number into parts that are easier to work with, such as 36 = 30 + 6."),
    ("Exchange (regrouping)", "Trading ten of one place value column for one of the next, used in column addition and subtraction."),
    ("Place value", "The value a digit holds because of its position. The 7 in 4 703 is worth 700."),
    ("BIDMAS", "Brackets, Indices, Division and Multiplication, Addition and Subtraction — the order in which operations are carried out."),
]


def _toc():
    return "\n            ".join(
        f'<li><a href="#{slug}" class="block rounded-md px-3 py-2 text-sm text-soft transition-colors hover:bg-accent-soft hover:text-accent-soft-fg">{label}</a></li>'
        for slug, label in TOC
    )


def _guide_sections():
    out = []
    for n, cat in enumerate(CATEGORIES):
        gs = [g for g in GUIDES if g["cat"] == cat]
        cards = "\n".join(f"""              <a href="guides/{g['slug']}.html" class="group flex flex-col rounded-xl border border-line bg-surface p-5 transition-all hover:-translate-y-0.5 hover:border-accent hover:shadow-card">
                <span class="font-display text-lg font-bold text-strong group-hover:text-accent-text">{g['nav']}</span>
                <span class="mt-1.5 flex-1 text-sm leading-snug text-soft">{g['card']}</span>
                <span class="mt-3 flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-faint">
                  <span>{g['years']}</span><span aria-hidden="true">&middot;</span><span>{g['read']} min</span>
                  <span class="ml-auto text-accent-text opacity-0 transition-opacity group-hover:opacity-100">Read &rarr;</span>
                </span>
              </a>""" for g in gs)
        rule = '          <hr class="my-14 border-line">\n' if n else ""
        out.append(f"""{rule}          <section id="{_anchor(cat)}" class="scroll-mt-24">
            <span class="kicker">{len(gs)} guide{'s' if len(gs) != 1 else ''}</span>
            <h2 class="mt-4 font-display text-3xl font-bold sm:text-4xl">{cat}</h2>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
{cards}
            </div>
          </section>""")
    return "\n".join(out)


def _downloads():
    out = []
    for href, title, blurb, meta in DOWNLOADS:
        out.append(f"""          <div class="flex flex-col rounded-2xl border border-line bg-surface p-6 shadow-card">
            <div class="flex items-start gap-3">
              <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-warn-soft text-warn-soft-fg">
                <svg viewBox="0 0 20 20" class="h-5 w-5" fill="currentColor" aria-hidden="true"><path d="M9 2h2v7h3l-4 5-4-5h3V2z"/><path d="M3 15h14v3H3z"/></svg>
              </span>
              <div class="min-w-0">
                <h3 class="font-display text-lg font-bold leading-tight text-strong">{title}</h3>
                <p class="mt-0.5 text-xs font-semibold uppercase tracking-wider text-faint">{meta}</p>
              </div>
            </div>
            <p class="mt-4 flex-1 text-sm leading-relaxed text-soft">{blurb}</p>
            <div class="mt-5 flex gap-2">
              <a href="downloads/{href}" class="btn btn-sm btn-primary">Open &amp; print</a>
              <a href="downloads/{href}" download class="btn btn-sm btn-ghost">Download</a>
            </div>
          </div>""")
    return "\n".join(out)


def _glossary():
    return "\n            ".join(
        f'<div class="border-b border-line py-3 last:border-0"><dt class="font-semibold text-strong">{t}</dt>'
        f'<dd class="mt-1 text-sm leading-relaxed text-soft">{d}</dd></div>'
        for t, d in GLOSSARY
    )


BODY = f"""  <main id="main">

    <!-- ===================== HEADER ===================== -->
    <section class="border-b border-line bg-surface">
      <div class="mx-auto max-w-page px-4 py-14 sm:px-6 lg:px-8">
        <nav class="mb-5 flex items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
          <a href="index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
          <span aria-hidden="true" class="text-faint">/</span>
          <span class="font-semibold text-strong" aria-current="page">Guides</span>
        </nav>
        <span class="kicker">Resource hub &middot; {len(GUIDES)} guides</span>
        <h1 class="mt-4 max-w-3xl font-display text-4xl font-bold leading-tight sm:text-5xl">
          The methods behind the worksheets
        </h1>
        <p class="mt-5 max-w-3xl text-lg leading-relaxed text-body">
          {len(GUIDES)} plain-English guides to the topics primary children find hardest, written
          for the adult doing the explaining. Every guide sets out the method step by step, works
          full examples, lists the mistakes to watch for, and links straight through to a
          worksheet on that topic. Printable one-page reference sheets are at the bottom.
        </p>
        <div class="mt-7 flex flex-wrap gap-3">
          <a href="practice.html" class="btn btn-primary">Make a worksheet</a>
          <a href="tables.html" class="btn btn-ghost">Times tables drill</a>
        </div>
      </div>
    </section>

    <div class="mx-auto max-w-page px-4 py-12 sm:px-6 lg:px-8">
      <div class="grid gap-10 lg:grid-cols-12">

        <!-- ================= TOC SIDEBAR ================= -->
        <aside class="lg:col-span-3" aria-label="On this page">
          <div class="lg:sticky lg:top-24">
            <div class="card p-4">
              <h2 class="px-3 text-xs font-bold uppercase tracking-[0.14em] text-soft">On this page</h2>
              <ul class="mt-2 space-y-0.5">
            {_toc()}
              </ul>
            </div>
            <div class="mt-6">
              {ad("resources-sidebar", size="300 × 250", shape="box")}
            </div>
            <div class="card mt-6 p-5">
              <h2 class="font-display text-lg font-bold">Practise what you have read</h2>
              <p class="mt-2 text-sm leading-relaxed text-soft">Turn any of these topics into a thirty-six question worksheet in one click.</p>
              <a href="practice.html?year=6&amp;level=medium" class="btn btn-primary btn-sm mt-4 w-full">Open the generator</a>
            </div>
          </div>
        </aside>

        <!-- ================= ARTICLES ================= -->
        <div class="lg:col-span-9">

{_guide_sections()}

          <hr class="my-14 border-line">

          <!-- ---------- DOWNLOADS ---------- -->
          <section id="downloads" class="scroll-mt-24">
            <span class="kicker">Free printables</span>
            <h2 class="mt-4 font-display text-3xl font-bold sm:text-4xl">Printable reference sheets</h2>
            <p class="mt-4 max-w-3xl text-lg leading-relaxed text-body">
              One-page summaries designed to be printed and stuck inside the front cover of an
              exercise book, or laminated for a maths working wall. Each opens in your browser and
              prints to a single sheet of A4 — no account, no watermark, free to copy for
              classroom and home use.
            </p>
            <div class="mt-8 grid gap-5 sm:grid-cols-2">
{_downloads()}
            </div>
          </section>

          <hr class="my-14 border-line">

          <!-- ---------- GLOSSARY ---------- -->
          <section id="glossary" class="scroll-mt-24">
            <span class="kicker">Reference</span>
            <h2 class="mt-4 font-display text-3xl font-bold sm:text-4xl">Glossary of primary maths terms</h2>
            <p class="mt-4 max-w-3xl text-lg leading-relaxed text-body">
              The vocabulary children meet in Years 2 to 6, in plain English. Using the correct
              word consistently is one of the cheapest ways to improve a child's mathematical
              reasoning — “denominator” is far more useful than “the bottom one”.
            </p>
            <dl class="mt-8 rounded-2xl border border-line bg-surface px-6 py-2 shadow-card">
            {_glossary()}
            </dl>
          </section>

        </div>
      </div>
    </div>
  </main>"""
