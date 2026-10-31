# -*- coding: utf-8 -*-
"""New suburb pages under the /service-areas/ hub (strategy doc, section 05).
Deception Bay, Petrie and Kallangur are built but flagged: the doc says confirm the service
radius with Hamish before publishing. Flip CONFIRMED_RADIUS in suburbs.py to publish them."""

SUBURBS_B = [
dict(
    path="/service-areas/lawn-mowing-burpengary/", name="Burpengary", keyword="Lawn Mowing Burpengary", kind="lawn", region="mb", group="corridor",
    neighbours=["/service-areas/lawn-mowing-morayfield/", "/service-areas/lawn-mowing-narangba/"], image="commercial-lawn-mowing-units",
    alt="Lawn mowing Burpengary: mown lawn and tidy frontage at a modern property",
    h1="Lawn Mowing Burpengary: North Harbour Estates to Acreage in Burpengary West", h1_plain="Lawn Mowing Burpengary: North Harbour Estates to Acreage in Burpengary West",
    title="Lawn Mowing Burpengary | Green Estates Gardening",
    description="Lawn mowing Burpengary and Burpengary East on fixed-price fortnightly rounds: North Harbour estates, older blocks near the station and acreage out west.",
    quick="Green Estates Gardening provides lawn mowing in Burpengary, Burpengary East and Burpengary West on fortnightly and monthly rounds at a fixed price per visit, from the buffalo lawns of North Harbour and the newer estates to the 800 square metre blocks near the station and the acreage along Buchanan Road and Uhlmann Road.",
    lead="Lawn mowing Burpengary needs sits in the gap between Caboolture and North Lakes, and so do we: Wamuran is fifteen minutes away and Burpengary is on our round most days of the week. From the tight, covenant-controlled lawns of North Harbour and Burpengary East to the older streets around the station and the acreage of Burpengary West, Green Estates Gardening mows it all at a fixed price per cut, edges and blow-down included.",
    body="""
<h2>Lawn mowing in Burpengary: three very different neighbourhoods</h2>
<p>Burpengary East and North Harbour are the newest part of the suburb: 350 to 600 square metre blocks, soft-leaf buffalo laid on underlay, narrow side gates and an estate standard that expects the front lawn edged and the footpath clean. That is push-mower work at a high deck height with the clippings caught. The established streets between Station Road and Old Bay Road are a generation older, with bigger blocks, mature trees, couch and kikuyu lawns and enough side access for a wider mower. And Burpengary West, out along Buchanan Road, Uhlmann Road and Morris Road, is acreage: quarter-acre to several hectares of kikuyu around a house yard, mowed with a zero-turn and finished with a push mower.</p>
<p>The soil across Burpengary is on the heavier side and the low ground near Burpengary Creek and Little Burpengary Creek stays wet for days after a storm. We sequence those blocks last after rain and the sandy, higher ground first, so nobody gets ruts across the lawn.</p>
<h2>Who we mow for in Burpengary</h2>
<ul>
<li><strong>Families in North Harbour and Burpengary East</strong> who want a fortnightly round that keeps the frontage covenant-ready without a Saturday morning on it.</li>
<li><strong>Property managers</strong> with rentals around the station, Station Road and the older estates, needing routine mowing, end-of-lease resets and photos.</li>
<li><strong>Acreage owners in Burpengary West</strong> who want a fixed price per cut on the paddock and the house yard finished properly on the same visit.</li>
<li><strong>Commercial frontages</strong> along Station Road and Morayfield Road on a scheduled round with one invoice.</li>
</ul>
<h2>What is included in a Burpengary mowing visit</h2>
<p>Mowing at the right height for buffalo, couch or kikuyu, edging along paths, driveway and kerb, line trimming around fences, beds and sheds, clippings caught on residential lawns and mulch-mown on acreage, and a blow-down of hard surfaces before we leave. Hedge trimming for the lilly pilly and murraya screens that line North Harbour, weed treatment, garden bed mulching and minor tree work can be bundled at a fixed price.</p>
<h2>Why Burpengary chooses Green Estates</h2>
<p>Burpengary is at the centre of our Morayfield, Narangba and North Lakes rounds, so we are close by most days and can shift a cut around the weather rather than skip it for a month. Fixed price before we start, the same crew every visit, no contract, and 5.0 on Google from 23 reviews.</p>
""",
    faqs=[
        ("How much does lawn mowing cost in Burpengary?", "<p>A standard North Harbour or Burpengary East block on a fortnightly round is our most economical service per visit. The larger blocks near the station cost a little more, and acreage in Burpengary West is quoted on the area actually cut. Every property is a fixed price quoted before we start, usually the same day from the address.</p>"),
        ("Do you mow acreage in Burpengary West?", "<p>Yes. Blocks along Buchanan Road, Uhlmann Road, Morris Road and the Burpengary West lifestyle belt are on our ride-on rounds. We bring a commercial zero-turn for the open ground and a push mower and line trimmer for the house yard, sheds and gardens, quoted as one fixed price per cut.</p>"),
        ("How often should a North Harbour lawn be mowed?", "<p>Fortnightly from September to April and monthly from May to August. The estate's soft-leaf buffalo lawns want a high cut at 50 to 60 millimetres and the clippings caught, which keeps them dense, weed-free and inside the covenant standard all summer.</p>"),
        ("Do you cover Burpengary East and Deception Bay Road?", "<p>Yes. Burpengary East, North Harbour and the streets off Deception Bay Road and Old Bay Road are all on our Burpengary round, along with Morayfield to the north and Narangba to the south. We are based in Wamuran and run the corridor as one loop.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-deception-bay/", name="Deception Bay", keyword="Lawn Mowing Deception Bay", kind="lawn", region="mb", group="coast", flagged=True,
    neighbours=["/service-areas/lawn-mowing-beachmere/", "/service-areas/lawn-mowing-redcliffe/"], image="freshly-mown-lawn-redcliffe",
    alt="Lawn mowing Deception Bay: freshly cut coastal lawn and nature strip",
    h1="Lawn Mowing Deception Bay: Bayside Blocks, Older Homes &amp; Rentals Done Right", h1_plain="Lawn Mowing Deception Bay: Bayside Blocks, Older Homes & Rentals Done Right",
    title="Lawn Mowing Deception Bay | Green Estates Gardening",
    description="Lawn mowing Deception Bay homes and rentals on fixed-price fortnightly rounds: bayside blocks, older 600 to 800 m² yards and units, edges included.",
    quick="Green Estates Gardening provides lawn mowing in Deception Bay on fortnightly and monthly rounds at a fixed price per visit, covering the older 600 to 800 square metre blocks around Bayview Terrace and Deception Bay Road, the newer streets towards Rothwell and Kinsellas Road, and unit complexes near the Esplanade.",
    lead="Lawn mowing Deception Bay properties need is a bayside job with a big-block twist. The suburb has some of the largest older residential yards on the coast, a lot of rentals, and a foreshore strip where the sea breeze burns soft grass. Green Estates Gardening runs Deception Bay with Beachmere and Redcliffe on a fixed-price coastal round, edges and blow-down included.",
    body="""
<h2>Lawn mowing in Deception Bay: big yards and bay breezes</h2>
<p>The older heart of Deception Bay, between Bayview Terrace, Deception Bay Road and the Esplanade, was subdivided generously. Blocks of 700 to 900 square metres with a house in the middle and lawn on three sides are normal, and on the flat, sandy ground near the water that lawn is usually couch or old kikuyu that grows quickly after rain and browns off in a dry October. A wide push mower or a small ride-on where the side gate allows, a higher cut in the exposed streets, and a catcher so the clippings do not end up in the neighbour's yard is how we do it.</p>
<p>The newer streets south towards Rothwell and west along Kinsellas Road and Moreton Downs are smaller blocks with soft-leaf buffalo, and around the shopping centre and the Esplanade there are unit complexes and duplexes with shared strips of lawn. Each goes on the same fortnightly round but is mowed for what it is.</p>
<h2>Rentals and property managers</h2>
<p>Deception Bay has a high proportion of rental homes and we do a lot of work for property managers here: routine mowing between inspections, end-of-lease resets when a yard has been let go, and pre-sale presentation for the increasing number of listings. Every visit ends with a photo for the file, and each property is quoted as a fixed price so the owner knows the cost in advance.</p>
<h2>What is included in a Deception Bay mowing visit</h2>
<p>Mowing at the correct height for the grass and the exposure, edging along footpaths, driveway and kerb, line trimming around fences, beds and the clothesline, clippings caught and removed, and a blow-down of hard surfaces. Hedge trimming for the coastal westringia, lilly pilly and bougainvillea that line the older streets, weed treatment, mulching and green waste removal can be added at a fixed price.</p>
<h2>Why Deception Bay chooses Green Estates</h2>
<p>We run Deception Bay, Beachmere and the Redcliffe peninsula as one coastal loop on a set day, which keeps the price sharp and the schedule dependable. Fixed price before we start, the same crew each visit, no contract, and reliability that shows in every one of our 23 five-star Google reviews.</p>
""",
    faqs=[
        ("How much does lawn mowing cost in Deception Bay?", "<p>The bigger older blocks around Bayview Terrace cost a little more per visit than a standard estate block, because there is more lawn and more edge. On a fortnightly schedule both are our most economical service; one-off end-of-lease cuts cost more because of the extra passes and green waste. Every property is a fixed price quoted before we start.</p>"),
        ("Do you mow rentals in Deception Bay?", "<p>Yes. Routine mowing between inspections, end-of-lease resets and pre-sale presentation for Deception Bay rentals and listings are a large part of our coastal round. We photograph every visit and quote each property as a fixed price so owners and managers know the cost in advance.</p>"),
        ("How often should a Deception Bay lawn be mowed?", "<p>Fortnightly from September to April and every three to five weeks in winter. Couch and kikuyu on the sandy flats near the Esplanade grow fast after rain but slow in dry spells, so we adjust the round to the grass rather than scalping a stressed lawn to keep to a calendar.</p>"),
        ("Which parts of Deception Bay do you cover?", "<p>All of it: the older streets between Bayview Terrace and the Esplanade, the newer estates towards Rothwell and along Kinsellas Road, Moreton Downs, and the unit complexes near the shopping centre. Deception Bay is run with Beachmere and Redcliffe as one coastal round from our base in Wamuran.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-wamuran/", name="Wamuran", keyword="Lawn Mowing Wamuran", kind="lawn", region="mb", group="acreage",
    neighbours=["/service-areas/lawn-mowing-daguilar/", "/service-areas/lawn-mowing-caboolture/"], image="ride-on-mower-acreage-wamuran",
    alt="Lawn mowing Wamuran: zero-turn ride-on mowing an acreage block under gum trees",
    h1="Lawn Mowing Wamuran: Acreage &amp; Ride-On Mowing From Your Local Crew", h1_plain="Lawn Mowing Wamuran: Acreage & Ride-On Mowing From Your Local Crew",
    title="Lawn Mowing Wamuran | Green Estates Gardening",
    description="Lawn mowing Wamuran acreage and lifestyle blocks by the crew that lives here. Zero-turn ride-on mowing, house yards and paddocks, fixed price per cut.",
    quick="Green Estates Gardening is based in Wamuran and provides lawn mowing on Wamuran's acreage, lifestyle blocks and rural residential properties, from the house yard to the paddock, with commercial zero-turn ride-ons for the open ground and push mowers for around the house. Fixed price per cut, no travel charge, on a fortnightly or three-weekly round in summer.",
    lead="Lawn mowing Wamuran owners book from us has one advantage nobody else can offer: we live here. Green Estates Gardening is based in Wamuran, so the pineapple and strawberry country along the D'Aguilar Highway, the lifestyle blocks off Campbells Pocket Road and Wamuran Basin, and the rural residential streets around the school are our home round. Acreage mowing, ride-on and push, fixed price per cut, and no travel premium.",
    body="""
<h2>Lawn mowing in Wamuran: acreage first</h2>
<p>Almost every property in Wamuran is acreage of some kind, from a 2,500 square metre rural residential block near the township to five, ten and twenty hectare farms and lifestyle blocks stretching up towards Wamuran Basin, Campbells Pocket and Bracalba. The grass is kikuyu, and after a wet week in January it grows faster than anything else in the region. Left a month it becomes a hay crop with seed heads at hip height and snakes underneath. Our commercial zero-turns cut it wide and fast at a height that keeps the paddock dense, and we mulch-mow so nothing has to be carted away.</p>
<p>Around the house it is a different job: the yard, the tank stand, the shed surrounds, the fence lines, the drip line under the mango and the driveway edges all get the push mower and line trimmer so the whole block is finished, not just the paddock. On the red volcanic soils of the pineapple country the ground holds together well after rain; on the lower creek flats towards Caboolture River it does not, and we sequence accordingly.</p>
<h2>Who we mow for in Wamuran</h2>
<ul>
<li><strong>Lifestyle block owners</strong> who bought for the space and would rather not spend every second Saturday on a ride-on.</li>
<li><strong>Working farms and semi-rural properties</strong> that need the house yard and the road frontage kept tidy between the real work.</li>
<li><strong>Retirees on rural residential blocks</strong> around the township who want the same reliable crew every time.</li>
<li><strong>Neighbours.</strong> A good share of our Wamuran clients are people we see at the shop.</li>
</ul>
<h2>What is included in a Wamuran mowing visit</h2>
<p>Zero-turn mowing of the open ground at the right height for the season, push mowing and line trimming around the house, sheds, tanks and fence lines, driveway edges, a blow-down of the entertaining area and the front path, and mulch-mowing so clippings feed the paddock. Slashing of overgrown areas, hedge trimming, garden bed mulching and minor tree work such as low limbs over the driveway are quoted alongside.</p>
<h2>Why Wamuran chooses the local crew</h2>
<p>Because we are already here. No travel premium, a cut slotted in the morning after rain when it suits the block rather than a schedule set in Brisbane, and a fixed price per visit agreed before we start. The same standard we take to Caboolture, North Lakes and Kilcoy started on the blocks around Wamuran more than 13 years ago.</p>
""",
    faqs=[
        ("How much does acreage mowing cost in Wamuran?", "<p>Acreage in Wamuran is priced on the area actually cut, the terrain and how often we visit, as one fixed price per cut. A fortnightly cut on a two-acre block costs less per visit than a once-a-season knockdown of the same block, because the grass never gets long. There is no travel charge; we are based in Wamuran.</p>"),
        ("How often should kikuyu acreage be mowed in Wamuran?", "<p>Every two to three weeks from October to March and every five to six weeks from May to August. After a wet week in summer Wamuran kikuyu can put on 20 centimetres, so a fixed schedule is the only way to keep a paddock walkable and the price per cut low.</p>"),
        ("Do you slash overgrown paddocks as well as mow?", "<p>Yes. Paddocks that have got away are knocked down first with a slasher or a heavy-duty zero-turn at full height, then brought back to a normal mowing height over two visits so the kikuyu recovers green rather than yellow. Then it goes onto a regular round.</p>"),
        ("Do you cover Wamuran Basin, Campbells Pocket and Bracalba?", "<p>Yes. Wamuran, Wamuran Basin, Campbells Pocket, Bracalba, Moodlu and the blocks along the D'Aguilar Highway towards D'Aguilar are our home round. If you are anywhere between Caboolture and Woodford, you are close to base.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-kilcoy/", name="Kilcoy", keyword="Lawn Mowing Kilcoy", kind="lawn", region="som", group="acreage",
    neighbours=["/service-areas/lawn-mowing-daguilar/", "/service-areas/lawn-mowing-wamuran/"], image="acreage-dam-mowing-somerset",
    alt="Lawn mowing Kilcoy: freshly mown acreage beside a farm dam in the Somerset region",
    h1="Lawn Mowing Kilcoy: Acreage, Town Blocks &amp; Somerset Dam Properties", h1_plain="Lawn Mowing Kilcoy: Acreage, Town Blocks & Somerset Dam Properties",
    title="Lawn Mowing Kilcoy | Green Estates Gardening",
    description="Lawn mowing Kilcoy and the Somerset region on a regular round: acreage, town blocks, Somerset Dam and Hazeldean properties, fixed price per cut.",
    quick="Green Estates Gardening provides lawn mowing in Kilcoy and the surrounding Somerset region on a regular round from Wamuran, covering town blocks in Kilcoy itself, lifestyle acreage along the D'Aguilar Highway and Kilcoy–Murgon Road, and properties around Somerset Dam, Hazeldean and Villeneuve. Ride-on and push mowing at a fixed price per cut.",
    lead="Lawn mowing Kilcoy property owners can rely on has been hard to find, because most operators stop at the range. We do not. Green Estates Gardening comes over the D'Aguilar Range from Wamuran on a regular Somerset round that takes in Kilcoy's town blocks, the lifestyle acreage along the highway, and the properties around Somerset Dam, Hazeldean and Villeneuve, including a 3.74 acre bed-and-breakfast we have looked after for years.",
    body="""
<h2>Lawn mowing in Kilcoy and the Somerset valleys</h2>
<p>Kilcoy is two jobs. In town, around Mary Street, Hope Street and the showgrounds, the blocks are older, flat and generous, 800 to 1,200 square metres with kikuyu or couch lawns and enough side access for a ride-on. Outside town it is acreage: lifestyle blocks of one to ten hectares along the D'Aguilar Highway, Kilcoy–Murgon Road, Kilcoy–Beerwah Road and out towards Jimna, with house yards, dams, gullies and paddocks that need a commercial zero-turn and someone who knows where the soft ground is.</p>
<p>The Somerset climate matters too. Kilcoy is hotter in summer and much colder in winter than the coast, with proper frosts from June to August that stop the grass dead. Winter cuts are infrequent and mostly a tidy; summer cuts after storm rain need to be every two to three weeks or the kikuyu gets away. We set the round to that rhythm rather than a coastal one.</p>
<h2>Somerset Dam, Hazeldean and the lake properties</h2>
<p>Around Somerset Dam, Hazeldean and Villeneuve the properties are often holiday houses, bed-and-breakfasts and weekenders whose owners are not there between visits. We have been the groundsman for a 3.74 acre B&amp;B on the dam side for years, mowing two dwellings, a boat shed, a gully and the surrounds of two dams, and the same approach applies to any lake property: a set day, the whole block finished, gates left as found, and a photo sent when we leave.</p>
<h2>What is included in a Kilcoy mowing visit</h2>
<p>Zero-turn mowing of open ground and paddocks at the right height for the season, push mowing and line trimming around the house, sheds, tanks and fence lines, dam banks and gullies where they are safe and dry, mulch-mowing so clippings feed the grass, and a blow-down of the entertaining area and paths. Slashing, hedge trimming, garden bed mulching and minor tree work are quoted alongside.</p>
<h2>Why Kilcoy chooses Green Estates</h2>
<p>A regular round means you are not paying for a special trip over the range every time. Fixed price per cut, the same crew each visit, no contract, and an operator who understands frost, dams and kikuyu the way a coastal mower does not. Kilcoy anchors our Somerset round with Esk, Toogoolawah and Woodford.</p>
""",
    faqs=[
        ("Do you really come to Kilcoy from Wamuran?", "<p>Yes, on a regular Somerset round rather than as a one-off trip, which is what keeps the fixed price per cut reasonable. Kilcoy, Somerset Dam, Hazeldean, Villeneuve and the properties along the D'Aguilar Highway are on the round, along with Woodford, Esk and Toogoolawah.</p>"),
        ("How much does acreage mowing cost around Kilcoy?", "<p>Acreage is priced on the area actually cut, the terrain and how often we visit, as one fixed price per cut. A block on a regular schedule costs less per visit than an occasional knockdown, because the kikuyu never gets long. We usually drive past first so the price is right the first time.</p>"),
        ("How often should acreage be mowed in the Somerset region?", "<p>Every two to three weeks from October to March after storm rain, stretching to five or six weeks from May to August when Kilcoy's frosts stop growth almost completely. Dam banks and gullies are mowed when dry and skipped when wet, so they may run on a longer cycle than the flat ground.</p>"),
        ("Do you look after holiday houses and B&amp;Bs near Somerset Dam?", "<p>Yes. We have been the groundsman for a 3.74 acre bed-and-breakfast on the dam for years, and we look after weekenders and holiday houses around Somerset Dam, Hazeldean and Villeneuve for owners who are not there between visits. Set day, whole block finished, photo sent when we leave.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-beachmere/", name="Beachmere", keyword="Lawn Mowing Beachmere", kind="lawn", region="mb", group="coast",
    neighbours=["/service-areas/lawn-mowing-bribie-island/", "/service-areas/lawn-mowing-caboolture/"], image="garden-cleanup-tidy-yard",
    alt="Lawn mowing Beachmere: tidy front lawn and footpath at a coastal village home",
    h1="Lawn Mowing Beachmere: Coastal Village Lawns on a Regular Round", h1_plain="Lawn Mowing Beachmere: Coastal Village Lawns on a Regular Round",
    title="Lawn Mowing Beachmere | Green Estates Gardening",
    description="Lawn mowing Beachmere homes, retirees and holiday houses on a fixed-price coastal round: sandy low-lying lawns cut right, edges included.",
    quick="Green Estates Gardening provides lawn mowing in Beachmere on fortnightly and monthly rounds at a fixed price per visit, covering the village streets around Biggs Avenue and the Esplanade, the newer estates off Beachmere Road, and the acreage between Beachmere and Caboolture. Low-lying sandy lawns are cut higher and sequenced around the tides and rain.",
    lead="Lawn mowing Beachmere residents need is coastal, low-lying and seasonal. The village sits on sand at the mouth of the Caboolture River, half the blocks are within a few streets of the water, and a king tide or a summer storm can leave lawns soft for days. Green Estates Gardening runs Beachmere with Bribie Island and Caboolture on a fixed-price round from Wamuran, edges and blow-down included.",
    body="""
<h2>Lawn mowing in Beachmere: sand, salt and the tide</h2>
<p>Beachmere's older streets around Biggs Avenue, Moreton Terrace and the Esplanade are flat, sandy and close to sea level. Couch and old kikuyu lawns here drain fast after rain but can sit wet after a king tide pushes groundwater up, so we check the ground before putting a mower on it and mow the higher blocks off Beachmere Road first. The salt breeze off Deception Bay burns soft grasses on exposed corners, which is why most of the village's lawns are the tough couch that thrives on a higher cut and a spring feed.</p>
<p>The newer estates back towards Beachmere Road and the rural residential blocks between the village and Caboolture are a different job: buffalo lawns on smaller blocks in the estates, and kikuyu acreage of 2,000 square metres and up on the way out of town, which gets the ride-on.</p>
<h2>Retirees, holiday houses and families</h2>
<p>Beachmere is a village of retirees, holiday-house owners who come down from Brisbane on weekends, and young families in the newer streets. All three want the same thing from a mower: turn up on the day, do the whole job, and do not need to be supervised. We mow on a set day, leave gates as we found them, and send a photo when it is done, which suits the weekenders in particular.</p>
<h2>What is included in a Beachmere mowing visit</h2>
<p>Mowing at the right height for couch, buffalo or kikuyu, edging along footpaths, driveway and kerb, line trimming around fences, beds and the clothesline, clippings caught and removed on village blocks, mulch-mowing on acreage, and a blow-down of paths and the frontage. Hedge trimming for the coastal westringia and lilly pilly screens, weed treatment, mulching and green waste removal can be added at a fixed price.</p>
<h2>Why Beachmere chooses Green Estates</h2>
<p>We run Beachmere with Bribie Island, Sandstone Point and Caboolture as one coastal loop on a set day, so the fixed price reflects an efficient round rather than a special trip from the city. Same crew each visit, no contract, and 5.0 on Google from 23 reviews across Moreton Bay.</p>
""",
    faqs=[
        ("How often should a Beachmere lawn be mowed?", "<p>Fortnightly from September to April and every four to six weeks in winter for most village lawns. Couch on the sandy flats grows fast after rain but slows in dry spells, so we adjust the round to the grass. Kikuyu acreage between Beachmere and Caboolture runs every two to three weeks in summer.</p>"),
        ("Can you mow after a king tide or heavy rain in Beachmere?", "<p>We check the ground first. Low-lying lawns near the Esplanade can sit soft for a day or two after a king tide or storm, so we mow the higher blocks off Beachmere Road first and come back to the flats when they firm up, rather than leaving ruts across a soft lawn.</p>"),
        ("Do you look after holiday houses in Beachmere?", "<p>Yes. Weekenders and holiday houses whose owners are in Brisbane during the week are a large part of our Beachmere round. We mow on a set day, leave gates as we found them, and message a photo when the job is done, so the place is right when you arrive on Friday.</p>"),
        ("How much does lawn mowing cost in Beachmere?", "<p>A standard village block on a fortnightly round is our most economical service per visit; acreage between Beachmere and Caboolture is quoted on the area actually cut. Every property is a fixed price quoted before we start, and because Beachmere is on our coastal round there is no special-trip premium.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-petrie/", name="Petrie", keyword="Lawn Mowing Petrie", kind="lawn", region="mb", group="corridor", flagged=True,
    neighbours=["/service-areas/lawn-mowing-kallangur/", "/service-areas/lawn-mowing-strathpine/"], image="walkway-mowing-edging",
    alt="Lawn mowing Petrie: mown lawn and edged path at an established home",
    h1="Lawn Mowing Petrie: Established Lawns Near the River, the Mill &amp; the Station", h1_plain="Lawn Mowing Petrie: Established Lawns Near the River, the Mill & the Station",
    title="Lawn Mowing Petrie | Green Estates Gardening",
    description="Lawn mowing Petrie homes and rentals on fixed-price fortnightly rounds: established blocks, mature trees, river-flat soils and rentals near The Mill.",
    quick="Green Estates Gardening provides lawn mowing in Petrie on fortnightly and monthly rounds at a fixed price per visit, covering the established 600 to 800 square metre blocks between Dayboro Road and the North Pine River, the streets around the station and The Mill precinct, and the rentals that serve the university campus.",
    lead="Lawn mowing Petrie households need is old-suburb mowing: established 600 to 800 square metre blocks, big trees, kikuyu and couch lawns that have been there for decades, and river-flat soil near the North Pine that holds water after every storm. Add a growing number of student rentals around The Mill and the university, and you have our Petrie round. Fixed price per cut, edges and blow-down included.",
    body="""
<h2>Lawn mowing in Petrie: established blocks and river soil</h2>
<p>Petrie was built before small blocks were fashionable. The streets between Dayboro Road, Gympie Road and the North Pine River carry lawns of 600 to 800 square metres under mature gums, camphor laurels and jacarandas, with leaf litter that has to come off before the mow and tree roots that scalp a low deck. Down on the river flats and around Sweeney Reserve and Old Petrie Town the soil is heavy and slow to drain, so we sequence those blocks last after rain. Up the hill towards Whiteside and Kurwongbah the blocks open out and a small ride-on earns its place.</p>
<p>Kikuyu dominates the older lawns and grows hard through summer; couch holds the sunnier front yards; buffalo appears where owners have re-turfed. Each gets the right height and the right interval rather than one setting for the street.</p>
<h2>The Mill, the university and rentals</h2>
<p>The Mill precinct and the university campus have changed Petrie's rental market, and property managers with student and family rentals around the station, Anzac Avenue and Frenchs Road are now a big part of our round. Routine fortnightly or monthly mowing between inspections, end-of-lease resets, and a photo after every visit so the file is current without a drive-by.</p>
<h2>What is included in a Petrie mowing visit</h2>
<p>Leaf and bark cleared from the lawn, mowing at the right height for the grass and the shade, edging along footpaths, driveway and kerb, line trimming around fences, trees and beds, clippings caught and removed, and a blow-down of hard surfaces. Hedge trimming, garden bed weeding, mulching and minor tree work such as low limbs over the driveway can be added to the same visit at a fixed price.</p>
<h2>Why Petrie chooses Green Estates</h2>
<p>Petrie sits at the southern end of our corridor round through Narangba and Strathpine, so we are through regularly and can move a cut around the weather. Fixed price per visit, the same crew each time, no contract, and 13 years of looking after exactly this kind of established Pine Rivers block.</p>
""",
    faqs=[
        ("How much does lawn mowing cost in Petrie?", "<p>A standard Petrie block on a fortnightly round is our most economical service per visit. First visits with heavy leaf litter or long grass cost more because of the clearing and green waste, then drop to the regular price once the lawn is on a schedule. Every property is a fixed price quoted before we start.</p>"),
        ("Do you mow student and family rentals near The Mill and the university?", "<p>Yes. Routine mowing between inspections, end-of-lease resets and pre-sale presentation for rentals around the station, Anzac Avenue, Frenchs Road and The Mill are a growing part of our Petrie round. We photograph every visit and quote each property as a fixed price.</p>"),
        ("Can you handle the leaf litter and tree roots on an old Petrie block?", "<p>Yes. Leaf and bark are cleared before every mow, the deck runs higher over exposed roots so nothing is scalped, and low limbs over paths and roofs can be removed as minor tree work on the same visit. Larger climbing work is referred to an arborist.</p>"),
        ("Which parts of Petrie do you cover?", "<p>All of Petrie, including the river flats near Sweeney Reserve and Old Petrie Town, the streets around the station and The Mill, and the larger blocks up towards Whiteside and Kurwongbah. Petrie is run with Kallangur and Strathpine as one round from our base in Wamuran.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-kallangur/", name="Kallangur", keyword="Lawn Mowing Kallangur", kind="lawn", region="mb", group="corridor", flagged=True,
    neighbours=["/service-areas/lawn-mowing-petrie/", "/service-areas/lawn-mowing-north-lakes/"], image="push-mowing-residential-lawn",
    alt="Lawn mowing Kallangur: push mower on a neat suburban front lawn",
    h1="Lawn Mowing Kallangur: Family Blocks, Rentals &amp; Older Lawns on a Set Day", h1_plain="Lawn Mowing Kallangur: Family Blocks, Rentals & Older Lawns on a Set Day",
    title="Lawn Mowing Kallangur | Green Estates Gardening",
    description="Lawn mowing Kallangur families and landlords book fortnightly: 600 m² blocks, older couch and kikuyu lawns, newer estates towards Murrumba Downs.",
    quick="Green Estates Gardening provides lawn mowing in Kallangur on fortnightly and monthly rounds at a fixed price per visit, covering the established 600 square metre blocks between Anzac Avenue and Dohles Rocks Road, the older streets around the shops and school, and the newer estates towards Murrumba Downs and Griffin.",
    lead="Lawn mowing Kallangur homeowners want is straightforward suburban mowing done reliably: 600 square metre family blocks, couch and kikuyu lawns that have been there since the seventies, a growing number of rentals, and newer buffalo lawns on the Murrumba Downs side. Green Estates Gardening runs Kallangur with Petrie and North Lakes on a fixed-price round, edges and blow-down included.",
    body="""
<h2>Lawn mowing in Kallangur: the classic suburban block</h2>
<p>Kallangur is the Moreton Bay suburb most people picture when they think of a normal block: a lowset or highset house on 600 square metres, front lawn to the footpath, a Hills Hoist out the back and a side gate wide enough for a decent push mower. The lawns are mostly couch and kikuyu on a mix of sandy and clay soils, so some streets drain overnight and others near Freshwater Creek and the Pine River stay soft for a couple of days after a storm. We know which is which and sequence the round accordingly.</p>
<p>Along the Murrumba Downs and Griffin edge the newer estates bring smaller blocks and soft-leaf buffalo that wants a high cut and a catcher. Around Anzac Avenue, the shops and the school there are townhouse complexes and duplexes with shared strips that go on a scheduled round with one invoice.</p>
<h2>Families, retirees and rentals</h2>
<p>Kallangur is a family suburb with a lot of long-term residents and a lot of rentals, and both are on our round. Families want the weekend back and a frontage the neighbours do not comment on; retirees who have mowed their own lawn for forty years want it done to that standard; property managers want routine mowing between inspections, end-of-lease resets and a photo for the file. Fixed price per visit for all three, no contract.</p>
<h2>What is included in a Kallangur mowing visit</h2>
<p>Mowing at the right height for couch, kikuyu or buffalo, edging along footpaths, driveway and kerb, line trimming around fences, beds and the clothesline, clippings caught and removed, and a blow-down of hard surfaces. Hedge trimming, weed treatment for bindii and nutgrass, garden bed mulching and green waste removal can be added at a fixed price.</p>
<h2>Why Kallangur chooses Green Estates</h2>
<p>Kallangur fills the corridor between our Petrie and North Lakes rounds, so we are through regularly and can shift a cut around the weather instead of missing a month. Fixed price before we start, the same crew each visit, no contract, and 5.0 on Google from 23 reviews across Moreton Bay.</p>
""",
    faqs=[
        ("How much does lawn mowing cost in Kallangur?", "<p>A standard 600 square metre Kallangur block on a fortnightly round is our most economical service per visit. One-off cuts and end-of-lease resets cost more because of the extra passes and green waste, then drop to the regular price on a schedule. Every property is a fixed price quoted before we start, usually the same day.</p>"),
        ("How often should a Kallangur lawn be mowed?", "<p>Fortnightly from September to April and monthly from May to August for most Kallangur lawns. Kikuyu near Freshwater Creek and the river flats can need a weekly cut after storms in January and February; buffalo on the Murrumba Downs side is usually fine at fortnightly all summer.</p>"),
        ("Do you mow rentals in Kallangur?", "<p>Yes. Routine mowing between inspections, end-of-lease resets and pre-sale presentation for Kallangur rentals are a regular part of our round. We photograph every visit and quote each property as a fixed price so owners and managers know the cost in advance.</p>"),
        ("Do you cover Murrumba Downs, Griffin and Dakabin too?", "<p>Yes. Kallangur is run with Petrie, Murrumba Downs, Griffin, Dakabin and North Lakes as one corridor round from our base in Wamuran, so the whole area is covered on a set day and the fixed price reflects an efficient loop.</p>"),
    ],
),
dict(
    path="/service-areas/lawn-mowing-daguilar/", name="D'Aguilar", keyword="Lawn Mowing D'Aguilar", kind="lawn", region="mb", group="acreage",
    neighbours=["/service-areas/lawn-mowing-wamuran/", "/service-areas/lawn-mowing-kilcoy/"], image="acreage-mowing-shed",
    alt="Lawn mowing D'Aguilar: mown rural block with shed and gardens in the range foothills",
    h1="Lawn Mowing D'Aguilar: Range-Foothill Acreage Mowed by Your Neighbours", h1_plain="Lawn Mowing D'Aguilar: Range-Foothill Acreage Mowed by Your Neighbours",
    title="Lawn Mowing D'Aguilar | Green Estates Gardening",
    description="Lawn mowing D'Aguilar acreage and lifestyle blocks on a regular round from Wamuran next door: ride-on mowing, house yards, slopes and gullies, fixed price.",
    quick="Green Estates Gardening provides lawn mowing in D'Aguilar on a regular round from Wamuran, five minutes down the highway, covering lifestyle acreage and rural residential blocks in the foothills of the D'Aguilar Range between Wamuran and Woodford. Zero-turn ride-on mowing for the open ground, push mowing around the house, sloping blocks handled safely, fixed price per cut.",
    lead="Lawn mowing D'Aguilar blocks need is acreage mowing with hills in it. Sitting in the foothills between Wamuran and Woodford, D'Aguilar's lifestyle blocks and rural residential streets climb towards the range, with kikuyu paddocks, gullies, dams and the odd slope a domestic ride-on should never go near. Green Estates Gardening is based five minutes away in Wamuran and runs D'Aguilar as part of our home round, fixed price per cut.",
    body="""
<h2>Lawn mowing in D'Aguilar: acreage in the foothills</h2>
<p>D'Aguilar's blocks run from 2,500 square metre rural residential lots near the highway and the school to lifestyle acreage of two, five and ten hectares up Grigor Street, Ridge Road and the roads that climb towards Mount Mee and Bellthorpe. The grass is kikuyu almost everywhere, thick and fast after summer rain, and the ground is anything but flat: contour banks, gullies, dam walls and driveways cut into the hillside. A commercial zero-turn handles the moderate slopes and open ground; the steep banks and the wet gullies get a line trimmer or wait for dry weather, because the fastest way to wreck a hillside lawn is to put a heavy machine on it when it is soft.</p>
<p>Around the house it is the usual acreage finish: yard, tank stand, shed surrounds, fence lines, the drip line under the big trees and the driveway edges, all done with the push mower and trimmer so the whole block looks looked-after, not just the paddock.</p>
<h2>Who we mow for in D'Aguilar</h2>
<ul>
<li><strong>Lifestyle block owners</strong> who commute to Caboolture or Brisbane and want the weekend back.</li>
<li><strong>Semi-retired and retired residents</strong> who no longer want to wrestle a ride-on up a slope.</li>
<li><strong>Weekenders and hobby farms</strong> that need the house yard and road frontage kept tidy between visits.</li>
<li><strong>New arrivals</strong> who bought the view and discovered what kikuyu does in January.</li>
</ul>
<h2>What is included in a D'Aguilar mowing visit</h2>
<p>Zero-turn mowing of paddocks and open ground at the right height for the season, push mowing and line trimming around the house, sheds, tanks and fence lines, slopes and dam banks mowed when they are safe and dry, mulch-mowing so clippings feed the grass, and a blow-down of the entertaining area and paths. Slashing of overgrown areas, hedge trimming, mulching and minor tree work such as limbs over the driveway are quoted alongside.</p>
<h2>Why D'Aguilar chooses the crew from next door</h2>
<p>Wamuran to D'Aguilar is five minutes, so there is no travel premium and a cut can be slotted in the first dry morning after rain rather than whenever a city operator gets out this way. Fixed price per visit agreed before we start, the same crew every time, no contract, and more than 13 years on exactly this kind of range-foothill block.</p>
""",
    faqs=[
        ("Can you mow sloping acreage in D'Aguilar safely?", "<p>Yes, within limits. Commercial zero-turns handle gentle to moderate slopes when the ground is dry and are driven up and down rather than across. Steep banks, dam walls and wet gullies are line-trimmed or left until they dry. We price a sloping block after seeing it, so the quote reflects the real work.</p>"),
        ("How much does acreage mowing cost in D'Aguilar?", "<p>Acreage is priced on the area actually cut, the slope and terrain, and how often we visit, as one fixed price per cut. Because D'Aguilar is five minutes from our base in Wamuran there is no travel premium, and a block on a regular round costs less per visit than an occasional knockdown.</p>"),
        ("How often should kikuyu be mowed in D'Aguilar?", "<p>Every two to three weeks from October to March and every five to six weeks from May to August. The foothills get more rain than the coast and kikuyu responds fast, so a fixed schedule is what keeps a D'Aguilar paddock walkable and the seed heads and snakes down.</p>"),
        ("Do you also cover Woodford, Mount Mee and Bellthorpe?", "<p>Yes. D'Aguilar, Woodford, Bracalba, Wamuran and the lower slopes towards Mount Mee are our home round, and Bellthorpe and the Somerset side of the range are covered on the Kilcoy round. If you are along the D'Aguilar Highway between Caboolture and Kilcoy, you are close to base.</p>"),
    ],
),
]
