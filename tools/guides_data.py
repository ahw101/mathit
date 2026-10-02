# -*- coding: utf-8 -*-
"""Aggregates the 30 topic guides into one ordered list.

Each guide dict has:
    slug      url stem, lives at guides/<slug>.html
    cat       category heading (must appear in CATEGORIES)
    nav       short label for nav, cards and breadcrumbs
    h1        page heading
    card      one-line blurb for hub and related cards
    years     year-group chip, e.g. "Years 4-6"
    read      estimated reading minutes
    seo       <title>
    desc      meta description
    keywords  meta keywords
    intro     HTML paragraphs
    steps     [(title, html), ...]            -> numbered method
    examples  [(question, [lines], answer)]   -> worked examples
    mistakes  [(wrong, fix), ...]
    sections  [(h2, html), ...]               -> free prose
    faqs      [(q, a), ...]                   -> FAQPage JSON-LD
    cta       (label, href)
    related   [slug, ...]
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import guides_number       # noqa: E402
import guides_calc         # noqa: E402
import guides_mental       # noqa: E402
import guides_fractions    # noqa: E402
import guides_decimals     # noqa: E402
import guides_ratio        # noqa: E402

MODULES = [
    guides_number,
    guides_calc,
    guides_mental,
    guides_fractions,
    guides_decimals,
    guides_ratio,
]

CATEGORIES = [m.CAT for m in MODULES]

GUIDES = []
for _m in MODULES:
    GUIDES.extend(_m.GUIDES)

BY_SLUG = {g["slug"]: g for g in GUIDES}

# ------------------------------------------------------------------ checks
REQUIRED = ("slug", "cat", "nav", "h1", "card", "years", "read", "seo", "desc",
            "keywords", "intro", "steps", "examples", "mistakes", "sections",
            "faqs", "cta")

assert len(GUIDES) == len(BY_SLUG), "duplicate guide slug"

for _g in GUIDES:
    _missing = [k for k in REQUIRED if not _g.get(k)]
    assert not _missing, f"{_g.get('slug')}: missing {_missing}"
    assert _g["cat"] in CATEGORIES, f"{_g['slug']}: unknown category {_g['cat']}"
    for _s in _g.get("related", []):
        assert _s in BY_SLUG, f"{_g['slug']}: related slug '{_s}' does not exist"
    _href = _g["cta"][1]
    assert _href.split("?")[0] in ("practice.html", "tables.html"), \
        f"{_g['slug']}: odd CTA target {_href}"
