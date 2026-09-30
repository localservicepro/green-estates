# -*- coding: utf-8 -*-
"""Shared constants, icons and components for the Green Estates Gardening static build."""
import json, html, re

SITE = dict(
    name="Green Estates Gardening",
    legal="Green Estates Gardening Pty Ltd",
    url="https://www.greenestatesgardening.com",
    phone="0439 550 850",
    phone_tel="+61439550850",
    email="greenestatesgardening@outlook.com",
    locality="Wamuran", region="QLD", postcode="4512", country="AU",
    facebook="https://www.facebook.com/profile.php?id=61552302307968",
    hours="Mon–Sat 7:00am–4:00pm",
    lat=-27.0402, lng=152.8613,
    owner="Hamish Baggley",
    tracking_id="tk_b225e621e85a44b586690a7c2a3a39be",
)

MORETON_BAY = ["Wamuran", "Caboolture", "D'Aguilar", "Redcliffe", "Strathpine", "North Lakes", "Woodford",
               "Elimbah", "Narangba", "Burpengary", "Morayfield", "Bracalba"]
SOMERSET = ["Kilcoy", "Esk", "Toogoolawah", "Lowood", "Fernvale"]
ALL_SUBURBS = MORETON_BAY + SOMERSET

SERVICES = [
    dict(slug="lawn-mowing-moreton-bay", nav="Lawn Mowing", card="Acreage & Ride-On Mowing",
         descriptor="Acreage & ride-on · Wamuran, Caboolture & Somerset", icon="mower",
         img="ride-on-mowing-acreage-moreton-bay",
         alt="Ride-on acreage mowing service in Moreton Bay with a zero-turn mower on a rural block",
         blurb="Zero-turn ride-on mowing for acreage, lifestyle blocks and large yards, plus push mowing and edging for standard residential lawns.",
         points=["Acreage & lifestyle blocks", "Ride-on and push mowing", "Edging, trimming & blow-down"]),
    dict(slug="hedge-trimming-moreton-bay", nav="Hedge Trimming", card="Hedge Trimming & Pruning",
         descriptor="Morayfield, Burpengary & North Lakes", icon="shears",
         img="hedge-trimming-shaped-hedges",
         alt="Hedge trimming Moreton Bay: neatly shaped round hedges beside a freshly mown lawn",
         blurb="Sharp, even hedges and tidy shrubs. Formal shaping, height reduction and seasonal pruning with every clipping removed.",
         points=["Formal & informal hedges", "Height reduction & shaping", "Shrub & screen pruning"]),
    dict(slug="garden-cleanup-moreton-bay", nav="Garden Cleanups", card="Garden Cleanups & Weed Control",
         descriptor="Caboolture, Narangba & Redcliffe", icon="leaf",
         img="garden-cleanup-after-cleared",
         alt="Garden cleanup Moreton Bay: overgrown yard cleared, weeded and tidied under established trees",
         blurb="Overgrown block? One-off cleanups, weed control, green waste removal and a reset so regular maintenance is easy again.",
         points=["Overgrown yard resets", "Weed spraying & removal", "Green waste taken away"]),
    dict(slug="mulching-services-moreton-bay", nav="Mulching & Tree Work", card="Mulching & Minor Tree Work",
         descriptor="Kilcoy, Woodford & D'Aguilar", icon="tree",
         img="mulching-garden-bed-commercial",
         alt="Mulching services Moreton Bay: freshly mulched garden bed along a commercial building",
         blurb="Garden bed preparation and mulching that holds moisture through a Queensland summer, plus small limb and branch removal.",
         points=["Bed prep & mulch supply", "Small limb & branch removal", "Storm tidy-ups"]),
]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
SUBURB_LINKS = {}  # filled by build.py from suburbs.LIVE

ICONS = {
    "grid": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="2"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="2"/></svg>',
    "mower": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 16.5h9.5l3-7h3.5"/><rect x="4" y="12" width="9.5" height="4.5" rx="1.5"/><circle cx="6.5" cy="19" r="2"/><circle cx="16.5" cy="19" r="2"/><path d="M13.5 12 15 8.5"/><path d="M2 11.5 4 7h4"/></svg>',
    "shears": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="18" r="3"/><circle cx="18" cy="18" r="3"/><path d="M8.1 15.9 19 3"/><path d="M15.9 15.9 5 3"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20c0-9 5-15 16-16-1 11-7 16-16 16Z"/><path d="M4 20c3-5 7-9 12-12"/></svg>',
    "tree": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 6.5 11h3L5.5 17h13l-4-6h3L12 3Z"/><path d="M12 17v4"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 5 6v6c0 4.5 3 7.5 7 9 4-1.5 7-4.5 7-9V6l-7-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12V4h8l10 10-8 8L3 12Z"/><circle cx="7.5" cy="8.5" r="1.5"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    "truck": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>',
    "star": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.4l-5.9 3.2 1.3-6.6L2.5 9.4l6.6-.8L12 2.5z"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V14h2.8v8h3.3Z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.5a5 5 0 0 1 6 5"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/></svg>',
}

def icon(name):
    return ICONS[name]

def stars(n=5):
    return '<span class="stars" aria-hidden="true">' + ICONS["star"] * n + '</span>'

def esc(s):
    return html.escape(s, quote=True)

def picture(name, alt, sizes="(min-width: 1024px) 50vw, 100vw", cls="", loading="lazy", fetchpriority=None, width=None, height=None):
    src = f"/assets/img/{name}-1000.webp"
    srcset = f"/assets/img/{name}-600.webp 600w, /assets/img/{name}-1000.webp 1000w, /assets/img/{name}-1600.webp 1600w"
    extra = f' fetchpriority="{fetchpriority}"' if fetchpriority else ""
    dims = f' width="{width}" height="{height}"' if width and height else ""
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{src}" srcset="{srcset}" sizes="{sizes}" alt="{esc(alt)}" loading="{loading}" decoding="async"{extra}{dims}{c}>'

# ---------------- Header / footer ----------------

def header(current="/"):
    dd_items = [
        f'<a class="dd-item" role="menuitem" href="/#services"><span class="dd-icon">{icon("grid")}</span><span class="dd-text"><strong>All Services</strong><em>Lawn &amp; garden care across Moreton Bay &amp; Somerset</em></span></a>'
    ]
    for s in SERVICES:
        dd_items.append(f'<a class="dd-item" role="menuitem" href="/{s["slug"]}/"><span class="dd-icon">{icon(s["icon"])}</span><span class="dd-text"><strong>{esc(s["card"])}</strong><em>{esc(s["descriptor"])}</em></span></a>')
    dd = "\n".join(dd_items)
    m_items = "\n".join(
        f'<a class="dd-item" href="/{s["slug"]}/"><span class="dd-icon">{icon(s["icon"])}</span><span class="dd-text"><strong>{esc(s["card"])}</strong><em>{esc(s["descriptor"])}</em></span></a>' for s in SERVICES)
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="nav-inner">
    <a href="/" class="brand" aria-label="Green Estates Gardening — home">
      <img class="logo-light" src="/assets/img/logo-green-estates-gardening.webp" alt="Green Estates Gardening logo" width="328" height="253">
      <img class="logo-dark" src="/assets/img/logo-green-estates-gardening-knockout.png" alt="Green Estates Gardening logo" width="328" height="253">
    </a>
    <nav class="nav-main" aria-label="Main navigation">
      <a href="/" class="nav-link">Home</a>
      <div class="nav-dropdown">
        <button class="nav-link nav-trigger" aria-expanded="false" aria-controls="services-menu" aria-haspopup="true">Services
          <svg class="caret" viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5 6 6.5l5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
        <div class="dropdown-panel" id="services-menu" role="menu">{dd}</div>
      </div>
      <a href="/about/" class="nav-link">About</a>
      <a href="/service-areas/" class="nav-link">Areas</a>
      <a href="/blog/" class="nav-link">Blog</a>
      <a href="/contact/" class="nav-link">Contact</a>
    </nav>
    <div class="nav-actions">
      <a href="tel:{SITE['phone_tel']}" class="nav-phone">{icon("phone")}<span>{SITE['phone']}</span></a>
      <a href="/contact/#quote" class="btn btn--primary nav-cta">Get a Free Quote</a>
    </div>
    <button class="nav-burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav">
  <nav aria-label="Mobile navigation">
    <a class="m-link" href="/">Home</a>
    <button class="m-link m-acc" aria-expanded="false" aria-controls="m-services">Services <svg class="caret" viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5 6 6.5l5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
    <div class="m-sub" id="m-services">{m_items}</div>
    <a class="m-link" href="/about/">About</a>
    <a class="m-link" href="/service-areas/">Service Areas</a>
    <a class="m-link" href="/blog/">Blog</a>
    <a class="m-link" href="/contact/">Contact</a>
  </nav>
  <div class="m-foot">
    <a href="/contact/#quote" class="btn btn--primary btn--lg">Get a Free Quote</a>
    <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} Call {SITE['phone']}</a>
  </div>
  <p class="m-nap">{SITE['legal']} · Wamuran QLD 4512 · {SITE['hours']}</p>
</div>
<div class="callbar" aria-label="Quick actions">
  <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary">{icon("phone")} Call now</a>
  <a href="/contact/#quote" class="btn btn--primary">Free quote</a>
</div>
'''

def footer():
    svc = "\n".join(f'<li><a href="/{s["slug"]}/">{esc(s["card"])}</a></li>' for s in SERVICES)
    def _l(n):
        u = SUBURB_LINKS.get(n)
        return f'<a href="{u}">{esc(n)}</a>' if u else esc(n)
    areas_mb = ", ".join(_l(n) for n in MORETON_BAY)
    areas_som = ", ".join(_l(n) for n in SOMERSET)
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/logo-green-estates-gardening-knockout.png" alt="Green Estates Gardening logo" width="328" height="253">
        <p>Lawn mowing, hedge trimming, garden cleanups and mulching for homes, acreage and commercial properties across the Moreton Bay and Somerset regions. Based in Wamuran, Queensland.</p>
        <a class="social" href="{SITE['facebook']}" rel="noopener" target="_blank">{icon("facebook")} Follow us on Facebook</a>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc}<li><a href="/#services">All services</a></li></ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About Green Estates</a></li>
          <li><a href="/service-areas/">Service areas</a></li>
          <li><a href="/blog/">Lawn &amp; garden advice</a></li>
          <li><a href="/contact/">Contact &amp; free quote</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>Wamuran QLD 4512</li>
          <li>{SITE['hours']}</li>
        </ul>
        <h4 style="margin-top:22px">Service areas</h4>
        <p class="footer-areas"><strong>Moreton Bay:</strong> {areas_mb}.<br><strong>Somerset:</strong> {areas_som}.</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> {SITE['legal']}. All rights reserved.</span>
      <span>Quotes are free and obligation-free.</span>
    </div>
  </div>
</footer>
<script src="/assets/js/vendor/gsap.min.js" defer></script>
<script src="/assets/js/vendor/ScrollTrigger.min.js" defer></script>
<script src="/assets/js/site.js" defer></script>
'''

# ---------------- Quote form ----------------

SERVICE_OPTIONS = ["Ride-On / Acreage Mowing", "Push Mowing", "Hedge Trimming", "Garden Cleanup", "Weed Control",
                   "Mulching", "Minor Tree Work", "Regular Maintenance Package", "Something else"]
SIZE_OPTIONS = ["Under 500 m² (standard block)", "500–1,000 m²", "1,000–2,500 m²", "2,500 m² – 1 acre", "1–5 acres", "5+ acres", "Commercial / strata"]

def quote_form(form_id="quote", preselect=None, title="Get your free quote", intro="Tell us about the property and we'll come back with a fixed price. No obligation.", source="", button="Send my quote request"):
    def opts(options, selected=None, placeholder="Please select…"):
        out = [f'<option value="" disabled{" selected" if not selected else ""}>{placeholder}</option>']
        for o in options:
            sel = " selected" if o == selected else ""
            out.append(f'<option value="{esc(o)}"{sel}>{esc(o)}</option>')
        return "".join(out)
    p = form_id
    return f'''
<div class="quote-card" id="{p}">
  <h2>{esc(title)}</h2>
  <p class="form-intro">{esc(intro)}</p>
  <form data-quote-form="{p}" action="/thank-you/" method="post" data-redirect="/thank-you/" novalidate>
    <div class="form-summary" role="alert" aria-live="assertive"></div>
    <input type="hidden" name="source_page" value="{esc(source)}">
    <div class="field-row">
      <div class="field"><label for="{p}-name">Name</label><input id="{p}-name" name="full_name" type="text" autocomplete="name" required><span class="error" aria-live="polite"></span></div>
      <div class="field"><label for="{p}-phone">Phone</label><input id="{p}-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required pattern="[0-9+ ()-]{{8,}}"><span class="error" aria-live="polite"></span></div>
    </div>
    <div class="field"><label for="{p}-email">Email</label><input id="{p}-email" name="email" type="email" autocomplete="email" required><span class="error" aria-live="polite"></span></div>
    <div class="field"><label for="{p}-address">Property address <span class="opt">(street &amp; suburb)</span></label><input id="{p}-address" name="property_address" type="text" autocomplete="street-address" placeholder="e.g. 12 Smith Rd, Caboolture" required><span class="error" aria-live="polite"></span></div>
    <div class="field-row">
      <div class="field"><label for="{p}-size">Property size <span class="opt">(optional)</span></label><select id="{p}-size" name="property_size">{opts(SIZE_OPTIONS, placeholder="Not sure")}</select></div>
      <div class="field"><label for="{p}-service">Service needed</label><select id="{p}-service" name="service_needed" required>{opts(SERVICE_OPTIONS, preselect)}</select><span class="error" aria-live="polite"></span></div>
    </div>
    <div class="field"><label for="{p}-notes">Job notes <span class="opt">(optional)</span></label><textarea id="{p}-notes" name="job_notes" rows="3" placeholder="Anything we should know — gates, slopes, how overgrown it is, how often you'd like us"></textarea></div>
    <div class="hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label></div>
    <button type="submit" class="btn btn--primary btn--lg btn--block">{esc(button)} {icon("arrow")}</button>
    <p class="form-fine">We reply within one business day, Mon–Sat. Or call <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a>.</p>
  </form>
</div>'''

# ---------------- Reusable sections ----------------

def faq_section(faqs, heading="Frequently asked questions", eyebrow="FAQ", intro=None, theme="light", id_="faq"):
    items = []
    for q, a in faqs:
        items.append(f'<details><summary><span>{esc(q)}</span><span class="plus"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span></summary><div class="faq__a">{a}</div></details>')
    intro_html = f'<p class="lead">{intro}</p>' if intro else ""
    return f'''
<section class="section section--{theme}" id="{id_}" aria-labelledby="{id_}-h">
  <div class="container">
    <div class="section-head center" data-reveal>
      <span class="eyebrow">{esc(eyebrow)}</span>
      <h2 id="{id_}-h">{esc(heading)}</h2>
      {intro_html}
    </div>
    <div class="faq" data-reveal-stagger>{''.join(items)}</div>
  </div>
</section>'''

def service_cards(exclude_slug=None, sizes="(min-width: 1024px) 33vw, 100vw"):
    cards = []
    for s in SERVICES:
        if s["slug"] == exclude_slug:
            continue
        pts = "".join(f"<li>{esc(p)}</li>" for p in s["points"])
        cards.append(f'''<a class="card service-card" href="/{s["slug"]}/">
  <div class="service-card__img">{picture(s["img"], s["alt"], sizes=sizes)}</div>
  <div class="service-card__body"><span class="icon-tile">{icon(s["icon"])}</span><h3>{esc(s["card"])}</h3><p>{esc(s["blurb"])}</p><ul>{pts}</ul><span class="card-link">View service {icon("arrow")}</span></div>
</a>''')
    return "".join(cards)

def related_services(exclude_slug=None, heading="Related services", theme="light"):
    return f'''
<section class="section section--{theme}" aria-labelledby="related-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">More from Green Estates</span><h2 id="related-h">{esc(heading)}</h2><p class="lead">Most clients combine two or three of these into one regular visit. Everything is quoted as a fixed price up front.</p></div>
    <div class="grid grid--3" data-reveal-stagger>{service_cards(exclude_slug)}</div>
  </div>
</section>'''

def cta_band(heading="Ready for a tidy, healthy property?", text="Send a few details and we'll give you a fixed price. Most quotes go out within one business day.", theme="light"):
    return f'''
<section class="section section--{theme} section--tight">
  <div class="container">
    <div class="cta-band" data-reveal>
      <div><h2>{esc(heading)}</h2><p>{esc(text)}</p></div>
      <div class="btn-row"><a href="/contact/#quote" class="btn btn--primary btn--lg">Get a Free Quote {icon("arrow")}</a><a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} {SITE['phone']}</a></div>
    </div>
  </div>
</section>'''

def suburbs_section(heading, intro, theme="dark", id_="areas", service_word="lawn mowing", extra=""):
    def chips(lst):
        out = []
        for s in lst:
            cls = ' class="is-home"' if s == "Wamuran" else ""
            u = SUBURB_LINKS.get(s)
            out.append(f'<li{cls}><a href="{u}">{esc(s)}</a></li>' if u else f'<li{cls}>{esc(s)}</li>')
        return "".join(out)
    return f'''
<section class="section section--{theme}" id="{id_}" aria-labelledby="{id_}-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Suburbs we serve</span><h2 id="{id_}-h">{heading}</h2><p class="lead">{intro}</p></div>
    <div class="area-groups" data-reveal-stagger>
      <div class="area-group"><h3>{icon("pin")} Moreton Bay Region</h3><ul class="chips">{chips(MORETON_BAY)}</ul></div>
      <div class="area-group"><h3>{icon("pin")} Somerset Region</h3><ul class="chips">{chips(SOMERSET)}</ul></div>
    </div>
    {extra}
    <p class="muted" style="margin-top:24px;max-width:70ch" data-reveal>Not on the list? We travel throughout the Moreton Bay and Somerset regions for regular {service_word} and larger one-off jobs. <a href="/service-areas/">See all service areas</a> or <a href="/contact/">ask us about your suburb</a>.</p>
  </div>
</section>'''

REVIEWS = [
    ("Raymond Jack", "Google review", "Hamish has been doing our lawns and gardens for several years now, and always does a good job. No fuss, reasonably priced, and always reliable"),
    ("Barry Harvey", "Google review · Somerset Dam", "The Lake House - Hazeldean - Somerset Dam area, Hamish has been the groundsman for our 3.74 acre B&B property which consists of 2 dwellings and a boat shed with a gully and two dams, he has been doing a fantastic job, and always punctual. I highly recommend his services."),
    ("Dylan Penny", "Google review", "Hamish has been a wonderful contractor to assist me with managing my landscaping needs across a few properties. He is very well priced, and maintains a high standard of work. Could not recommend enough!"),
    ("Kathy Fowler", "Google review", "Green Estates Gardening has collaborated with me on garden decisions for the past thirteen years. Hamish Baggley is my go-to man for gardening decisions of all kinds — one of the few people whose judgment I trust implicitly."),
]

def review_cards():
    cards = []
    for name, meta, text in REVIEWS:
        cards.append(f'''<blockquote class="review-card">
  <div class="review-card__head"><span class="review-card__avatar" aria-hidden="true">{esc(name[0])}</span><div><strong>{esc(name)}</strong><span>{esc(meta)}</span></div></div>
  {stars()}<span class="visually-hidden">Rated 5 out of 5</span>
  <p>“{esc(text)}”</p>
</blockquote>''')
    return '<div class="grid grid--4 reviews" data-reveal-stagger>' + "".join(cards) + '</div>'

def trust_strip():
    return f'''<ul class="trust-strip">
  <li>{stars()}<span><strong>5.0</strong> Google rating · 23 five-star reviews</span></li>
  <li>{icon("shield")}<span>13+ years of local experience</span></li>
  <li>{icon("tag")}<span>Fixed-price quotes, no surprises</span></li>
  <li>{icon("clock")}<span>{SITE['hours']}</span></li>
</ul>'''

def breadcrumbs(items):
    lis = []
    for label, href in items:
        if href:
            lis.append(f'<li><a href="{href}">{esc(label)}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{esc(label)}</li>')
    return f'<ol class="breadcrumbs" aria-label="Breadcrumb">{"".join(lis)}</ol>'

def check_list(items):
    return '<ul class="check-list">' + "".join(f'<li>{icon("check")}<span>{i}</span></li>' for i in items) + '</ul>'

def before_after(before, after, alt_before, alt_after, label="Drag to compare before and after"):
    return f'''<div class="ba" data-reveal>
  <img src="/assets/img/{before}-1000.webp" srcset="/assets/img/{before}-600.webp 600w, /assets/img/{before}-1000.webp 1000w, /assets/img/{before}-1600.webp 1600w" sizes="(min-width: 900px) 50vw, 100vw" alt="{esc(alt_before)}" loading="lazy" decoding="async">
  <img class="ba__after" src="/assets/img/{after}-1000.webp" srcset="/assets/img/{after}-600.webp 600w, /assets/img/{after}-1000.webp 1000w, /assets/img/{after}-1600.webp 1600w" sizes="(min-width: 900px) 50vw, 100vw" alt="{esc(alt_after)}" loading="lazy" decoding="async">
  <span class="ba__tag ba__tag--before">Before</span><span class="ba__tag ba__tag--after">After</span>
  <input type="range" min="0" max="100" value="50" aria-label="{esc(label)}">
  <span class="ba__handle" aria-hidden="true"></span>
</div>'''

# ---------------- Schema ----------------

def local_business():
    return {
        "@type": "LocalBusiness",
        "@id": SITE["url"] + "/#business",
        "name": SITE["name"],
        "legalName": SITE["legal"],
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/logo-green-estates-gardening.webp",
        "image": SITE["url"] + "/assets/img/hero-lawn-mowing-moreton-bay-1600.webp",
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "description": "Lawn mowing, acreage and ride-on mowing, hedge trimming, garden cleanups, weed control, mulching and minor tree work across the Moreton Bay and Somerset regions of Queensland.",
        "address": {"@type": "PostalAddress", "addressLocality": SITE["locality"], "addressRegion": SITE["region"], "postalCode": SITE["postcode"], "addressCountry": SITE["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Moreton Bay Region, Queensland"},
            {"@type": "AdministrativeArea", "name": "Somerset Region, Queensland"},
        ] + [{"@type": "Place", "name": f"{s}, QLD"} for s in ALL_SUBURBS],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "07:00", "closes": "16:00"}],
        "founder": {"@type": "Person", "name": SITE["owner"]},
        "sameAs": [SITE["facebook"]],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Lawn and garden services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["card"], "url": f"{SITE['url']}/{s['slug']}/"}} for s in SERVICES]},
    }

def _strip(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()

def schema_graph(page):
    graph = [local_business(), {
        "@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/", "name": SITE["name"], "publisher": {"@id": SITE["url"] + "/#business"}}]
    url = SITE["url"] + page["path"]
    webpage = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": page["title"], "description": page["description"],
               "isPartOf": {"@id": SITE["url"] + "/#website"}, "about": {"@id": SITE["url"] + "/#business"}, "inLanguage": "en-AU"}
    if page.get("speakable", True):
        webpage["speakable"] = {"@type": "SpeakableSpecification", "cssSelector": [".speakable", "h1"]}
    graph.append(webpage)
    if page.get("crumbs"):
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["url"] + h} for i, (n, h) in enumerate(page["crumbs"])]})
    if page.get("service"):
        s = page["service"]
        graph.append({"@type": "Service", "@id": url + "#service", "name": s["name"], "serviceType": s["type"], "description": page["description"],
                      "provider": {"@id": SITE["url"] + "/#business"}, "url": url,
                      "areaServed": ([{"@type": "Place", "name": a} for a in s["area"]] if s.get("area") else [{"@type": "AdministrativeArea", "name": "Moreton Bay Region, Queensland"}, {"@type": "AdministrativeArea", "name": "Somerset Region, Queensland"}]),
                      "hasOfferCatalog": {"@type": "OfferCatalog", "name": s["name"], "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in s["items"]]}})
    if page.get("article"):
        a = page["article"]
        graph.append({"@type": "BlogPosting", "@id": url + "#article", "headline": a["headline"], "description": page["description"],
                      "image": SITE["url"] + f"/assets/img/{page['hero_img']}-1600.webp", "datePublished": a["date"], "dateModified": a["date"],
                      "author": {"@type": "Person", "name": SITE["owner"], "jobTitle": "Owner, Green Estates Gardening", "url": SITE["url"] + "/about/"},
                      "publisher": {"@type": "Organization", "name": SITE["name"], "logo": {"@type": "ImageObject", "url": SITE["url"] + "/assets/img/logo-green-estates-gardening.webp"}},
                      "mainEntityOfPage": {"@id": url + "#webpage"}, "articleSection": a["section"], "wordCount": a["words"], "inLanguage": "en-AU",
                      "about": {"@id": SITE["url"] + "/#business"}, "isPartOf": {"@type": "Blog", "@id": SITE["url"] + "/blog/#blog", "name": "Green Estates Gardening Blog"}})
    if page.get("blog_index"):
        graph.append({"@type": "Blog", "@id": SITE["url"] + "/blog/#blog", "name": "Green Estates Gardening Blog", "url": SITE["url"] + "/blog/",
                      "publisher": {"@id": SITE["url"] + "/#business"},
                      "blogPost": [{"@type": "BlogPosting", "headline": b["name"], "url": b["url"]} for b in page["blog_index"]]})
    if page.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}} for q, a in page["faqs"]]})
    return {"@context": "https://schema.org", "@graph": graph}

# ---------------- Page shell ----------------

def shell(page, body):
    url = SITE["url"] + page["path"]
    robots = '<meta name="robots" content="noindex, nofollow">' if page.get("noindex") else '<meta name="robots" content="index, follow, max-image-preview:large">'
    hero_img = page.get("hero_img", "hero-lawn-mowing-moreton-bay")
    og_img = SITE["url"] + f"/assets/img/{hero_img}-1600.webp"
    schema = json.dumps(schema_graph(page), ensure_ascii=False)
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page["title"])}</title>
<meta name="description" content="{esc(page["description"])}">
{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{esc(page["title"])}">
<meta property="og:description" content="{esc(page["description"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(page["title"])}">
<meta name="twitter:description" content="{esc(page["description"])}">
<meta name="twitter:image" content="{og_img}">
<meta name="theme-color" content="#1A3C0E">
<meta name="geo.region" content="AU-QLD">
<meta name="geo.placename" content="Wamuran">
<meta name="geo.position" content="{SITE['lat']};{SITE['lng']}">
<meta name="ICBM" content="{SITE['lat']}, {SITE['lng']}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/img/favicon.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/Montserrat-800-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/SourceSans3-400-latin.woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/fonts.css">
<link rel="preload" as="image" href="/assets/img/{hero_img}-1600.webp" imagesrcset="/assets/img/{hero_img}-1000.webp 1000w, /assets/img/{hero_img}-1600.webp 1600w" imagesizes="100vw">
<link rel="stylesheet" href="/assets/css/site.css">
<script type="application/ld+json">{schema}</script>
<!-- CRM form tracking (LeadConnector) -->
<script src="https://link.msgsndr.com/js/external-tracking.js" data-tracking-id="{SITE['tracking_id']}"></script>
</head>
<body>
{header(page["path"])}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
