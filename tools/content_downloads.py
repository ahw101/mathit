# -*- coding: utf-8 -*-
"""Printable one-page reference sheets (downloads/*.html)."""
from shell import THEME_BOOT, SUN_ICON, MOON_ICON

SHEET_SHELL = """<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Math It! printable reference sheet</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.mathit.co.uk/downloads/{filename}">
  <meta name="robots" content="index, follow">
  <link rel="icon" href="../favicon.ico" sizes="any">
  <link rel="stylesheet" href="../assets/css/app.css">
  <style>
    /* Every reference sheet must print on exactly ONE side of A4. The shared
       print rules in app.css strip the chrome; these tighten the internals.
       Note that Chrome's PDF pagination ignores `zoom` and CSS transforms, so
       the fit has to come from real layout values. The fixed height on .sheet
       is a hard guarantee: whatever else changes, the sheet can never
       paginate onto a second side. */
    @media print {{
      @page {{ size: A4 portrait; margin: 8mm; }}
      .sheet-chrome {{ display: none !important; }}
      .sheet {{
        padding: 0 !important; margin: 0 !important;
        width: 100% !important; max-width: 100% !important;
        height: 281mm !important; overflow: hidden !important;
      }}
      /* Stop a wide multiplication square pushing the sheet past the page box,
         which Chrome resolves by spilling onto a second sheet. */
      .sheet table {{ width: 100% !important; max-width: 100% !important; table-layout: fixed !important; }}
      .sheet pre {{ overflow: hidden !important; white-space: pre-wrap !important; }}
      .sheet header {{ padding-bottom: 2mm !important; }}
      .sheet footer {{ margin-top: 3mm !important; padding-top: 2mm !important; }}
      .sheet section {{ padding: 2.6mm !important; break-inside: avoid; }}
      .sheet h1 {{ font-size: 19pt !important; }}
      .sheet h2 {{ font-size: 10.5pt !important; }}
      .sheet table {{ font-size: 8.2pt !important; }}
      .sheet td, .sheet th {{ padding: .5mm !important; }}
      .sheet .gap-5 {{ gap: 2.6mm !important; }}
      .sheet .gap-4 {{ gap: 2.2mm !important; }}
      .sheet .gap-3 {{ gap: 1.8mm !important; }}
      .sheet .mt-8 {{ margin-top: 3mm !important; }}
      .sheet .mt-6 {{ margin-top: 2.4mm !important; }}
      .sheet .mt-5 {{ margin-top: 2mm !important; }}
      .sheet .mt-4 {{ margin-top: 1.8mm !important; }}
      .sheet .mt-3 {{ margin-top: 1.4mm !important; }}
      .sheet .space-y-2 > * + * {{ margin-top: 1.2mm !important; }}
      .sheet .space-y-1 > * + * {{ margin-top: .7mm !important; }}
{print_css}    }}
  </style>

  {theme_boot}
</head>
<body class="bg-canvas">
  <div class="sheet-chrome no-print sticky top-0 z-10 border-b border-line bg-canvas/95 backdrop-blur">
    <div class="mx-auto flex max-w-[210mm] flex-wrap items-center gap-3 px-4 py-3">
      <a href="../resources.html" class="btn btn-sm btn-ghost">← All printables</a>
      <span class="text-sm font-semibold text-body">{title}</span>
      <button type="button" data-theme-toggle class="icon-btn ml-auto h-8 w-8" aria-label="Switch between light and dark">{sun}{moon}</button>
      <button type="button" data-print-trigger="worksheet" class="btn btn-sm btn-primary">Print this sheet</button>
    </div>
  </div>

  <main class="sheet mx-auto my-6 max-w-[210mm] bg-surface p-10 shadow-card print:my-0 print:shadow-none">
    <header class="flex items-end justify-between border-b-2 border-line-strong pb-3">
      <div>
        <h1 class="font-display text-3xl font-bold leading-none text-strong">{title}</h1>
        <p class="mt-1.5 text-sm text-soft">{subtitle}</p>
      </div>
      <div class="text-right">
        <p class="font-display text-lg font-bold text-strong">Math It!</p>
        <p class="text-[0.7rem] uppercase tracking-wider text-soft">www.mathit.co.uk</p>
      </div>
    </header>

{body}

    <footer class="mt-8 border-t border-line-strong pt-3 text-[0.7rem] text-soft">
      Free to photocopy for classroom and home use · © Math It! · {filename}
    </footer>
  </main>

  <script src="../assets/js/settings.js"></script>
  <script src="../assets/js/site.js"></script>
</body>
</html>
"""


def f(n, d):
    return f'<span class="frac"><span class="num">{n}</span><span class="den">{d}</span></span>'


def box(title, body, tone="ink"):
    tones = {
        "ink": "border-line-strong bg-raise",
        "emerald": "border-accent-line bg-accent-soft/60",
        "amber": "border-warn-line bg-warn-soft/60",
    }
    return f"""      <section class="rounded-xl border {tones[tone]} p-4">
        <h2 class="font-display text-base font-bold text-strong">{title}</h2>
        {body}
      </section>"""


# ---------------------------------------------------------------- fractions
FRACTIONS_BODY = f"""    <div class="mt-6 grid gap-4 sm:grid-cols-2">
{box("Multiply by a whole number", f'''
        <p class="mt-2 text-sm text-body">Multiply the <strong>numerator</strong>. Leave the denominator alone.</p>
        <p class="mt-3 text-center text-lg">{f("3","4")} × 16 = {f("48","4")} = <strong>12</strong></p>
        <p class="mt-2 text-xs text-soft">Shortcut: ÷ by the denominator first — a quarter of 16 is 4, so three quarters is 12.</p>''', "emerald")}

{box("Multiply two fractions", f'''
        <p class="mt-2 text-sm text-body">Multiply straight across the top, then straight across the bottom. Simplify at the end.</p>
        <p class="mt-3 text-center text-lg">{f("2","3")} × {f("3","5")} = {f("6","15")} = <strong>{f("2","5")}</strong></p>''')}

{box("Add or subtract", f'''
        <p class="mt-2 text-sm text-body">Make the denominators the same, then add or subtract the <strong>numerators only</strong>.</p>
        <p class="mt-3 text-center text-lg">{f("2","3")} + {f("1","4")} = {f("8","12")} + {f("3","12")} = <strong>{f("11","12")}</strong></p>
        <p class="mt-2 text-xs text-soft">Use the lowest common multiple of the two denominators.</p>''', "emerald")}

{box("Divide by a whole number", f'''
        <p class="mt-2 text-sm text-body">The parts get smaller, so the <strong>denominator</strong> grows.</p>
        <p class="mt-3 text-center text-lg">{f("3","5")} ÷ 4 = {f("3","20")}</p>''')}

{box("Divide by a fraction — keep, change, flip", f'''
        <p class="mt-2 text-sm text-body">Keep the first, change ÷ to ×, flip the second.</p>
        <p class="mt-3 text-center text-lg">{f("1","2")} ÷ {f("3","4")} = {f("1","2")} × {f("4","3")} = {f("4","6")} = <strong>{f("2","3")}</strong></p>''', "amber")}

{box("Mixed ↔ improper", f'''
        <p class="mt-2 text-sm text-body">Whole × denominator + numerator, over the denominator.</p>
        <p class="mt-3 text-center text-lg">2{f("3","5")} = {f("13","5")} &nbsp;&nbsp;·&nbsp;&nbsp; {f("17","5")} = 3{f("2","5")}</p>
        <p class="mt-2 text-xs text-soft">Always convert before multiplying or dividing.</p>''')}
    </div>

    <section class="mt-5 rounded-xl border border-line-strong p-4">
      <h2 class="font-display text-base font-bold">Simplifying — divide top and bottom by the same number</h2>
      <div class="mt-3 grid grid-cols-2 gap-x-6 gap-y-1.5 text-sm sm:grid-cols-4">
        <p>{f("18","24")} = {f("3","4")}</p><p>{f("16","20")} = {f("4","5")}</p>
        <p>{f("45","60")} = {f("3","4")}</p><p>{f("21","28")} = {f("3","4")}</p>
        <p>{f("24","36")} = {f("2","3")}</p><p>{f("30","48")} = {f("5","8")}</p>
        <p>{f("50","100")} = {f("1","2")}</p><p>{f("36","81")} = {f("4","9")}</p>
      </div>
    </section>

    <section class="mt-5 rounded-xl border-2 border-dashed border-bad-line bg-bad-soft/50 p-4">
      <h2 class="font-display text-base font-bold text-bad-soft-fg">Traps</h2>
      <ul class="mt-2 grid gap-1.5 text-sm text-bad-soft-fg sm:grid-cols-2">
        <li>✗ {f("1","2")} + {f("1","3")} = {f("2","5")} — never add denominators.</li>
        <li>✗ Flipping the first fraction when dividing.</li>
        <li>✗ Multiplying the denominator by a whole number.</li>
        <li>✗ Leaving the answer unsimplified.</li>
      </ul>
    </section>

    <section class="mt-5">
      <h2 class="font-display text-base font-bold">Equivalents worth knowing by heart</h2>
      <table class="mt-2 w-full border-collapse text-center text-sm">
        <thead><tr class="bg-invert text-invert-fg">
          <th class="border border-line px-2 py-1.5">Fraction</th>
          <th class="border border-line px-2 py-1.5">Decimal</th>
          <th class="border border-line px-2 py-1.5">Percentage</th>
          <th class="border border-line px-2 py-1.5">Fraction</th>
          <th class="border border-line px-2 py-1.5">Decimal</th>
          <th class="border border-line px-2 py-1.5">Percentage</th>
        </tr></thead>
        <tbody>
          <tr><td class="border border-line-strong px-2 py-1.5">{f("1","2")}</td><td class="border border-line-strong px-2 py-1.5">0.5</td><td class="border border-line-strong px-2 py-1.5">50%</td>
              <td class="border border-line-strong px-2 py-1.5">{f("1","5")}</td><td class="border border-line-strong px-2 py-1.5">0.2</td><td class="border border-line-strong px-2 py-1.5">20%</td></tr>
          <tr class="bg-raise"><td class="border border-line-strong px-2 py-1.5">{f("1","4")}</td><td class="border border-line-strong px-2 py-1.5">0.25</td><td class="border border-line-strong px-2 py-1.5">25%</td>
              <td class="border border-line-strong px-2 py-1.5">{f("2","5")}</td><td class="border border-line-strong px-2 py-1.5">0.4</td><td class="border border-line-strong px-2 py-1.5">40%</td></tr>
          <tr><td class="border border-line-strong px-2 py-1.5">{f("3","4")}</td><td class="border border-line-strong px-2 py-1.5">0.75</td><td class="border border-line-strong px-2 py-1.5">75%</td>
              <td class="border border-line-strong px-2 py-1.5">{f("1","8")}</td><td class="border border-line-strong px-2 py-1.5">0.125</td><td class="border border-line-strong px-2 py-1.5">12.5%</td></tr>
          <tr class="bg-raise"><td class="border border-line-strong px-2 py-1.5">{f("1","3")}</td><td class="border border-line-strong px-2 py-1.5">0.333…</td><td class="border border-line-strong px-2 py-1.5">33⅓%</td>
              <td class="border border-line-strong px-2 py-1.5">{f("3","8")}</td><td class="border border-line-strong px-2 py-1.5">0.375</td><td class="border border-line-strong px-2 py-1.5">37.5%</td></tr>
          <tr><td class="border border-line-strong px-2 py-1.5">{f("2","3")}</td><td class="border border-line-strong px-2 py-1.5">0.666…</td><td class="border border-line-strong px-2 py-1.5">66⅔%</td>
              <td class="border border-line-strong px-2 py-1.5">{f("1","10")}</td><td class="border border-line-strong px-2 py-1.5">0.1</td><td class="border border-line-strong px-2 py-1.5">10%</td></tr>
        </tbody>
      </table>
    </section>"""


# ---------------------------------------------------------- long division
LONG_DIVISION_BODY = """    <div class="mt-6 grid gap-4 sm:grid-cols-2">
      <section class="rounded-xl border border-accent-line bg-accent-soft/60 p-4">
        <h2 class="font-display text-base font-bold">Short division (bus stop) — dividing by one digit</h2>
        <p class="mt-2 text-sm text-body">Work left to right. Carry each remainder into the next column as a small digit.</p>
        <pre class="mt-3 overflow-x-auto rounded-lg bg-surface p-3 font-mono text-sm leading-relaxed">   1  2  1
 ┌──────────
7│ 8 ¹4  7

8 ÷ 7 = 1 r 1  → carry the 1
14 ÷ 7 = 2
7 ÷ 7 = 1
847 ÷ 7 = 121</pre>
      </section>

      <section class="rounded-xl border border-warn-line bg-warn-soft/60 p-4">
        <h2 class="font-display text-base font-bold">The cycle — say it every time</h2>
        <ol class="mt-3 space-y-2 text-sm text-strong">
          <li><strong class="font-display text-lg">D</strong>ivide — how many times does it go in?</li>
          <li><strong class="font-display text-lg">M</strong>ultiply — write the product underneath.</li>
          <li><strong class="font-display text-lg">S</strong>ubtract — find what is left.</li>
          <li><strong class="font-display text-lg">B</strong>ring down — take the next digit.</li>
        </ol>
        <p class="mt-3 text-xs text-soft">Repeat until every digit of the dividend has been brought down.</p>
      </section>
    </div>

    <section class="mt-5 rounded-xl border border-line-strong p-4">
      <h2 class="font-display text-base font-bold">Long division — 4 356 ÷ 12</h2>
      <div class="mt-3 grid gap-4 sm:grid-cols-5">
        <pre class="sm:col-span-2 overflow-x-auto rounded-lg bg-raise p-3 font-mono text-sm leading-relaxed">      3  6  3
   ┌──────────
12 │ 4  3  5  6
     3  6          ← 3 × 12
     ──────
        7  5
        7  2       ← 6 × 12
        ──────
           3  6
           3  6    ← 3 × 12
           ──────
              0</pre>
        <div class="sm:col-span-3">
          <ol class="space-y-1.5 text-sm text-body">
            <li><strong>1.</strong> 12 into 4? No. 12 into 43? Three times. Write 3.</li>
            <li><strong>2.</strong> 3 × 12 = 36. Write it under 43.</li>
            <li><strong>3.</strong> 43 − 36 = 7.</li>
            <li><strong>4.</strong> Bring down the 5 → 75.</li>
            <li><strong>5.</strong> 12 into 75? Six times. 6 × 12 = 72. 75 − 72 = 3.</li>
            <li><strong>6.</strong> Bring down the 6 → 36. 12 into 36 is exactly 3.</li>
            <li><strong>7.</strong> Nothing left: <strong>4 356 ÷ 12 = 363</strong>.</li>
          </ol>
        </div>
      </div>
    </section>

    <section class="mt-5 rounded-xl border border-line-strong p-4">
      <h2 class="font-display text-base font-bold">Write the multiples list first — it removes all the guessing</h2>
      <table class="mt-3 w-full border-collapse text-center text-sm">
        <thead><tr class="bg-invert text-invert-fg"><th class="border border-line px-1.5 py-1">×</th>
          <th class="border border-line px-1.5 py-1">1</th><th class="border border-line px-1.5 py-1">2</th>
          <th class="border border-line px-1.5 py-1">3</th><th class="border border-line px-1.5 py-1">4</th>
          <th class="border border-line px-1.5 py-1">5</th><th class="border border-line px-1.5 py-1">6</th>
          <th class="border border-line px-1.5 py-1">7</th><th class="border border-line px-1.5 py-1">8</th>
          <th class="border border-line px-1.5 py-1">9</th></tr></thead>
        <tbody>""" + "".join(
    '<tr class="{bg}"><th class="border border-line-strong bg-raise px-1.5 py-1 font-bold">{d}</th>{cells}</tr>'.format(
        bg="bg-raise" if i % 2 else "",
        d=d,
        cells="".join(f'<td class="border border-line-strong px-1.5 py-1">{d*k}</td>' for k in range(1, 10)),
    )
    for i, d in enumerate([12, 14, 15, 16, 18, 24, 25])
) + """
        </tbody>
      </table>
      <p class="mt-2 text-xs text-soft">Build your own list for any divisor by repeatedly adding it on.</p>
    </section>

    <section class="mt-5 grid gap-4 sm:grid-cols-2">
      <div class="rounded-xl border border-line-strong bg-raise p-4">
        <h2 class="font-display text-base font-bold">Three ways to show a remainder</h2>
        <ul class="mt-2 space-y-1.5 text-sm text-body">
          <li><strong>Whole number:</strong> 4 357 ÷ 12 = 363 r 1</li>
          <li><strong>Fraction:</strong> 363<span class="frac"><span class="num">1</span><span class="den">12</span></span></li>
          <li><strong>Decimal:</strong> 363.083…</li>
        </ul>
        <p class="mt-2 text-xs text-soft">Word problems decide which one: buses round up, money needs decimals.</p>
      </div>
      <div class="rounded-xl border-2 border-dashed border-bad-line bg-bad-soft/50 p-4">
        <h2 class="font-display text-base font-bold text-bad-soft-fg">Traps</h2>
        <ul class="mt-2 space-y-1.5 text-sm text-bad-soft-fg">
          <li>✗ Columns drifting — use squared paper.</li>
          <li>✗ Forgetting to write 0 when the divisor will not go.</li>
          <li>✗ Stopping before the last digit is brought down.</li>
          <li>✗ A subtraction slip carried silently through every later step.</li>
        </ul>
      </div>
    </section>"""


# ---------------------------------------------------------------- BIDMAS
BIDMAS_BODY = """    <div class="mt-6 grid gap-4 sm:grid-cols-3">
      <section class="sm:col-span-2 rounded-xl border border-accent-line bg-accent-soft/60 p-4">
        <h2 class="font-display text-base font-bold">The hierarchy</h2>
        <table class="mt-3 w-full border-collapse text-sm">
          <thead><tr class="bg-invert text-invert-fg">
            <th class="border border-line px-2 py-1.5 text-left">Order</th>
            <th class="border border-line px-2 py-1.5 text-left">Operation</th>
            <th class="border border-line px-2 py-1.5 text-left">Direction</th></tr></thead>
          <tbody>
            <tr><td class="border border-line-strong px-2 py-1.5 font-bold">1</td><td class="border border-line-strong px-2 py-1.5"><strong>B</strong>rackets</td><td class="border border-line-strong px-2 py-1.5">Innermost first</td></tr>
            <tr class="bg-surface"><td class="border border-line-strong px-2 py-1.5 font-bold">2</td><td class="border border-line-strong px-2 py-1.5"><strong>I</strong>ndices — powers and roots</td><td class="border border-line-strong px-2 py-1.5">Left to right</td></tr>
            <tr><td class="border border-line-strong px-2 py-1.5 font-bold">3</td><td class="border border-line-strong px-2 py-1.5"><strong>D</strong>ivision <em>and</em> <strong>M</strong>ultiplication</td><td class="border border-line-strong px-2 py-1.5"><strong>Left to right</strong></td></tr>
            <tr class="bg-surface"><td class="border border-line-strong px-2 py-1.5 font-bold">4</td><td class="border border-line-strong px-2 py-1.5"><strong>A</strong>ddition <em>and</em> <strong>S</strong>ubtraction</td><td class="border border-line-strong px-2 py-1.5"><strong>Left to right</strong></td></tr>
          </tbody>
        </table>
      </section>

      <section class="rounded-xl border-2 border-dashed border-bad-line bg-bad-soft/50 p-4">
        <h2 class="font-display text-base font-bold text-bad-soft-fg">Two myths</h2>
        <p class="mt-2 text-sm text-bad-soft-fg"><strong>✗ Division before multiplication.</strong><br>
          24 ÷ 4 × 3 = 6 × 3 = <strong>18</strong>, not 2.</p>
        <p class="mt-3 text-sm text-bad-soft-fg"><strong>✗ Addition before subtraction.</strong><br>
          20 − 8 + 5 = 12 + 5 = <strong>17</strong>, not 7.</p>
        <p class="mt-3 text-xs text-bad-soft-fg">They share a level. Work left to right.</p>
      </section>
    </div>

    <section class="mt-5 rounded-xl border border-line-strong p-4">
      <h2 class="font-display text-base font-bold">Eight worked examples</h2>
      <div class="mt-3 grid gap-x-8 gap-y-2.5 text-sm sm:grid-cols-2">
        <p><strong>18 + 24 ÷ 6</strong> → 24 ÷ 6 = 4 → 18 + 4 = <strong>22</strong></p>
        <p><strong>(18 + 24) ÷ 6</strong> → 42 ÷ 6 = <strong>7</strong></p>
        <p><strong>40 − 6 × 3</strong> → 18 → 40 − 18 = <strong>22</strong></p>
        <p><strong>5 × 4<sup>2</sup></strong> → 16 → 5 × 16 = <strong>80</strong></p>
        <p><strong>(5 × 4)<sup>2</sup></strong> → 20<sup>2</sup> = <strong>400</strong></p>
        <p><strong>36 ÷ (2 + 4) × 5</strong> → 6 → 6 × 5 = <strong>30</strong></p>
        <p><strong>100 − 20 ÷ 4 − 5</strong> → 5 → 100 − 5 − 5 = <strong>90</strong></p>
        <p><strong>2 + 3 × (8 − 5)<sup>2</sup></strong> → 3<sup>2</sup> = 9 → 27 → <strong>29</strong></p>
      </div>
    </section>

    <section class="mt-5 grid gap-4 sm:grid-cols-2">
      <div class="rounded-xl border border-warn-line bg-warn-soft/60 p-4">
        <h2 class="font-display text-base font-bold">The habit that fixes it</h2>
        <p class="mt-2 text-sm text-strong">Underline the part that happens first <em>before</em> writing anything. One underline, one new line, one step.</p>
        <pre class="mt-3 rounded-lg bg-surface p-3 font-mono text-sm leading-relaxed">100 − 20 ÷ 4 − 5
         ‾‾‾‾‾‾
100 −   5   − 5
‾‾‾‾‾‾‾‾‾
     95     − 5
            90</pre>
      </div>
      <div class="rounded-xl border border-line-strong bg-raise p-4">
        <h2 class="font-display text-base font-bold">Practise it</h2>
        <p class="mt-2 text-sm text-body">Try these, then check on a Math It! worksheet.</p>
        <ol class="mt-3 space-y-1.5 text-sm text-strong">
          <li>1. 7 + 8 × 2 = ______</li>
          <li>2. (7 + 8) × 2 = ______</li>
          <li>3. 48 ÷ 6 × 2 = ______</li>
          <li>4. 60 − 4<sup>2</sup> = ______</li>
          <li>5. 9 + 36 ÷ (5 + 4) = ______</li>
          <li>6. 3 × 5 − 12 ÷ 4 = ______</li>
        </ol>
        <p class="mt-3 text-xs text-soft">Answers: 23 · 30 · 16 · 44 · 13 · 12</p>
      </div>
    </section>"""


# ------------------------------------------------------------ times tables
def _times_grid(blank=False):
    head = '<tr><th class="border border-line bg-invert px-1 py-1 text-invert-fg">×</th>' + "".join(
        f'<th class="border border-line bg-invert px-1 py-1 text-invert-fg">{c}</th>' for c in range(1, 13)
    ) + "</tr>"
    rows = []
    for r in range(1, 13):
        cells = []
        for c in range(1, 13):
            sq = r == c
            if blank:
                cells.append(f'<td class="h-7 border border-line-strong {"bg-warn-soft" if sq else ""}"></td>')
            else:
                cls = "bg-warn-soft font-bold text-warn-soft-fg" if sq else ("bg-raise" if (r + c) % 2 else "")
                cells.append(f'<td class="border border-line-strong px-1 py-1 {cls}">{r*c}</td>')
        rows.append(
            f'<tr><th class="border border-line bg-invert px-1 py-1 text-invert-fg">{r}</th>' + "".join(cells) + "</tr>"
        )
    return (
        '<table class="w-full border-collapse text-center text-[0.78rem] tabular-nums">'
        f"<thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>"
    )


TIMES_TABLES_BODY = f"""    <section class="mt-6">
      <h2 class="font-display text-base font-bold">Multiplication square to 12 × 12</h2>
      <p class="mt-1 text-sm text-soft">Square numbers run down the diagonal, shaded amber.</p>
      <div class="mt-3">{_times_grid(False)}</div>
    </section>

    <section class="mt-6 grid gap-4 sm:grid-cols-2">
      <div class="rounded-xl border border-accent-line bg-accent-soft/60 p-4">
        <h2 class="font-display text-base font-bold">Square numbers</h2>
        <p class="mt-2 text-sm text-strong">1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144</p>
        <h2 class="mt-4 font-display text-base font-bold">Cube numbers</h2>
        <p class="mt-2 text-sm text-strong">1, 8, 27, 64, 125, 216, 343, 512, 729, 1000</p>
      </div>
      <div class="rounded-xl border border-warn-line bg-warn-soft/60 p-4">
        <h2 class="font-display text-base font-bold">Tricks worth knowing</h2>
        <ul class="mt-2 space-y-1.5 text-sm text-strong">
          <li><strong>×4</strong> — double, then double again.</li>
          <li><strong>×8</strong> — double three times.</li>
          <li><strong>×9</strong> — ×10 then subtract one lot. The digits always sum to 9.</li>
          <li><strong>×11</strong> (to 9) — repeat the digit: 7 × 11 = 77.</li>
          <li><strong>×12</strong> — ×10 plus ×2.</li>
          <li><strong>×5</strong> — half of ×10.</li>
        </ul>
      </div>
    </section>

    <section class="mt-6" style="break-before:page">
      <h2 class="font-display text-base font-bold">Blank grid — fill it in against the clock</h2>
      <p class="mt-1 text-sm text-soft">Time yourself. A confident Year 4 should complete this in under five minutes.</p>
      <div class="mt-3">{_times_grid(True)}</div>
      <p class="mt-3 text-sm text-body">Time taken: ________________ &nbsp;&nbsp;·&nbsp;&nbsp; Correct: ________ / 144 &nbsp;&nbsp;·&nbsp;&nbsp; Date: ________________</p>
    </section>"""


SHEETS = [
    dict(filename="fractions-reference-sheet.html",
         title="Fractions reference sheet",
         subtitle="All four operations, mixed numbers, simplifying and key equivalents · Years 4–6",
         description="A free printable one-page fractions reference sheet: multiplying, dividing, adding and subtracting fractions, mixed numbers and fraction-decimal-percentage equivalents.",
         body=FRACTIONS_BODY),
    dict(filename="long-division-reference-sheet.html",
         title="Long division reference sheet",
         subtitle="Short division, the DMSB cycle, a full worked example and multiples lists · Years 5–6",
         description="A free printable long division reference sheet with the divide-multiply-subtract-bring down cycle, a worked 4-digit by 2-digit example and ready-made multiples lists.",
         body=LONG_DIVISION_BODY),
    dict(filename="bidmas-reference-sheet.html",
         title="BIDMAS reference sheet",
         subtitle="The correct hierarchy, the two common myths and eight worked examples · Years 5–6",
         description="A free printable BIDMAS order of operations reference sheet, including the two myths about division and subtraction, with eight worked examples and practice questions.",
         body=BIDMAS_BODY),
    dict(filename="times-tables-grid.html",
         title="Times tables grid to 12 × 12",
         subtitle="A completed multiplication square, square and cube numbers, and a blank grid to time · Years 2–6",
         description="A free printable times tables grid to 12 x 12 with square numbers highlighted, cube numbers, multiplication tricks and a blank grid to complete against the clock.",
         body=TIMES_TABLES_BODY),
]


# Per-sheet print tightening, verified one sheet at a time with
# `node tools/pagecount.js`. Only add rules here when a sheet measures over the
# 281 mm content box; the shared rules in SHEET_SHELL handle everything else.
PRINT_CSS = {
    "long-division-reference-sheet.html": """      .sheet table { font-size: 8pt !important; }
      .sheet td, .sheet th { padding: .35mm !important; line-height: 1.2 !important; }
      .sheet section, .sheet section > div { padding: 2.2mm !important; }
      .sheet h1 { font-size: 17pt !important; }
      .sheet pre { font-size: 7.8pt !important; line-height: 1.3 !important; padding: 1.8mm !important; }
      .sheet .text-sm { font-size: 8.1pt !important; }
      .sheet li { line-height: 1.3 !important; }
""",
    "times-tables-grid.html": """      .sheet table { font-size: 7.4pt !important; }
      .sheet td, .sheet th { padding: .25mm !important; line-height: 1.15 !important; }
      .sheet section, .sheet section > div { padding: 2mm !important; }
      .sheet h1 { font-size: 16pt !important; }
      .sheet h2 { font-size: 9.5pt !important; }
      .sheet .text-sm { font-size: 7.8pt !important; }
      .sheet .text-xs { font-size: 7pt !important; }
      .sheet li { line-height: 1.25 !important; }
""",
}


def build():
    return {
        s["filename"]: SHEET_SHELL.format(
            theme_boot=THEME_BOOT, sun=SUN_ICON, moon=MOON_ICON,
            print_css=PRINT_CSS.get(s["filename"], ""), **s)
        for s in SHEETS
    }
