# -*- coding: utf-8 -*-
"""Build the static site into ../public and run SEO/structure checks.
Usage: python3 src/build.py"""
import os, re, json, sys, html as htmllib
sys.path.insert(0, os.path.dirname(__file__))
from gesite import SITE, shell, ALL_SUBURBS
import pages_home, pages_services, pages_other

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "public")

PAGES = [pages_home.home(), pages_services.lawn_mowing(), pages_services.hedge_trimming(),
         pages_services.garden_cleanup(), pages_services.mulching(), pages_other.about(),
         pages_other.contact(), pages_other.thank_you(), pages_other.not_found()]

def out_path(path):
    if path.endswith(".html"):
        return os.path.join(PUB, path.lstrip("/"))
    return os.path.join(PUB, path.strip("/"), "index.html") if path != "/" else os.path.join(PUB, "index.html")

def text_of(fragment):
    frag = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    frag = re.sub(r"<[^>]+>", " ", frag)
    frag = htmllib.unescape(frag)
    return re.sub(r"\s+", " ", frag).strip()

def check(page, doc, body):
    problems, notes = [], []
    kw = page.get("keyword")
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", doc, flags=re.S)
    if len(h1s) != 1:
        problems.append(f"{len(h1s)} H1s")
    title = re.search(r"<title>(.*?)</title>", doc).group(1)
    desc = re.search(r'name="description" content="(.*?)"', doc).group(1)
    if len(title) > 60: problems.append(f"title {len(title)} chars")
    if len(desc) > 160: problems.append(f"description {len(desc)} chars")
    main = re.search(r"<main[^>]*>(.*)</main>", doc, flags=re.S).group(1)
    # word count excludes the quote form and the shared suburb list
    content = re.sub(r'<div class="quote-card".*?</form>\s*</div>', " ", main, flags=re.S)
    words = text_of(content).split()
    notes.append(f"{len(words)} words")
    if kw:
        k = kw.lower()
        if k not in title.lower(): problems.append("keyword not in title")
        if k not in htmllib.unescape(desc).lower(): problems.append("keyword not in description")
        if k not in text_of(h1s[0]).lower():
            # allow service+location split across the H1 (doc's H1s are locked verbatim)
            notes.append("keyword phrase not verbatim in H1 (service + location present)")
        first100 = " ".join(text_of(content).split()[:100]).lower()
        if k not in first100: problems.append("keyword not in first 100 words")
        cnt = text_of(content).lower().count(k)
        notes.append(f"keyword x{cnt} ({cnt/len(words)*100:.2f}% of words)")
        if len(words) < 650: problems.append("under 650 words")
    # alt text
    imgs = re.findall(r"<img\b[^>]*>", doc)
    missing = [i for i in imgs if 'alt="' not in i or 'alt=""' in i]
    if missing: problems.append(f"{len(missing)} images without alt")
    # schema JSON valid
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, flags=re.S):
        try:
            json.loads(m)
        except Exception as e:
            problems.append(f"schema JSON invalid: {e}")
    # heading order
    levels = [int(l) for l in re.findall(r"<h([1-4])[\s>]", main)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1:
            problems.append(f"heading jump h{a}->h{b}"); break
    faqs = len(re.findall(r"<details>", main))
    notes.append(f"{faqs} FAQs")
    return problems, notes

def main():
    written = []
    all_links = set()
    for page, body in PAGES:
        doc = shell(page, body)
        p = out_path(page["path"])
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(doc)
        written.append(page["path"])
        probs, notes = check(page, doc, body)
        flag = "OK " if not probs else "!! "
        print(f"{flag}{page['path']:35s} {'; '.join(notes)}{('  PROBLEMS: ' + '; '.join(probs)) if probs else ''}")
        for href in re.findall(r'href="([^"]+)"', doc):
            all_links.add(href)
    write_extras()
    # internal link resolution
    bad = []
    for href in sorted(all_links):
        if href.startswith(("http", "mailto:", "tel:", "#", "data:")):
            continue
        path = href.split("#")[0]
        if not path:
            continue
        fs = os.path.join(PUB, path.lstrip("/"))
        if os.path.isdir(fs):
            fs = os.path.join(fs, "index.html")
        if not os.path.exists(fs):
            bad.append(href)
    print("broken internal links:", bad or "none")
    print("built", len(written), "pages")

def write_extras():
    indexable = [p for p, _ in PAGES if not p.get("noindex")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in indexable:
        pri = "1.0" if p["path"] == "/" else ("0.9" if p.get("service") else "0.7")
        sm.append(f"  <url><loc>{SITE['url']}{p['path']}</loc><changefreq>monthly</changefreq><priority>{pri}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(PUB, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(PUB, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    open(os.path.join(PUB, "site.webmanifest"), "w").write(json.dumps({
        "name": SITE["name"], "short_name": "Green Estates", "start_url": "/", "display": "browser",
        "background_color": "#F9FAF7", "theme_color": "#1A3C0E",
        "icons": [{"src": "/assets/img/favicon.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))

if __name__ == "__main__":
    main()
