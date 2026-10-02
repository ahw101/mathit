# -*- coding: utf-8 -*-
"""Renderer for the per-topic guide pages (guides/<slug>.html).

Each guide is a plain dict (see guides_data.py). This module turns one into
a full page body: breadcrumbs, intro, method steps, worked examples, common
mistakes, free prose sections, a practice CTA, related guides and an FAQ.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shell import ad  # noqa: E402
from guides_data import GUIDES, BY_SLUG, CATEGORIES  # noqa: E402

PRE = "../"


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------- fragments
def _crumbs(g):
    return f"""    <nav class="breadcrumbs mb-6 flex flex-wrap items-center gap-1.5 text-sm text-soft" aria-label="Breadcrumb">
      <a href="{PRE}index.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Home</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <a href="{PRE}resources.html" class="rounded px-1 py-0.5 hover:text-accent-text hover:underline">Guides</a>
      <span aria-hidden="true" class="text-faint">/</span>
      <span class="font-semibold text-strong" aria-current="page">{g['nav']}</span>
    </nav>"""


def _steps(g):
    if not g.get("steps"):
        return ""
    items = []
    for i, (title, body) in enumerate(g["steps"], 1):
        items.append(f"""        <li class="relative pl-12">
          <span class="absolute left-0 top-0 flex h-8 w-8 items-center justify-center rounded-lg bg-invert font-mono text-sm font-bold text-invert-fg">{i}</span>
          <h3 class="font-display text-lg font-bold text-strong">{title}</h3>
          <div class="mt-1.5 text-body">{body}</div>
        </li>""")
    inner = "\n".join(items)
    return f"""
      <section id="method" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">The method, step by step</h2>
        <ol class="mt-6 space-y-6">
{inner}
        </ol>
      </section>"""


def _examples(g):
    if not g.get("examples"):
        return ""
    blocks = []
    for n, (q, lines, ans) in enumerate(g["examples"], 1):
        rows = "\n".join(
            f'            <li class="flex gap-3"><span class="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-accent"></span><span>{ln}</span></li>'
            for ln in lines
        )
        blocks.append(f"""        <figure class="rounded-2xl border border-line bg-surface p-6 shadow-card">
          <figcaption class="flex flex-wrap items-baseline justify-between gap-2 border-b border-line pb-3">
            <span class="kicker">Worked example {n}</span>
            <span class="font-mono text-xl font-bold text-strong">{q}</span>
          </figcaption>
          <ul class="mt-4 space-y-2.5 text-body">
{rows}
          </ul>
          <p class="mt-4 rounded-lg bg-accent-soft px-4 py-2.5 font-mono text-lg font-bold text-accent-soft-fg">{ans}</p>
        </figure>""")
    inner = "\n".join(blocks)
    return f"""
      <section id="examples" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Worked examples</h2>
        <div class="mt-6 grid gap-5">
{inner}
        </div>
      </section>"""


def _mistakes(g):
    if not g.get("mistakes"):
        return ""
    rows = []
    for wrong, fix in g["mistakes"]:
        rows.append(f"""          <div class="rounded-xl border border-line bg-surface p-5">
            <p class="flex items-start gap-2.5 font-semibold text-strong">
              <span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-bad-soft text-xs font-bold text-bad-soft-fg">✕</span>
              <span>{wrong}</span>
            </p>
            <p class="mt-2.5 flex items-start gap-2.5 text-body">
              <span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-accent-soft text-xs font-bold text-accent-soft-fg">✓</span>
              <span>{fix}</span>
            </p>
          </div>""")
    inner = "\n".join(rows)
    return f"""
      <section id="mistakes" class="mt-10 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Where it usually goes wrong</h2>
        <div class="mt-6 grid gap-4 sm:grid-cols-2">
{inner}
        </div>
      </section>"""


def _sections(g):
    if not g.get("sections"):
        return ""
    out = []
    for i, (h2, html) in enumerate(g["sections"]):
        out.append(f"""      <section class="article mt-10 max-w-none">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">{h2}</h2>
        {html}
      </section>""")
        if i == 0 and len(g["sections"]) > 2:
            out.append(f'      <div class="mt-8">{ad("guide-inarticle", size="728 × 90", shape="leaderboard")}</div>')
    return "\n".join(out)


def _faq(g):
    if not g.get("faqs"):
        return ""
    items = "\n".join(f"""          <details class="group rounded-xl border border-line bg-surface px-5 py-4 open:bg-raise">
            <summary class="flex cursor-pointer list-none items-center justify-between gap-4 font-semibold text-strong">
              <span>{q}</span>
              <svg viewBox="0 0 20 20" class="h-5 w-5 shrink-0 text-faint transition-transform group-open:rotate-180" fill="currentColor" aria-hidden="true"><path d="M10 13L4 7h12z"/></svg>
            </summary>
            <div class="mt-3 border-t border-line pt-3 text-body">{a}</div>
          </details>""" for q, a in g["faqs"])
    return f"""
      <section id="faq" class="mt-12 scroll-mt-24">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Questions people ask</h2>
        <div class="mt-6 grid gap-3">
{items}
        </div>
      </section>"""


def related_slugs(g):
    if g.get("related"):
        return [s for s in g["related"] if s in BY_SLUG][:4]
    same = [x["slug"] for x in GUIDES if x["cat"] == g["cat"] and x["slug"] != g["slug"]]
    others = [x["slug"] for x in GUIDES if x["cat"] != g["cat"]]
    return (same + others)[:4]


def _related(g):
    out = []
    for s in related_slugs(g):
        o = BY_SLUG[s]
        out.append(f"""          <a href="{s}.html" class="group flex flex-col rounded-xl border border-line bg-surface p-5 transition-colors hover:border-accent hover:bg-accent-soft">
            <span class="kicker">{o['cat']}</span>
            <span class="mt-1.5 font-display text-lg font-bold text-strong group-hover:text-accent-soft-fg">{o['nav']}</span>
            <span class="mt-1 text-sm text-soft">{o['card']}</span>
          </a>""")
    inner = "\n".join(out)
    return f"""
      <section class="mt-12">
        <h2 class="font-display text-2xl font-bold tracking-tight sm:text-3xl">Carry on from here</h2>
        <div class="mt-6 grid gap-4 sm:grid-cols-2">
{inner}
        </div>
      </section>"""


def _cta(g):
    label, href = g["cta"]
    return f"""
      <section class="mt-10 overflow-hidden rounded-2xl bg-invert p-7 text-invert-fg sm:p-9">
        <span class="kicker text-invert-soft">Practise it</span>
        <h2 class="mt-2 font-display text-2xl font-bold tracking-tight sm:text-3xl">{label}</h2>
        <p class="mt-2.5 max-w-xl text-invert-soft">
          Reading about a method only gets you so far. Generate a fresh sheet, work through it,
          and mark it in one click — the questions change every time, so it never turns into
          memorising one worksheet.
        </p>
        <div class="mt-6 flex flex-wrap gap-3">
          <a href="{PRE}{href}" class="btn btn-lg bg-canvas text-strong hover:bg-raise">Open the generator</a>
          <a href="{PRE}resources.html" class="btn btn-lg border border-invert-soft/40 text-invert-fg hover:bg-white/10">All 30 guides</a>
        </div>
      </section>"""


def _onpage_nav(g):
    links = []
    if g.get("steps"):
        links.append(("#method", "The method"))
    if g.get("examples"):
        links.append(("#examples", "Worked examples"))
    if g.get("mistakes"):
        links.append(("#mistakes", "Common mistakes"))
    if g.get("faqs"):
        links.append(("#faq", "Questions"))
    inner = "\n".join(
        f'            <li><a href="{h}" class="block rounded-md px-3 py-1.5 text-sm text-soft transition-colors hover:bg-accent-soft hover:text-accent-soft-fg">{t}</a></li>'
        for h, t in links
    )
    return f"""          <nav class="card p-4" aria-label="On this page">
            <h2 class="label px-3">On this page</h2>
            <ul class="mt-1.5">
{inner}
            </ul>
          </nav>"""


def _sidebar_guides(g):
    """Other guides in the same category."""
    same = [x for x in GUIDES if x["cat"] == g["cat"] and x["slug"] != g["slug"]][:6]
    if not same:
        return ""
    inner = "\n".join(
        f'              <li><a href="{x["slug"]}.html" class="link">{x["nav"]}</a></li>' for x in same
    )
    return f"""          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">More on {g['cat'].lower()}</h2>
            <ul class="mt-3 space-y-2 text-sm">
{inner}
            </ul>
          </div>"""


# --------------------------------------------------------------- page body
def body(g):
    label, href = g["cta"]
    return f"""  <main id="main" class="mx-auto max-w-page px-4 py-8 sm:px-6 lg:px-8">
{_crumbs(g)}

    <div class="grid gap-10 lg:grid-cols-12">
      <article class="lg:col-span-8">
        <span class="kicker">{g['cat']}</span>
        <h1 class="mt-2 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.6rem] lg:leading-[1.1]">{g['h1']}</h1>
        <div class="mt-4 flex flex-wrap items-center gap-2 text-sm">
          <span class="chip">{g['years']}</span>
          <span class="chip">{g['read']} min read</span>
          <a href="{PRE}{href}" class="chip hover:border-accent hover:bg-accent-soft hover:text-accent-soft-fg">Practise this &rarr;</a>
        </div>

        <div class="article mt-6 max-w-none text-lg">
          {g['intro']}
        </div>

        <div class="mt-8">
          {ad("guide-top", size="728 × 90", shape="leaderboard")}
        </div>
{_steps(g)}
{_examples(g)}
{_mistakes(g)}
{_sections(g)}
{_cta(g)}
{_faq(g)}
{_related(g)}

        <p class="mt-10 border-t border-line pt-5 text-sm text-soft">
          Written by the Math It! team for parents, tutors and primary teachers in the UK.
          Spotted something wrong? <a href="{PRE}contact.html" class="link">Tell us</a> and we will fix it.
        </p>
      </article>

      <aside class="lg:col-span-4" aria-label="Sidebar">
        <div class="space-y-6 lg:sticky lg:top-24">
{_onpage_nav(g)}

          <div class="card p-5">
            <h2 class="font-display text-lg font-bold">Make a worksheet</h2>
            <p class="mt-1.5 text-sm text-soft">36 fresh questions, marked instantly, printed on one A4 page.</p>
            <a href="{PRE}{href}" class="btn btn-primary mt-4 w-full">Start practising</a>
            <a href="{PRE}tables.html" class="btn btn-ghost btn-sm mt-2 w-full">Times tables drill</a>
          </div>

          {ad("guide-sidebar", size="300 × 250", shape="box")}

{_sidebar_guides(g)}

          {ad("guide-sidebar-bottom", size="300 × 600", shape="tall")}
        </div>
      </aside>
    </div>
  </main>"""


# --------------------------------------------------------------- hub index
def hub_cards():
    out = []
    for cat in CATEGORIES:
        gs = [g for g in GUIDES if g["cat"] == cat]
        items = "\n".join(f"""            <li>
              <a href="guides/{g['slug']}.html" class="group flex items-start gap-3 rounded-lg px-3 py-2.5 transition-colors hover:bg-accent-soft">
                <span class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-accent-line group-hover:bg-accent"></span>
                <span>
                  <span class="block font-semibold text-strong group-hover:text-accent-soft-fg">{g['nav']}</span>
                  <span class="mt-0.5 block text-sm leading-snug text-soft">{g['card']}</span>
                </span>
              </a>
            </li>""" for g in gs)
        out.append(f"""        <div class="rounded-2xl border border-line bg-surface p-6 shadow-card">
          <div class="flex items-baseline justify-between gap-3 border-b border-line pb-3">
            <h3 class="font-display text-xl font-bold">{cat}</h3>
            <span class="font-mono text-xs text-faint">{len(gs)} guide{'s' if len(gs) != 1 else ''}</span>
          </div>
          <ul class="mt-3 -mx-3">
{items}
          </ul>
        </div>""")
    return "\n".join(out)
