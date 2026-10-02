# -*- coding: utf-8 -*-
"""Practice generator page for Math It!"""
from shell import ad


def toggle_row(key, title, blurb):
    return f"""              <label class="opt">
                <input type="checkbox" data-setting="{key}">
                <span><span class="font-medium text-strong">{title}</span>
                <span class="mt-0.5 block text-xs leading-snug text-soft">{blurb}</span></span>
              </label>"""


SETTINGS_TOGGLES = "\n".join([
    toggle_row("compact", "Compact density",
               "Tighter padding and text, so more questions fit on one screen or one sheet of paper."),
    toggle_row("contrast", "High contrast",
               "Heavier borders and maximum contrast, for low vision or a bright classroom."),
    toggle_row("showKey", "Show the answer key on screen",
               "Adds a numbered answer list under the sheet. Handy when you are marking by hand."),
    toggle_row("showNumbers", "Show question numbers",
               "Numbers each question so a class can call out answers by number."),
    toggle_row("autoAdvance", "Enter moves to the next box",
               "Keeps hands on the keyboard. Press Enter on the last box to mark the sheet."),
    toggle_row("hideTopicTags", "Hide topic labels",
               "Turn this off to print the topic name beside every question, which helps with diagnosis."),
])

KBD = 'rounded border border-line bg-raise px-1 font-mono text-[0.95em]'

PRINT_MENU_ITEMS = [
    ("worksheet", "Questions only", "The worksheet with blank boxes. No answers."),
    ("answers", "Answer key only", "A numbered list of answers on its own page."),
    ("both", "Questions and answer key", "The worksheet, then the key on a fresh page."),
]


def _print_menu():
    rows = []
    for mode, title, blurb in PRINT_MENU_ITEMS:
        rows.append(
            f'<button type="button" role="menuitem" data-print-mode="{mode}" '
            f'class="block w-full rounded-md px-3 py-2 text-left transition-colors hover:bg-raise">'
            f'<span class="block text-sm font-semibold text-strong">{title}</span>'
            f'<span class="mt-0.5 block text-xs text-soft">{blurb}</span></button>'
        )
    return "\n              ".join(rows)


BODY = f"""  <main id="main" class="mx-auto max-w-page px-4 py-6 sm:px-6 lg:px-8">

    <!-- ===================== PRINT-ONLY HEADER ===================== -->
    <div class="print-only sheet-head" style="margin-bottom:6mm">
      <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:10mm;border-bottom:1pt solid #000;padding-bottom:3mm">
        <div>
          <div style="font-size:14pt;font-weight:700">Math It! · <span data-sheet-title>Mental maths</span></div>
          <div style="font-size:9pt;color:#444;margin-top:1mm">Sheet <span data-sheet-id>#000000</span> · <span data-print-date></span> · www.mathit.co.uk</div>
        </div>
        <div style="font-size:10pt;text-align:right;white-space:nowrap">
          Name: <span style="display:inline-block;width:42mm;border-bottom:0.6pt solid #000"></span>
          &nbsp;&nbsp;Class: <span style="display:inline-block;width:20mm;border-bottom:0.6pt solid #000"></span><br>
          <span style="display:inline-block;margin-top:2.5mm">Date: <span style="display:inline-block;width:28mm;border-bottom:0.6pt solid #000"></span>
          &nbsp;&nbsp;Score: <span style="display:inline-block;width:14mm;border-bottom:0.6pt solid #000"></span> / <span data-sheet-count>36</span></span>
        </div>
      </div>
    </div>

    <!-- ===================== BREADCRUMBS ===================== -->
    <nav class="breadcrumbs mb-5 flex items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
      <a href="index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <a href="index.html#choose" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Worksheets</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <span class="font-semibold text-strong" data-crumb-current aria-current="page">Year 5 · Medium</span>
    </nav>

    <div class="grid gap-8 lg:grid-cols-12">

      <!-- ================= MAIN COLUMN ================= -->
      <div class="lg:col-span-9">

        <!-- Sheet header -->
        <div class="mi-screen-only mb-5 flex flex-wrap items-end justify-between gap-4">
          <div class="min-w-0">
            <h1 class="font-display text-3xl font-bold tracking-tight sm:text-4xl" data-sheet-title>Year 5 · Medium mental maths</h1>
            <p class="mt-1.5 text-soft" data-sheet-sub>36 questions · Expected standard.</p>
          </div>
          <div class="flex items-center gap-3">
            <div data-timer class="hidden items-center gap-2 rounded-lg border border-line bg-surface px-3 py-2">
              <svg viewBox="0 0 20 20" class="h-4 w-4 text-accent-text" fill="currentColor" aria-hidden="true"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zm1 8.6V5H9v6.4l4 2.4 1-1.7z"/></svg>
              <span class="font-mono text-lg font-bold tabular-nums text-strong" data-timer-value>0:00</span>
              <button type="button" data-timer-toggle class="rounded-md px-2 py-1 text-xs font-bold uppercase tracking-wider text-accent-text hover:bg-accent-soft">Start</button>
              <button type="button" data-timer-reset class="rounded-md px-2 py-1 text-xs font-bold uppercase tracking-wider text-faint hover:bg-raise">Reset</button>
            </div>
            <span class="chip font-mono" title="Share this link and everyone gets an identical sheet">Sheet <span data-sheet-id>#000000</span></span>
          </div>
        </div>

        <!-- ================= TOOLBAR ================= -->
        <div class="toolbar sticky top-[4.3rem] z-30 mb-6 rounded-xl border border-line bg-surface/95 p-3 backdrop-blur">
          <div class="flex flex-wrap items-center gap-2">
            <button type="button" data-action="new" class="btn btn-primary">
              <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M10 3a7 7 0 106.33 4h-2.2A5 5 0 1110 5c1.3 0 2.47.5 3.36 1.3L11 8.6h6V2.6l-2.2 2.2A6.97 6.97 0 0010 3z"/></svg>
              New
            </button>
            <button type="button" data-action="reset" class="btn btn-ghost">
              <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M5 4h10a1 1 0 011 1v2H4V5a1 1 0 011-1zm-1 5h12v6a2 2 0 01-2 2H6a2 2 0 01-2-2V9zm3 2v4h2v-4H7zm4 0v4h2v-4h-2z"/></svg>
              Reset
            </button>
            <button type="button" data-action="mark" class="btn btn-dark">
              <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M7.6 14.2L3.4 10l1.4-1.4 2.8 2.8 7-7L16 5.8z"/></svg>
              Mark
            </button>
            <button type="button" data-action="answers" aria-pressed="false" class="btn btn-ghost">
              <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M10 4c-4 0-7.3 2.5-9 6 1.7 3.5 5 6 9 6s7.3-2.5 9-6c-1.7-3.5-5-6-9-6zm0 10a4 4 0 110-8 4 4 0 010 8zm0-2a2 2 0 100-4 2 2 0 000 4z"/></svg>
              <span data-answer-label>Answers</span>
            </button>

            <!-- Print split button -->
            <div class="relative" data-print-menu-wrap>
              <div class="flex">
                <button type="button" data-action="print" class="btn btn-ghost rounded-r-none">
                  <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M6 2h8v4H6V2zm-2 5h12a2 2 0 012 2v5h-3v3H5v-3H2V9a2 2 0 012-2zm3 7v3h6v-3H7zm7-3.5a1 1 0 100-2 1 1 0 000 2z"/></svg>
                  Print
                </button>
                <button type="button" data-print-menu-toggle aria-expanded="false" aria-haspopup="menu"
                        class="btn btn-ghost -ml-px rounded-l-none px-2" aria-label="Print options">
                  <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M10 13L4 7h12z"/></svg>
                </button>
              </div>
              <div data-print-menu role="menu"
                   class="absolute right-0 z-40 mt-2 hidden w-72 rounded-xl border border-line bg-surface p-2 shadow-pop">
                {_print_menu()}
                <div class="my-2 border-t border-line"></div>
                <div class="px-3 pb-1 pt-1">
                  <p class="text-sm font-semibold text-strong">Print a class set</p>
                  <p class="mt-0.5 text-xs leading-snug text-soft">Different sheets, one per child, printed in a single job.</p>
                  <div class="mt-2.5 flex items-center gap-2">
                    <label for="set-classsize" class="sr-only">Number of sheets</label>
                    <input id="set-classsize" type="number" min="2" max="35" value="6" data-setting="classSetSize"
                           class="field w-20 py-1.5 text-center font-mono">
                    <label class="flex items-center gap-1.5 text-xs text-soft">
                      <input type="checkbox" data-setting="classSetKeys" class="h-4 w-4 rounded border-line-strong text-accent focus:ring-accent">
                      with keys
                    </label>
                    <button type="button" data-print-mode="set" class="btn btn-primary btn-sm ml-auto">Print set</button>
                  </div>
                </div>
              </div>
            </div>

            <button type="button" data-drawer-toggle aria-expanded="false" aria-controls="settings-drawer"
                    class="btn btn-ghost ml-auto">
              <svg viewBox="0 0 20 20" class="h-4 w-4" fill="currentColor" aria-hidden="true"><path d="M8.3 2h3.4l.4 2.2 1.6.9 2.1-.8 1.7 3-1.7 1.4V10l1.7 1.4-1.7 3-2.1-.8-1.6.9-.4 2.2H8.3l-.4-2.2-1.6-.9-2.1.8-1.7-3L4.2 10V8.7L2.5 7.3l1.7-3 2.1.8 1.6-.9L8.3 2zm1.7 5.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5z"/></svg>
              Settings
              <svg data-drawer-chevron viewBox="0 0 20 20" class="h-4 w-4 transition-transform" fill="currentColor" aria-hidden="true"><path d="M10 13L4 7h12z"/></svg>
            </button>
          </div>

          <!-- Progress -->
          <div class="mt-3 flex items-center gap-3 px-1">
            <div class="h-1 flex-1 overflow-hidden rounded-full bg-sunken">
              <div data-progress-bar class="h-full w-0 rounded-full bg-accent transition-all duration-200"></div>
            </div>
            <span data-progress-text class="shrink-0 font-mono text-xs tabular-nums text-soft">0 / 36 answered</span>
          </div>

          <p class="mt-2 hidden px-1 text-xs text-faint sm:block">
            Keyboard: <kbd class="{KBD}">N</kbd> new ·
            <kbd class="{KBD}">M</kbd> mark ·
            <kbd class="{KBD}">A</kbd> answers ·
            <kbd class="{KBD}">R</kbd> reset ·
            <kbd class="{KBD}">P</kbd> print ·
            <kbd class="{KBD}">Ctrl</kbd>+<kbd class="{KBD}">Enter</kbd> mark from any box
          </p>
        </div>

        <!-- ================= SETTINGS DRAWER ================= -->
        <section id="settings-drawer" data-drawer class="settings-drawer mb-6 hidden scroll-mt-40 rounded-xl border border-line bg-surface"
                 aria-label="Advanced worksheet settings">
          <div class="flex items-center justify-between border-b border-line px-6 py-4">
            <div>
              <h2 class="font-display text-xl font-bold">Worksheet settings</h2>
              <p class="mt-0.5 text-sm text-soft">Changes apply straight away and are remembered on this device.</p>
            </div>
            <button type="button" data-drawer-close class="btn btn-ghost btn-sm">Close</button>
          </div>

          <div class="grid gap-8 p-6 lg:grid-cols-12">

            <!-- Column 1: the sheet itself -->
            <div class="lg:col-span-5">
              <h3 class="label">The sheet</h3>
              <div class="mt-3 grid gap-4 sm:grid-cols-2">
                <div>
                  <label for="set-year" class="mb-1.5 block text-sm font-medium text-body">Year group</label>
                  <select id="set-year" data-setting="year" class="field">
                    <option value="2">Year 2</option>
                    <option value="3">Year 3</option>
                    <option value="4">Year 4</option>
                    <option value="5">Year 5</option>
                    <option value="6">Year 6</option>
                  </select>
                </div>
                <div>
                  <label for="set-level" class="mb-1.5 block text-sm font-medium text-body">Difficulty</label>
                  <select id="set-level" data-setting="level" class="field">
                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>
                  </select>
                </div>
                <div>
                  <label for="set-count" class="mb-1.5 block text-sm font-medium text-body">Questions</label>
                  <select id="set-count" data-setting="count" class="field">
                    <option value="12">12</option>
                    <option value="18">18</option>
                    <option value="24">24</option>
                    <option value="36">36 (default)</option>
                    <option value="48">48</option>
                    <option value="60">60</option>
                  </select>
                </div>
                <div>
                  <label for="set-font" class="mb-1.5 block text-sm font-medium text-body">Text size</label>
                  <select id="set-font" data-setting="fontScale" class="field">
                    <option value="normal">Standard</option>
                    <option value="large">Large</option>
                    <option value="xlarge">Extra large</option>
                  </select>
                </div>
              </div>

              <h3 class="label mt-8">Appearance</h3>
              <div class="mt-3 flex flex-wrap items-center gap-3">
                <div class="seg" role="group" aria-label="Colour theme">
                  <button type="button" data-theme-set="auto">Auto</button>
                  <button type="button" data-theme-set="light">Light</button>
                  <button type="button" data-theme-set="dark">Dark</button>
                </div>
                <span class="text-xs text-soft">Currently: <span data-theme-label class="font-semibold text-strong">Light</span></span>
              </div>

              <h3 class="label mt-8">Timer</h3>
              <div class="mt-3 grid gap-4 sm:grid-cols-2">
                <div>
                  <label for="set-timer" class="mb-1.5 block text-sm font-medium text-body">Mode</label>
                  <select id="set-timer" data-setting="timerMode" class="field">
                    <option value="off">Off</option>
                    <option value="stopwatch">Stopwatch (count up)</option>
                    <option value="countdown">Countdown (against the clock)</option>
                  </select>
                </div>
                <div data-countdown-row class="hidden">
                  <label for="set-mins" class="mb-1.5 block text-sm font-medium text-body">Minutes</label>
                  <select id="set-mins" data-setting="countdownMins" class="field">
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="5">5</option>
                    <option value="8">8</option>
                    <option value="10">10</option>
                    <option value="15">15</option>
                    <option value="20">20</option>
                  </select>
                </div>
              </div>
              <p class="mt-2 text-xs leading-relaxed text-soft">
                The stopwatch starts when the first answer box is clicked. Countdown mode marks the
                sheet automatically at zero.
              </p>

              <h3 class="label mt-8">Display and accessibility</h3>
              <div class="mt-3 grid gap-2">
{SETTINGS_TOGGLES}
              </div>

              <h3 class="label mt-8">Share this exact sheet</h3>
              <div class="mt-3 flex gap-2">
                <input type="text" data-share-url readonly class="field font-mono text-xs" aria-label="Shareable worksheet link">
                <button type="button" data-copy-link class="btn btn-ghost shrink-0">Copy</button>
              </div>
              <p class="mt-2 text-xs leading-relaxed text-soft">
                The link carries the year, difficulty, your topic selection and the sheet number, so
                everyone who opens it gets the identical worksheet.
              </p>
            </div>

            <!-- Column 2: topics -->
            <div class="lg:col-span-7">
              <div class="flex flex-wrap items-center justify-between gap-3">
                <div>
                  <h3 class="label">Question types</h3>
                  <p class="mt-1 text-sm text-soft"><span data-topic-count>0 of 0</span> topics active for this year group.</p>
                </div>
                <div class="flex gap-2">
                  <button type="button" data-topics-all class="btn btn-sm btn-ghost">Select all</button>
                  <button type="button" data-topics-core class="btn btn-sm btn-ghost">Core arithmetic only</button>
                </div>
              </div>
              <div data-topic-list class="mt-4 grid gap-4"></div>
            </div>
          </div>
        </section>

        <!-- ================= SCORE BANNER ================= -->
        <div data-score-banner class="score-banner hidden" role="status" aria-live="polite"></div>

        <!-- ================= WORKSHEET ================= -->
        <section class="worksheet-shell card p-5 sm:p-7" aria-label="Worksheet questions">
          <noscript>
            <div class="note-warn mt-0 text-sm">
              <strong>JavaScript is switched off.</strong> Math It! builds every worksheet in your
              browser, so the questions cannot be generated. Please enable JavaScript, or read the
              <a href="resources.html" class="link">topic guides</a>, which are fully readable without it.
            </div>
          </noscript>
          <div data-sheet class="q-grid"></div>
        </section>

        <!-- ================= ANSWER KEY ================= -->
        <section class="answer-key mt-8" aria-label="Answer key">
          <div class="card p-5 sm:p-7">
            <div class="flex flex-wrap items-baseline justify-between gap-3 border-b border-line pb-3">
              <h2 class="font-display text-xl font-bold">Answer key</h2>
              <p class="font-mono text-xs text-soft">Sheet <span data-sheet-id>#000000</span> · <span data-sheet-title>Year 5 · Medium</span></p>
            </div>
            <div data-answer-key class="ak-grid mt-4"></div>
          </div>
        </section>

        <!-- ================= CLASS SET (print only) ================= -->
        <div class="class-set" data-class-set aria-hidden="true"></div>

        <!-- ================= AD: BELOW SHEET ================= -->
        <div class="mi-screen-only mt-8">
          {ad("practice-footer", size="728 × 90", shape="leaderboard")}
        </div>

        <!-- ================= SUPPORTING CONTENT ================= -->
        <section class="mi-screen-only article mt-12 max-w-none">
          <h2 class="font-display text-2xl font-bold sm:text-3xl">Getting the most from this worksheet</h2>
          <p>
            A sheet is meant to be finished in one short sitting. Thirty-six questions is about ten
            to fifteen minutes for most primary children: long enough to cover every topic in the
            year group, short enough that concentration holds to the last question. If a sheet
            regularly takes more than twenty minutes, drop a difficulty level rather than pushing on.
          </p>

          <h3>Work down the columns, not across</h3>
          <p>
            Questions run in two columns of eighteen, numbered down the left column first. That
            matches the layout of most arithmetic papers and makes it easy to call out answers by
            number when marking with a group. On a phone the columns collapse into one list and the
            numbering stays the same.
          </p>

          <h3>Typing answers</h3>
          <ul>
            <li><strong>Fractions</strong>: type a slash, <code>3/4</code>. Any equivalent fraction is accepted, so <code>6/8</code> is correct too.</li>
            <li><strong>Mixed numbers</strong>: put a space between the whole number and the fraction, <code>2 1/4</code>. The improper form <code>9/4</code> also works.</li>
            <li><strong>Remainders</strong>: <code>12 r 3</code>, <code>12r3</code> and <code>12 remainder 3</code> all work.</li>
            <li><strong>Ratios</strong>: use a colon, <code>3:4</code> or <code>3 : 4</code>.</li>
            <li><strong>Negative numbers</strong>: a plain hyphen is fine, <code>-7</code>.</li>
            <li><strong>Decimals and money</strong>: digits only. Commas are ignored, so <code>1,560</code> and <code>1560</code> both mark correct.</li>
          </ul>

          <h3>Marking, and what to do next</h3>
          <p>
            <strong>Mark</strong> scores every box that has something in it. Correct answers turn
            green; incorrect ones turn red with the right answer beside them. The score card lists
            the topics that produced mistakes, and that list is the most useful thing on the page.
            One error in a topic is noise. Three errors in the same topic across a week is a
            teaching point.
          </p>
          <p>
            <strong>Answers</strong> reveals every solution without scoring, which suits a child
            self-checking as they go. <strong>Reset</strong> empties the boxes but keeps the same
            questions, so they can have a second attempt at a sheet they found hard.
          </p>

          <h3>Printing</h3>
          <p>
            The arrow next to <strong>Print</strong> opens the print options. You can print the
            questions on their own, the answer key on its own, or both with the key on a fresh page.
            Either way the navigation, sidebar, adverts and score banner are removed, and the sheet
            prints black on white whichever theme you are using on screen.
          </p>
          <p>
            <strong>Print a class set</strong> generates several different sheets at the same year
            and difficulty, each on its own page, with optional answer keys. Set the number of
            sheets, press the button, and send the whole lot to the printer in one job. Sheet
            numbers are sequential from the current sheet, so you can always reprint an individual
            copy from its link later.
          </p>

          <div class="note">
            <h3 class="mt-0 font-display text-lg font-bold text-strong">Targeting a single topic</h3>
            <p class="mt-2 text-body">
              Open <strong>Settings</strong>, press <em>Select all</em> to clear the slate, then tick
              only the topic you are working on. Thirty-six questions on nothing but fraction
              division makes a good intervention, and the link can be shared with a parent for
              homework.
            </p>
          </div>

          <h3>Where to read more</h3>
          <p>
            If a topic needs explaining rather than practising, the
            <a href="resources.html" class="link">topic guides</a> walk through the standard written
            methods with worked examples and the mistakes children most commonly make:
            <a href="resources.html#fractions" class="link">fractions</a>,
            <a href="resources.html#long-division" class="link">long division</a>,
            <a href="resources.html#order-of-operations" class="link">order of operations</a> and
            <a href="resources.html#decimal-multiplication" class="link">decimal multiplication</a>.
          </p>
        </section>
      </div>

      <!-- ================= SIDEBAR ================= -->
      <aside class="mi-screen-only lg:col-span-3" aria-label="Sidebar">
        <div class="space-y-6 lg:sticky lg:top-24">
          {ad("practice-sidebar-top", size="300 × 250", shape="box")}

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">This session</h2>
            <dl class="mt-3 grid grid-cols-3 gap-2 text-center">
              <div class="rounded-lg border border-line bg-raise py-2">
                <dt class="stat-cap">Sheets</dt>
                <dd class="font-mono text-lg font-bold text-strong" data-stat="sheets">0</dd>
              </div>
              <div class="rounded-lg border border-line bg-raise py-2">
                <dt class="stat-cap">Average</dt>
                <dd class="font-mono text-lg font-bold text-strong" data-stat="avg">–</dd>
              </div>
              <div class="rounded-lg border border-line bg-raise py-2">
                <dt class="stat-cap">Best</dt>
                <dd class="font-mono text-lg font-bold text-strong" data-stat="best">–</dd>
              </div>
            </dl>
            <h3 class="label mt-4">Recent sheets</h3>
            <ul data-recent class="mt-2 space-y-1 text-sm">
              <li class="text-soft">Nothing marked yet today.</li>
            </ul>
            <button type="button" data-clear-history class="mt-3 text-xs font-semibold text-soft underline underline-offset-2 hover:text-strong">Clear history</button>
          </div>

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Quick switch</h2>
            <div class="mt-3 grid grid-cols-5 gap-1.5">
              <a href="practice.html?year=2&amp;level=medium" class="rounded-md border border-line bg-surface py-2 text-center text-sm font-bold text-body hover:border-accent hover:bg-accent-soft">2</a>
              <a href="practice.html?year=3&amp;level=medium" class="rounded-md border border-line bg-surface py-2 text-center text-sm font-bold text-body hover:border-accent hover:bg-accent-soft">3</a>
              <a href="practice.html?year=4&amp;level=medium" class="rounded-md border border-line bg-surface py-2 text-center text-sm font-bold text-body hover:border-accent hover:bg-accent-soft">4</a>
              <a href="practice.html?year=5&amp;level=medium" class="rounded-md border border-line bg-surface py-2 text-center text-sm font-bold text-body hover:border-accent hover:bg-accent-soft">5</a>
              <a href="practice.html?year=6&amp;level=medium" class="rounded-md border border-line bg-surface py-2 text-center text-sm font-bold text-body hover:border-accent hover:bg-accent-soft">6</a>
            </div>
            <div class="mt-2 grid grid-cols-3 gap-1.5">
              <a href="practice.html?year=5&amp;level=easy" class="rounded-md border border-line bg-surface py-2 text-center text-xs font-bold text-body hover:border-warn hover:bg-warn-soft">Easy</a>
              <a href="practice.html?year=5&amp;level=medium" class="rounded-md border border-line bg-surface py-2 text-center text-xs font-bold text-body hover:border-warn hover:bg-warn-soft">Medium</a>
              <a href="practice.html?year=5&amp;level=hard" class="rounded-md border border-line bg-surface py-2 text-center text-xs font-bold text-body hover:border-warn hover:bg-warn-soft">Hard</a>
            </div>
          </div>

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Answer formats</h2>
            <dl class="mt-3 space-y-2 text-sm">
              <div class="flex justify-between gap-3"><dt class="text-soft">Fraction</dt><dd class="font-mono text-strong">3/4</dd></div>
              <div class="flex justify-between gap-3"><dt class="text-soft">Mixed number</dt><dd class="font-mono text-strong">2 1/4</dd></div>
              <div class="flex justify-between gap-3"><dt class="text-soft">Remainder</dt><dd class="font-mono text-strong">12 r 3</dd></div>
              <div class="flex justify-between gap-3"><dt class="text-soft">Ratio</dt><dd class="font-mono text-strong">3 : 4</dd></div>
              <div class="flex justify-between gap-3"><dt class="text-soft">Negative</dt><dd class="font-mono text-strong">-7</dd></div>
              <div class="flex justify-between gap-3"><dt class="text-soft">Decimal</dt><dd class="font-mono text-strong">0.28</dd></div>
            </dl>
          </div>

          {ad("practice-sidebar-bottom", size="300 × 600", shape="tall")}

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Stuck on a method?</h2>
            <ul class="mt-3 space-y-2 text-sm">
              <li><a href="resources.html#fractions" class="link">Fractions, four operations</a></li>
              <li><a href="resources.html#long-division" class="link">Long division, step by step</a></li>
              <li><a href="resources.html#order-of-operations" class="link">BIDMAS without the myths</a></li>
              <li><a href="resources.html#decimal-multiplication" class="link">Multiplying decimals</a></li>
              <li><a href="resources.html#downloads" class="link">Printable reference sheets</a></li>
            </ul>
          </div>
        </div>
      </aside>
    </div>
  </main>"""
