# -*- coding: utf-8 -*-
"""
Math It! static site builder.

    python3 tools/build.py

Regenerates every HTML page, the sitemap and robots.txt from the shared
shell in tools/shell.py so that navigation, metadata and footers can never
drift apart between pages.
"""
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from shell import page, SITE_NAME, SITE_URL, SITE_TAGLINE, CONTACT_EMAIL  # noqa: E402
import content_home, content_practice, content_resources, content_legal, content_downloads  # noqa: E402
import content_tables  # noqa: E402
import content_guides  # noqa: E402
from guides_data import GUIDES, CATEGORIES  # noqa: E402

TODAY = date.today().isoformat()


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


# ---------------------------------------------------------------- JSON-LD
ORG = {
    "@type": "Organization",
    "@id": SITE_URL + "/#organization",
    "name": SITE_NAME,
    "url": SITE_URL + "/",
    "logo": {"@type": "ImageObject", "url": SITE_URL + "/assets/img/og-image.png"},
    "email": CONTACT_EMAIL,
    "description": "Free mental maths worksheet generator and topic guides for primary school children in Years 2 to 6.",
}

WEBSITE = {
    "@type": "WebSite",
    "@id": SITE_URL + "/#website",
    "url": SITE_URL + "/",
    "name": SITE_NAME,
    "description": SITE_TAGLINE,
    "publisher": {"@id": SITE_URL + "/#organization"},
    "inLanguage": "en-GB",
}

HOME_JSONLD = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        ORG, WEBSITE,
        {
            "@type": "WebApplication",
            "name": SITE_NAME,
            "url": SITE_URL + "/practice.html",
            "applicationCategory": "EducationalApplication",
            "operatingSystem": "Any modern web browser",
            "browserRequirements": "Requires JavaScript",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"},
            "description": "Generates unlimited printable mental maths worksheets for Years 2 to 6, marked instantly in the browser.",
            "educationalLevel": "Primary education, Key Stage 1 and Key Stage 2",
            "audience": {"@type": "EducationalAudience", "educationalRole": ["student", "teacher", "parent"]},
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": strip_tags(q),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in content_home.FAQS
            ],
        },
    ],
}, separators=(",", ":"))


def breadcrumbs(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + "/" + u}
            for i, (n, u) in enumerate(items)
        ],
    }


PRACTICE_JSONLD = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        ORG, WEBSITE,
        breadcrumbs([("Home", "index.html"), ("Worksheets", "practice.html")]),
        {
            "@type": "LearningResource",
            "name": "Mental maths worksheet generator",
            "url": SITE_URL + "/practice.html",
            "learningResourceType": "Worksheet",
            "educationalLevel": "Key Stage 2",
            "isAccessibleForFree": True,
            "inLanguage": "en-GB",
            "teaches": "Mental and written arithmetic: fractions, decimals, percentages, long multiplication, long division, order of operations, ratio and simple algebra.",
            "publisher": {"@id": SITE_URL + "/#organization"},
        },
    ],
}, separators=(",", ":"))

TABLES_JSONLD = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        ORG, WEBSITE,
        breadcrumbs([("Home", "index.html"), ("Times tables", "tables.html")]),
        {
            "@type": "LearningResource",
            "name": "Times tables worksheet generator",
            "url": SITE_URL + "/tables.html",
            "learningResourceType": "Worksheet",
            "educationalLevel": "Key Stage 1 and Key Stage 2",
            "isAccessibleForFree": True,
            "inLanguage": "en-GB",
            "teaches": "Multiplication and division facts for any times table from 1 to 100, including missing-number questions.",
            "publisher": {"@id": SITE_URL + "/#organization"},
        },
    ],
}, separators=(",", ":"))

RESOURCES_JSONLD = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        ORG, WEBSITE,
        breadcrumbs([("Home", "index.html"), ("Guides", "resources.html")]),
        {
            "@type": "CollectionPage",
            "name": "Primary maths topic guides",
            "url": SITE_URL + "/resources.html",
            "description": "Thirty step-by-step guides to the primary maths topics children find hardest.",
            "inLanguage": "en-GB",
            "isPartOf": {"@id": SITE_URL + "/#website"},
            "dateModified": TODAY,
        },
        {
            "@type": "ItemList",
            "name": "Primary maths topic guides",
            "numberOfItems": len(GUIDES),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": g["nav"],
                 "url": SITE_URL + "/guides/" + g["slug"] + ".html"}
                for i, g in enumerate(GUIDES)
            ],
        },
    ],
}, separators=(",", ":"))


def legal_jsonld(name, url, desc):
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            ORG, WEBSITE,
            breadcrumbs([("Home", "index.html"), (name, url)]),
            {"@type": "WebPage", "name": name, "url": SITE_URL + "/" + url,
             "description": desc, "inLanguage": "en-GB",
             "isPartOf": {"@id": SITE_URL + "/#website"}, "dateModified": TODAY},
        ],
    }, separators=(",", ":"))


def guide_jsonld(g):
    url = f"{SITE_URL}/guides/{g['slug']}.html"
    graph = [
        ORG, WEBSITE,
        breadcrumbs([("Home", "index.html"), ("Guides", "resources.html"),
                     (g["nav"], "guides/" + g["slug"] + ".html")]),
        {
            "@type": ["Article", "LearningResource"],
            "headline": g["h1"],
            "url": url,
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "description": g["desc"],
            "author": {"@id": SITE_URL + "/#organization"},
            "publisher": {"@id": SITE_URL + "/#organization"},
            "datePublished": "2026-01-12",
            "dateModified": TODAY,
            "inLanguage": "en-GB",
            "articleSection": g["cat"],
            "learningResourceType": "Guide",
            "educationalLevel": g["years"],
            "isAccessibleForFree": True,
            "timeRequired": f"PT{g['read']}M",
            "audience": {"@type": "EducationalAudience",
                         "educationalRole": ["student", "teacher", "parent"]},
        },
    ]
    if g.get("faqs"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": strip_tags(q),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in g["faqs"]
            ],
        })
    if g.get("steps"):
        graph.append({
            "@type": "HowTo",
            "name": g["h1"],
            "description": g["desc"],
            "step": [
                {"@type": "HowToStep", "position": i + 1, "name": strip_tags(t),
                 "text": strip_tags(b)}
                for i, (t, b) in enumerate(g["steps"])
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      separators=(",", ":"))


GUIDE_PAGES = [
    dict(
        filename="guides/" + g["slug"] + ".html",
        current="resources.html",
        title=g["seo"],
        description=g["desc"],
        keywords=g["keywords"],
        body=content_guides.body(g),
        jsonld=guide_jsonld(g),
        og_type="article",
        prefix="../",
    )
    for g in GUIDES
]


# ---------------------------------------------------------------- pages
PAGES = [
    dict(
        filename="index.html",
        current="index.html",
        title="Math It! — Free mental maths worksheets for Years 2–6 | Daily KS2 arithmetic practice",
        description="Free printable mental maths worksheets for Years 2 to 6. Pick a year group and difficulty, get 36 National Curriculum questions on fractions, decimals, long division, percentages and BIDMAS — marked instantly. No sign-up.",
        keywords="mental maths worksheets, KS2 maths practice, year 6 arithmetic, year 5 maths worksheets, fractions worksheet, long division practice, BIDMAS questions, printable maths worksheets, national curriculum maths",
        body=content_home.BODY,
        jsonld=HOME_JSONLD,
    ),
    dict(
        filename="practice.html",
        current="practice.html",
        title="Mental maths worksheet generator — Years 2 to 6 | Math It!",
        description="Generate a fresh 36-question mental maths worksheet in one click. Choose year group, difficulty and exact topics, mark instantly, reveal answers, and print a clean A4 sheet. Free, no account needed.",
        keywords="maths worksheet generator, arithmetic practice, times tables test, fractions practice, long division worksheet, printable maths worksheet, KS2 arithmetic paper",
        body=content_practice.BODY,
        jsonld=PRACTICE_JSONLD,
        extra_scripts=(
            '\n  <script src="assets/js/generator.js"></script>'
            '\n  <script src="assets/js/practice.js"></script>'
        ),
    ),
    dict(
        filename="tables.html",
        current="tables.html",
        title="Times tables worksheets — any table from 1 to 100, × and ÷ | Math It!",
        description="Free printable times tables worksheets. Pick any tables from 1 to 100, choose multiplication, division or missing numbers, set the multiplier range, then mark instantly or print a clean one-page A4 sheet.",
        keywords="times tables worksheets, multiplication worksheets, division facts, times tables test, MTC practice, year 4 multiplication check, 7 times table, printable times tables",
        body=content_tables.BODY,
        jsonld=TABLES_JSONLD,
        body_attrs='data-sheet-source="tables"',
        extra_scripts=(
            '\n  <script src="assets/js/generator.js"></script>'
            '\n  <script src="assets/js/practice.js"></script>'
        ),
    ),
    dict(
        filename="resources.html",
        current="resources.html",
        title="30 primary maths topic guides — fractions, long division, BIDMAS, ratio | Math It!",
        description="Thirty step-by-step guides to the primary maths topics children find hardest: place value, times tables, fractions, long division, BIDMAS, percentages, ratio and algebra — plus free printable A4 reference sheets.",
        keywords="how to divide fractions, long division method, BIDMAS explained, multiplying decimals, times tables grid printable, KS2 maths help for parents",
        body=content_resources.BODY,
        jsonld=RESOURCES_JSONLD,
        og_type="article",
    ),
    dict(
        filename="privacy.html",
        current="",
        title="Privacy and cookie notice | Math It!",
        description="How Math It! handles data: no accounts, no tracking cookies of our own, preferences stored only in your browser, and full detail on how advertising cookies work and how to opt out.",
        body=content_legal.PRIVACY,
        jsonld=legal_jsonld("Privacy &amp; cookies", "privacy.html",
                            "Privacy and cookie notice for Math It!"),
    ),
    dict(
        filename="terms.html",
        current="",
        title="Terms of use | Math It!",
        description="The terms covering use of Math It! — including the free licence for teachers and parents to print, photocopy and share worksheets for classroom and home use.",
        body=content_legal.TERMS,
        jsonld=legal_jsonld("Terms of use", "terms.html", "Terms of use for Math It!"),
    ),
    dict(
        filename="contact.html",
        current="contact.html",
        title="Contact Math It! — report a question, suggest a topic",
        description="Get in touch with Math It! to report an incorrect question, suggest a new topic, ask about accessibility, or make a school or advertising enquiry.",
        body=content_legal.CONTACT,
        jsonld=legal_jsonld("Contact", "contact.html", "Contact Math It!"),
    ),
    dict(
        filename="404.html",
        current="",
        title="Page not found | Math It!",
        description="That page could not be found. Jump back to the Math It! home page, the worksheet generator or the topic guides.",
        body=content_legal.NOT_FOUND,
    ),
]


# ---------------------------------------------------------------- writers
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    return len(content)


def build_sitemap():
    urls = [
        ("index.html", "1.0", "weekly"),
        ("practice.html", "0.9", "weekly"),
        ("tables.html", "0.9", "weekly"),
        ("resources.html", "0.8", "monthly"),
        ("contact.html", "0.4", "yearly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
    ]
    for y in range(2, 7):
        for lvl in ("easy", "medium", "hard"):
            urls.append((f"practice.html?year={y}&amp;level={lvl}", "0.7", "weekly"))
    for g in GUIDES:
        urls.append(("guides/" + g["slug"] + ".html", "0.7", "monthly"))
    for t in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        urls.append((f"tables.html?tables={t}&amp;ops=mul", "0.6", "monthly"))
    for s in content_downloads.SHEETS:
        urls.append(("downloads/" + s["filename"], "0.6", "monthly"))

    body = "\n".join(
        f"  <url>\n    <loc>{SITE_URL}/{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
        f"    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>"
        for u, pri, freq in urls
    )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{body}\n</urlset>\n")


ROBOTS = f"""# Math It! — robots.txt
User-agent: *
Allow: /
Disallow: /tools/
Disallow: /src/

# Ad crawlers need access to render pages correctly
User-agent: Mediapartners-Google
Allow: /

User-agent: AdsBot-Google
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

ADS_TXT = """# ads.txt — Authorised Digital Sellers
# https://iabtechlab.com/ads-txt/
google.com, pub-9904590475432919, DIRECT, f08c47fec0942fa0
"""

def main():
    written = []
    for spec in PAGES:
        html = page(**spec)
        written.append((spec["filename"], write(spec["filename"], html)))

    for spec in GUIDE_PAGES:
        html = page(**spec)
        written.append((spec["filename"], write(spec["filename"], html)))

    for name, html in content_downloads.build().items():
        written.append(("downloads/" + name, write("downloads/" + name, html)))

    written.append(("sitemap.xml", write("sitemap.xml", build_sitemap())))
    written.append(("robots.txt", write("robots.txt", ROBOTS)))
    written.append(("ads.txt", write("ads.txt", ADS_TXT)))

    print(f"Built {len(written)} files into {ROOT}")
    for name, size in written:
        print(f"  {name:48s} {size/1024:7.1f} kB")


if __name__ == "__main__":
    main()
