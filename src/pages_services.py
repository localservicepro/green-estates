# -*- coding: utf-8 -*-
from gesite import *

def service_hero(s, h1, eyebrow, lead, preselect, hero_img, hero_alt, crumb_label):
    return f'''
<section class="hero hero--compact">
  <div class="hero__bg">{picture(hero_img, hero_alt, sizes=SIZES_HERO, loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    <div class="hero__grid">
      <div>
        {breadcrumbs([("Home", "/"), ("Services", "/#services"), (crumb_label, None)])}
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <span class="gold-rule" aria-hidden="true"></span>
        <p class="lead">{lead}</p>
        <div class="btn-row hero__cta">
          <a href="#quote" class="btn btn--primary btn--lg" data-open-quote>Get a Fixed-Price Quote {icon("arrow")}</a>
          <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} {SITE['phone']}</a>
        </div>
        {trust_strip()}
      </div>
      {quote_form("quote", preselect=preselect, title="Quote this job", intro="Address, rough size and what you need. We reply within one business day with a fixed price.", source="/" + s["slug"] + "/")}
    </div>
  </div>
</section>'''

# =====================================================================
def hedge_trimming():
    s = SERVICE_BY_SLUG["hedge-trimming-moreton-bay"]
    faqs = [
        ("When is the best time of year to trim hedges in South-East Queensland?",
         "<p>For most common Moreton Bay hedges (lilly pilly, murraya, photinia, viburnum, duranta) the main shaping cut is best in early spring, with lighter tidy-ups through summer and a final trim in autumn. Avoid hard cuts in the middle of a heatwave or right before a frost in the Somerset valleys. A twice- or three-times-a-year schedule keeps a hedge dense without stressing it.</p>"),
        ("Can you reduce the height of an overgrown hedge?",
         "<p>Usually, yes. Most hedging species tolerate a staged reduction: we take it down in one or two cuts across a season so the plant keeps enough leaf to recover and does not end up as bare sticks. Conifers and some natives do not reshoot from old wood, so we will tell you honestly what is achievable before we start.</p>"),
        ("Do you take the clippings away?",
         "<p>Always. Hedge trimming Moreton Bay wide includes raking, blowing down paths and garden beds and removing all green waste. You will not find a pile left by the fence.</p>"),
        ("How much does hedge trimming cost?",
         "<p>It depends on the length and height of the hedge, how long since it was last cut and access (ladders, slopes, neighbouring fences). A short front hedge in Morayfield is a quick job; a 40-metre boundary screen in Narangba that has not been touched in two years is not. We quote a fixed price after seeing the hedge or a couple of photos.</p>"),
        ("Do you trim hedges for body corporates and commercial properties?",
         "<p>Yes. We look after townhouse complexes, business parks and street frontages across North Lakes, Burpengary, Strathpine and Redcliffe on scheduled rounds, and we can combine hedging with lawn mowing and garden bed maintenance under one invoice.</p>"),
    ]
    body = service_hero(
        s, "Hedge Trimming &amp; Pruning Moreton Bay", "Formal shaping · height reduction · seasonal pruning",
        "Sharp lines, even tops and a hedge that stays healthy. Green Estates Gardening provides professional hedge trimming Moreton Bay and Somerset property owners book two or three times a year: formal shaping, height reduction, screen and shrub pruning, with every clipping removed before we leave.",
        "Hedge Trimming", "hero-hedge-trimming-moreton-bay", "Hedge trimming Moreton Bay: hedge trimmer cutting a long boundary hedge beside a lawn", "Hedge Trimming & Pruning")
    body += f'''
<section class="section section--light" aria-labelledby="intro-h">
  <div class="container">
    <div class="split split--rev">
      <div data-reveal>
        <span class="eyebrow">Hedges &amp; pruning</span>
        <h2 id="intro-h">Hedge trimming that keeps Moreton Bay gardens looking finished</h2>
        <p class="speakable"><strong>Green Estates Gardening trims and prunes hedges across the Moreton Bay and Somerset regions: formal shaping, height reduction, screening hedges and shrub pruning. Visits are quoted at a fixed price, timed to the species and the season, and all clippings are removed.</strong></p>
        <p>A well-cut hedge does more for a property than almost anything else in the garden. Lilly pilly and murraya screens along a Burpengary boundary, clipped photinia at a Morayfield entrance, a row of box balls beside a North Lakes driveway: when the lines are crisp the whole place looks cared for, and when they are not it is the first thing a visitor notices.</p>
        <p>We cut with sharp, well-maintained trimmers for a clean edge that heals quickly, shape by eye and string line for level tops, and time the heavier cuts so the plant pushes fresh growth rather than sulking. If a hedge has got away from you, we will tell you honestly whether it can be brought back in one visit or needs a staged reduction over a season.</p>
        {check_list(["Formal and informal hedges, screens and topiary balls", "Height and width reduction, staged where the species needs it", "Shrub, ornamental and fruit tree pruning up to minor-tree height", "Raked, blown down and green waste removed every visit"])}
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("hedge-trimming-formal-hedges", "Formal hedge trimming and shaped shrubs in a Moreton Bay front garden", sizes="(min-width: 1200px) 560px, (min-width: 900px) 46vw, calc(100vw - 32px)")}
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="types-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What we trim</span><h2 id="types-h">Hedge trimming Moreton Bay: the hedges we look after most</h2></div>
    <div class="grid grid--3" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("shears")}</span><h3>Lilly pilly &amp; murraya screens</h3><p>The workhorse privacy hedges of Caboolture, Narangba and Burpengary. Fast growers that need a firm cut two or three times a year to stay dense from the ground up.</p></div>
      <div class="card"><span class="icon-tile">{icon("leaf")}</span><h3>Photinia, viburnum &amp; duranta</h3><p>Colourful feature hedges that respond well to shaping. We cut after each flush of growth so the new red or gold tips are what you see.</p></div>
      <div class="card"><span class="icon-tile">{icon("tree")}</span><h3>Natives, conifers &amp; bougainvillea</h3><p>Westringia, callistemon, grevillea, conifer and bougainvillea screens each need a different approach. We know which reshoot from old wood and which do not, and prune accordingly.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="how-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">How we work</span>
        <h2 id="how-h">A hedge trimming visit, step by step</h2>
        <div class="steps" style="grid-template-columns:1fr;margin-top:24px">
          <div class="step"><h3>Assess and set the line</h3><p>Check the species, the last cut and the shape you want, then set string lines for level tops and straight faces.</p></div>
          <div class="step"><h3>Cut sides first, then the top</h3><p>Faces are cut slightly wider at the base so light reaches the lower leaves and the hedge stays full to the ground.</p></div>
          <div class="step"><h3>Clean up completely</h3><p>Clippings raked from beds and lawn, paths blown down, green waste loaded and removed. The garden looks better than when we arrived.</p></div>
        </div>
      </div>
      <div class="img-frame" data-reveal>
        {picture("hedge-trimming-round-hedge-house", "Perfectly rounded hedge beside a home after hedge trimming in Moreton Bay", sizes="(min-width: 1200px) 560px, (min-width: 900px) 46vw, calc(100vw - 32px)")}
      </div>
    </div>
  </div>
</section>

<section class="section section--light" aria-labelledby="gal-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Recent hedge work</span><h2 id="gal-h">Hedge trimming Moreton Bay results</h2></div>
    {gallery([
        ("hedge-trimming-long-hedge", "Long boundary hedge freshly trimmed level in Moreton Bay", True),
        ("hedge-trimming-shaped-hedges", "Shaped round hedges and mown lawn after hedge trimming", False),
        ("hedge-trimming-townhouse-hedges", "Neatly trimmed hedges at a Moreton Bay townhouse complex", False),
        ("garden-beds-trees-tidy", "Tidy garden beds and pruned shrubs beside a house in Moreton Bay", True),
    ])}
  </div>
</section>

{suburbs_section("Hedge trimming Moreton Bay &amp; Somerset: suburbs we cover", "Residential hedges, body-corporate screens and commercial frontages from Redcliffe and North Lakes through Caboolture to Kilcoy and the Somerset towns.", service_word="hedge trimming")}
{faq_section(faqs, heading="Hedge trimming Moreton Bay: frequently asked questions")}
{related_services(s["slug"], theme="white")}
{cta_band("Book a hedge trim before it gets away from you", "Send a photo of the hedge with the quote form and we will give you a fixed price, usually the same day.")}
'''
    page = dict(
        path=f"/{s['slug']}/",
        title="Hedge Trimming Moreton Bay | Green Estates Gardening",
        description="Hedge trimming Moreton Bay & Somerset: formal shaping, height reduction and pruning for lilly pilly, murraya and photinia. Fixed price, clippings removed.",
        keyword="Hedge Trimming Moreton Bay",
        hero_img="hero-hedge-trimming-moreton-bay",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Hedge Trimming & Pruning", f"/{s['slug']}/")],
        service=dict(name="Hedge Trimming & Pruning", type="Hedge trimming", items=["Formal hedge trimming", "Hedge height reduction", "Screen and shrub pruning", "Topiary shaping", "Green waste removal"]),
    )
    return page, body

# =====================================================================
def garden_cleanup():
    s = SERVICE_BY_SLUG["garden-cleanup-moreton-bay"]
    faqs = [
        ("How much does a garden cleanup cost in Moreton Bay?",
         "<p>Cleanups vary more than any other job we do, so we always quote after seeing the property or clear photos. The price reflects how overgrown it is, how much green waste has to be removed, and whether weed spraying, hedge work or mulching is included. You get a single fixed price for the whole reset, not an open-ended hourly rate.</p>"),
        ("What is included in a garden cleanup?",
         "<p>A typical garden cleanup Moreton Bay clients book includes mowing and edging overgrown lawn, whipper-snipping long grass, weeding garden beds, cutting back shrubs and hedges, clearing leaf litter and debris, and removing all green waste. Weed spraying, mulching and minor tree work can be added to the same visit.</p>"),
        ("Do you do weed spraying, and is it safe for pets and kids?",
         "<p>Yes. We treat lawn weeds like bindii, nutgrass and crowsfoot, and clear paths, driveways and garden beds. We use registered products applied to label rates, tell you exactly what has been used and how long to keep pets and children off treated areas (usually until the product has dried). Manual removal is available where you would rather avoid spraying altogether.</p>"),
        ("Can you clear a severely overgrown block or a rental between tenants?",
         "<p>That is our bread and butter. End-of-lease cleanups in Caboolture and Morayfield, sale preparations in Redcliffe and North Lakes, and blocks in Woodford or Kilcoy that have had a wet summer to themselves. We bring the ride-on, brushcutter, hedge trimmers and trailer and get it back to maintainable in one visit wherever possible.</p>"),
        ("What happens after the cleanup?",
         "<p>Most clients move onto a regular maintenance schedule so it never gets to that point again: fortnightly or monthly <a href='/lawn-mowing-moreton-bay/'>lawn mowing</a>, seasonal <a href='/hedge-trimming-moreton-bay/'>hedge trimming</a> and a spring <a href='/mulching-services-moreton-bay/'>mulch</a> to keep the weeds down. There is no obligation, but the cleanup price is much lower the second time around if we are maintaining it.</p>"),
        ("Do you take the green waste away?",
         "<p>Yes, every time. Green waste removal is part of every cleanup quote. We load it on the trailer and dispose of it properly, so you are not left with a pile for the council bin to chew through over the next month.</p>"),
    ]
    body = service_hero(
        s, "Garden Cleanup &amp; Weed Control Moreton Bay", "Overgrown yards · weed control · green waste removed",
        "Got a block that has got away from you? Green Estates Gardening provides one-off garden cleanup Moreton Bay and Somerset property owners, landlords and agents call when a yard needs a proper reset: overgrown lawn cut back, beds weeded, shrubs tamed, weeds treated and every scrap of green waste taken away. Fixed price, one visit wherever possible.",
        "Garden Cleanup", "hero-garden-cleanup-moreton-bay", "Garden cleanup Moreton Bay: overgrown yard cleared and tidied under established trees with bougainvillea", "Garden Cleanups & Weed Control")
    body += f'''
<section class="section section--light" aria-labelledby="intro-h">
  <div class="container">
    <div class="split">
      {before_after("garden-cleanup-before-overgrown", "garden-cleanup-after-cleared", "Before: severely overgrown back yard with long grass and weeds in Moreton Bay", "After: the same Moreton Bay yard cleared, weeded and tidied by Green Estates Gardening")}
      <div data-reveal>
        <span class="eyebrow">Real before &amp; after</span>
        <h2 id="intro-h">Garden cleanups that bring a Moreton Bay yard back in one visit</h2>
        <p class="speakable"><strong>Green Estates Gardening provides one-off garden cleanups and weed control across the Moreton Bay and Somerset regions. A cleanup covers overgrown lawn, garden bed weeding, shrub and hedge cut-backs, weed treatment and full green waste removal, quoted as a single fixed price.</strong></p>
        <p>Drag the slider. That is a real Moreton Bay back yard: knee-high grass and a season of weeds turned back into a clean, open space in a single visit. It is the same reset we do for rentals between tenants in Caboolture and Morayfield, for owners preparing to sell in Redcliffe and North Lakes, and for acreage in Wamuran, Woodford and Kilcoy that a wet summer took over.</p>
        {check_list(["Overgrown lawn mowed, brushcut and edged", "Beds hand-weeded, shrubs and hedges cut back", "Lawn, path and driveway weeds treated", "All green waste loaded and removed"])}
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="incl-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What's included</span><h2 id="incl-h">Garden cleanup Moreton Bay: one fixed price for the whole reset</h2><p class="lead">Pick the parts you need or hand us the lot. Every cleanup is scoped up front so there are no surprises on the invoice.</p></div>
    <div class="grid grid--3" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("mower")}</span><h3>Overgrown lawn &amp; long grass</h3><p>Brushcutter first, then the mower at a raised height, then a second pass for a clean finish. Edges, paths and driveways reclaimed. Snake habitat gone.</p></div>
      <div class="card"><span class="icon-tile">{icon("leaf")}</span><h3>Garden beds &amp; shrubs</h3><p>Hand weeding, dead-heading, cutting back overgrown shrubs and hedges, clearing leaf litter and palm fronds so the beds are ready for mulch.</p></div>
      <div class="card"><span class="icon-tile">{icon("drop")}</span><h3>Weed control</h3><p>Bindii, nutgrass, crowsfoot and broadleaf weeds in lawns; weeds in paths, gravel and garden beds. Registered products at label rates, or manual removal if you prefer.</p></div>
      <div class="card"><span class="icon-tile">{icon("shears")}</span><h3>Hedge &amp; screen cut-backs</h3><p>Overgrown lilly pilly, murraya and bougainvillea brought back to size. Staged where the species needs it so it recovers well.</p></div>
      <div class="card"><span class="icon-tile">{icon("tree")}</span><h3>Minor tree work</h3><p>Low branches over paths, sheds and roofs, storm-dropped limbs and small trees removed as part of the same visit.</p></div>
      <div class="card"><span class="icon-tile">{icon("truck")}</span><h3>Green waste removal</h3><p>Everything loaded on the trailer and taken away. You are left with a tidy yard, not a mountain for the wheelie bin.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="who-h">
  <div class="container">
    <div class="split split--rev">
      <div data-reveal>
        <span class="eyebrow">Who calls us</span>
        <h2 id="who-h">Who books a garden cleanup Moreton Bay wide? Landlords, agents, sellers and anyone who wants it sorted</h2>
        <p class="lead">A cleanup is usually triggered by a deadline: a tenant moving out, a photographer booked for Saturday, a council letter about long grass, or a family event in the back yard.</p>
        <div class="grid grid--2" style="margin-top:28px">
          <div class="feature"><span class="icon-tile">{icon("calendar")}</span><div><h3>End-of-lease resets</h3><p>Rentals across Caboolture, Morayfield, Burpengary and Narangba returned to the condition on the entry report.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("tag")}</span><div><h3>Pre-sale presentation</h3><p>Street appeal for listings in Redcliffe, North Lakes and Strathpine. Clean edges photograph well.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("shield")}</span><div><h3>Overgrown acreage</h3><p>Blocks in Wamuran, D'Aguilar, Woodford and the Somerset valleys knocked back before the snakes and fire season arrive.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("users")}</span><div><h3>Help for owners who can't</h3><p>Older residents, new parents, FIFO workers. One visit, then an easy schedule to keep it that way.</p></div></div>
        </div>
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("garden-cleanup-tidy-yard", "Tidy front yard and footpath after a garden cleanup in Moreton Bay", sizes="(min-width: 1200px) 560px, (min-width: 900px) 46vw, calc(100vw - 32px)")}
      </div>
    </div>
  </div>
</section>

{suburbs_section("Garden cleanup Moreton Bay &amp; Somerset: suburbs we cover", "From coastal Redcliffe to rural Esk. If the yard has got away from you, we can almost certainly get to it this week.", service_word="garden cleanups and weed control")}
{faq_section(faqs, heading="Garden cleanup Moreton Bay: frequently asked questions")}
{related_services(s["slug"], theme="white")}
{cta_band("Send a photo, get a fixed price", "The worse it looks, the more we enjoy the before-and-after. Attach a couple of photos to your enquiry or describe it in the notes.")}
'''
    page = dict(
        path=f"/{s['slug']}/",
        title="Garden Cleanup Moreton Bay | Green Estates Gardening",
        description="One-off garden cleanup Moreton Bay & Somerset: overgrown yards cleared, weeds treated, shrubs cut back, green waste removed. Fixed-price quote, free.",
        keyword="Garden Cleanup Moreton Bay",
        hero_img="hero-garden-cleanup-moreton-bay",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Garden Cleanups & Weed Control", f"/{s['slug']}/")],
        service=dict(name="Garden Cleanups & Weed Control", type="Garden cleanup", items=["Overgrown yard cleanup", "Weed spraying and removal", "Garden bed weeding", "End-of-lease garden cleanup", "Green waste removal"]),
    )
    return page, body

# =====================================================================
def mulching():
    s = SERVICE_BY_SLUG["mulching-services-moreton-bay"]
    faqs = [
        ("When is the best time to mulch a garden in Queensland?",
         "<p>Late winter to early spring (August to October) is ideal across Moreton Bay: the soil is warming, the beds have just been weeded, and a fresh layer of mulch is in place before the summer heat and storm rain arrive. A top-up in autumn keeps beds covered through the drier months. We can mulch at any time of year, but spring gives the best return.</p>"),
        ("How thick should mulch be, and what type do you use?",
         "<p>Around 75 millimetres settled is the sweet spot: thick enough to suppress weeds and hold moisture, thin enough for rain to get through. We work with hardwood chip, forest mulch, tea tree and sugar cane depending on the bed. Hardwood and forest mulch last longest in landscape beds; tea tree and sugar cane suit vegetable and native gardens. We will recommend one and price the supply and spread as a single figure.</p>"),
        ("Do you supply the mulch or do I?",
         "<p>Either. Most clients let us supply, because we buy in bulk, know which landscape yards around Caboolture and Morayfield are reliable, and can price supply plus spread as one fixed number. If you already have a pile in the driveway, we will spread that instead.</p>"),
        ("What counts as minor tree work?",
         "<p>Small limbs and branches you can safely reach from the ground or a step ladder: growth over gutters, paths and sheds, storm-dropped limbs, small trees and palms, and crown lifting to let light onto the lawn. It is scope-clear work priced alongside mulching or a cleanup. Large removals, climbing work and anything near power lines need a qualified arborist, and we will tell you if that is the case.</p>"),
        ("Will mulching stop weeds?",
         "<p>It will dramatically reduce them. Our mulching services Moreton Bay clients book each spring work because mulch blocks the light most weed seeds need to germinate and makes the ones that do come up easy to pull. For persistent problems like nutgrass we treat the bed first, then mulch. Combined with our <a href='/garden-cleanup-moreton-bay/'>weed control</a> service it is the lowest-maintenance garden you can have in a Moreton Bay summer.</p>"),
    ]
    body = service_hero(
        s, "Mulching &amp; Minor Tree Work Moreton Bay", "Bed prep · mulch supply &amp; spread · small limb removal",
        "Beds that hold moisture through a Queensland summer and keep the weeds down. Green Estates Gardening provides mulching services Moreton Bay and Somerset gardens are built for: bed preparation, weed treatment, mulch supplied and spread to the right depth, plus small limb and branch removal so light gets where it should.",
        "Mulching", "hero-mulching-moreton-bay", "Mulching services Moreton Bay: freshly mulched garden bed with shrubs along a commercial building", "Mulching & Minor Tree Work")
    body += f'''
<section class="section section--light" aria-labelledby="intro-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">Mulching done right</span>
        <h2 id="intro-h">Mulching services for Moreton Bay gardens that have to survive summer</h2>
        <p class="speakable"><strong>Green Estates Gardening supplies and spreads mulch across the Moreton Bay and Somerset regions, preparing and weeding beds first, then laying hardwood, forest, tea tree or sugar cane mulch to around 75 millimetres. Minor tree work such as small limb and branch removal is offered on the same fixed-price visit.</strong></p>
        <p>Between the January storms, the humid weeks that follow and the dry stretch through winter, garden beds in Caboolture, Narangba and North Lakes take a beating. A properly prepared and mulched bed holds water for days longer, keeps root zones cooler, feeds the soil as it breaks down and starves out the weeds that otherwise fill every gap by February.</p>
        <p>The difference between mulch that works and mulch that looks tired by Christmas is the preparation. We weed and edge the bed, treat anything persistent, top up soil where it has slumped, then spread to an even depth and keep it clear of trunks and stems. Out in the Somerset towns of Kilcoy, Esk and Toogoolawah, the same approach on larger rural beds and driveways saves a lot of watering.</p>
        {check_list(["Bed preparation: weeding, edging, soil top-up and weed treatment", "Mulch supplied in bulk and spread to an even 75 mm", "Hardwood chip, forest mulch, tea tree or sugar cane to suit the bed", "Small limb and branch removal on the same visit"])}
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("mulched-garden-bed-fenceline", "Freshly mulched garden bed along a fence line at a Moreton Bay property", sizes="(min-width: 1200px) 560px, (min-width: 900px) 46vw, calc(100vw - 32px)")}
        <div class="img-badge"><div><strong>75 mm</strong><br><span>settled mulch depth</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="incl-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What's included</span><h2 id="incl-h">Mulching services Moreton Bay: what is included</h2></div>
    <div class="grid grid--3" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("leaf")}</span><h3>Bed preparation</h3><p>Beds weeded, edges re-cut, old mulch turned or removed, soil topped up where needed and persistent weeds treated before a single barrow goes down.</p></div>
      <div class="card"><span class="icon-tile">{icon("truck")}</span><h3>Mulch supply &amp; spread</h3><p>Bulk mulch delivered and spread to an even depth, kept clear of trunks and building slabs. One fixed price for supply and labour, from a single bed to a whole acreage garden.</p></div>
      <div class="card"><span class="icon-tile">{icon("tree")}</span><h3>Minor tree work</h3><p>Small limbs over roofs, gutters and paths, storm-dropped branches, small trees and palms, and crown lifting for more light. Ground and step-ladder work only; we refer larger jobs to an arborist.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="types-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Choosing a mulch</span><h2 id="types-h">Which mulch suits your Moreton Bay garden?</h2></div>
    <div class="grid grid--4" data-reveal-stagger>
      <div class="card"><h3>Hardwood chip</h3><p>Longest lasting in landscape beds and along driveways. Neutral colour, slow to break down, ideal for large rural gardens in Wamuran, Woodford and Kilcoy.</p></div>
      <div class="card"><h3>Forest mulch</h3><p>Mixed leaf and chip that knits together and resists washing out on slopes. Good value across big areas and popular in Morayfield and Burpengary estates.</p></div>
      <div class="card"><h3>Tea tree</h3><p>Fine, dark and tidy. Suits native gardens and feature beds around entrances where appearance matters. Breaks down faster and feeds the soil.</p></div>
      <div class="card"><h3>Sugar cane</h3><p>Best for vegetable patches, herb beds and anything you want to improve the soil quickly. Top up each season.</p></div>
    </div>
  </div>
</section>

<section class="section section--light" aria-labelledby="gal-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Recent work</span><h2 id="gal-h">Recent mulching services Moreton Bay jobs</h2></div>
    {gallery([
        ("mulching-garden-bed-commercial", "Commercial garden bed freshly mulched and planted in Moreton Bay", True),
        ("garden-beds-trees-tidy", "Mulched garden beds and pruned trees beside a house in Moreton Bay", False),
        ("garden-maintenance-commercial-strip", "Mulched frontage and mown lawn at a Moreton Bay business", False),
        ("hedge-trimming-townhouse-hedges", "Hedges and mulched beds at a Moreton Bay townhouse complex", False),
        ("garden-cleanup-tidy-yard", "Tidy front garden after mulching and cleanup in Moreton Bay", False),
        ("acreage-mowing-shed", "Rural property in the Somerset region with mown lawn and garden beds", True),
    ])}
  </div>
</section>

{suburbs_section("Mulching services Moreton Bay &amp; Somerset: suburbs we cover", "Spring mulching rounds run through the residential corridor from Redcliffe to Caboolture and out to the rural blocks of D'Aguilar, Woodford and the Somerset towns.", service_word="mulching and minor tree work")}
{faq_section(faqs, heading="Mulching services Moreton Bay: frequently asked questions")}
{related_services(s["slug"], theme="white")}
{cta_band("Get your beds ready before summer", "Send the number and rough size of the beds, or a couple of photos, and we will quote supply and spread as one fixed price.")}
'''
    page = dict(
        path=f"/{s['slug']}/",
        title="Mulching Services Moreton Bay | Green Estates",
        description="Mulching services Moreton Bay & Somerset: bed prep, mulch supplied and spread, plus minor tree work and branch removal. Free fixed-price quotes.",
        keyword="Mulching Services Moreton Bay",
        hero_img="hero-mulching-moreton-bay",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Mulching & Minor Tree Work", f"/{s['slug']}/")],
        service=dict(name="Mulching & Minor Tree Work", type="Mulching", items=["Garden bed preparation", "Mulch supply and spreading", "Minor tree work and branch removal", "Storm tidy-ups"]),
    )
    return page, body
