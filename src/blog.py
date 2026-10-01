# -*- coding: utf-8 -*-
"""Blog: index + article renderer. Post content lives in blog_posts_a.py / blog_posts_b.py."""
import re, math, datetime
from gesite import *

CATEGORIES = {
    "lawn": ("Lawn Mowing", "lawn-mowing-moreton-bay"),
    "hedge": ("Hedges & Pruning", "hedge-trimming-moreton-bay"),
    "cleanup": ("Cleanups & Weeds", "garden-cleanup-moreton-bay"),
    "mulch": ("Mulching & Trees", "mulching-services-moreton-bay"),
}

def _words(html_):
    return len(re.sub(r"<[^>]+>", " ", html_).split())

def reading_time(post):
    w = _words(post["body"]) + sum(_words(a) for _, a in post["faqs"]) + 60
    return max(3, math.ceil(w / 220))

def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%-d %B %Y")

def post_url(p):
    return f"/blog/{p['slug']}/"

def blog_card(p, sizes="(min-width: 1024px) 33vw, 100vw"):
    cat, _ = CATEGORIES[p["category"]]
    return f'''<a class="card service-card post-card" href="{post_url(p)}">
  <div class="service-card__img">{picture(p["image"], p["alt"], sizes=sizes)}</div>
  <div class="service-card__body">
    <div class="post-card__meta"><span class="post-card__cat">{esc(cat)}</span><span>{reading_time(p)} min read</span></div>
    <h3>{p["title"]}</h3>
    <p>{esc(p["excerpt"])}</p>
    <span class="card-link">Read the answer {icon("arrow")}</span>
  </div>
</a>'''

def blog_teaser_section(posts, heading="Straight answers from the mower seat", intro="Question-led guides written for Moreton Bay and Somerset conditions: when to mow, what things cost, and how to keep a Queensland garden under control.", theme="white", n=3):
    cards = "".join(blog_card(p) for p in posts[:n])
    return f'''
<section class="section section--{theme}" id="blog" aria-labelledby="blog-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">From the blog</span><h2 id="blog-h">{esc(heading)}</h2><p class="lead">{esc(intro)}</p></div>
    <div class="grid grid--3" data-reveal-stagger>{cards}</div>
    <p style="margin-top:28px" data-reveal><a class="btn btn--secondary" href="/blog/">All articles {icon("arrow")}</a></p>
  </div>
</section>'''

def toc(body):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if not items:
        return ""
    lis = "".join(f'<li><a href="#{i}">{re.sub(r"<[^>]+>", "", t)}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-label="In this article"><strong>In this article</strong><ol>{lis}</ol></nav>'

def render_post(p, all_posts):
    cat, svc_slug = CATEGORIES[p["category"]]
    svc = SERVICE_BY_SLUG[svc_slug]
    related = [q for q in all_posts if q["slug"] != p["slug"] and q["category"] == p["category"]][:2]
    if len(related) < 2:
        related += [q for q in all_posts if q["slug"] != p["slug"] and q not in related][: 2 - len(related)]
    rel_cards = "".join(blog_card(q, sizes="(min-width: 1024px) 50vw, 100vw") for q in related)
    faq_items = "".join(f'<details><summary><span>{esc(q)}</span><span class="plus"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span></summary><div class="faq__a">{a}</div></details>' for q, a in p["faqs"])
    body = f'''
<section class="hero hero--compact hero--post">
  <div class="hero__bg">{picture(p["image"], p["alt"], sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    {breadcrumbs([("Home", "/"), ("Blog", "/blog/"), (cat, "/blog/#" + p["category"]), (p["short"], None)])}
    <span class="eyebrow">{esc(cat)}</span>
    <h1>{p["h1"]}</h1>
    <span class="gold-rule" aria-hidden="true"></span>
    <p class="lead">{p["lead"]}</p>
    <p class="byline">By <strong>{SITE['owner']}</strong>, owner of Green Estates Gardening · Published <time datetime="{p['date']}">{nice_date(p['date'])}</time> · {reading_time(p)} min read</p>
  </div>
</section>

<section class="section section--light post-layout">
  <div class="container">
    <div class="post-grid">
      <article class="post-body prose">
        <div class="quick-answer speakable">
          <span class="quick-answer__label">Quick answer</span>
          <p>{p["quick"]}</p>
        </div>
        {toc(p["body"])}
        {p["body"]}
        <h2 id="faq">Frequently asked questions</h2>
        <div class="faq faq--inline">{faq_items}</div>
        <div class="post-cta">
          <h2 id="cta">{p["cta_heading"]}</h2>
          <p>{p["cta_text"]}</p>
          <div class="btn-row"><a href="/contact/#quote" class="btn btn--primary">Get a Free Quote {icon("arrow")}</a><a href="tel:{SITE['phone_tel']}" class="btn btn--secondary">{icon("phone")} {SITE['phone']}</a></div>
        </div>
        <div class="about-box">
          <h3>About Green Estates Gardening</h3>
          <p>Green Estates Gardening Pty Ltd is an owner-operated lawn and garden business based in Wamuran, Queensland, run by {SITE['owner']} with more than 13 years of hands-on experience. We provide <a href="/lawn-mowing-moreton-bay/">lawn mowing</a>, <a href="/acreage-mowing-moreton-bay/">acreage and ride-on mowing</a>, <a href="/hedge-trimming-moreton-bay/">hedge trimming</a>, <a href="/garden-cleanup-moreton-bay/">garden cleanups and weed control</a> and <a href="/mulching-services-moreton-bay/">mulching and minor tree work</a> across the Moreton Bay and Somerset regions, including Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Redcliffe, Woodford, D'Aguilar, Kilcoy and Esk. Call {SITE['phone']} for a fixed-price quote.</p>
        </div>
      </article>
      <aside class="post-aside">
        <div class="aside-card aside-card--cta">
          <h3>Need it done rather than read about it?</h3>
          <p>Fixed-price {esc(svc['card'].lower())} across Moreton Bay &amp; Somerset. Quotes within one business day.</p>
          <a href="/contact/#quote" class="btn btn--primary btn--block">Get a free quote {icon("arrow")}</a>
          <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--block" style="margin-top:10px">{icon("phone")} {SITE['phone']}</a>
        </div>
        <div class="aside-card">
          <h3>Related service</h3>
          <a class="dd-item" href="/{svc['slug']}/"><span class="dd-icon">{icon(svc['icon'])}</span><span class="dd-text"><strong>{esc(svc['card'])}</strong><em>{esc(svc['descriptor'])}</em></span></a>
        </div>
        <div class="aside-card">
          <h3>Service areas</h3>
          <p class="muted" style="font-size:.95rem">{", ".join(MORETON_BAY)}; {", ".join(SOMERSET)}.</p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="more-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Keep reading</span><h2 id="more-h">More guides for Moreton Bay gardens</h2></div>
    <div class="grid grid--2" data-reveal-stagger>{rel_cards}</div>
    <p style="margin-top:28px" data-reveal><a class="btn btn--secondary" href="/blog/">All articles {icon("arrow")}</a></p>
  </div>
</section>
'''
    page = dict(
        path=post_url(p), title=p["meta_title"], description=p["description"], keyword=p["keyword"],
        hero_img=p["image"], faqs=p["faqs"],
        crumbs=[("Home", "/"), ("Blog", "/blog/"), (p["short"], post_url(p))],
        article=dict(headline=p["h1_plain"], date=p["date"], section=cat, words=_words(p["body"])),
    )
    return page, body

def render_index(posts):
    groups = []
    for key, (name, svc_slug) in CATEGORIES.items():
        ps = [p for p in posts if p["category"] == key]
        if not ps:
            continue
        cards = "".join(blog_card(p) for p in ps)
        groups.append(f'''<div class="blog-group" id="{key}"><div class="section-head" data-reveal><span class="eyebrow">{esc(name)}</span><h2>{esc(name)} questions, answered for Moreton Bay</h2></div><div class="grid grid--3" data-reveal-stagger>{cards}</div></div>''')
    body = f'''
<section class="hero hero--compact">
  <div class="hero__bg">{picture("hero-lawn-mowing-moreton-bay", "Freshly mown lawn in Moreton Bay, the Green Estates Gardening blog", sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    {breadcrumbs([("Home", "/"), ("Blog", None)])}
    <span class="eyebrow">Lawn &amp; garden guides</span>
    <h1>Lawn Care and Garden Advice for Moreton Bay &amp; Somerset</h1>
    <span class="gold-rule" aria-hidden="true"></span>
    <p class="lead">Practical, question-led lawn care and garden advice Moreton Bay and Somerset property owners can act on, written by {SITE['owner']} from more than 13 years of mowing, hedging and clearing blocks from Redcliffe to Kilcoy. Each guide opens with a direct answer, then the detail behind it.</p>
  </div>
</section>
<section class="section section--light">
  <div class="container" style="display:grid;gap:64px">
    <div class="prose" data-reveal>
      <h2>How these guides are written</h2>
      <p>Every article on this page starts with a direct answer you can act on, then explains the reasoning for South-East Queensland conditions specifically: buffalo, couch and kikuyu rather than cool-climate grasses, storm-season growth rather than a gentle European spring, frost pockets in the Somerset valleys and sandy soils on the Redcliffe peninsula. The topics come from the questions we are asked most often on quotes across Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Wamuran, Woodford and Kilcoy, checked against what people actually search for in Australia. Where a question is really a job, each guide links to the <a href="/#services">service that does it</a>, and every quote we give is a fixed price.</p>
    </div>
    {''.join(groups)}
  </div>
</section>
{cta_band("Would rather we just handled it?", "Every guide here ends the same way: a fixed price and a date. Send the property details and we will come back within one business day.")}
'''
    page = dict(
        path="/blog/", title="Lawn & Garden Advice Moreton Bay | Green Estates Blog",
        description="Question-led lawn and garden advice Moreton Bay owners can use: mowing frequency, costs, wet grass, hedges, mulch and weeds, from a Wamuran local.",
        keyword="Garden Advice Moreton Bay", hero_img="hero-lawn-mowing-moreton-bay",
        crumbs=[("Home", "/"), ("Blog", "/blog/")],
        blog_index=[dict(url=SITE["url"] + post_url(p), name=p["h1_plain"]) for p in posts],
    )
    return page, body
