# -*- coding: utf-8 -*-
"""Blog posts 6–10: hedges, mulch, weeds, cleanups."""
from gesite import SITE, icon

D = "2026-09-29"

def callout(text, ic="check"):
    return f'<div class="callout"><span class="icon-tile">{icon(ic)}</span><p>{text}</p></div>'

POSTS_B = [
# ---------------------------------------------------------------- 6
dict(
    slug="best-time-to-trim-hedges-queensland", short="When to trim hedges", category="hedge", date=D,
    image="hedge-trimming-long-hedge",
    alt="Long boundary hedge freshly trimmed level in Moreton Bay, showing the best time to trim hedges in Queensland",
    title="When Is the Best Time to Trim Hedges in South-East Queensland?",
    h1="When Is the Best Time to Trim Hedges in South-East Queensland?", h1_plain="When Is the Best Time to Trim Hedges in South-East Queensland?",
    meta_title="Best Time to Trim Hedges in Queensland | Green Estates",
    description="Best time to trim hedges in South-East Queensland: main cut in early spring, light tidies in summer, final trim in autumn. Species timing for Moreton Bay.",
    keyword="best time to trim hedges",
    excerpt="A main shaping cut in early spring, light tidies through summer and a final trim in autumn, with timing by species for Moreton Bay gardens.",
    lead="The best time to trim hedges in South-East Queensland is not the same as the advice in a UK gardening book or a Melbourne blog, and following either is how a lilly pilly screen in Burpengary ends up bare-stemmed in February. This guide gives the calendar we use for hedges across Moreton Bay and Somerset, species by species, plus the cuts to avoid and how to trim a hedge so it stays dense to the ground.",
    quick="In South-East Queensland the best time to trim most hedges is early spring, from late August to October, after the last cold snap and before the summer growth surge. Follow with light tidy-up cuts through summer and a final shaping trim in autumn, and avoid hard cuts during heatwaves or right before a frost.",
    body=f'''
<h2 id="calendar">What does the hedge trimming calendar look like in Moreton Bay?</h2>
<p>Warm-season hedging plants in Moreton Bay grow in flushes: a big one in spring, steady growth through the wet summer, a smaller flush in autumn, and very little between June and August. Trimming works with those flushes rather than against them.</p>
<div class="tbl-wrap"><table>
<thead><tr><th>Period</th><th>What to do</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Late August – October</td><td>Main shaping cut, any height reduction</td><td>Plant is about to push hard; cuts heal fast and fill in within weeks.</td></tr>
<tr><td>November – February</td><td>Light tidy cuts every 6–8 weeks</td><td>Keeps lines crisp without stripping leaf in the heat.</td></tr>
<tr><td>March – April</td><td>Final shaping trim</td><td>Sets the hedge up to look neat through the slow winter months.</td></tr>
<tr><td>May – July</td><td>Leave it alone (except dead wood)</td><td>Growth is minimal; cuts stay visible and frost can burn fresh growth in Somerset valleys.</td></tr>
</tbody></table></div>
<p>Two or three cuts a year is the norm for a formal hedge in Caboolture or North Lakes. Fast growers like lilly pilly and murraya on a boundary screen may need a fourth in a wet year.</p>

<h2 id="species">When should you trim each common Moreton Bay hedge?</h2>
<h3>Lilly pilly (Syzygium, Acmena)</h3>
<p>The most planted screen in South-East Queensland. Trim after each flush of pink new growth hardens off, typically September, December and March. Cutting mid-flush wastes the plant's energy and encourages psyllid damage on the soft tips.</p>
<h3>Murraya (orange jessamine)</h3>
<p>Trim straight after flowering finishes so you do not lose the next lot of flowers. In Moreton Bay that usually means late spring and again in late summer. Murraya tolerates hard cutting well and reshoots from old wood.</p>
<h3>Photinia and viburnum</h3>
<p>Both are grown for the coloured new growth, so time cuts to trigger a flush: early spring and mid-summer. Avoid cutting in late autumn or the fresh red tips can be frost-damaged in Kilcoy, Esk and Toogoolawah.</p>
<h3>Duranta and bougainvillea</h3>
<p>Trim after flowering, and do not be shy: both are vigorous. A late winter cut back sets them up for the season. Wear gloves for bougainvillea and expect to remove thorny prunings, which is one reason clients hand this one to us.</p>
<h3>Natives: westringia, callistemon, grevillea, syzygium 'Resilience'</h3>
<p>Light, frequent tipping after flowering is the rule. Most natives do not reshoot from bare old wood, so never cut back into it. Westringia, in particular, wants a tip-prune every eight weeks in the growing season rather than one hard cut a year.</p>
<h3>Conifers</h3>
<p>Once a year in early spring, and only into green growth. Cut a conifer back to brown wood and it stays brown. If a conifer hedge has got too big, the honest answer is often a replacement rather than a reduction.</p>

<h2 id="avoid">When should you not trim a hedge?</h2>
<ul>
<li><strong>During a heatwave.</strong> Removing leaf in 35-degree heat exposes inner branches to sunburn and stresses the plant. Wait for a cooler week.</li>
<li><strong>Right before a frost.</strong> In the Somerset valleys, fresh cuts and soft new growth in June or July can be burnt. Finish the autumn trim by mid-April.</li>
<li><strong>In the middle of a growth flush.</strong> You will be cutting again in three weeks and you have wasted the flush.</li>
<li><strong>When birds are nesting.</strong> Check dense hedges in spring before starting; give an active nest a few weeks.</li>
<li><strong>When the hedge is drought-stressed.</strong> Water it well for a fortnight first, then cut.</li>
</ul>

<h2 id="how">How do you trim a hedge so it stays thick to the ground?</h2>
<p>Timing is half of it; technique is the other half. Whether you are doing it yourself or checking someone else's work, these are the fundamentals we apply on every job from Redcliffe to Woodford:</p>
<ol>
<li><strong>Cut the faces slightly wider at the base than the top.</strong> A gentle batter lets light reach the lower leaves, which is the only thing that keeps a hedge full at the bottom. Hedges that are cut dead vertical, or wider at the top, always go bare at the base within a few years.</li>
<li><strong>Do the sides first, then the top.</strong> Use a string line for the top on anything longer than a couple of metres; eyes lie, especially on sloping ground.</li>
<li><strong>Use sharp blades.</strong> Torn leaves brown at the edges and invite disease. Sharpen or replace blades before each season.</li>
<li><strong>Take little and often rather than a lot at once.</strong> A hedge trimmed three times a year with light cuts looks better every day of the year than one hacked back annually.</li>
<li><strong>Clean up completely.</strong> Clippings left in the base of a hedge hold moisture against the stems and hide the growth of weeds. Rake them out and remove them.</li>
</ol>
{callout("<strong>Reducing an overgrown hedge:</strong> take it down in stages across a season, never more than a third at once, and only on species that reshoot from old wood (lilly pilly, murraya, photinia, viburnum, duranta). Conifers and most natives will not recover from a hard cut.", "shears")}

<h2 id="pro">When is it worth getting a professional to trim your hedges?</h2>
<p>Anything over head height, anything on a boundary you cannot reach from your own side, anything long enough to need a string line, and anything you have been putting off for a year. A professional cut with the right timing costs less over a season than replacing a hedge that was cut at the wrong time. Our <a href="/hedge-trimming-moreton-bay/">hedge trimming service</a> covers formal shaping, staged height reduction and screen pruning across Moreton Bay and Somerset, with every clipping removed.</p>
''',
    faqs=[
        ("How many times a year should hedges be trimmed in Queensland?", "<p>Two to three times a year for most formal hedges in South-East Queensland: a main shaping cut in early spring, a light tidy in mid-summer and a final trim in autumn. Fast-growing screens such as lilly pilly and murraya may need a fourth light cut in a wet year, while conifers need only one cut in spring.</p>"),
        ("Can you trim hedges in summer in Queensland?", "<p>Yes, with light cuts only. Summer trims keep lines crisp on lilly pilly, murraya and photinia, but avoid cutting during heatwaves above about 33 degrees, because exposed inner leaves sunburn and the plant is already under stress. Trim in the morning, water well afterwards, and save any hard reduction for early spring.</p>"),
        ("Is it too late to trim hedges in autumn?", "<p>No. A final shaping trim in March or April is ideal in Moreton Bay; it tidies the hedge for the slow winter months. Finish by mid-April in the Somerset region so fresh growth hardens before frost. Avoid heavy cuts from May to July, when growth is minimal and cuts stay visible for months.</p>"),
        ("What month is best to cut back a lilly pilly hedge?", "<p>September is the best month for a main cut on a lilly pilly hedge in South-East Queensland, just as spring growth begins. Follow with lighter trims in December and March after each flush of new growth has hardened off. Cutting during a flush of soft pink growth wastes the plant's energy and invites psyllid damage.</p>"),
        ("Do you remove the clippings when you trim hedges?", "<p>Yes. Every Green Estates Gardening hedge trimming visit across Moreton Bay and Somerset includes raking clippings from garden beds and lawn, blowing down paths and removing all green waste. Clippings left in the base of a hedge trap moisture against the stems and hide weeds, so we never leave them behind.</p>"),
    ],
    cta_heading="Book the spring cut before the growth surge",
    cta_text="Send a photo of the hedge with the quote form and Green Estates Gardening will give you a fixed price for shaping, reduction or a seasonal trimming schedule across Moreton Bay and Somerset.",
),
# ---------------------------------------------------------------- 7
dict(
    slug="best-hedge-plants-moreton-bay", short="Best hedge plants", category="hedge", date=D,
    image="hedge-trimming-formal-hedges",
    alt="Formal clipped hedges and shaped shrubs in a Moreton Bay front garden, examples of the best hedge plants for the region",
    title="The Best Hedge Plants for Moreton Bay Gardens (and How Much Trimming Each Needs)",
    h1="The Best Hedge Plants for Moreton Bay Gardens (and How Much Trimming Each Needs)", h1_plain="The Best Hedge Plants for Moreton Bay Gardens (and How Much Trimming Each Needs)",
    meta_title="Best Hedge Plants for Moreton Bay Gardens | Green Estates",
    description="Best hedge plants for Moreton Bay: lilly pilly, murraya, viburnum, photinia, westringia and more, with height, growth rate and how often each needs a trim.",
    keyword="best hedge plants",
    excerpt="Lilly pilly, murraya, viburnum, photinia, westringia and more, compared on height, growth rate, pests and how often each needs the trimmer.",
    lead="Choosing the best hedge plants for a Moreton Bay garden is mostly about matching the plant to the job: privacy screen, low formal border, windbreak on acreage, or something that survives a Somerset frost. After 13 years of trimming almost every hedge species planted in South-East Queensland, here is our honest ranking, with how much maintenance each one really needs.",
    quick="The best hedge plants for Moreton Bay are lilly pilly for tall privacy screens, murraya for a fragrant 1.5 to 3 metre hedge, viburnum odoratissimum for fast dense screening, photinia for colour, westringia and Syzygium 'Resilience' for low-maintenance natives, and buxus or Japanese box for low formal borders. Match the species to the height you want and the trimming you will actually do.",
    body=f'''
<h2 id="choose">How do you choose a hedge plant for South-East Queensland?</h2>
<p>Four questions settle it. How tall does it need to be at maturity? How fast do you need it to get there? How much sun does the spot get? And how often will it actually be trimmed? The last one is where most hedges go wrong. A vigorous screen that needs cutting four times a year is a great choice with a <a href="/hedge-trimming-moreton-bay/">regular hedge trimming</a> schedule and a disaster without one. Soil matters too: sandy coastal soils around Redcliffe and Bribie drain fast and need mulch, while the heavier soils inland around Caboolture and the Somerset valleys hold water and can waterlog in a wet summer.</p>

<h2 id="tall">What are the best tall privacy hedges (2 to 5 metres)?</h2>
<h3>Lilly pilly (Syzygium australe 'Resilience', Acmena smithii 'Minor')</h3>
<p>The default privacy screen for a reason: fast, dense, glossy, native and happy in sun or part shade. 'Resilience' resists the psyllid that pimples older varieties. Expect a metre of growth a year once established and plan on three trims a season. Best for boundary screens in Narangba, Burpengary and North Lakes where you want privacy from a two-storey neighbour within three years.</p>
<h3>Viburnum odoratissimum ('Dense Fence', 'Emerald Lustre')</h3>
<p>Possibly the fastest dense screen available in Queensland, with large soft leaves and very forgiving of hard cuts. It needs water in dry spells and three to four trims a year to stay tidy. Excellent where speed matters more than a fine formal finish.</p>
<h3>Photinia 'Red Robin'</h3>
<p>Grown for the bright red new growth in spring and after each trim. Handles frost better than lilly pilly, so it suits Kilcoy, Esk and Toogoolawah. Watch for leaf spot in humid, shaded spots on the coast.</p>
<h3>Bamboo (clumping only: Bambusa textilis 'Gracilis')</h3>
<p>For a narrow, very tall screen in a tight space. Choose clumping varieties only and never running bamboo. Maintenance is thinning old culms rather than trimming, once or twice a year.</p>

<h2 id="medium">What are the best medium hedges (1 to 2 metres)?</h2>
<h3>Murraya paniculata</h3>
<p>Glossy, dense, fragrant white flowers several times a year, and tolerant of both hard pruning and humidity. It is the most reliable medium hedge in Moreton Bay and suits formal front-garden hedges in Morayfield and Caboolture. Trim after each flowering.</p>
<h3>Duranta 'Sheena's Gold' and 'Geisha Girl'</h3>
<p>Fast, bright and cheap, which makes them common in new estates. They need frequent trimming and can look tired after a few years. Good for colour, less good for a low-maintenance garden.</p>
<h3>Syzygium 'Cascade', 'Bush Christmas'</h3>
<p>Compact lilly pilly cultivars for a native hedge at 1.5 to 2 metres with fluffy pink flowers and bird-attracting fruit. Two to three trims a year.</p>
<h3>Westringia fruticosa ('Grey Box', 'Zena')</h3>
<p>Native, drought-hardy, salt-tolerant and unbothered by coastal wind, which makes it the pick for Redcliffe and the bayside. It will not reshoot from bare wood, so it wants light tip-pruning every couple of months rather than one hard cut. Superb low-maintenance hedge if trimmed little and often.</p>

<h2 id="low">What are the best low formal hedges and borders (under 1 metre)?</h2>
<ul>
<li><strong>Japanese box (Buxus microphylla var. japonica):</strong> the classic tight formal border. Slow, so fewer trims, and it tolerates the heat better than English box.</li>
<li><strong>Dwarf lilly pilly ('Tiny Trev', 'Little Ruby'):</strong> native, colourful new growth, 60 to 90 centimetres.</li>
<li><strong>Dwarf murraya ('Min-a-Min'):</strong> all the murraya virtues at knee height.</li>
<li><strong>Dwarf westringia ('Mundi', 'Aussie Box'):</strong> ball hedges and low borders on the coast.</li>
<li><strong>Coastal rosemary and Lomandra:</strong> for a soft, unclipped border along an acreage driveway.</li>
</ul>

<h2 id="acreage">What are the best hedges and windbreaks for acreage and Somerset properties?</h2>
<p>On larger blocks around Wamuran, D'Aguilar, Woodford and the Somerset region the hedge is usually a windbreak, a screen from the road, or a boundary planting that gets trimmed once a year from a ride-on with a hedge trimmer on a pole. Lilly pilly 'Resilience', Acmena 'Minor', Photinia and Callistemon 'Kings Park Special' all cope with frost pockets and infrequent trimming. Space them at 1 to 1.5 metres, mulch heavily in the first two summers, and keep the kikuyu away from the base while they establish.</p>
{callout("<strong>Avoid these in Moreton Bay:</strong> English box (hates humidity), running bamboo (spreads under fences), and Cocky Apple or Golden Cane palms as ‘hedges’ (they are not hedges and they never look like one).", "shield")}

<h2 id="maintenance">How much trimming does each hedge really need?</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Plant</th><th>Growth rate</th><th>Trims per year</th><th>Reshoots from old wood?</th></tr></thead>
<tbody>
<tr><td>Lilly pilly 'Resilience'</td><td>Fast</td><td>3</td><td>Yes</td></tr>
<tr><td>Viburnum odoratissimum</td><td>Very fast</td><td>3–4</td><td>Yes</td></tr>
<tr><td>Murraya</td><td>Medium</td><td>2–3</td><td>Yes</td></tr>
<tr><td>Photinia 'Red Robin'</td><td>Fast</td><td>2–3</td><td>Yes</td></tr>
<tr><td>Duranta</td><td>Very fast</td><td>4</td><td>Yes</td></tr>
<tr><td>Westringia</td><td>Medium</td><td>4–6 light tips</td><td>No</td></tr>
<tr><td>Japanese box</td><td>Slow</td><td>2</td><td>Yes, slowly</td></tr>
<tr><td>Conifers</td><td>Medium</td><td>1</td><td>No</td></tr>
</tbody></table></div>
<p>If the number in the third column is higher than the number of Saturdays you will genuinely spend on it, choose a slower plant or book the trimming in. The best hedge is the one that is actually maintained. For when to make each of those cuts, see our guide to the <a href="/blog/best-time-to-trim-hedges-queensland/">best time to trim hedges in South-East Queensland</a>.</p>
''',
    faqs=[
        ("What is the fastest growing hedge plant in Queensland?", "<p>Viburnum odoratissimum and lilly pilly 'Resilience' are the fastest dense screening hedges in South-East Queensland, each putting on around a metre a year once established. Duranta is quicker still but shorter-lived. Fast growth means more trimming: budget for three to four cuts a year to keep any of them tidy.</p>"),
        ("What is the best low-maintenance hedge for Moreton Bay?", "<p>Westringia for coastal and sunny sites, Japanese box for low formal borders, and Syzygium 'Resilience' for a native screen. All three need fewer or lighter cuts than viburnum or duranta. Westringia must be tip-pruned little and often, because it will not reshoot if cut back into bare wood.</p>"),
        ("Which hedge plants handle frost in the Somerset region?", "<p>Photinia 'Red Robin', Acmena smithii 'Minor', Callistemon 'Kings Park Special', Japanese box and most westringias cope with the frost pockets around Kilcoy, Esk, Toogoolawah and Lowood. Young lilly pilly and murraya can be burnt by hard frost, so plant them in spring and protect them for the first two winters.</p>"),
        ("How far apart should hedge plants be planted?", "<p>For a dense screen, plant lilly pilly, viburnum and photinia 80 centimetres to 1 metre apart, murraya 60 to 80 centimetres, and low box or dwarf lilly pilly 30 to 40 centimetres. On acreage windbreaks 1 to 1.5 metres is fine. Closer spacing gives a solid hedge sooner but costs more and needs more trimming.</p>"),
        ("Do you plant hedges as well as trim them?", "<p>Green Estates Gardening focuses on trimming, shaping, reducing and maintaining existing hedges across Moreton Bay and Somerset, along with garden bed preparation and mulching. For new plantings we are happy to advise on species and spacing during a quote, and we take over the trimming schedule once the hedge is in.</p>"),
    ],
    cta_heading="Got a hedge that has outgrown its owner?",
    cta_text="Green Estates Gardening trims, shapes and reduces every species on this list across Moreton Bay and Somerset, on a schedule matched to the plant. Send a photo for a fixed price.",
),
# ---------------------------------------------------------------- 8
dict(
    slug="when-to-mulch-garden-queensland", short="When to mulch", category="mulch", date=D,
    image="mulched-garden-bed-fenceline",
    alt="Freshly mulched garden bed along a fence line in Moreton Bay, showing when to mulch a garden in Queensland",
    title="When to Mulch a Garden in Queensland (and How Much Mulch You Need)",
    h1="When to Mulch a Garden in Queensland (and How Much Mulch You Need)", h1_plain="When to Mulch a Garden in Queensland (and How Much Mulch You Need)",
    meta_title="When to Mulch a Garden in Queensland | Green Estates",
    description="When to mulch a garden in Queensland: late winter to early spring, topped up in autumn. How thick, how much you need per m², and which mulch stops weeds.",
    keyword="when to mulch",
    excerpt="Late winter to early spring, topped up in autumn. How thick to lay it, how many cubic metres you need, and which mulch actually stops weeds.",
    lead="Knowing when to mulch in Queensland makes the difference between beds that sail through a Moreton Bay summer and beds that are cracked, weedy and thirsty by Christmas. Timing, depth and the type of mulch each matter. This guide gives the calendar we work to across Caboolture, North Lakes and the Somerset region, a simple way to calculate how much mulch you need, and which mulch actually suppresses weeds.",
    quick="The best time to mulch a garden in Queensland is late winter to early spring, from August to October, with a top-up in autumn. Lay organic mulch 50 to 75 millimetres deep, keep it clear of stems and trunks, and allow roughly one cubic metre for every 13 square metres of bed at 75 millimetres.",
    body=f'''
<h2 id="timing">Why is late winter to early spring the best time to mulch in Queensland?</h2>
<p>Three things line up between August and October in South-East Queensland. The soil is warming but not yet hot, so mulch traps warmth rather than sealing in heat. The beds have just been weeded after the slow winter, so you are covering clean soil. And the storm season has not started, so a fresh 75 millimetre layer is in place before the first big downpour, ready to slow run-off and hold the moisture that follows.</p>
<p>Mulch laid in December still helps, but you are usually spreading it over weeds that have already germinated and soil that is already baked. Mulch laid in June sits on cold soil and, in the Somerset valleys, can keep the ground colder for longer. Spring is the sweet spot; autumn (March to April) is the second-best window and the right time for a top-up before the dry months.</p>

<h2 id="thick">How thick should mulch be?</h2>
<p>Between 50 and 75 millimetres once it has settled, which means spreading closer to 80 to 90 millimetres of loose material. Thinner than 50 and light reaches the soil, so weed seeds germinate. Thicker than 100 and rain cannot get through to the roots, and the mulch itself can go sour and hydrophobic. Keep it 5 to 10 centimetres clear of plant stems and tree trunks; mulch piled against bark keeps it wet and invites collar rot, which is a common killer of young citrus and lilly pilly in humid Moreton Bay gardens.</p>
{callout("<strong>How much mulch do I need?</strong> Multiply the bed area (m²) by the depth (m). A 40 m² bed at 0.075 m deep needs 3 cubic metres. As a rule of thumb, 1 m³ covers about 13 m² at 75 mm, or 20 m² at 50 mm. Order about 10 percent extra for settling.", "tag")}

<h2 id="types">Which type of mulch is best for Moreton Bay gardens?</h2>
<p>Every landscape yard from Caboolture to Kilcoy sells five or six options. They are not interchangeable.</p>
<div class="tbl-wrap"><table>
<thead><tr><th>Mulch</th><th>Best for</th><th>Lasts</th><th>Weed suppression</th></tr></thead>
<tbody>
<tr><td>Hardwood chip</td><td>Landscape beds, driveways, large rural gardens</td><td>18–24 months</td><td>Excellent</td></tr>
<tr><td>Forest / cypress mulch</td><td>Slopes, large areas, value</td><td>12–18 months</td><td>Very good; knits together</td></tr>
<tr><td>Tea tree mulch</td><td>Native gardens, feature beds</td><td>9–12 months</td><td>Good; fine texture</td></tr>
<tr><td>Sugar cane mulch</td><td>Vegetable and herb beds</td><td>3–6 months</td><td>Fair; feeds soil fast</td></tr>
<tr><td>Pine bark</td><td>Ornamental beds</td><td>12 months</td><td>Good; can float in heavy rain</td></tr>
<tr><td>Pebbles / gravel</td><td>Paths, succulents, around pools</td><td>Permanent</td><td>Good with weed mat; holds heat</td></tr>
</tbody></table></div>
<p>For most garden beds in Moreton Bay we recommend hardwood chip or forest mulch: they last the longest, stay put in a storm, and give the best weed suppression per dollar. Tea tree looks best around an entrance. Sugar cane is for the veggie patch, where you want it to break down and feed the soil. Save pebbles for paths and pool surrounds; around plants they radiate heat in summer.</p>

<h2 id="weeds">Does mulch stop weeds, and which mulch is best for it?</h2>
<p>Mulch stops most weeds by blocking the light their seeds need to germinate, and it makes the few that do come up easy to pull because the soil underneath stays soft and moist. Coarse hardwood chip at 75 millimetres is the best weed suppressor because it does not compact into a seedbed the way fine mulches do. What mulch will not do is kill established perennial weeds such as nutgrass, couch runners or onion weed; those push straight through. Treat or remove them first, then mulch. Our <a href="/garden-cleanup-moreton-bay/">weed control and garden cleanup</a> service does exactly that sequence.</p>
<p>Weed mat under mulch is worth it under pebbles and on paths. Under organic mulch in a planted bed we usually skip it: it stops the mulch improving the soil, roots tangle in it, and within two years weeds grow in the mulch on top of it anyway.</p>

<h2 id="prep">How should you prepare a bed before mulching?</h2>
<ol>
<li><strong>Weed thoroughly</strong>, including roots. Spray or hand-pull nutgrass and runners a week before.</li>
<li><strong>Re-cut the edges</strong> so the lawn cannot creep in under the new layer.</li>
<li><strong>Remove or turn the old mulch</strong> if it has matted or gone hydrophobic (water beads on it instead of soaking in).</li>
<li><strong>Top up soil</strong> where it has slumped away from roots, and fertilise if the plants need it; mulch on top locks the feed in.</li>
<li><strong>Water the bed deeply</strong>, then mulch. Dry soil under mulch stays dry.</li>
<li><strong>Spread evenly</strong> to 80 to 90 millimetres loose, clear of stems, and rake level.</li>
</ol>
<p>On acreage gardens around Wamuran, Woodford and Esk the same steps apply, just with a trailer and a bobcat rather than a barrow. Bulk delivery is far cheaper per cubic metre than bags once you are past about two cubic metres, which is why we supply and spread as one fixed price on our <a href="/mulching-services-moreton-bay/">mulching service</a>.</p>

<h2 id="topup">How often should you top up mulch?</h2>
<p>Organic mulch is supposed to break down; that is how it feeds the soil. In Moreton Bay's heat and rain, expect hardwood chip to need topping up every 18 months to two years, forest mulch annually, and sugar cane every season. Rather than replacing the whole layer, rake the old mulch over, add 30 to 40 millimetres on top, and keep the total depth around 75 millimetres. If the layer has turned into a grey crust that sheds water, break it up with a fork first or replace it.</p>
''',
    faqs=[
        ("What month should I mulch my garden in Queensland?", "<p>August to October is the ideal window in South-East Queensland, after the last cold snap and before the storm season. A second, lighter application in March or April tops the beds up for the dry months. Avoid mulching in mid-winter, when it keeps cold soil cold, or in the peak of summer over already-baked ground.</p>"),
        ("How much mulch do I need per square metre?", "<p>At the recommended 75 millimetre depth you need 0.075 cubic metres per square metre, so one cubic metre covers about 13 square metres. At 50 millimetres one cubic metre covers about 20 square metres. Measure the beds, multiply length by width by depth, and order roughly 10 percent extra for settling.</p>"),
        ("What is the best mulch to stop weeds?", "<p>Coarse hardwood chip or forest mulch laid 75 millimetres deep is the best organic mulch for suppressing weeds in Moreton Bay gardens. It blocks light, does not compact into a seedbed and lasts up to two years. It will not stop established nutgrass or couch runners, which must be treated or removed before mulching.</p>"),
        ("Should I put weed mat under mulch?", "<p>Under pebbles and on paths, yes. Under organic mulch in a planted garden bed, usually no. Weed mat stops the mulch feeding the soil, roots tangle in it, and weeds end up growing in the decomposed mulch on top of it within a couple of years. A thick 75 millimetre layer of coarse mulch works better on its own.</p>"),
        ("Do you supply mulch or do I have to buy it?", "<p>Either. Green Estates Gardening can supply bulk mulch and spread it as one fixed price across Moreton Bay and Somerset, which is usually cheaper than bags once you need more than two cubic metres. If you already have mulch delivered, we prepare the beds and spread it. Bed weeding and edging are done first on every job.</p>"),
    ],
    cta_heading="Get the beds mulched before the storms, not after",
    cta_text="Send the number and rough size of your beds, or a couple of photos, and Green Estates Gardening will quote preparation, mulch supply and spreading as one fixed price across Moreton Bay and Somerset.",
),
# ---------------------------------------------------------------- 9
dict(
    slug="get-rid-of-lawn-weeds-queensland", short="Lawn weeds", category="cleanup", date=D,
    image="garden-cleanup-tidy-yard",
    alt="Weed-free tidy lawn and footpath at a Moreton Bay home after lawn weed control",
    title="How to Get Rid of Weeds in a Queensland Lawn: Bindii, Nutgrass, Clover and More",
    h1="How to Get Rid of Weeds in a Queensland Lawn: Bindii, Nutgrass, Clover and More", h1_plain="How to Get Rid of Weeds in a Queensland Lawn: Bindii, Nutgrass, Clover and More",
    meta_title="How to Get Rid of Weeds in a Queensland Lawn | Green Estates",
    description="How to get rid of weeds in a Queensland lawn: identify bindii, nutgrass, clover and crabgrass, treat each at the right time, and keep them out for good.",
    keyword="get rid of weeds",
    excerpt="Identify bindii, nutgrass, clover, crowsfoot and crabgrass, treat each at the right time of year, and stop them coming back with a thicker lawn.",
    lead="Trying to get rid of weeds in a Moreton Bay lawn without knowing which weed you have is how people end up spraying three products, burning their buffalo and still stepping on bindii in October. Each of the common South-East Queensland lawn weeds has a season when it is easy to beat and a season when it is nearly impossible. This guide covers identification, timing, what is safe on each grass type, and the only long-term fix.",
    quick="To get rid of weeds in a Queensland lawn, identify the weed first, then treat at the right time: bindii with a selective broadleaf herbicide in winter before it seeds, nutgrass with a sedge-specific product in warm weather, clover and broadleaf weeds in spring or autumn, and crabgrass or crowsfoot by hand or pre-emergent. Then mow higher and feed the lawn so weeds cannot get back in.",
    body=f'''
<h2 id="why">Why do weeds take over lawns in Moreton Bay?</h2>
<p>Weeds are opportunists. They germinate wherever light reaches bare soil, which happens when a lawn is mown too short, starved of nitrogen, compacted by foot traffic, or thinned by shade, drought or lawn grub. South-East Queensland adds a wet, humid summer that germinates everything at once and a dry winter that thins warm-season grass while cool-season weeds like bindii and winter grass move in. Fixing the weed without fixing the reason it got a foothold means doing it all again next year.</p>

<h2 id="identify">Which weeds are you dealing with?</h2>
<h3>Bindii (Soliva sessilis)</h3>
<p>The one that stabs bare feet. A low, feathery rosette that germinates in autumn, grows through winter and sets its spiky seed in spring. If you can feel it, it has already seeded.</p>
<h3>Nutgrass (Cyperus rotundus)</h3>
<p>A sedge, not a grass: glossy, triangular stems that shoot up faster than the lawn between mows. It spreads by underground nuts, so pulling it makes it worse. Common in the heavier soils around Caboolture and Morayfield and in any bed that has had garden soil brought in.</p>
<h3>Clover and other broadleaf weeds</h3>
<p>White clover, cudweed, creeping oxalis, dandelion and fleabane. Broad leaves, easy to identify, and the group most selective lawn herbicides are designed for.</p>
<h3>Crowsfoot, crabgrass and summer grass</h3>
<p>Coarse, pale, fast-growing annual grasses that appear in bare patches from November on. Tough to kill selectively once established because they are grasses among grass.</p>
<h3>Winter grass (Poa annua)</h3>
<p>Soft, bright green tufts with white seed heads that appear in couch and kikuyu lawns in June and July and die off by October, leaving bare patches.</p>

<h2 id="timing">When is the best time to treat lawn weeds in Queensland?</h2>
<div class="tbl-wrap"><table>
<thead><tr><th>Weed</th><th>Treat</th><th>How</th></tr></thead>
<tbody>
<tr><td>Bindii</td><td>June – August, before seed sets</td><td>Selective broadleaf herbicide (bromoxynil + MCPA type); repeat after 3 weeks</td></tr>
<tr><td>Nutgrass</td><td>October – March, actively growing</td><td>Sedge-specific herbicide (halosulfuron); two applications, do not pull</td></tr>
<tr><td>Clover, oxalis, cudweed</td><td>Spring and autumn</td><td>Selective broadleaf herbicide; hand-pull small patches</td></tr>
<tr><td>Crowsfoot, crabgrass</td><td>Pre-emergent in September; hand-pull in summer</td><td>Pre-emergent granules before germination; thicken the lawn</td></tr>
<tr><td>Winter grass</td><td>Pre-emergent in April – May</td><td>Pre-emergent; then over-sow bare patches in spring</td></tr>
</tbody></table></div>
{callout("<strong>Buffalo lawn warning:</strong> Sir Walter, Palmetto and other soft-leaf buffalo lawns are damaged by herbicides containing dicamba or 2,4-D, which are in many general ‘weed and feed’ products. Use only products labelled safe for buffalo, and read the label rate; more is not better.", "shield")}

<h2 id="methods">What are the ways to get rid of lawn weeds, and which actually work?</h2>
<h3>Selective herbicides</h3>
<p>The most effective option for broadleaf weeds and bindii. Selective means it kills the weed and leaves the grass, provided you match the product to your grass type. Spray on a still, dry morning when the weed is actively growing, and do not mow for three days before or after so there is leaf to absorb the product.</p>
<h3>Sedge-specific herbicides</h3>
<p>The only thing that beats nutgrass. General weedkillers and hand-pulling do not touch the nuts. Two applications a fortnight apart in warm weather, with a wetting agent, and expect to follow up the next season.</p>
<h3>Pre-emergent herbicides</h3>
<p>These stop seeds germinating rather than killing plants. Applied in early spring they prevent crabgrass and summer grass; applied in autumn they prevent winter grass and much of the bindii. They are the most under-used tool in home lawn care and the biggest single reason professionally maintained lawns in North Lakes and Redcliffe stay clean.</p>
<h3>Hand removal</h3>
<p>Fine for a few clover patches or young crowsfoot after rain, when the whole root comes out. Useless on nutgrass and hopeless once bindii has seeded.</p>
<h3>Vinegar, salt and boiling water</h3>
<p>All three kill whatever they touch, including your lawn, and salt damages soil for years. They have a place on cracks in paths and driveways and nowhere near a lawn you want to keep.</p>

<h2 id="prevent">How do you stop weeds coming back?</h2>
<p>A thick lawn is the only permanent weed control. Everything above buys you the window to grow one. Once the weeds are down:</p>
<ul>
<li><strong>Mow higher.</strong> Buffalo at 50 to 60 millimetres and kikuyu at 40 to 50 shades the soil so seeds cannot germinate. Scalping is an open invitation.</li>
<li><strong>Feed it.</strong> A slow-release lawn fertiliser in September, December and March keeps warm-season grass growing hard enough to out-compete anything.</li>
<li><strong>Water deeply, not often.</strong> Two deep soaks a week in dry spells beats a daily sprinkle that only wets the surface where weed seeds sit.</li>
<li><strong>Relieve compaction.</strong> Core or fork-aerate high-traffic areas each spring.</li>
<li><strong>Fix the bare patches.</strong> Over-sow or plug bare areas in spring so weeds do not get there first.</li>
<li><strong>Keep the mower clean.</strong> A mower that has just done a weedy lawn spreads seed to the next one. Ours are blown down between jobs for exactly this reason.</li>
</ul>

<h2 id="help">When should you get professional weed control?</h2>
<p>When you cannot identify the weed, when it is buffalo lawn and you are not sure what is safe, when nutgrass has taken over a bed or a lawn, or when the whole yard has got away and needs a reset before any of this can start. Our <a href="/garden-cleanup-moreton-bay/">garden cleanup and weed control</a> service uses registered products at label rates, tells you exactly what was applied and when pets and kids can go back on, and then puts the lawn on a mowing and feeding schedule so the weeds stay gone. It works alongside a <a href="/blog/when-to-mulch-garden-queensland/">fresh layer of mulch</a> on the beds, which handles the other half of the weed problem.</p>
''',
    faqs=[
        ("How do I get rid of bindii in my lawn?", "<p>Treat bindii in June, July or August with a selective broadleaf herbicide labelled for your grass type, before the plant sets its spiky seed in spring, and repeat three weeks later. Once you can feel the prickles it has already seeded, and the only option is to prevent next year's crop with a pre-emergent in autumn and a thicker lawn.</p>"),
        ("What kills nutgrass but not the lawn?", "<p>A sedge-specific herbicide containing halosulfuron kills nutgrass without harming buffalo, couch, kikuyu or zoysia when used at the label rate. Apply twice, two weeks apart, in warm weather when the nutgrass is actively growing, and add a wetting agent. Do not hand-pull nutgrass: it leaves the nuts behind and spreads it.</p>"),
        ("Is it safe to spray weeds on a buffalo lawn?", "<p>Only with products labelled safe for buffalo. Many general weed-and-feed products contain dicamba or 2,4-D, which burn soft-leaf buffalo such as Sir Walter and Palmetto. Look for bromoxynil and MCPA formulations for broadleaf weeds and halosulfuron for nutgrass, follow the label rate exactly, and spray on a cool, still morning.</p>"),
        ("When is the best time of year to kill weeds in Queensland?", "<p>It depends on the weed. Winter, from June to August, is the time for bindii and other cool-season broadleaf weeds. Spring and autumn suit clover and general broadleaf treatment. Nutgrass needs warm weather between October and March. Pre-emergent herbicides go down in September for summer grasses and April for winter weeds.</p>"),
        ("Do you offer lawn weed spraying in Moreton Bay?", "<p>Yes. Green Estates Gardening treats lawn, path and garden bed weeds across Moreton Bay and Somerset as part of a garden cleanup or a regular maintenance schedule. We use registered products at label rates, match them to your grass type, tell you when treated areas are safe for pets and children, and quote it as a fixed price.</p>"),
    ],
    cta_heading="Identify it, treat it, then keep it out",
    cta_text="Send a photo of the weed and your suburb, and Green Estates Gardening will tell you what it is and quote the treatment as a fixed price, with a mowing schedule to stop it coming back.",
),
# ---------------------------------------------------------------- 10
dict(
    slug="overgrown-garden-cleanup-guide", short="Overgrown garden guide", category="cleanup", date=D,
    image="garden-cleanup-before-overgrown",
    alt="Severely overgrown back garden with long grass and weeds in Moreton Bay before a garden cleanup",
    title="What It Takes to Clear a Severely Overgrown Garden (Without Making It Worse)",
    h1="What It Takes to Clear a Severely Overgrown Garden (Without Making It Worse)", h1_plain="What It Takes to Clear a Severely Overgrown Garden (Without Making It Worse)",
    meta_title="Clearing an Overgrown Garden in Moreton Bay | Green Estates",
    description="How to clear an overgrown garden the right way: the order of work, green waste, snakes and safety, what it costs, and how to stop it getting away again.",
    keyword="overgrown garden",
    excerpt="The order of work, what to keep and what to cut, green waste volumes, snakes and safety, and how to stop the block getting away again.",
    lead="An overgrown garden is not just a long lawn. By the time grass is knee high in Moreton Bay there are usually weeds seeding in the beds, hedges a metre out of shape, a shed you cannot get to and, in summer, a real chance of a snake in the long grass. Clearing it is a sequence, not a single mow. This guide sets out how we approach a severely overgrown garden, what it involves, what it costs relative to maintenance, and how to make sure it never gets to that point again.",
    quick="Clearing a severely overgrown garden means working in order: a safety walk, brushcutting long grass, a high first mow, cutting back shrubs and hedges, weeding and treating the beds, then removing all green waste and doing a second, lower mow a week later. Done properly it takes one to two visits and resets the block so normal maintenance can take over.",
    body=f'''
<h2 id="define">What counts as a severely overgrown garden?</h2>
<p>In our quoting, a lawn is overgrown when the grass is more than about three times its normal cut height, roughly 15 centimetres on a residential lawn or 30 centimetres on acreage. It is severely overgrown when you can no longer see the ground, weeds have seeded through the beds, shrubs have merged, and there are things hidden in the growth: hoses, toys, timber, a rabbit hutch. That last point is not a joke; it is the main reason a first visit is never priced by the square metre.</p>
<p>We see three versions across Moreton Bay. Rentals in Caboolture, Morayfield and Burpengary between tenants. Homes in Redcliffe and North Lakes where the owner has been unwell, away or simply busy. And acreage in Wamuran, D'Aguilar, Woodford and the Somerset valleys where one wet summer turned a paddock into a hay crop.</p>

<h2 id="first">What should you do before anyone starts cutting?</h2>
<ol>
<li><strong>Walk it slowly, in boots, with a rake.</strong> You are looking for snakes, wasp nests, hidden objects, uneven ground, tap heads and irrigation. In summer, assume there is a snake until proven otherwise.</li>
<li><strong>Decide what stays.</strong> Under the growth there may be plants worth keeping: a citrus, a frangipani, a decent hedge line. Flag them before the brushcutter starts.</li>
<li><strong>Check access.</strong> Can a trailer get close? Is the side gate wide enough for a mower? Green waste volume from an overgrown block surprises people; being able to load directly saves hours.</li>
<li><strong>Photograph it.</strong> For rentals and sales you will want the before and after, and it settles arguments about the state of the property.</li>
</ol>
{callout("<strong>Snakes:</strong> eastern browns and red-bellied blacks both like long grass near water and sheds in Moreton Bay. Clear from the house outwards so anything in there is pushed away from you, make noise, and never reach into growth you cannot see through.", "shield")}

<h2 id="order">In what order do you clear an overgrown block?</h2>
<h3>1. Brushcut the long grass</h3>
<p>A mower will not cut 40 centimetres of seeded kikuyu; it will stall, clog and scalp. A brushcutter or slasher takes it down to a height the mower can handle. On acreage this might be a tractor slasher or a heavy-duty zero-turn with the deck at its highest.</p>
<h3>2. Rake and remove the cut material</h3>
<p>Long grass left where it falls forms a mat that kills the lawn underneath in a week. Rake it off or use a catcher, and get it on the trailer.</p>
<h3>3. First mow, high</h3>
<p>With the bulk gone, mow at the highest deck setting. This evens it out and reveals the ground you could not see, along with anything the walk missed.</p>
<h3>4. Cut back shrubs, hedges and overhanging branches</h3>
<p>Take hedges back towards shape in stages, no more than a third at once on species that will not reshoot from old wood. Remove low branches over paths, gutters and sheds. Cut bougainvillea and lantana out completely if they have escaped.</p>
<h3>5. Weed and treat the beds</h3>
<p>Hand-weed, then spray persistent problems like nutgrass and running couch so they do not reappear under the new mulch. Re-cut the bed edges so the lawn stops creeping in.</p>
<h3>6. Load and remove the green waste</h3>
<p>A severely overgrown suburban block routinely fills a 6 by 4 trailer two or three times. Acreage can be a skip. This is the part that makes DIY exhausting and is a large share of the cost of a professional clearance.</p>
<h3>7. Second mow, a week later</h3>
<p>Bringing the lawn down to its normal height in one go would scalp and stress it. Come back after five to seven days and take it to the final height. Now it is a lawn again.</p>
<h3>8. Mulch and set a schedule</h3>
<p>Fresh <a href="/mulching-services-moreton-bay/">mulch on the cleared beds</a> and a fortnightly or monthly mowing round is what stops the whole thing happening again.</p>

<h2 id="cost">How much does an overgrown garden cleanup cost compared with regular maintenance?</h2>
<p>Substantially more per visit, and the reason is time and tonnage rather than any premium. A first visit on a badly overgrown block typically takes three to five times as long as a maintenance visit on the same property, involves two machines instead of one, and generates several trailer loads of green waste that have to be disposed of. That is why we quote cleanups only after seeing the block or clear photos, as a single fixed price for the whole reset rather than an hourly rate that could run anywhere.</p>
<p>The flip side is that once the block is cleared and on a schedule, each visit is a fast, light cut at a much lower price. Over a year, a fortnightly round on a Caboolture rental costs less than two emergency clearances between tenants, and the property is presentable every week in between. See how we structure it on our <a href="/garden-cleanup-moreton-bay/">garden cleanup and weed control</a> page.</p>

<h2 id="diy">Can you clear an overgrown garden yourself?</h2>
<p>A moderately overgrown suburban block, yes, over a weekend with a hired brushcutter, a mower, a lot of green waste bags and a tip run. A severely overgrown block, or anything on acreage, is a different proposition: the equipment is heavier, the volume of waste is measured in trailer loads, and the snake and heat risk in a Moreton Bay summer is real. The most common call we get is from someone who started on Saturday morning, got a third of the way through and rang us on Sunday.</p>
<p>If you do tackle it yourself, work in the cool of the morning, wear boots, long pants and gloves, keep the brushcutter guard on, and do not try to take the lawn to its final height in one cut. And book the tip before you start; overgrown gardens produce far more waste than people expect.</p>

<h2 id="prevent">How do you stop a garden getting overgrown again?</h2>
<ul>
<li><strong>A fixed mowing schedule</strong>, fortnightly in the growing season, monthly in winter. Our guide to <a href="/blog/how-often-to-mow-lawn-moreton-bay/">how often to mow in Moreton Bay</a> explains the intervals.</li>
<li><strong>Seasonal hedge trims</strong> in spring and autumn so nothing ever needs a hard cut.</li>
<li><strong>Mulched beds</strong> topped up each spring so weeds cannot get started.</li>
<li><strong>Someone responsible for it</strong> when you are away, unwell or between tenants. For property managers, that is usually us.</li>
</ul>
''',
    faqs=[
        ("How long does it take to clear an overgrown garden?", "<p>A severely overgrown suburban block in Moreton Bay usually takes a professional crew one full day for the first visit, with a short second visit a week later to bring the lawn to its final height. Acreage that has had a wet summer to itself can take two days plus green waste removal. DIY typically takes two to three weekends.</p>"),
        ("Should I mow an overgrown lawn or brushcut it first?", "<p>Brushcut first. A domestic mower cannot cut grass much over 15 centimetres without stalling, clogging and scalping. Brushcut or slash it down, rake off the cut material so it does not smother the lawn, then mow at the highest setting. Come back a week later for a second, lower cut so the lawn recovers green rather than yellow.</p>"),
        ("What happens to the green waste from a garden cleanup?", "<p>Green Estates Gardening loads all cut grass, prunings and weeds onto the trailer and disposes of it at a licensed green waste facility. A severely overgrown suburban block often produces two or three trailer loads; acreage can fill a skip. Removal is included in every fixed-price cleanup quote across Moreton Bay and Somerset.</p>"),
        ("Are there snakes in overgrown gardens in Moreton Bay?", "<p>Often, especially from October to April near water, sheds, timber piles and long grass. Eastern browns and red-bellied blacks are both common in the region. Walk the block slowly in boots before cutting, clear from the house outwards so snakes are pushed away, and never reach into growth you cannot see through. If you see one, leave it and call a licensed catcher.</p>"),
        ("Do you clean up overgrown gardens for rentals and sales?", "<p>Yes. End-of-lease resets in Caboolture, Morayfield, Burpengary and Narangba and pre-sale presentation in Redcliffe, North Lakes and Strathpine are the most common cleanups we do, along with overgrown acreage in Wamuran, Woodford and the Somerset region. Every job is quoted as one fixed price with green waste removal included, and we send photos when it is done.</p>"),
    ],
    cta_heading="Send a photo, the worse the better",
    cta_text="Green Estates Gardening clears severely overgrown gardens and blocks across Moreton Bay and Somerset in one to two visits, green waste included, then puts them on a schedule so it never happens again. Fixed price, quoted from photos or a quick drive-by.",
),
]
