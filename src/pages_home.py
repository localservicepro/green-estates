# -*- coding: utf-8 -*-
from gesite import *
BLOG_TEASER = ''

def home():
    faqs = [
        ("How much does lawn mowing cost in Moreton Bay?",
         "<p>Price depends on the size of the block, how long the grass is and how much edging and trimming is involved. A standard residential lawn in Caboolture, Morayfield or North Lakes is quoted differently from a two-acre lifestyle block in Wamuran or Kilcoy. We quote every property as a fixed price before we start, so the number you agree to is the number you pay. Send the address and a rough size through the quote form and we will come back with a firm price.</p>"),
        ("How often should I have my lawn mowed in South-East Queensland?",
         "<p>Through the warm, wet months from roughly October to March, most lawns in Moreton Bay need mowing every one to two weeks. Buffalo, couch and kikuyu all grow hard in humidity. From May to August growth slows and monthly or six-weekly visits are usually enough. We set a schedule that suits your grass type and adjust it with the season.</p>"),
        ("Do you do ride-on mowing for acreage and larger blocks?",
         "<p>Yes. Acreage and ride-on mowing is one of our specialities. We run commercial zero-turn mowers for lifestyle blocks, hobby farms and large yards across Wamuran, D'Aguilar, Woodford, Elimbah, Kilcoy and the wider Somerset region, and we still bring the push mower and edger for the tight areas around the house. See our <a href='/acreage-mowing-moreton-bay/'>acreage mowing page</a> for details.</p>"),
        ("Which suburbs do you service?",
         "<p>We are based in Wamuran and cover the Moreton Bay Region, including Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Strathpine, Redcliffe, Bribie Island, Beachmere, Elimbah, D'Aguilar, Woodford and Bracalba, plus the Somerset Region: Kilcoy, Esk, Toogoolawah, Lowood and Fernvale. See the <a href='/service-areas/'>service areas</a> page for local detail. If you are nearby but not listed, ask us.</p>"),
        ("Do I need to be home when you mow?",
         "<p>No. Most of our regular clients are at work when we visit. As long as we can get to the lawn and any gates are unlocked (or you have given us the code) we get on with it, tidy up and message you when we are done. Payment is by bank transfer or card, so there is nothing to organise on the day.</p>"),
        ("Can you take care of hedges, weeds and mulching as well as mowing?",
         "<p>Yes. Many clients bundle <a href='/hedge-trimming-moreton-bay/'>hedge trimming</a>, <a href='/garden-cleanup-moreton-bay/'>weed control and garden cleanups</a> and <a href='/mulching-services-moreton-bay/'>mulching</a> into one <a href='/garden-maintenance-moreton-bay/'>regular garden maintenance</a> visit. One crew, one invoice, and a property that always looks looked-after.</p>"),
    ]
    # Recent work: every suburb-labelled tile links to that suburb's page (review v2, section 5);
    # tiles without a suburb link to the service page.
    gal = gallery([
        ("ride-on-mower-acreage-wamuran", "Ride-on acreage mowing under gum trees on a lifestyle block in Wamuran", True, SUBURB_LINKS.get("Wamuran"), "Acreage mowing · Wamuran"),
        ("freshly-mown-lawn-redcliffe", "Freshly mown and edged nature strip after lawn mowing in Redcliffe", False, SUBURB_LINKS.get("Redcliffe"), "Lawn mowing · Redcliffe"),
        ("push-mower-striped-lawn-morayfield", "Push mowing leaving neat stripes on a residential lawn in Morayfield", False, SUBURB_LINKS.get("Morayfield"), "Lawn mowing · Morayfield"),
        ("garden-maintenance-commercial-strip", "Mown lawn and tidy garden beds at a Moreton Bay business park on a garden maintenance round", True, "/garden-maintenance-moreton-bay/", "Garden maintenance · commercial"),
        ("zero-turn-mower-caboolture", "Zero-turn mower on a large lawn on the Caboolture acreage fringe", True, SUBURB_LINKS.get("Caboolture"), "Ride-on mowing · Caboolture"),
        ("hedge-trimming-round-hedge-house", "Neatly rounded hedge after hedge trimming at a Moreton Bay home", False, "/hedge-trimming-moreton-bay/", "Hedge trimming"),
        ("mulched-garden-bed-fenceline", "Freshly mulched garden bed along a fence line in Moreton Bay", False, "/mulching-services-moreton-bay/", "Mulching"),
        ("footpath-edging-strathpine", "Crisp footpath edging after lawn mowing on a residential street in Strathpine", True, SUBURB_LINKS.get("Strathpine"), "Lawn mowing · Strathpine"),
    ])

    body = f'''
<section class="hero">
  <div class="hero__bg">{picture("hero-lawn-mowing-moreton-bay", "Freshly mown striped lawn in front of a Moreton Bay home after professional lawn mowing", sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    <div class="hero__grid">
      <div>
        <span class="eyebrow">Wamuran based · Moreton Bay &amp; Somerset</span>
        <h1>Lawn Mowing &amp; Garden Maintenance Across Moreton Bay &amp; Somerset</h1>
        <span class="gold-rule" aria-hidden="true"></span>
        <p class="lead">Green Estates Gardening is the Wamuran-based crew homeowners, landlords and acreage owners rely on week in, week out for lawn mowing, acreage and ride-on mowing, hedge trimming, garden cleanups, weed control and mulching. Fixed-price quotes, one reliable local operator, and a property you are proud to pull into.</p>
        <div class="btn-row hero__cta">
          <a href="#quote" class="btn btn--primary btn--lg" data-open-quote>Get a Free Quote {icon("arrow")}</a>
          <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} {SITE['phone']}</a>
        </div>
        {trust_strip()}
      </div>
      {quote_form("quote", source="/")}
    </div>
  </div>
</section>

<section class="section section--light" id="services" aria-labelledby="services-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">What we do</span>
      <h2 id="services-h">Six services, one local team</h2>
      <p class="lead">Whether you need a fortnightly mow in Caboolture, an acreage cut in Woodford, a hedge brought back into line in North Lakes or an overgrown block in Narangba reset, everything is quoted up front and done properly. Pick the service, or send the address and let us scope it.</p>
    </div>
    <div class="grid grid--services" data-reveal-stagger>{service_cards()}</div>
  </div>
</section>

<section class="section section--dark" id="why" aria-labelledby="why-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">Why Green Estates</span>
        <h2 id="why-h">Why Moreton Bay homeowners and property managers choose us</h2>
        <p class="lead">Owner-operated by {SITE['owner']}, with more than 13 years of hands-on lawn and garden experience across the Moreton Bay and Somerset regions. When you book Green Estates Gardening you get the same person, the same standard and the same fixed price every visit.</p>
        <div class="grid grid--2" style="margin-top:32px">
          <div class="feature"><span class="icon-tile">{icon("tag")}</span><div><h3>Fixed-price quotes</h3><p>Every job is priced before we start. No hourly surprises, no add-ons on the invoice.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("calendar")}</span><div><h3>Reliable schedules</h3><p>Weekly, fortnightly or monthly rounds you can plan around, because the visit happens on the day we said it would.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("truck")}</span><div><h3>Commercial equipment</h3><p>Zero-turn ride-ons for acreage, sharp push mowers for residential lawns, and the right gear for hedges and cleanups.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("pin")}</span><div><h3>Genuinely local</h3><p>Based in Wamuran, so Caboolture, Morayfield, Kilcoy and D'Aguilar are our backyard, not the end of a long run.</p></div></div>
        </div>
      </div>
      <div>
        <div class="stats" data-reveal-stagger>
          <div class="stat"><div class="stat__num"><span data-count="5" data-decimals="1">5.0</span><span class="gold">★</span></div><div class="stat__label">Google rating from local clients</div></div>
          <div class="stat"><div class="stat__num" data-count="23">23</div><div class="stat__label">Five-star Google reviews</div></div>
          <div class="stat"><div class="stat__num"><span data-count="13">13</span>+</div><div class="stat__label">Years of local experience</div></div>
          <div class="stat"><div class="stat__num" data-count="{len(ALL_SUBURBS)}">{len(ALL_SUBURBS)}</div><div class="stat__label">Suburbs across Moreton Bay &amp; Somerset</div></div>
        </div>
        <div class="img-frame" style="margin-top:32px" data-reveal>
          {picture("branded-trailer-green-estates", "Green Estates Gardening branded trailer on site at a Moreton Bay lawn mowing job", sizes="(min-width: 900px) 45vw, 100vw")}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--light" id="results" aria-labelledby="results-h">
  <div class="container">
    <div class="split">
      {before_after("yard-cleanup-before-long-grass", "yard-cleanup-after-mown", "Before: overgrown long grass beside a shed in Moreton Bay before lawn mowing and cleanup", "After: the same Moreton Bay yard freshly mown and tidied by Green Estates Gardening")}
      <div data-reveal>
        <span class="eyebrow">Real results</span>
        <h2 id="results-h">Before and after: a real Moreton Bay yard reset</h2>
        <p>Drag the slider. This is our own work, not a stock photo: long, seed-headed grass around a shed brought back to a clean, even cut in one visit. It is the kind of reset we do every week for rental properties in Caboolture, sale preparations in Redcliffe and acreage that got away from the owner over a wet summer.</p>
        {check_list(["One-off cleanups or ongoing lawn mowing schedules", "Green waste taken away, not left in a pile", "Edges, paths and driveways blown down before we leave"])}
        <a href="/garden-cleanup-moreton-bay/" class="btn btn--primary">Garden cleanups &amp; weed control {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="process" aria-labelledby="process-h">
  <div class="container">
    <div class="section-head center" data-reveal>
      <span class="eyebrow">How it works</span>
      <h2 id="process-h">Booking us is a three-step job</h2>
    </div>
    <div class="steps" data-reveal-stagger>
      <div class="step"><h3>Send the details</h3><p>Fill in the quote form with the address, rough block size and what you need, or call {SITE['phone']}. Photos help but are not essential.</p></div>
      <div class="step"><h3>Get a fixed price</h3><p>We price the job, usually within one business day. For acreage or big cleanups we may swing past first so the number is right.</p></div>
      <div class="step"><h3>We turn up and do it properly</h3><p>Mowed, edged, trimmed and blown down. Then we lock in a schedule so you never have to think about the lawn again.</p></div>
    </div>
  </div>
</section>

{suburbs_section("The suburbs we serve across Moreton Bay &amp; Somerset", "From our base in Wamuran we cover the northern corridor, the Redcliffe peninsula and Bribie Island, and out through the D'Aguilar Range into the Somerset Region. Suburbs with a local page are linked; the rest are on the same rounds.")}

<section class="section section--light" id="gallery" aria-labelledby="gallery-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Recent work</span>
      <h2 id="gallery-h">Recent work from Wamuran to Redcliffe</h2>
      <p class="lead">Acreage, residential streets, commercial strips and body-corporate hedges. Each tile opens the local page for that suburb or service.</p>
    </div>
    {gal}
  </div>
</section>

<section class="section section--white" id="reviews" aria-labelledby="reviews-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">Rated by locals</span>
        <h2 id="reviews-h">Rated 5.0 on Google by Moreton Bay locals</h2>
        <p class="lead">Every one of our 23 Google reviews is five stars. Reliability is the word that comes up most: punctual, well priced, and the same standard visit after visit, from suburban lawns in Caboolture to a 3.74-acre property on Somerset Dam.</p>
        <p>Regular mowing clients across Morayfield, Burpengary, North Lakes and Strathpine, acreage owners in Wamuran and Woodford, and property managers with a list of rentals to keep tidy. If you would like references for a larger or commercial job, just ask.</p>
        <div class="btn-row"><a class="btn btn--primary" href="https://www.google.com/search?q=Green+Estates+Gardening+Wamuran+reviews" rel="noopener" target="_blank">Read our Google reviews {icon("arrow")}</a><a class="btn btn--secondary" href="{SITE['facebook']}" rel="noopener" target="_blank">{icon("facebook")} Facebook</a></div>
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("ride-on-mowing-acreage-moreton-bay", "Green Estates Gardening operator on a zero-turn ride-on mower on Moreton Bay acreage", sizes="(min-width: 900px) 45vw, 100vw")}
        <div class="img-badge">{stars()}<div><strong>5.0</strong><br><span>23 Google reviews</span></div></div>
      </div>
    </div>
    <div class="section-head" style="margin-top:64px;margin-bottom:28px" data-reveal><h3>What our clients say</h3><p class="muted">Four of the 23 five-star reviews, quoted as written.</p></div>
    {review_cards()}
  </div>
</section>

{BLOG_TEASER}
{faq_section(faqs, heading="Questions we get asked", intro="Straight answers on pricing, scheduling and what is included.")}
{cta_band("Ready to hand the lawn over?", "Fixed-price lawn mowing, hedging, cleanups and mulching across Moreton Bay and Somerset. Send the details and we will come back with a price within one business day.")}
'''
    page = dict(
        path="/",
        title="Lawn Mowing & Garden Care Moreton Bay | Green Estates",
        description="Green Estates Gardening: lawn mowing, acreage mowing, hedge trimming, garden cleanups and mulching across Moreton Bay and Somerset. Fixed-price quotes.",
        keyword="Lawn Mowing",
        hero_img="hero-lawn-mowing-moreton-bay",
        faqs=faqs,
        crumbs=[("Home", "/")],
    )
    return page, body
