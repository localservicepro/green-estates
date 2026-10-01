# -*- coding: utf-8 -*-
"""Service-areas hub + suburb landing page renderer."""
import re
from gesite import *
from suburbs_data_a import SUBURBS_A
from suburbs_data_b import SUBURBS_B

# Strategy doc 05: Deception Bay, Petrie and Kallangur sit south of the core service area and
# need Hamish to confirm the radius. Until then they are built (for review) but noindexed and
# left out of the hub, the suburb chips, related links and the sitemap.
CONFIRMED_RADIUS = False

ALL = SUBURBS_A + SUBURBS_B
BY_PATH = {s["path"]: s for s in ALL}

def is_live(s):
    return CONFIRMED_RADIUS or not s.get("flagged")

LIVE = [s for s in ALL if is_live(s)]

GROUPS = [
    ("corridor", "Northern corridor", "Caboolture to Strathpine along the Bruce Highway and rail line"),
    ("coast", "Coast and peninsula", "Redcliffe, Bribie Island and the bayside villages"),
    ("acreage", "Acreage and Somerset", "Wamuran, the range foothills and over the hill to Kilcoy"),
]

def suburb_url_for(name):
    """Return the live lawn-mowing page path for a suburb name, or None."""
    for s in LIVE:
        if s["name"] == name and s["kind"] == "lawn":
            return s["path"]
    return None

def parent_service(s):
    """The service page each suburb page links up to (review v2, section 4)."""
    if s["kind"] == "garden":
        return SERVICE_BY_SLUG["garden-maintenance-moreton-bay"]
    if s["group"] == "acreage":
        return SERVICE_BY_SLUG["acreage-mowing-moreton-bay"]
    return SERVICE_BY_SLUG["lawn-mowing-moreton-bay"]

def suburb_card(s):
    kind = "Lawn mowing" if s["kind"] == "lawn" else "Garden maintenance"
    return f'<a class="suburb-card" href="{s["path"]}"><span class="icon-tile">{icon("pin")}</span><span><strong>{esc(s["name"])}</strong><em>{kind}</em></span>{icon("arrow")}</a>'

def render_suburb(s):
    svc = parent_service(s)
    kind_word = "lawn mowing" if s["kind"] == "lawn" else "garden maintenance"
    preselect = "Push Mowing" if s["kind"] == "lawn" else "Regular Maintenance Package"
    if s["group"] == "acreage":
        preselect = "Ride-On / Acreage Mowing"
    nb = [BY_PATH[p] for p in s["neighbours"] if p in BY_PATH and is_live(BY_PATH[p])]
    nb_html = "".join(suburb_card(n) for n in nb)
    other_services = "".join(f'<a class="dd-item" href="/{x["slug"]}/"><span class="dd-icon">{icon(x["icon"])}</span><span class="dd-text"><strong>{esc(x["card"])}</strong><em>{esc(x["descriptor"])}</em></span></a>' for x in SERVICES if x is not svc)
    parent_card = f'<a class="dd-item dd-item--parent" href="/{svc["slug"]}/"><span class="dd-icon">{icon(svc["icon"])}</span><span class="dd-text"><strong>{esc(svc["card"])} across Moreton Bay</strong><em>The service page this {esc(s["name"])} guide belongs to</em></span></a>'
    parent_word = {"garden-maintenance-moreton-bay": "garden maintenance", "acreage-mowing-moreton-bay": "acreage and ride-on mowing"}.get(svc["slug"], "residential lawn mowing")
    faq_items = "".join(f'<details><summary><span>{esc(q)}</span><span class="plus"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span></summary><div class="faq__a">{a}</div></details>' for q, a in s["faqs"])
    region = "Moreton Bay Region" if s["region"] == "mb" else "Somerset Region"
    body = f'''
<section class="hero hero--compact">
  <div class="hero__bg">{picture(s["image"], s["alt"], sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    <div class="hero__grid">
      <div>
        {breadcrumbs([("Home", "/"), ("Service Areas", "/service-areas/"), (s["name"], None)])}
        <span class="eyebrow">{esc(s["name"])} · {region}</span>
        <h1>{s["h1"]}</h1>
        <span class="gold-rule" aria-hidden="true"></span>
        <p class="lead">{s["lead"]}</p>
        <div class="btn-row hero__cta">
          <a href="#quote" class="btn btn--primary btn--lg" data-open-quote>Get a Fixed-Price Quote {icon("arrow")}</a>
          <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} {SITE['phone']}</a>
        </div>
        {trust_strip()}
      </div>
      {quote_form("quote", preselect=preselect, title=f"Quote a job in {s['name']}", intro="Address, rough size and what you need. We reply within one business day with a fixed price.", source=s["path"])}
    </div>
  </div>
</section>

<section class="section section--light">
  <div class="container">
    <div class="post-grid">
      <article class="post-body prose">
        <div class="quick-answer speakable"><span class="quick-answer__label">In short</span><p>{s["quick"]}</p></div>
        <p class="parent-link">Part of our <a href="/{svc["slug"]}/">{parent_word} service across Moreton Bay and Somerset</a>. This page covers what is different about {esc(s["name"])}.</p>
        {s["body"]}
        <h2>Frequently asked questions about {kind_word} in {esc(s["name"])}</h2>
        <div class="faq faq--inline">{faq_items}</div>
        <div class="post-cta">
          <h2>Get a fixed price for your {esc(s["name"])} property</h2>
          <p>Send the address, a rough size and what you need. Standard blocks are usually quoted the same day; acreage within one business day. No contract, no obligation.</p>
          <div class="btn-row"><a href="#quote" class="btn btn--primary">Get a Free Quote {icon("arrow")}</a><a href="tel:{SITE['phone_tel']}" class="btn btn--secondary">{icon("phone")} {SITE['phone']}</a></div>
        </div>
      </article>
      <aside class="post-aside">
        <div class="aside-card">
          <h3>Services in {esc(s["name"])}</h3>
          {parent_card}{other_services}
        </div>
        <div class="aside-card">
          <h3>Nearby suburbs</h3>
          <div class="suburb-list">{nb_html}<a class="suburb-card" href="/service-areas/"><span class="icon-tile">{icon("grid")}</span><span><strong>All service areas</strong><em>Moreton Bay &amp; Somerset</em></span>{icon("arrow")}</a></div>
        </div>
      </aside>
    </div>
  </div>
</section>
{cta_band(f"Ready to hand over the {kind_word} in {s['name']}?", "One local crew, one fixed price per visit, and a photo when it is done. Quotes within one business day across Moreton Bay and Somerset.")}
'''
    page = dict(
        path=s["path"], title=s["title"], description=s["description"], keyword=s["keyword"], hero_img=s["image"], faqs=s["faqs"],
        noindex=not is_live(s),
        crumbs=[("Home", "/"), ("Service Areas", "/service-areas/"), (s["name"], s["path"])],
        service=dict(name=f"{svc['card']} {s['name']}", type=svc["card"],
                     items=[x["card"] for x in SERVICES], area=[s["name"] + ", QLD", region + ", Queensland"]),
    )
    return page, body

def render_hub():
    groups_html = []
    for key, name, blurb in GROUPS:
        cards = "".join(suburb_card(s) for s in LIVE if s["group"] == key)
        groups_html.append(f'<div class="hub-group" data-reveal><h3>{esc(name)}</h3><p class="muted">{esc(blurb)}</p><div class="suburb-grid" data-reveal-stagger>{cards}</div></div>')
    covered = {s["name"] for s in LIVE}
    others = [n for n in ALL_SUBURBS if n not in covered]
    others_html = "".join(f'<li>{esc(n)}</li>' for n in others)
    body = f'''
<section class="hero hero--compact">
  <div class="hero__bg">{picture("hero-acreage-mowing-somerset", "Service areas: freshly mown acreage in the Somerset region served by Green Estates Gardening", sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    {breadcrumbs([("Home", "/"), ("Service Areas", None)])}
    <span class="eyebrow">Where we work</span>
    <h1>Lawn Mowing &amp; Garden Service Areas Across Moreton Bay &amp; Somerset</h1>
    <span class="gold-rule" aria-hidden="true"></span>
    <p class="lead">Green Estates Gardening's service areas run from the Redcliffe peninsula and Bribie Island, up the Bruce Highway corridor through North Lakes, Narangba, Burpengary, Morayfield and Caboolture, out to our home base in Wamuran and over the D'Aguilar Range to Kilcoy and the Somerset valleys. Pick your suburb below for local detail, or send the address and we will confirm.</p>
    <div class="btn-row hero__cta"><a href="/contact/#quote" class="btn btn--primary btn--lg" data-open-quote>Get a Free Quote {icon("arrow")}</a><a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} {SITE['phone']}</a></div>
  </div>
</section>

<section class="section section--light">
  <div class="container">
    <div class="split" style="align-items:start">
      <div class="prose" data-reveal>
        <span class="eyebrow">How the rounds work</span>
        <h2>One local crew, three regular rounds</h2>
        <p class="speakable"><strong>Green Estates Gardening services the Moreton Bay and Somerset regions of Queensland from a base in Wamuran, running three regular rounds: the northern corridor from Caboolture to Strathpine, the coast from Bribie Island to Redcliffe, and the acreage belt from Wamuran over the range to Kilcoy. Every suburb is quoted at a fixed price per visit.</strong></p>
        <p>Working in rounds is what keeps the price sharp and the schedule reliable. Each area is mowed on a set day in an efficient loop rather than as a one-off trip, so a fortnightly cut in North Lakes costs what it should and a Kilcoy acreage block is not paying for a special drive over the range. It also means we are nearby most days of the week, which is how we move a cut around the weather instead of skipping a month.</p>
        <p>The suburb pages below explain what the lawns, soils and properties are like in each area and what we do differently there: high buffalo cuts in the estates, sandy coastal lawns on the peninsula, kikuyu paddocks and slopes in the foothills. Each one links up to the service it belongs to, <a href="/lawn-mowing-moreton-bay/">residential lawn mowing</a> for the corridor and coast, <a href="/acreage-mowing-moreton-bay/">acreage mowing</a> for the range and Somerset, and <a href="/garden-maintenance-moreton-bay/">garden maintenance</a> for North Lakes and Redcliffe. Suburbs without their own page yet, such as Elimbah, Woodford, Bracalba, Esk, Toogoolawah, Lowood and Fernvale, are covered on the same rounds; <a href="/contact/">send the address</a> and we will confirm the day.</p>
        <p>Whatever the suburb, the visit is the same: mowing at the right height for the grass, edging along every path and driveway, line trimming around fences and beds, a blow-down before we leave, and hedges, weed control or mulching added to the same visit if you want them. You never need to be home, and you get a photo when the job is done.</p>
      </div>
      <div class="map-embed" data-reveal>
        <iframe title="Map of the Moreton Bay and Somerset regions served by Green Estates Gardening" src="https://www.google.com/maps?q=Wamuran+QLD+4512&z=9&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="suburbs">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Suburb guides</span><h2>Choose your suburb</h2><p class="lead">Local pages for the suburbs we visit most, with the detail that matters for your block.</p></div>
    <div style="display:grid;gap:48px">{''.join(groups_html)}</div>
    <div class="hub-others" data-reveal>
      <h3>Also on our rounds</h3>
      <ul class="chips">{others_html}</ul>
      <p class="muted">Plus Mango Hill, Griffin, Murrumba Downs, Dakabin, Rothwell, Sandstone Point, Ningi, Bellmere, Upper Caboolture, Moodlu, Campbells Pocket, Somerset Dam, Hazeldean and Villeneuve.</p>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What we do in every area</span><h2>Six services, one fixed price per visit</h2></div>
    <div class="grid grid--services" data-reveal-stagger>{service_cards(sizes="(min-width: 1024px) 25vw, 100vw")}</div>
  </div>
</section>
{cta_band("Not sure if we cover you?", "If you are anywhere between Bribie Island, Redcliffe and Esk, the answer is almost certainly yes. Send the address and we will confirm the day and a fixed price.")}
'''
    page = dict(
        path="/service-areas/", title="Service Areas Moreton Bay & Somerset | Green Estates",
        description="Service areas for lawn mowing and garden care across Moreton Bay and Somerset: Redcliffe, Bribie Island, North Lakes, Caboolture, Wamuran and Kilcoy.",
        keyword="Service Areas", hero_img="hero-acreage-mowing-somerset",
        crumbs=[("Home", "/"), ("Service Areas", "/service-areas/")],
    )
    return page, body

def suburb_pages():
    return [render_hub()] + [render_suburb(s) for s in ALL]
