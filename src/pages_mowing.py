# -*- coding: utf-8 -*-
"""Mowing pages split by intent (review v2, section 1) plus the light garden maintenance parent (section 2).

/lawn-mowing-moreton-bay/     residential push-mowing rounds, corridor and peninsula suburbs
/acreage-mowing-moreton-bay/  ride-on and acreage mowing, Wamuran, the range and Somerset
/garden-maintenance-moreton-bay/  recurring garden care, parent for the North Lakes and Redcliffe garden pages
Each mowing page links to the other exactly once, in context. No paragraph is shared between them."""
from gesite import *
from pages_services import service_hero


# =====================================================================
def lawn_mowing():
    s = SERVICE_BY_SLUG["lawn-mowing-moreton-bay"]
    faqs = [
        ("How much does lawn mowing cost in Moreton Bay?",
         "<p>A standard 500 to 800 square metre residential lawn on a fortnightly schedule is our most economical service per visit, and the price covers mowing, edging, line trimming and blow-down, not just the cut. Bigger yards, long grass, steep driveways and awkward access cost more. Every lawn is quoted as a fixed price before we start, usually from the address and a satellite view the same day.</p>"),
        ("How often should a residential lawn be mowed in South-East Queensland?",
         "<p>Fortnightly from September to April and monthly from May to August suits most lawns across Caboolture, Morayfield, North Lakes and Redcliffe. Couch and kikuyu on heavy soil may need weekly cuts in January and February after storms; soft-leaf buffalo in the newer estates is usually fine at fortnightly all summer. We set the schedule with you and adjust it as the season turns.</p>"),
        ("Do I need to be home when you mow?",
         "<p>No. Most of our residential clients are at work when we visit. As long as the gate is unlocked or we have the code, we mow, edge, blow down and message you a photo when it is done. Payment is by bank transfer or card, so there is nothing to organise on the day.</p>"),
        ("What happens to the clippings on a residential lawn?",
         "<p>We catch and remove them. Paths, pool surrounds and entertaining areas stay clean, and buffalo lawns in particular look better and stay healthier without a layer of clippings sitting on top. If you would rather we mulch-mow to feed the lawn through a dry spell, just say so.</p>"),
        ("Do you mow rentals, townhouses and body corporate lawns?",
         "<p>Yes. Property managers across Caboolture, Morayfield, Burpengary and Narangba use us for routine mowing, end-of-lease presentation and photos for the file. Townhouse complexes and business frontages in North Lakes, Strathpine and Redcliffe sit on scheduled rounds with one invoice a month.</p>"),
        ("My block is more than 2,500 square metres. Is that still lawn mowing?",
         "<p>That is acreage mowing, which we also do, on a zero-turn ride-on with the house yard finished by push mower. The pricing and schedule work differently, so it has its own page and its own quote form.</p>"),
    ]
    body = service_hero(
        s, "Lawn Mowing Moreton Bay: Reliable Residential Rounds from Caboolture to Redcliffe", "Push mowing · edging · weekly, fortnightly or monthly",
        f"Looking for lawn mowing Moreton Bay homeowners, landlords and body corporates can set their calendar by? Green Estates Gardening runs fortnightly and monthly push-mowing rounds through Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Strathpine, Redcliffe, Bribie Island and Beachmere. Every visit includes edging, line trimming and a blow-down, at a fixed price per cut.",
        "Push Mowing", "hero-lawn-mowing-moreton-bay", "Lawn mowing Moreton Bay: freshly mown striped residential lawn in front of a Queensland home", "Lawn Mowing")
    body += f'''
<section class="section section--light" aria-labelledby="intro-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">Residential rounds</span>
        <h2 id="intro-h">Lawn mowing that leaves a Moreton Bay street frontage finished, not just cut</h2>
        <p class="speakable"><strong>Green Estates Gardening provides residential lawn mowing across the Moreton Bay Region from a base in Wamuran. Weekly, fortnightly and monthly rounds cover homes, rentals, townhouses and business frontages from Caboolture to Redcliffe, with mowing, edging, line trimming and blow-down included at a fixed price per visit.</strong></p>
        <p>A suburban lawn is a detail job. The estates at North Lakes, North Harbour and Central Lakes are soft-leaf buffalo on narrow blocks with side gates, pool fences and a clothesline to work around; the older quarter-acre streets of Caboolture, Strathpine and Redcliffe are couch and kikuyu on heavier ground that bolts after rain. Each wants a different cutting height, a sharp blade and a catcher, and both show every missed edge from the footpath.</p>
        <p>So the push mower, the edger and the line trimmer come to every residential job, and the visit is not over until the driveway, paths and kerb are edged, the fence lines and bed edges are trimmed, and the hard surfaces are blown down. It is the difference between a lawn that has been mowed and a frontage that looks looked after.</p>
        {check_list(["Mowing at the right height for buffalo, couch or kikuyu and the season", "Edging along every path, driveway and kerb", "Line trimming around fences, beds, sheds and the clothesline", "Clippings caught and removed, hard surfaces blown down"])}
        <p>Blocks above about 2,500 square metres, lifestyle properties and hobby farms are a different job on different machines: see our <a href="/acreage-mowing-moreton-bay/">acreage and ride-on mowing</a> page.</p>
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("push-mower-front-lawn-north-lakes", "Push mower and freshly cut front lawn at a North Lakes home, lawn mowing by Green Estates Gardening", sizes="(min-width: 900px) 45vw, 100vw")}
        <div class="img-badge"><div><strong>Fixed price</strong><br><span>per visit, quoted first</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="incl-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What's included</span><h2 id="incl-h">Every lawn mowing visit in Moreton Bay, start to finish</h2></div>
    <div class="grid grid--3" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("lawn")}</span><h3>Mow &amp; catch</h3><p>Sharp blades, the right deck height for your grass, overlapping passes for an even finish and the clippings caught so the lawn and the paths stay clean.</p></div>
      <div class="card"><span class="icon-tile">{icon("shears")}</span><h3>Edge &amp; trim</h3><p>Crisp edges along the driveway, footpath, kerb and garden beds, then line trimming around fences, posts, sheds and anything the mower cannot reach.</p></div>
      <div class="card"><span class="icon-tile">{icon("calendar")}</span><h3>Blow down &amp; schedule</h3><p>Paths, patio and driveway blown clear before we leave, a photo sent, and the next visit already locked in: weekly, fortnightly or monthly, adjusted with the season.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="who-h">
  <div class="container">
    <div class="split split--rev">
      <div data-reveal>
        <span class="eyebrow">Who we mow for</span>
        <h2 id="who-h">Homes, rentals, townhouses and frontages across the Moreton Bay corridor and coast</h2>
        <div class="grid grid--2" style="margin-top:28px">
          <div class="feature"><span class="icon-tile">{icon("users")}</span><div><h3>Busy households</h3><p>Fortnightly rounds through summer and monthly through winter so the weekend is yours. Caboolture, Morayfield, Burpengary and Narangba are on the round most days.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("tag")}</span><div><h3>Property managers</h3><p>Routine mowing on rentals, end-of-lease presentation and a dated photo for the file after every visit. One invoice across the whole rent roll.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("shield")}</span><div><h3>Body corporates &amp; business frontages</h3><p>Townhouse common areas in North Lakes and Strathpine and shopfront strips in Redcliffe kept presentable on a scheduled round.</p></div></div>
          <div class="feature"><span class="icon-tile">{icon("sun")}</span><div><h3>Retirees &amp; coastal homes</h3><p>Sandy, salt-exposed lawns on Bribie Island, Beachmere and the Redcliffe peninsula cut a little higher and kept thick, with the edges and nature strip done too.</p></div></div>
        </div>
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("walkway-mowing-edging", "Mown lawn and edged walkway at a Moreton Bay residential property", sizes="(min-width: 900px) 45vw, 100vw")}
      </div>
    </div>
  </div>
</section>

<section class="section section--light" aria-labelledby="gal-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Recent residential jobs</span><h2 id="gal-h">Recent lawn mowing in Moreton Bay suburbs</h2><p class="lead">Each tile opens the local page for that suburb.</p></div>
    {gallery([
        ("push-mower-striped-lawn-morayfield", "Push mowing leaving neat stripes on a residential lawn in Morayfield", True, SUBURB_LINKS.get("Morayfield"), "Morayfield"),
        ("freshly-mown-lawn-redcliffe", "Freshly mown and edged nature strip in Redcliffe", False, SUBURB_LINKS.get("Redcliffe"), "Redcliffe"),
        ("push-mower-front-lawn-north-lakes", "Push mower on a front lawn in North Lakes", False, SUBURB_LINKS.get("North Lakes"), "North Lakes"),
        ("push-mowing-residential-lawn", "Residential lawn mowing in Caboolture", False, SUBURB_LINKS.get("Caboolture"), "Caboolture"),
        ("footpath-edging-strathpine", "Crisp footpath edging after lawn mowing in Strathpine", False, SUBURB_LINKS.get("Strathpine"), "Strathpine"),
        ("commercial-lawn-mowing-units", "Mown lawn and tidy frontage at a unit complex in Burpengary", True, SUBURB_LINKS.get("Burpengary"), "Burpengary"),
    ])}
  </div>
</section>

<section class="section section--white" id="areas" aria-labelledby="areas-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Suburbs on the residential round</span><h2 id="areas-h">Lawn mowing suburbs from the northern corridor to the coast</h2><p class="lead">Local pages for the suburbs we mow most, with the detail that matters for your block: soil, grass type, estate covenants and how the round runs.</p></div>
    {suburb_link_block(RESIDENTIAL_SUBURBS)}
    <p class="muted" style="margin-top:24px;max-width:70ch" data-reveal>Not listed? We run residential mowing throughout the Moreton Bay Region. <a href="/service-areas/">See all service areas</a> or <a href="/contact/">ask about your suburb</a>.</p>
  </div>
</section>

{faq_section(faqs, heading="Lawn mowing Moreton Bay: your questions answered", theme="light")}
{related_services(s["slug"], theme="white")}
{cta_band("Get a fixed price for your lawn", "Send the address and we will usually have a price back the same day. No contract, no obligation.")}
'''
    page = dict(
        path=f"/{s['slug']}/",
        title="Lawn Mowing Moreton Bay | Green Estates Gardening",
        description="Lawn mowing Moreton Bay homes, rentals and body corporates book fortnightly: push mowing, edging and blow-down from Caboolture to Redcliffe. Fixed price.",
        keyword="Lawn Mowing Moreton Bay",
        hero_img="hero-lawn-mowing-moreton-bay",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Lawn Mowing", f"/{s['slug']}/")],
        service=dict(name="Lawn Mowing", type="Lawn mowing", items=["Residential lawn mowing", "Lawn edging and line trimming", "Fortnightly and monthly mowing rounds", "Rental and body corporate mowing"]),
    )
    return page, body


# =====================================================================
def acreage_mowing():
    s = SERVICE_BY_SLUG["acreage-mowing-moreton-bay"]
    faqs = [
        ("What counts as acreage mowing, and how do you price it?",
         "<p>Anything from around 2,500 square metres up to multi-acre lifestyle blocks and hobby farms. We price acreage mowing Moreton Bay wide by the area actually being cut, the terrain (slopes, dams, trees to work around) and how often we visit, then give you a fixed price per cut. A well-kept two-acre block in Wamuran on a fortnightly schedule costs less per visit than a once-a-season knockdown of the same block.</p>"),
        ("Ride-on or push mowing: which does my block need?",
         "<p>As a rule of thumb, blocks under about 800 square metres with garden beds, paths and a pool fence are quicker and neater with a push mower. Open blocks above that, and anything described as acreage, are ride-on territory. Most acreage properties get both: the zero-turn does the open ground and we finish the tight spots around the house, sheds and trees with a push mower and line trimmer.</p>"),
        ("How often should acreage be mowed in Moreton Bay and Somerset?",
         "<p>Through the growing season (roughly October to March) every two to three weeks keeps kikuyu and couch paddocks under control and stops seed heads and snakes finding cover. From May to August most blocks in the Somerset region only need a cut every five to six weeks. We set the schedule with you and adjust it after a wet spell.</p>"),
        ("Do you mow steep or rough ground?",
         "<p>Yes, within reason. Zero-turn mowers handle gentle to moderate slopes, dam banks and uneven paddocks well. Very steep embankments, boggy ground after heavy rain or areas with hidden stumps and rubbish may need a line trimmer or a first pass at a higher deck height. Tell us in the job notes and we will price it correctly the first time.</p>"),
        ("What happens to the clippings on acreage?",
         "<p>We usually mulch-mow, which returns the clippings to the paddock as fine mulch and is better for the grass. Around the house, pool and entertaining areas we catch and remove them so the hard surfaces stay clean. If you prefer one method over the other, just say so.</p>"),
    ]
    body = service_hero(
        s, "Acreage &amp; Ride-On Mowing Across Moreton Bay &amp; Somerset", "Zero-turn · lifestyle blocks · hobby farms",
        f"Looking for acreage mowing Moreton Bay property owners can set their calendar by? Green Estates Gardening runs commercial zero-turn ride-on mowers across lifestyle blocks, hobby farms and large yards from Wamuran and D'Aguilar out to Kilcoy, and still brings the push mower and edger for the tight spots around the house. Fixed price per cut, on a schedule that suits your grass.",
        "Ride-On / Acreage Mowing", "hero-acreage-mowing-somerset", "Acreage mowing Moreton Bay: freshly mown rural block with a dam and gum trees in the Somerset region", "Acreage & Ride-On Mowing")
    body += f'''
<section class="section section--light" aria-labelledby="intro-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">Acreage specialists</span>
        <h2 id="intro-h">Acreage mowing built for Moreton Bay and Somerset blocks</h2>
        <p class="speakable"><strong>Green Estates Gardening provides acreage and ride-on mowing across the Moreton Bay and Somerset regions from a base in Wamuran. Commercial zero-turn mowers handle lifestyle blocks, hobby farms and large yards, with push mowing and edging for the areas around the house, all at a fixed price per visit.</strong></p>
        <p>Large blocks around Wamuran, Bracalba, D'Aguilar, Woodford and Elimbah grow differently from a suburban lawn in North Lakes. Kikuyu and couch paddocks bolt after summer rain, seed heads come up in a week, and a domestic ride-on that cannot keep up becomes an expensive shed ornament. Our zero-turns cut wide and fast, leave an even finish on uneven ground and get around dams, fence lines and tree drip lines without scalping.</p>
        <p>Out past the range in Kilcoy, Esk, Toogoolawah, Lowood and Fernvale we mow lifestyle blocks, house paddocks and rural driveways on a regular round, so you are not paying a travel premium every time. Closer in, the same ride-on service covers the larger yards on the acreage fringe of Caboolture, Morayfield and Burpengary where a push mower simply takes too long.</p>
        {check_list(["Lifestyle blocks, hobby farms and house paddocks from 2,500 m² to 20+ acres", "Zero-turn ride-on mowing with an even, striped finish", "Push mowing, edging and line trimming around buildings, beds and fences", "Mulch-mowing or catch-and-remove, your choice"])}
        <p>Standard suburban block under 2,500 square metres? That is a different round on different machines: see our <a href="/lawn-mowing-moreton-bay/">residential lawn mowing</a> page.</p>
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("ride-on-mowing-acreage-moreton-bay", "Green Estates Gardening operator ride-on mowing an acreage block in Moreton Bay", sizes="(min-width: 900px) 45vw, 100vw")}
        <div class="img-badge"><div><strong>2,500 m²+</strong><br><span>ride-on territory</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="incl-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What's included</span><h2 id="incl-h">Every acreage mowing Moreton Bay visit, done properly</h2></div>
    <div class="grid grid--3" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("mower")}</span><h3>Open ground on the zero-turn</h3><p>Paddocks, house yards and driveways cut with a commercial zero-turn at the right deck height for your grass and the season. Dam banks, fence lines and tree surrounds included.</p></div>
      <div class="card"><span class="icon-tile">{icon("shears")}</span><h3>House yard finished by hand</h3><p>Push mower and line trimmer around the house, sheds, tanks, garden beds and the pool fence, so the part you look at every day is as neat as a suburban lawn.</p></div>
      <div class="card"><span class="icon-tile">{icon("calendar")}</span><h3>Schedules that hold</h3><p>Fortnightly, three-weekly or monthly, adjusted with the season. Same operator, same fixed price per visit, and a message when the job is done so you know the property has been looked after.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="vs-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Ride-on vs push mowing</span><h2 id="vs-h">Which mower does your Moreton Bay block need?</h2></div>
    <div class="grid grid--2" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("mower")}</span><h3>Ride-on and zero-turn</h3><p>Best for open blocks above roughly 800 square metres and anything called acreage. Faster, more even on uneven ground, and it mulch-mows so the paddock feeds itself. Standard on our rounds through Wamuran, D'Aguilar, Elimbah, Bracalba and the Somerset towns.</p></div>
      <div class="card"><span class="icon-tile">{icon("lawn")}</span><h3>Push mowing</h3><p>Best for standard suburban blocks with beds, paths, a pool fence and a clothesline to work around. Neater in tight spaces, gentler on soft buffalo lawns, and it catches clippings so entertaining areas stay clean. On acreage it does the house yard after the zero-turn has done the paddock.</p></div>
    </div>
    <p class="lead" style="margin-top:32px;max-width:70ch" data-reveal>Most acreage properties we look after get both on the same visit. You do not have to decide; describe the block in the quote form and we will bring the right gear.</p>
  </div>
</section>

<section class="section section--light" aria-labelledby="gal-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Recent acreage jobs</span><h2 id="gal-h">Recent acreage mowing in Moreton Bay and Somerset</h2><p class="lead">Each tile opens the local page for that area.</p></div>
    {gallery([
        ("ride-on-mower-acreage-wamuran", "Zero-turn ride-on mowing under gum trees on a Wamuran acreage block", True, SUBURB_LINKS.get("Wamuran"), "Wamuran"),
        ("acreage-dam-mowing-somerset", "Acreage mowing around a farm dam near Kilcoy in the Somerset region", False, SUBURB_LINKS.get("Kilcoy"), "Kilcoy"),
        ("zero-turn-mower-caboolture", "Commercial zero-turn mower on a large lawn on the Caboolture acreage fringe", False, SUBURB_LINKS.get("Caboolture"), "Caboolture"),
        ("acreage-mowing-shed", "Mown rural property with shed and garden beds in D'Aguilar", False, SUBURB_LINKS.get("D'Aguilar"), "D'Aguilar"),
        ("hero-acreage-mowing-somerset", "Freshly mown lifestyle block with a dam in the Somerset region", True),
    ])}
  </div>
</section>

<section class="section section--white" id="areas" aria-labelledby="areas-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">Acreage belt and Somerset</span><h2 id="areas-h">Acreage mowing from Wamuran over the range to the Somerset towns</h2><p class="lead">Ride-on rounds run through the range foothills and the Somerset valleys. Local pages where we have them; the rest are covered on the same round.</p></div>
    {suburb_link_block(ACREAGE_SUBURBS, kind_label="Acreage mowing")}
    <p class="muted" style="margin-top:24px;max-width:70ch" data-reveal>Plus Moodlu, Campbells Pocket, Mount Mee, Somerset Dam, Hazeldean and Villeneuve. <a href="/service-areas/">See all service areas</a> or <a href="/contact/">send the address</a> and we will confirm.</p>
  </div>
</section>

{faq_section(faqs, heading="Acreage mowing Moreton Bay: your questions answered", theme="light")}
{related_services(s["slug"], theme="white")}
{cta_band("Get a fixed price for your block", "Tell us the address and rough size. Acreage quotes may include a quick drive-by so the price is right the first time.")}
'''
    page = dict(
        path=f"/{s['slug']}/",
        title="Acreage Mowing Moreton Bay & Somerset | Green Estates",
        description="Acreage mowing Moreton Bay & Somerset: zero-turn ride-on mowing for lifestyle blocks, hobby farms and big yards from Wamuran to Kilcoy. Fixed price per cut.",
        keyword="Acreage Mowing Moreton Bay",
        hero_img="hero-acreage-mowing-somerset",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Acreage & Ride-On Mowing", f"/{s['slug']}/")],
        service=dict(name="Acreage & Ride-On Mowing", type="Acreage mowing", items=["Acreage mowing", "Zero-turn ride-on mowing", "Lifestyle block and hobby farm mowing", "House yard mowing and edging"]),
    )
    return page, body


# =====================================================================
def garden_maintenance():
    s = SERVICE_BY_SLUG["garden-maintenance-moreton-bay"]
    faqs = [
        ("What does regular garden maintenance include?",
         "<p>Whatever the garden needs to stay tidy between visits: weeding and edging the beds, light pruning and dead-heading, keeping hedges and screens in shape, clearing leaf litter and palm fronds, and a blow-down of paths and the patio. It is scoped per property, bundled with the lawn mowing visit and quoted as one fixed price per round.</p>"),
        ("How often do you visit for garden maintenance in Moreton Bay?",
         "<p>Most gardens tick along on a monthly garden round alongside fortnightly mowing through summer, dropping to six-weekly in winter. Formal gardens, body corporate common areas and properties on the market usually want fortnightly. We set the frequency with you and adjust it with the season.</p>"),
        ("Is garden maintenance cheaper if you already mow the lawn?",
         "<p>Yes. The garden work is added to a visit we are already making, so there is no second call-out and no second travel charge. One crew, one visit, one invoice, and the price per round is lower than booking a separate gardener.</p>"),
        ("Which suburbs do you run garden maintenance rounds in?",
         "<p>Across the Moreton Bay Region, with dedicated local pages for <a href='/service-areas/garden-maintenance-north-lakes/'>North Lakes</a> and <a href='/service-areas/garden-maintenance-redcliffe/'>Redcliffe</a>, where most of our regular garden clients are. Caboolture, Morayfield, Burpengary, Narangba and Strathpine are on the same rounds. Send the address and we will confirm the day.</p>"),
    ]
    body = service_hero(
        s, "Garden Maintenance Moreton Bay: Regular Garden Care Bundled With Your Mowing", "Beds · hedges · pruning · tidy between visits",
        "Green Estates Gardening provides garden maintenance Moreton Bay homeowners, landlords and body corporates add to their regular mowing round: beds weeded and edged, hedges kept in shape, shrubs pruned and everything blown down, on a schedule, at one fixed price per visit.",
        "Regular Maintenance Package", "garden-maintenance-commercial-strip", "Garden maintenance Moreton Bay: mown lawn and tidy garden beds along a commercial frontage", "Garden Maintenance")
    body += f'''
<section class="section section--light" aria-labelledby="intro-h">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <span class="eyebrow">One crew, one visit</span>
        <h2 id="intro-h">Garden maintenance that keeps a Moreton Bay property tidy between cuts</h2>
        <p class="speakable"><strong>Green Estates Gardening offers recurring garden maintenance across the Moreton Bay Region, bundled with its lawn mowing rounds. A garden round covers bed weeding and edging, hedge and shrub upkeep, light pruning, leaf and debris clearing and a blow-down, quoted as one fixed price per visit.</strong></p>
        <p>We are a mowing-led business, and that is exactly why the garden work makes sense: we are already at the property every fortnight. Adding the beds, the hedges and the paths to the same visit keeps a garden looking cared for without a second contractor, a second call-out or a second invoice, and it stops small jobs becoming the kind of overgrown reset that needs a <a href="/garden-cleanup-moreton-bay/">full garden cleanup</a>.</p>
        <p>The round is scoped to the property. A North Lakes townhouse frontage might need its lilly pilly screen tipped and the bed edges re-cut once a month; a Redcliffe home with established gardens needs the frangipani and bougainvillea kept off the paths, palm fronds cleared after a blow and the beds weeded before they seed. We write it down, price it, and do the same thing every visit.</p>
        {check_list(["Garden beds weeded, edged and kept free of leaf litter", "Hedges and screens tipped between the main seasonal cuts", "Shrubs, roses and ornamentals pruned and dead-headed", "Paths, patio and driveway blown down before we leave"])}
      </div>
      <div class="img-frame img-frame--tall" data-reveal>
        {picture("garden-beds-trees-tidy", "Tidy garden beds and pruned shrubs beside a Moreton Bay home on a regular garden maintenance round", sizes="(min-width: 900px) 45vw, 100vw")}
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="incl-h">
  <div class="container">
    <div class="section-head" data-reveal><span class="eyebrow">What's included</span><h2 id="incl-h">Garden maintenance Moreton Bay: what a round covers</h2><p class="lead">Pick the parts your garden needs. Each is added to the mowing visit and priced as a single fixed figure per round.</p></div>
    <div class="grid grid--3" data-reveal-stagger>
      <div class="card"><span class="icon-tile">{icon("leaf")}</span><h3>Beds &amp; borders</h3><p>Hand weeding, edge re-cutting, leaf litter cleared and mulch raked level, so the beds frame the lawn instead of competing with it.</p></div>
      <div class="card"><span class="icon-tile">{icon("shears")}</span><h3>Hedges &amp; shrubs</h3><p>Screens and formal hedges tipped between the main <a href="/hedge-trimming-moreton-bay/">seasonal hedge trims</a>, shrubs shaped, roses and ornamentals dead-headed.</p></div>
      <div class="card"><span class="icon-tile">{icon("sun")}</span><h3>Seasonal jobs</h3><p>A spring <a href="/mulching-services-moreton-bay/">mulch top-up</a>, weed treatment before summer, palm fronds and storm debris cleared, and gutters checked for leaf build-up on request.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark" id="areas" aria-labelledby="areas-h">
  <div class="container">
    <div class="split split--rev">
      <div data-reveal>
        <span class="eyebrow">Where the garden rounds run</span>
        <h2 id="areas-h">Garden maintenance in North Lakes, Redcliffe and across the corridor</h2>
        <p class="lead">Two suburbs have their own garden maintenance pages because that is where most of our regular garden clients are. The rest of the Moreton Bay corridor is covered on the same rounds.</p>
        <div class="suburb-grid" data-reveal-stagger>
          <a class="suburb-card" href="/service-areas/garden-maintenance-north-lakes/"><span class="icon-tile">{icon("pin")}</span><span><strong>North Lakes</strong><em>Garden maintenance</em></span>{icon("arrow")}</a>
          <a class="suburb-card" href="/service-areas/garden-maintenance-redcliffe/"><span class="icon-tile">{icon("pin")}</span><span><strong>Redcliffe</strong><em>Garden maintenance</em></span>{icon("arrow")}</a>
          <a class="suburb-card" href="/service-areas/"><span class="icon-tile">{icon("grid")}</span><span><strong>All service areas</strong><em>Moreton Bay &amp; Somerset</em></span>{icon("arrow")}</a>
        </div>
        <p style="margin-top:20px">Also on the round: Caboolture, Morayfield, Burpengary, Narangba, Strathpine, Bribie Island and Beachmere, and acreage gardens around Wamuran and D'Aguilar.</p>
      </div>
      <div class="img-frame" data-reveal>
        {picture("hedge-trimming-townhouse-hedges", "Trimmed hedges and tidy beds at a Moreton Bay townhouse complex on a garden maintenance round", sizes="(min-width: 900px) 45vw, 100vw")}
      </div>
    </div>
  </div>
</section>

{faq_section(faqs, heading="Garden maintenance Moreton Bay: frequently asked questions", theme="light")}
{related_services(s["slug"], theme="white")}
{cta_band("Add the garden to your mowing round", "Tell us what the garden needs, or send a couple of photos, and we will quote the round as one fixed price.")}
'''
    page = dict(
        path=f"/{s['slug']}/",
        title="Garden Maintenance Moreton Bay | Green Estates Gardening",
        description="Garden maintenance Moreton Bay homes and body corporates bundle with mowing: beds weeded, hedges kept in shape, shrubs pruned. One visit, one fixed price.",
        keyword="Garden Maintenance Moreton Bay",
        hero_img="garden-maintenance-commercial-strip",
        faqs=faqs,
        crumbs=[("Home", "/"), ("Garden Maintenance", f"/{s['slug']}/")],
        service=dict(name="Garden Maintenance", type="Garden maintenance", items=["Garden bed weeding and edging", "Hedge and shrub upkeep", "Pruning and dead-heading", "Regular garden maintenance rounds"]),
    )
    return page, body
