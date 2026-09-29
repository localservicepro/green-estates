# -*- coding: utf-8 -*-
from gesite import *

def about():
    faqs = [
        ("Who will actually turn up to do the work?",
         f"<p>{SITE['owner']}, the owner, with the same small local team on every visit. We do not subcontract rounds out, which is why the standard is consistent from Redcliffe to Kilcoy.</p>"),
        ("Where are you based and how far do you travel?",
         "<p>We are based in Wamuran, north-west of Caboolture. Regular rounds cover the Moreton Bay Region from Redcliffe and North Lakes up through Morayfield and Caboolture to Woodford and D'Aguilar, and the Somerset Region including Kilcoy, Esk, Toogoolawah, Lowood and Fernvale.</p>"),
        ("Are you a registered business?",
         f"<p>Yes. We trade as {SITE['legal']} and invoice every job. Details are on every quote and invoice.</p>"),
        ("Do you offer regular maintenance packages?",
         "<p>Yes, and most clients end up on one. A package bundles lawn mowing with seasonal hedge trimming, weed control and a spring mulch under one fixed monthly or per-visit price, scheduled around your grass and your season.</p>"),
    ]
    body = f'''
<section class="hero hero--compact">
  <div class="hero__bg">{picture("hero-about-green-estates", "Green Estates Gardening ute and branded trailer parked on a Moreton Bay street", sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    <div class="hero__grid">
      <div>
        {breadcrumbs([("Home", "/"), ("About", None)])}
        <span class="eyebrow">Owner-operated · Wamuran QLD</span>
        <h1>Local Gardeners Serving Moreton Bay &amp; Somerset</h1>
        <span class="gold-rule" aria-hidden="true"></span>
        <p class="lead">Green Estates Gardening is a Wamuran-based, owner-operated lawn and garden business. We are the local gardeners Moreton Bay and Somerset property owners have trusted for reliable mowing, hedging, cleanups and mulching, with more than 13 years of hands-on experience behind every visit.</p>
        <div class="btn-row hero__cta">
          <a href="/contact/#quote" class="btn btn--primary btn--lg">Get a Free Quote {icon("arrow")}</a>
          <a href="tel:{SITE['phone_tel']}" class="btn btn--secondary btn--lg">{icon("phone")} {SITE['phone']}</a>
        </div>
        {trust_strip()}
      </div>
      <div class="hero__aside img-frame img-frame--tall">{picture("ride-on-mowing-acreage-moreton-bay", "Hamish Baggley of Green Estates Gardening ride-on mowing acreage in Moreton Bay", sizes="(min-width: 1024px) 40vw, 100vw")}</div>
    </div>
  </div>
</section>

<section class="section section--light" aria-labelledby="story-h">
  <div class="container">
    <div class="split">
      <div class="prose" data-reveal>
        <span class="eyebrow">Our story</span>
        <h2 id="story-h">A local lawn and garden business, built on turning up</h2>
        <p class="speakable"><strong>Green Estates Gardening is owned and operated by {SITE['owner']} from Wamuran, Queensland. The business provides lawn mowing, acreage mowing, hedge trimming, garden cleanups, weed control, mulching and minor tree work across the Moreton Bay and Somerset regions, with fixed-price quotes and a 5.0 Google rating.</strong></p>
        <p>Ask anyone who has tried to find a gardener in Caboolture or Morayfield what the hardest part is and they will tell you: getting someone to show up twice. Green Estates was built around that one problem. Every job is quoted as a fixed price, every visit goes in the calendar, and the same people come back each time so the standard never slips.</p>
        <p>{SITE['owner']} has spent more than 13 years mowing, hedging and clearing properties across South-East Queensland, from tight townhouse courtyards in North Lakes to 20-acre blocks in the Somerset valleys. That experience shows in the small things: knowing when a buffalo lawn wants to be cut higher, which hedges will not reshoot from old wood, and how a Wamuran paddock behaves after a week of February rain.</p>
        <h3>What local gardeners Moreton Bay property owners can expect from us</h3>
        {check_list(["<strong>Reliable:</strong> we come on the day we said, and we message when the job is done.", "<strong>Honest pricing:</strong> one fixed price, agreed before we start, no hourly surprises.", "<strong>Properly finished:</strong> edged, trimmed, blown down and green waste removed every time.", "<strong>Genuinely local:</strong> based in Wamuran, working across Moreton Bay and Somerset every week."])}
      </div>
      <div>
        <div class="img-frame" data-reveal>{picture("branded-trailer-green-estates", "Green Estates Gardening trailer with logo and phone number at a job in Moreton Bay", sizes="(min-width: 900px) 45vw, 100vw")}</div>
        <div class="stats" style="margin-top:28px" data-reveal-stagger>
          <div class="stat"><div class="stat__num"><span data-count="13">13</span>+</div><div class="stat__label">Years of experience</div></div>
          <div class="stat"><div class="stat__num"><span data-count="5" data-decimals="1">5.0</span><span class="gold">★</span></div><div class="stat__label">Google rating, 23 reviews</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="rev-h">
  <div class="container">
    <div class="section-head center" data-reveal><span class="eyebrow">What our clients say</span><h2 id="rev-h">Rated 5.0 on Google by the people we work for</h2><p class="lead">Four of our 23 five-star Google reviews, quoted as written. Several of these clients have been with us for more than a decade.</p></div>
    {review_cards()}
  </div>
</section>

<section class="section section--dark" aria-labelledby="serve-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Who we work with</span><h2 id="serve-h">Local gardeners Moreton Bay homes, acreage, rentals and commercial sites rely on</h2><p class="lead">The same fixed-price, turn-up-on-time approach whether it is a fortnightly lawn in Burpengary or a body-corporate contract in North Lakes.</p></div>
    <div class="grid grid--4" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("users")}</span><h3>Homeowners</h3><p>Regular lawn mowing, hedges and seasonal mulching so weekends are yours again. Caboolture, Morayfield, Narangba, Strathpine, Redcliffe and beyond.</p></div>
      <div class="card"><span class="icon-tile">{icon("mower")}</span><h3>Acreage owners</h3><p>Ride-on mowing and paddock maintenance for lifestyle blocks in Wamuran, D'Aguilar, Woodford, Elimbah, Bracalba and the Somerset towns.</p></div>
      <div class="card"><span class="icon-tile">{icon("calendar")}</span><h3>Property managers</h3><p>End-of-lease cleanups, routine maintenance on rental portfolios and photos sent when each job is done. One invoice per property.</p></div>
      <div class="card"><span class="icon-tile">{icon("shield")}</span><h3>Commercial &amp; strata</h3><p>Business parks, townhouse complexes and street frontages on scheduled rounds, with lawns, hedges and beds under one contract.</p></div>
    </div>
  </div>
</section>

<section class="section section--light" aria-labelledby="svc-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Our services</span><h2 id="svc-h">Everything a Moreton Bay property needs, from one local team</h2></div>
    <div class="grid grid--services" data-reveal-stagger>{service_cards(sizes="(min-width: 1024px) 25vw, 100vw")}</div>
  </div>
</section>

{faq_section(faqs, heading="About Green Estates Gardening: common questions", theme="white")}
{cta_band("Want a gardener who actually turns up?", "Send the details of your property and we will come back with a fixed price within one business day.")}
'''
    page = dict(
        path="/about/",
        title="Local Gardeners Moreton Bay | About Green Estates Gardening",
        description="Meet the local gardeners Moreton Bay & Somerset owners trust for reliable mowing, hedging and cleanups. Owner-operated from Wamuran, 5.0 Google rating.",
        keyword="Local Gardeners Moreton Bay",
        hero_img="hero-about-green-estates",
        faqs=faqs,
        crumbs=[("Home", "/"), ("About", "/about/")],
    )
    return page, body

# =====================================================================
def contact():
    faqs = [
        ("How quickly will I hear back about my quote?",
         "<p>Within one business day, Monday to Saturday, and usually the same day for standard residential lawn mowing quotes. Acreage mowing and large cleanups sometimes need a quick drive-by first so the price is accurate.</p>"),
        ("What information do you need to quote lawn mowing?",
         "<p>The property address, a rough idea of the block size, what you want done (mowing only, or mowing plus hedges, weeds or mulching) and how often. A photo or two of the yard helps but is not essential. The form on this page covers all of it.</p>"),
        ("Is the quote really free and fixed?",
         "<p>Yes. Every lawn mowing quote Moreton Bay and Somerset clients receive from us is free, with no obligation to go ahead. Once we agree a price for a job or a schedule, that is the price you pay unless you change the scope.</p>"),
        ("Can I just call instead of using the form?",
         f"<p>Of course. Call or text {SITE['phone']} between 7am and 4pm, Monday to Saturday. If we are on the mower we will call you back at the next stop.</p>"),
        ("Do you service my suburb?",
         "<p>We cover the Moreton Bay Region (Wamuran, Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Strathpine, Redcliffe, Elimbah, D'Aguilar, Woodford, Bracalba) and the Somerset Region (Kilcoy, Esk, Toogoolawah, Lowood, Fernvale). If you are close to any of those, send the address and we will confirm.</p>"),
    ]
    body = f'''
<section class="hero hero--compact">
  <div class="hero__bg">{picture("hero-contact-wamuran", "Neatly mown lawn and driveway edge at a Moreton Bay home ready for a lawn mowing quote", sizes="100vw", loading="eager", fetchpriority="high")}</div>
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container">
    <div class="hero__grid">
      <div>
        {breadcrumbs([("Home", "/"), ("Contact", None)])}
        <span class="eyebrow">Free, fixed-price quotes</span>
        <h1>Get a Free Lawn Mowing Quote in Moreton Bay</h1>
        <span class="gold-rule" aria-hidden="true"></span>
        <p class="lead">Request a free lawn mowing quote Moreton Bay and Somerset wide, or a price for hedge trimming, a garden cleanup, weed control or mulching. Send the form or call {SITE['phone']}; Green Estates Gardening replies within one business day with a fixed price and the earliest date we can start.</p>
        <ul class="contact-list" style="margin-top:28px">
          <li><span class="icon-tile">{icon("phone")}</span><div><strong>Call or text</strong><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div></li>
          <li><span class="icon-tile">{icon("mail")}</span><div><strong>Email</strong><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></li>
          <li><span class="icon-tile">{icon("pin")}</span><div><strong>Based in</strong><a href="https://www.google.com/maps/search/?api=1&query=Wamuran+QLD+4512" rel="noopener" target="_blank">Wamuran QLD 4512, servicing Moreton Bay &amp; Somerset</a></div></li>
          <li><span class="icon-tile">{icon("clock")}</span><div><strong>Hours</strong><span style="font-weight:600">{SITE['hours']} · Closed Sunday</span></div></li>
        </ul>
      </div>
      {quote_form("quote", title="Request your free quote", intro="Fill in what you can. The more we know about the property, the faster we can give you a firm price.", source="/contact/")}
    </div>
  </div>
</section>

<section class="section section--light" aria-labelledby="expect-h">
  <div class="container">
    <div class="split">
      <div class="prose" data-reveal>
        <span class="eyebrow">What happens next</span>
        <h2 id="expect-h">How a lawn mowing quote works with Green Estates</h2>
        <p class="speakable"><strong>To get a lawn mowing quote in Moreton Bay from Green Estates Gardening, send the property address, approximate block size and the services you need through the form or by phone. A fixed price is returned within one business day, and regular schedules can start the following week.</strong></p>
        <p>For a standard residential lawn in Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Strathpine or Redcliffe we can usually price from the address and a satellite view, so the quote comes back the same day. For acreage in Wamuran, D'Aguilar, Woodford, Elimbah or the Somerset towns, and for bigger cleanups, we may swing past first. It takes ten minutes and means the number we give you is the number you pay.</p>
        <p>Once you say yes, we lock in a start date and, if it is a regular job, a schedule: weekly or fortnightly through the growing season, stretching out through winter. You will get a message when each visit is done. Payment is by bank transfer or card, and there is no contract to sign; stay because the work is good.</p>
        <h3>Tips for a faster, more accurate quote</h3>
        {check_list(["Include the full address so we can see the block on the map", "Mention gates, dogs, slopes and access for a ride-on or trailer", "Attach or describe the current state: neat, overgrown or somewhere between", "Tell us how often you would like us and whether hedges, weeds or mulch are on the list"])}
      </div>
      <div>
        <div class="map-embed" data-reveal>
          <iframe title="Map of Wamuran QLD 4512, home base of Green Estates Gardening" src="https://www.google.com/maps?q=Wamuran+QLD+4512&z=10&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
        <div class="card" style="margin-top:20px" data-reveal>
          <h3 style="margin-top:0">Opening hours</h3>
          <dl class="hours">
            <dt>Monday – Saturday</dt><dd>7:00am – 4:00pm</dd>
            <dt>Sunday</dt><dd>Closed</dd>
          </dl>
          <p style="margin-top:14px;font-size:.95rem">Quotes and enquiries are answered during these hours. Leave a message outside them and we will call back first thing.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{suburbs_section("Lawn mowing quotes across Moreton Bay &amp; Somerset", "We quote and work in all of these suburbs every week. Regular rounds mean short travel times and sharper prices.", service_word="lawn mowing and garden maintenance")}

<section class="section section--light" aria-labelledby="svc-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What can we quote?</span><h2 id="svc-h">Lawn mowing quote Moreton Bay wide, and every other service</h2></div>
    <div class="grid grid--services" data-reveal-stagger>{service_cards(sizes="(min-width: 1024px) 25vw, 100vw")}</div>
  </div>
</section>

{faq_section(faqs, heading="Getting a quote: common questions", theme="white")}
'''
    page = dict(
        path="/contact/",
        title="Free Lawn Mowing Quote Moreton Bay | Contact Green Estates",
        description="Get a free lawn mowing quote Moreton Bay & Somerset wide. Call 0439 550 850 or send the form; Green Estates Gardening replies within one business day.",
        keyword="Lawn Mowing Quote Moreton Bay",
        hero_img="hero-contact-wamuran",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Contact", "/contact/")],
    )
    return page, body

# =====================================================================
def thank_you():
    body = f'''
<section class="hero hero--compact" style="min-height:0;padding-bottom:48px">
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container"><span class="eyebrow">Request received</span><h1>Thanks, we've got your quote request</h1><span class="gold-rule" aria-hidden="true"></span>
  <p class="lead">One of us will look at the property details and come back to you within one business day (Mon–Sat) with a fixed price.</p></div>
</section>
<section class="section section--light ty">
  <div class="container container--narrow">
    <div class="tick">{icon("check")}</div>
    <h2>What happens next</h2>
    <div class="steps" style="grid-template-columns:1fr">
      <div class="step"><h3>We review the job</h3><p>Address, block size and what you asked for. For acreage or a big cleanup we may drive past first.</p></div>
      <div class="step"><h3>You get a fixed price</h3><p>By phone, text or email, usually within one business day.</p></div>
      <div class="step"><h3>We lock in a date</h3><p>Say yes and we schedule the first visit, then a regular round if you want one.</p></div>
    </div>
    <p style="margin-top:32px">Need it sooner? Call <a href="tel:{SITE['phone_tel']}"><strong>{SITE['phone']}</strong></a> between 7am and 4pm, Monday to Saturday.</p>
    <div class="btn-row" style="margin-top:20px"><a href="/" class="btn btn--primary">Back to the homepage {icon("arrow")}</a><a href="/#services" class="btn btn--secondary">Browse our services</a></div>
  </div>
</section>
'''
    page = dict(
        path="/thank-you/",
        title="Thanks, request received | Green Estates Gardening",
        description="Your quote request has been received. Green Estates Gardening will reply within one business day with a fixed price.",
        keyword=None, noindex=True, hero_img="hero-lawn-mowing-moreton-bay", speakable=False,
    )
    return page, body

def not_found():
    body = f'''
<section class="hero hero--compact" style="min-height:0;padding-bottom:48px">
  <div class="hero__glow" aria-hidden="true"></div>
  <div class="container"><span class="eyebrow">Error 404</span><h1>That page has been mowed over</h1><span class="gold-rule" aria-hidden="true"></span>
  <p class="lead">The address you followed does not exist on this site. Try one of the links below or call us.</p></div>
</section>
<section class="section section--light ty">
  <div class="container container--narrow">
    <div class="btn-row"><a href="/" class="btn btn--primary">Homepage {icon("arrow")}</a><a href="/#services" class="btn btn--secondary">Our services</a><a href="/contact/" class="btn btn--secondary">Contact</a></div>
  </div>
</section>
'''
    page = dict(path="/404.html", title="Page not found | Green Estates Gardening", description="Page not found.", keyword=None, noindex=True, hero_img="hero-lawn-mowing-moreton-bay", speakable=False)
    return page, body
