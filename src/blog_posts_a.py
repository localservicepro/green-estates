# -*- coding: utf-8 -*-
"""Blog posts 1–5: lawn mowing cluster."""
from gesite import SITE

D = "2026-09-29"

def callout(text, ic="check"):
    from gesite import icon
    return f'<div class="callout"><span class="icon-tile">{icon(ic)}</span><p>{text}</p></div>'

POSTS_A = [
# ---------------------------------------------------------------- 1
dict(
    slug="how-often-to-mow-lawn-moreton-bay", date="2026-09-01", short="How often to mow", category="lawn",
    image="push-mower-striped-lawn-morayfield",
    alt="Freshly mown striped residential lawn in Morayfield showing how often to mow lawn in Moreton Bay",
    title="How Often Should You Mow Your Lawn in Moreton Bay?",
    h1="How Often Should You Mow Your Lawn in Moreton Bay?", h1_plain="How Often Should You Mow Your Lawn in Moreton Bay?",
    meta_title="How Often to Mow Lawn in Moreton Bay | Green Estates",
    description="How often to mow lawn in Moreton Bay: every 7–14 days Oct–Mar, every 3–6 weeks in winter. Buffalo, couch and kikuyu schedules from a Wamuran local.",
    keyword="how often to mow",
    excerpt="Weekly to fortnightly through the growing season, every three to six weeks in winter. Here is the schedule by grass type and month.",
    lead="Wondering how often to mow lawn in Moreton Bay so it stays thick instead of scalped or shaggy? The honest answer changes with the month and the grass. This guide gives the schedule we run across Caboolture, Morayfield, North Lakes and the Somerset acreage belt, and the one rule that matters more than the calendar.",
    quick="How often to mow in Moreton Bay: every 7 to 14 days from October to March, every 2 to 3 weeks in April, May and September, and every 3 to 6 weeks from June to August. Never remove more than one third of the blade in a single cut; if the grass has got away, bring it down over two visits, whatever the calendar says about how often to mow.",
    body=f'''
<h2 id="rule">What is the one-third rule and why does it decide your mowing schedule?</h2>
<p>The one-third rule says you should never cut off more than a third of the grass blade in one mow. Take more and the plant loses too much leaf to feed its roots, the lawn browns off for a week, and weeds move into the thin patches. In practice this rule, not the calendar, sets how often to mow lawn in South-East Queensland: you mow when the grass is about 50 percent taller than the height you want to keep it at.</p>
<p>For a buffalo lawn kept at 40 millimetres, that means mowing when it hits 60 millimetres. In a wet Caboolture January, buffalo can put on 20 millimetres in a week, so the interval is weekly. In a dry Kilcoy July it might take five weeks to grow the same amount. Same rule, very different frequency. Ask any contractor how often to mow and they will ask what grass it is and what month it is before they answer.</p>
{callout("<strong>If your lawn is knee high:</strong> do not take it down to 40 mm in one go. Cut at the mower's highest setting, wait four or five days, then cut again. It recovers green instead of yellow, and you avoid a mat of thatch on the surface.")}

<h2 id="season">How often to mow in each season in South-East Queensland</h2>
<p>Moreton Bay sits in a warm, humid climate where warm-season grasses do almost all their growing between the first storms in October and Easter. Here is the schedule we run for regular clients from Redcliffe to Woodford:</p>
<div class="tbl-wrap"><table>
<thead><tr><th>Months</th><th>Growth</th><th>Mow every</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>October – November</td><td>Fast, accelerating</td><td>10–14 days</td><td>Storm season starts; lift the deck a notch as heat builds.</td></tr>
<tr><td>December – February</td><td>Very fast</td><td>7–10 days</td><td>Peak growth. Weekly on kikuyu and couch after rain.</td></tr>
<tr><td>March – April</td><td>Fast, slowing</td><td>10–14 days</td><td>Still humid; watch for lawn grub damage.</td></tr>
<tr><td>May – June</td><td>Slowing</td><td>2–3 weeks</td><td>Last chance to fertilise before winter dormancy.</td></tr>
<tr><td>July – August</td><td>Slow / dormant</td><td>3–6 weeks</td><td>Mostly a tidy-up cut; keep the deck higher.</td></tr>
<tr><td>September</td><td>Waking up</td><td>2–3 weeks</td><td>First real cut of spring, then back onto the fortnightly round.</td></tr>
</tbody></table></div>
<p>That table is the short answer to how often to mow a healthy, established lawn. A new turf lawn in a North Lakes estate needs its first cut only once the roots hold when you tug a corner, usually two to three weeks after laying, and then the normal schedule.</p>

<h2 id="grass">Does the grass type change how often to mow?</h2>
<p>Yes. The four grasses that cover almost every lawn in Moreton Bay behave differently under the mower.</p>
<h3>Buffalo (Sir Walter, Palmetto, Sapphire)</h3>
<p>Buffalo grows steadily rather than explosively and tolerates shade better than the others. Keep it between 40 and 60 millimetres and mow every 10 to 14 days in summer. Cutting buffalo too short is the most common mistake we see on new-estate lawns in Narangba and Burpengary: it opens the canopy and lets weeds in.</p>
<h3>Couch (Queensland blue couch, green couch, Wintergreen)</h3>
<p>Couch is the fastest grower of the lot in summer and likes to be kept short, 20 to 35 millimetres. If you are wondering how often to mow couch in January, the answer is weekly. It goes noticeably brown in winter, which is dormancy, not death.</p>
<h3>Kikuyu</h3>
<p>Kikuyu dominates acreage and older lawns around Wamuran, D'Aguilar and the Somerset valleys because it survives anything. How often to mow kikuyu on acreage is a question of keeping it walkable: every two to three weeks through summer just to stay walkable. It is the grass that most often gets away from owners over a wet Christmas.</p>
<h3>Zoysia</h3>
<p>Zoysia changes how often to mow more than any other choice. It grows slowest and is the lowest-maintenance option, often stretching to three weeks between cuts even in January. It is becoming common in newer Moreton Bay estates for exactly that reason.</p>

<h2 id="height">How short should you cut grass in Queensland's heat?</h2>
<p>Higher than you think. Longer leaf shades the soil, holds moisture and out-competes weeds. Through summer we run buffalo at 50 to 60 millimetres, kikuyu at 40 to 50 millimetres and couch at 25 to 35 millimetres. In winter drop each by roughly a notch on the mower so light reaches the crown. Scalping a lawn to 15 millimetres in February to "make it last longer" does the opposite: it stresses the grass, so you end up mowing weeds instead.</p>

<h2 id="signs">What are the signs you are mowing too often or not often enough?</h2>
<p>The lawn will tell you how often to mow if you read it:</p>
<ul>
<li><strong>Yellow or brown tips a day after mowing:</strong> the blade is blunt or you took off too much. Sharpen or raise the deck.</li>
<li><strong>Clumps of clippings left on the surface:</strong> the interval is too long for the season. Shorten it or catch the clippings.</li>
<li><strong>Seed heads standing above the lawn within days:</strong> normal for kikuyu and couch in summer; it means the next cut is due.</li>
<li><strong>Bare, compacted lines where the mower wheels run:</strong> you are mowing the same pattern too often. Alternate directions each visit.</li>
<li><strong>Weeds outgrowing grass between cuts:</strong> the lawn is being cut too short, too rarely, or both.</li>
</ul>

<h2 id="schedule">How often to mow: the schedule professionals recommend for Moreton Bay</h2>
<p>For most residential lawns from Caboolture to Redcliffe we recommend a fortnightly round from September to April and a monthly round from May to August, adjusting after big rain events. Acreage in Wamuran, Elimbah, Woodford and the Somerset towns usually runs every two to three weeks in the growing season and every five to six weeks in winter, because ride-on mowing at a higher deck height tolerates a longer interval than a manicured front lawn.</p>
<p>A fixed schedule beats deciding how often to mow on the day for one simple reason: the grass never gets long enough to break the one-third rule, so every cut is a light one, the lawn stays dense, and the price per visit stays low. It is the same reason our <a href="/lawn-mowing-moreton-bay/">regular lawn mowing clients</a> pay less per cut than one-off jobs.</p>

<h2 id="takeaways">Key takeaways</h2>
<ul><li><strong>How often to mow in summer:</strong> every 7 to 14 days from October to March, weekly on couch and kikuyu after rain.</li><li><strong>How often to mow in winter:</strong> every 3 to 6 weeks from June to August, with the deck a notch higher.</li><li><strong>The one-third rule</strong> decides how often to mow more than the calendar does: cut when the grass is 50 percent taller than its target height.</li><li><strong>Grass type matters:</strong> buffalo and zoysia stretch the interval, couch and kikuyu shorten it.</li></ul>
''',
    faqs=[
        ("How often should you mow your lawn in summer in Queensland?", "<p>How often to mow in summer: every 7 to 10 days from December to February for couch and kikuyu, and every 10 to 14 days for buffalo and zoysia. After a week of storms in Moreton Bay, growth can double, so mow as soon as the grass is about one and a half times its target height rather than waiting for the calendar.</p>"),
        ("How often should you mow in winter in Moreton Bay?", "<p>How often to mow in winter: every three to six weeks from June to August. Warm-season grasses slow almost to a stop below 15 degrees, so winter mowing is mainly a tidy-up to keep edges sharp and leaf litter off the lawn. Raise the deck slightly so the grass keeps enough leaf to photosynthesise on short days.</p>"),
        ("Is it bad to mow your lawn every week?", "<p>No, as long as each cut removes less than a third of the blade and the mower blade is sharp. Weekly mowing in peak summer is the healthiest option for couch and kikuyu lawns in South-East Queensland. It becomes harmful only when you mow short and often on a stressed or drought-affected lawn.</p>"),
        ("Should I leave the clippings on the lawn?", "<p>Yes, if you are mowing on schedule and the clippings are short; clippings do not change how often to mow. Mulch-mowing returns nitrogen and moisture to the soil. If the grass has got long and the clippings sit in clumps, catch and remove them, otherwise they smother the lawn underneath and encourage fungal disease in humid weather.</p>"),
        ("How often do you mow lawns for regular clients in Moreton Bay?", "<p>How often to mow for our regular clients is set by the season. Most of Green Estates Gardening's residential clients in Caboolture, Morayfield, Burpengary, North Lakes and Redcliffe are on a fortnightly round from September to April and monthly through winter. Acreage clients in Wamuran, Woodford and the Somerset region are usually every two to three weeks in summer and five to six weeks in winter, all at a fixed price per visit.</p>"),
    ],
    cta_heading="Want the schedule handled for you?",
    cta_text="Stop guessing how often to mow. Green Estates Gardening runs fixed-price fortnightly and monthly lawn mowing rounds across Moreton Bay and Somerset, from Redcliffe and North Lakes to Wamuran and Kilcoy. Send the address and we will quote within one business day.",
),
# ---------------------------------------------------------------- 2
dict(
    slug="lawn-mowing-cost-moreton-bay", date="2026-07-24", short="Lawn mowing cost", category="lawn",
    image="push-mower-front-lawn-north-lakes",
    alt="Push mower on a freshly cut front lawn in North Lakes illustrating lawn mowing cost in Moreton Bay",
    title="How Much Does Lawn Mowing Cost in Moreton Bay?",
    h1="How Much Does Lawn Mowing Cost in Moreton Bay?", h1_plain="How Much Does Lawn Mowing Cost in Moreton Bay?",
    meta_title="Lawn Mowing Cost Moreton Bay: What You Pay | Green Estates",
    description="Lawn mowing cost in Moreton Bay explained: what sets the price for standard blocks, acreage and overgrown resets, and why fixed quotes beat hourly rates.",
    keyword="lawn mowing cost",
    excerpt="What actually drives the price for a standard block, an acreage cut and an overgrown reset, and why fixed quotes beat hourly rates.",
    lead="Lawn mowing cost is the first thing most people search before they ring anyone, and most answers online are either a national average or a sales pitch. This guide explains what actually sets the price in Moreton Bay and Somerset, how acreage and overgrown jobs are quoted differently, and how to keep the number down without cutting corners.",
    quick="Lawn mowing cost in Moreton Bay depends on four things: lawn area, how long since it was last cut, how much edging and trimming is involved, and how often you book. A regular fortnightly cut on a standard suburban block is priced very differently from a one-off knockdown of an acreage that has had a wet summer to itself.",
    body=f'''
<h2 id="drivers">What actually determines lawn mowing cost?</h2>
<p>Every quote we write, from a townhouse courtyard in North Lakes to a five-acre block in D'Aguilar, comes down to time on site and what has to leave on the trailer. Four factors set that time, and therefore the lawn mowing cost:</p>
<ol>
<li><strong>Area being cut.</strong> A 400 square metre suburban block and a 4,000 square metre lifestyle block are different jobs, but the price does not scale in a straight line: a ride-on covers the big open block faster per square metre than a push mower covers a fiddly small one.</li>
<li><strong>Grass height and condition.</strong> A lawn on a regular schedule is a quick, clean cut. A lawn that has not been touched since March needs a brushcutter pass, a high first cut, a second cut and a lot more green waste. That first visit can cost two to three times a maintenance visit.</li>
<li><strong>Edging, trimming and obstacles.</strong> Long fence lines, garden beds, retaining walls, pool fences, play equipment and trees all add line-trimming time. Two blocks of identical area can differ by 30 minutes because of this alone.</li>
<li><strong>Frequency.</strong> Fortnightly clients pay less per visit than monthly clients, who pay less than one-off jobs, because the grass is shorter, the cut is faster and the run is planned.</li>
</ol>
<p>Access changes lawn mowing cost too. If the ride-on cannot get through a side gate, the back yard gets push-mowed, which takes longer. Steep banks, boggy ground after rain and hidden rubbish in long grass also add time, which is why we ask about them in the quote form.</p>

<h2 id="hourly">Fixed price or hourly rate: which lawn mowing cost model is fairer?</h2>
<p>Some operators quote an hourly rate. It sounds cheap until the invoice arrives and the job took longer than the estimate. A fixed price puts the risk on us, not you: if the grass is thicker than expected or the mower needs a second pass, that is our problem. It also makes budgeting simple, because a fortnightly cut costs the same in a wet February as it does in a dry August.</p>
{callout("<strong>How we quote lawn mowing cost:</strong> from the address and a satellite view for standard residential blocks in Caboolture, Morayfield, Burpengary, Narangba, North Lakes, Strathpine and Redcliffe, usually the same day. For acreage and big cleanups we often drive past first so the number is right the first time.", "tag")}

<h2 id="types">How does lawn mowing cost differ for residential, acreage and one-off jobs?</h2>
<h3>Standard residential lawn mowing</h3>
<p>Blocks under about 800 square metres are push-mowed, edged along every path and driveway, line-trimmed around beds and fences and blown down. On a fortnightly schedule through the growing season this is the lowest lawn mowing cost per visit we offer, because the lawn never gets long and the round is planned street by street.</p>
<h3>Acreage and ride-on mowing</h3>
<p>Lifestyle blocks from 2,500 square metres up to 20 acres around Wamuran, Bracalba, Elimbah, Woodford and the Somerset towns are priced by the area actually cut, the terrain and the interval. Ride-on mowing is efficient on open ground, so the lawn mowing cost per square metre is far lower than a residential lawn, but the total reflects the size of the block. Mulch-mowing keeps the cost down because nothing has to be carted away. See our <a href="/acreage-mowing-moreton-bay/">acreage mowing page</a> for what is included.</p>
<h3>One-off cuts and overgrown resets</h3>
<p>End-of-lease tidy-ups, pre-sale presentation and blocks that have got away carry a higher first-visit lawn mowing cost because of the extra passes and the green waste. Most clients then move to a maintenance schedule where the price per visit drops sharply. We explain the difference in our <a href="/garden-cleanup-moreton-bay/">garden cleanup guide</a>.</p>

<h2 id="extras">What is usually included, and what costs extra?</h2>
<p>A standard mowing visit from Green Estates includes mowing, edging along hard surfaces, line trimming around fences and beds, and a blow-down of paths and driveways. Clippings are mulched back in on acreage or caught and removed on residential lawns. Things that are quoted separately, because they take real extra time, include:</p>
<ul>
<li><a href="/hedge-trimming-moreton-bay/">Hedge trimming</a> and shrub pruning</li>
<li>Weed spraying of lawns, paths and garden beds</li>
<li>Garden bed weeding and <a href="/mulching-services-moreton-bay/">mulching</a></li>
<li>Green waste removal beyond normal clippings, such as palm fronds or storm debris</li>
<li>First-visit knockdowns of long grass</li>
</ul>
<p>Bundling two or three of these into one regular visit keeps the overall lawn mowing cost lower than booking them separately, because the travel and set-up happen once.</p>

<h2 id="save">How can you reduce your lawn mowing cost without lowering the standard?</h2>
<ul>
<li><strong>Book a schedule, not one-offs.</strong> Regular clients pay the lowest per-visit price because every cut is a light one.</li>
<li><strong>Keep gates clear and unlocked.</strong> Ten minutes moving a trailer or a trampoline is ten minutes on the clock.</li>
<li><strong>Let the ride-on in.</strong> A wider side gate on an acreage property can halve the mowing time.</li>
<li><strong>Bundle services.</strong> Hedges and edges on the same visit as the lawn cost less than a separate trip.</li>
<li><strong>Do not let it get away.</strong> The highest lawn mowing cost is the one after four months of neglect. The second most expensive is the one after a wet summer on kikuyu.</li>
</ul>

<h2 id="compare">How does Moreton Bay lawn mowing cost compare with Brisbane?</h2>
<p>Quotes in the outer northern corridor and the Somerset region are generally more competitive than inner Brisbane, because blocks are larger, travel between jobs is shorter for a locally based operator, and there is less of a premium for parking and access. The trade-off is that acreage jobs dominate out here, so the range between a small residential cut and a large rural block is much wider than it is in the city. That is exactly why a fixed, property-specific quote beats any published average.</p>

<h2 id="takeaways">Key takeaways</h2>
<ul><li><strong>Lawn mowing cost is set by four things:</strong> area, grass condition, edging and obstacles, and how often you book.</li><li><strong>A fixed price beats an hourly rate:</strong> the lawn mowing cost you agree to is the one you pay.</li><li><strong>Regular schedules cost less per visit</strong> than one-off cuts, and far less than an overgrown reset.</li></ul>
''',
    faqs=[
        ("How much does lawn mowing cost per hour in Australia?", "<p>Hourly rates for lawn mowing in Australia vary widely by region and equipment, and most reputable operators in Moreton Bay quote a fixed price per visit instead. A fixed price protects you from a job running long and lets you compare quotes on the result, not the clock. Green Estates Gardening quotes every property as a fixed price before starting.</p>"),
        ("Is it cheaper to mow your own lawn?", "<p>For a small block with a mower you already own, yes, in cash terms. Once you factor in a reliable mower, line trimmer, blower, fuel, blade sharpening and two to three hours a fortnight through summer, the lawn mowing cost of a fortnightly professional cut on a standard Moreton Bay block is often the better value, and it happens even when you are away or it rains on Saturday.</p>"),
        ("Why is the first mow more expensive than the regular price?", "<p>Because long grass takes more passes and produces far more green waste, so the first-visit lawn mowing cost reflects that time. A first visit on an overgrown lawn in Caboolture or Morayfield may need a brushcutter, a high cut, a second cut and a trailer load removed. Once the lawn is back on a schedule, each visit is a quick, light cut and the price per visit drops.</p>"),
        ("How much does acreage mowing cost in Moreton Bay?", "<p>Acreage lawn mowing cost is quoted on the area actually cut, the terrain and how often it is done. A ride-on covers open ground quickly, so the cost per square metre is low, but a two-acre block in Wamuran on a fortnightly round is still priced differently from a one-off knockdown of the same block. Send the address for a fixed quote.</p>"),
        ("Do you charge extra for edging and blowing down?", "<p>No. Edging along paths and driveways, line trimming around fences and beds, and blowing down hard surfaces are included in every Green Estates Gardening mowing visit across Moreton Bay and Somerset. Hedge trimming, weed spraying, mulching and bulk green waste removal are quoted separately because they add real time.</p>"),
    ],
    cta_heading="Get your actual lawn mowing cost, not an average",
    cta_text="Send the address, a rough block size and how often you would like us. Standard residential quotes in Moreton Bay usually go out the same day; acreage in Wamuran, Woodford and the Somerset region within one business day.",
),
# ---------------------------------------------------------------- 3
dict(
    slug="can-you-mow-wet-grass", date="2026-09-18", short="Mowing wet grass", category="lawn",
    image="acreage-dam-mowing-somerset",
    alt="Damp acreage lawn beside a farm dam in the Somerset region after rain, showing whether you can mow wet grass",
    title="Can You Mow Wet Grass? Mowing After Rain in South-East Queensland",
    h1="Can You Mow Wet Grass? Mowing After Rain in South-East Queensland", h1_plain="Can You Mow Wet Grass? Mowing After Rain in South-East Queensland",
    meta_title="Can You Mow Wet Grass? SEQ Wet-Season Guide | Green Estates",
    description="Can you mow wet grass? You can, but you usually shouldn't. When it's safe, when to wait, and how Moreton Bay lawns stay under control in storm season.",
    keyword="mow wet grass",
    excerpt="You can, but usually you shouldn't. When it is safe, when it damages the lawn, and how we keep Moreton Bay lawns under control in storm season.",
    lead="Can you mow wet grass? Every Moreton Bay lawn owner asks it by the second week of a wet January, when the grass is growing two centimetres a week and it has not stopped raining. The short answer is that you can, but it usually costs you a clean cut and a healthy lawn. Here is when it is fine to mow wet grass, when to wait, and how we keep lawns from Redcliffe to Kilcoy under control through storm season.",
    quick="You can mow wet grass, but it is usually a bad idea: wet blades bend instead of cutting cleanly, clippings clump and smother the lawn, the mower can slip and tear turf, and disease spreads in the damp. If you have to mow wet grass, do it only when it is lightly wet, the ground is firm, the blade is sharp and the deck is raised.",
    body=f'''
<h2 id="why-not">Why is it a problem to mow wet grass?</h2>
<p>Dry grass stands up and gets sliced cleanly. Wet grass lies down under the weight of the water, so the blade tears and bruises it instead. The result is a ragged, uneven cut that browns off within a day and leaves the lawn looking worse than before you started. That is the cosmetic problem. The practical ones are worse:</p>
<ul>
<li><strong>Clumping.</strong> Wet clippings stick together and to the underside of the deck. They drop in mats that smother the grass beneath and turn into slimy thatch in a Queensland summer.</li>
<li><strong>Rutting and tearing.</strong> Soft ground under a ride-on or even a push mower leaves wheel ruts, and on slopes the wheels spin and rip turf out by the roots.</li>
<li><strong>Disease.</strong> Fungal problems like brown patch and dollar spot spread on wet leaf tissue. A mower moving across a wet lawn carries spores from one patch to the next.</li>
<li><strong>Soil compaction.</strong> Saturated soil compresses under the machine, which is the opposite of what a lawn needs after weeks of rain.</li>
<li><strong>Safety and the machine.</strong> Wet grass is slippery, electric mowers and water do not mix, and the extra load on the engine blunts blades and clogs the deck.</li>
</ul>
<p>Every one of those is a reason not to mow wet grass if you can wait a day.</p>

<h2 id="when-ok">When is it okay to mow wet grass, or at least damp grass?</h2>
<p>There is a difference between wet and damp. Morning dew, a light shower an hour ago, or humidity that never quite lets the lawn dry are all realities of Moreton Bay from November to March. Waiting for a bone-dry lawn can mean waiting until May. Mowing damp grass is acceptable when all of these are true:</p>
<ol>
<li>The ground is firm underfoot and does not squelch or leave footprints.</li>
<li>Water does not bead on the leaf when you run your hand across it.</li>
<li>The mower blade is sharp. A sharp blade cuts damp grass; a blunt one tears it.</li>
<li>You raise the deck at least one notch above your usual height.</li>
<li>You slow down, overlap passes, and empty the catcher more often.</li>
</ol>
{callout("<strong>The squelch test:</strong> walk the wettest part of the lawn. If your shoe sinks or water rises around it, do not put a mower on it today. If it is merely soft and springy, you can mow wet grass with a light, high cut.")}

<h2 id="tips">How do you mow wet grass properly if you have to?</h2>
<p>Sometimes there is no choice: a tenant is moving out on Friday, a house is being photographed on Saturday, or the kikuyu on an acreage block in Wamuran is so far ahead that another week of rain will make it unmowable. When we have to mow wet grass after rain, this is the method:</p>
<ul>
<li><strong>Wait for the middle of the day.</strong> Even two hours of sun and breeze after a shower dries the leaf enough to make a real difference.</li>
<li><strong>Sharpen the blade first.</strong> Non-negotiable. It is the single biggest factor in cut quality on damp grass.</li>
<li><strong>Raise the cutting height.</strong> Take the top off now and come back for the proper cut when it dries.</li>
<li><strong>Cut in half-width passes.</strong> Overlapping by half the deck reduces clogging and leaves fewer clumps.</li>
<li><strong>Catch rather than mulch.</strong> When you mow wet grass the clippings do not spread evenly. Bag them, or rake and blow the clumps off afterwards.</li>
<li><strong>Stay off the slopes and dam banks.</strong> On acreage around Kilcoy, Esk and Toogoolawah the banks can wait a few days; the flat paddock cannot.</li>
<li><strong>Clean the deck afterwards.</strong> Grass packed under the deck after you mow wet grass rusts steel and throws the blade off balance.</li>
</ul>

<h2 id="season">How do professionals keep lawns under control in a Moreton Bay wet season?</h2>
<p>The trick is not to mow wet grass in the rain. It is to never be more than one cut behind when the rain comes. Through summer our regular rounds in Caboolture, Morayfield, Burpengary and North Lakes run fortnightly or weekly, so a lawn that misses a visit because of a week of storms is only a few days overdue, not a month. That is a light, high cut on the first dry morning rather than a knockdown.</p>
<p>We also move the round around the weather. Acreage and open paddocks that dry quickly are mowed first after rain; shaded suburban back yards that hold moisture are mowed last. If we would have to mow wet grass that squelches underfoot, the job is rescheduled rather than done badly. Our clients would rather have a two-day delay than ruts across the front lawn.</p>

<h2 id="after">What should you do with a lawn after weeks of rain?</h2>
<p>Once it dries out, a lawn that has been through a wet fortnight usually needs three things. First, a staged cut: high, then normal, a few days apart; resist the urge to mow wet grass twice in a week to catch up. Second, a check for fungal disease, which shows as circular brown or straw-coloured patches; it often clears once airflow improves and the lawn is cut, but persistent patches may need a fungicide. Third, a light feed once growth resumes, because heavy rain leaches nitrogen out of sandy coastal soils around Redcliffe and Bribie faster than the clay soils inland.</p>
<p>If weeds have exploded in the wet, that is a separate job. Our guide to <a href="/blog/get-rid-of-lawn-weeds-queensland/">getting rid of weeds in a Queensland lawn</a> covers bindii, nutgrass and clover, and our <a href="/garden-cleanup-moreton-bay/">weed control service</a> handles it for you.</p>

<h2 id="takeaways">Key takeaways</h2>
<ul><li><strong>You can mow wet grass, but you usually shouldn't:</strong> torn leaf, clumping, rutting and disease are the price.</li><li><strong>Damp is different from wet:</strong> firm ground, a sharp blade and a raised deck make a light cut acceptable.</li></ul>
''',
    faqs=[
        ("Is it bad to mow the lawn when it is wet?", "<p>It is usually bad to mow wet grass: you get a torn, uneven cut, leaves clumps of clippings that smother the lawn, can rut soft ground and spreads fungal disease. If the ground is firm and the grass is only damp rather than soaked, a slow, high cut with a sharp blade is acceptable. If the soil squelches, wait.</p>"),
        ("How long after rain can you mow the lawn?", "<p>In Moreton Bay's summer heat a lawn is often mowable four to six hours after a shower and by the next morning after heavy overnight rain, provided the ground is firm. Shaded, clay or low-lying lawns can take two or three days. Test the soil with your foot rather than the calendar.</p>"),
        ("Can you mow wet grass with a ride-on mower?", "<p>A ride-on is heavier than a push mower, so it ruts and compacts wet ground more easily and can slide on damp slopes. On open, firm acreage a high cut is usually fine once surface water has gone. Avoid dam banks, gullies and anything steep until they dry, and clean packed grass out of the deck afterwards.</p>"),
        ("Why does my lawn go brown after mowing in the wet?", "<p>Because you chose to mow wet grass and the wet leaf was torn rather than cut, and the damaged tips dry out and brown within a day. A blunt blade makes it much worse. It is cosmetic and grows out with the next cut, but repeated wet mowing weakens the lawn and invites disease. Sharpen the blade and raise the deck before mowing damp grass.</p>"),
        ("Do you still mow in wet weather in Moreton Bay?", "<p>Green Estates Gardening will mow wet grass that is merely damp when the ground is firm, and reschedules when it is not. Because our regular rounds across Caboolture, Morayfield, North Lakes, Wamuran and the Somerset region are fortnightly or weekly through summer, a rained-out visit only puts a lawn a few days behind rather than weeks.</p>"),
    ],
    cta_heading="Never more than one cut behind",
    cta_text="A regular Green Estates mowing round through storm season keeps Moreton Bay and Somerset lawns short enough that nobody has to mow wet grass in a hurry: a wet week is a delay, not a disaster. Fixed price per visit, rescheduled around the weather.",
),
# ---------------------------------------------------------------- 4
dict(
    slug="what-time-can-you-mow-lawn-qld", date="2026-09-26", short="Mowing hours in QLD", category="lawn",
    image="walkway-mowing-edging",
    alt="Neatly mown lawn and edged footpath in a quiet Moreton Bay street in the early morning mowing hours",
    title="What Time Can You Start Mowing in Queensland? Mowing Hours Explained",
    h1="What Time Can You Start Mowing in Queensland? Mowing Hours Explained", h1_plain="What Time Can You Start Mowing in Queensland? Mowing Hours Explained",
    meta_title="QLD Mowing Hours: What Time Can You Start? | Green Estates",
    description="Queensland mowing hours: 7am weekdays and Saturdays, 8am Sundays and public holidays, finished by 7pm. What time you can start mowing, plus etiquette.",
    keyword="mowing hours",
    excerpt="7am weekdays and Saturdays, 8am Sundays and public holidays, and finished by 7pm. The rules, the etiquette and the best time to mow in summer.",
    lead="Asking what time can you start mowing is the most searched lawn question in Queensland every December and January, usually by someone lying in bed listening to a neighbour's two-stroke. The mowing hours are simpler than most people think. Here is what the Queensland regulations say, what counts as a regulated device, and the best time to mow in Moreton Bay's summer heat.",
    quick="Queensland mowing hours: you can start mowing at 7am on weekdays and Saturdays and at 8am on Sundays and public holidays, and you must finish by 7pm on any day. The same hours apply to line trimmers, blowers and other powered garden tools under the state's noise rules for regulated devices.",
    body=f'''
<h2 id="rules">What are the legal mowing hours in Queensland?</h2>
<p>Queensland's noise rules treat lawn mowers, line trimmers, leaf blowers, chainsaws and similar powered garden tools as regulated devices under the Environmental Protection Act. Used at home, they must not be operated outside these hours:</p>
<div class="tbl-wrap"><table>
<thead><tr><th>Day</th><th>Earliest start</th><th>Latest finish</th></tr></thead>
<tbody>
<tr><td>Monday to Friday</td><td>7:00am</td><td>7:00pm</td></tr>
<tr><td>Saturday</td><td>7:00am</td><td>7:00pm</td></tr>
<tr><td>Sunday and public holidays</td><td>8:00am</td><td>7:00pm</td></tr>
</tbody></table></div>
<p>These are state-wide defaults, so they apply the same in Caboolture, Redcliffe, Kilcoy and Esk. Local councils, including Moreton Bay City Council and Somerset Regional Council, enforce them and can issue directions or fines for repeated breaches. The Queensland Government publishes the current rules on its <a href="https://www.qld.gov.au/environment/pollution/pollution-management/noise" rel="noopener" target="_blank">noise pollution pages</a>; check there if you are in a body corporate or a rural zone, because by-laws can be stricter but never more lenient.</p>
{callout("<strong>The one people miss:</strong> the 7pm cut-off. A quick mow after work at 7:15pm in daylight saving-free Queensland is technically outside the hours, even though it is still light. Most complaints we hear about are evening ones, not early-morning ones.", "clock")}

<h2 id="devices">Which garden tools are covered by the mowing hours?</h2>
<p>The rules cover the whole kit, not just the mower: petrol and electric mowers, ride-ons, line trimmers, edgers, hedge trimmers, chainsaws, leaf blowers, mulchers and pressure washers. Battery tools are quieter but are still regulated devices, so the hours apply. Hand tools such as shears and rakes are not covered, which is why we sometimes do the quiet jobs on a property first if we arrive early.</p>

<h2 id="pro">Do professional lawn mowing businesses follow the same mowing hours?</h2>
<p>Yes. Commercial operators working on residential properties are bound by the same regulated device hours, and a reputable business plans its rounds around them. At Green Estates we do not start a mower before 7am on any residential job, even on acreage in Wamuran where the nearest neighbour is a paddock away, and we schedule Sunday work rarely and never before 8am. Our published hours are Monday to Saturday, 7am to 4pm, which sits comfortably inside the legal mowing hours and inside the cooler part of the day.</p>
<p>Commercial and industrial sites can be different. Business parks in North Lakes and Strathpine often ask for mowing before staff arrive, and the mowing hours for commercial premises are assessed differently from residential noise. If you manage a site with early access, ask; we can usually work with it.</p>

<h2 id="best">What are the best mowing hours in Moreton Bay's summer?</h2>
<p>Legal and ideal mowing hours are not the same thing. For the health of the grass and the person pushing the mower, the best windows in a South-East Queensland summer are:</p>
<ul>
<li><strong>8am to 10am.</strong> Dew has usually lifted, the temperature is still under 30 degrees and the grass is not heat-stressed. This is when most of our residential round runs.</li>
<li><strong>4pm to 6pm.</strong> The heat has broken, the lawn has the evening to recover, and you are still an hour inside the 7pm cut-off. Avoid this window if storms are forecast, because you will be mowing wet grass tomorrow anyway.</li>
</ul>
<p>Avoid midday in January and February. Cutting grass at 35 degrees stresses the plant, the clippings dry into hay before you can catch them, and it is genuinely dangerous work in the humidity. It is also when neighbours with young children are least tolerant of engine noise.</p>

<h2 id="etiquette">What is reasonable mowing etiquette, beyond the law?</h2>
<p>The mowing hours set the outer limits; being a good neighbour in a Moreton Bay estate is a little tighter. A few habits that keep the peace in Narangba, Burpengary and North Lakes streets where houses are close together:</p>
<ul>
<li>Save the earliest weekday starts for open acreage, not a townhouse block.</li>
<li>Keep Sunday mowing to late morning, and skip it entirely on public holidays if you can.</li>
<li>Do the blower last and keep it short; it is the tool that generates the most complaints per minute of use.</li>
<li>If you share a fence with shift workers or a newborn, a quick text before a big cleanup goes a long way.</li>
<li>Maintain the mower. A well-tuned four-stroke with a clean muffler is noticeably quieter than a neglected one.</li>
</ul>

<h2 id="complaints">What can you do about a neighbour mowing outside the hours?</h2>
<p>Start with a conversation; most people genuinely do not know the Sunday mowing hours start at 8am, not 7am. If it continues, keep a simple diary of dates and times and contact your local council. Moreton Bay City Council and Somerset Regional Council handle residential noise complaints about regulated devices and can issue a direction notice. Police are only involved where noise is part of a wider disturbance. Hiring a regular <a href="/lawn-mowing-moreton-bay/">lawn mowing service</a> that works inside the mowing hours and does the whole street on one visit also, quietly, solves it for everyone.</p>

<h2 id="takeaways">Key takeaways</h2>
<ul><li><strong>Queensland mowing hours:</strong> 7am to 7pm Monday to Saturday, 8am to 7pm Sundays and public holidays.</li><li><strong>Every powered tool is covered,</strong> including blowers, trimmers and battery gear.</li></ul>
''',
    faqs=[
        ("Can you mow your lawn on a Sunday in Queensland?", "<p>Yes. Queensland mowing hours on a Sunday are 8am to 7pm. The same 8am start applies to public holidays. Weekdays and Saturdays allow a 7am start. These hours cover mowers, line trimmers, blowers and other powered garden tools, and apply across Moreton Bay and the Somerset region.</p>"),
        ("What time can you use a leaf blower in Queensland?", "<p>The same mowing hours as a lawn mower: from 7am on weekdays and Saturdays, from 8am on Sundays and public holidays, and never after 7pm. Leaf blowers are regulated devices under Queensland's noise rules. Because they attract the most complaints, keep blower use short and do it last.</p>"),
        ("Is 7am too early to mow the lawn?", "<p>It is inside the legal mowing hours on weekdays and Saturdays in Queensland, but on a close-packed suburban street it is on the early side. Professional operators such as Green Estates Gardening typically run residential rounds in Moreton Bay from around 7:30am to 8am onwards, and save the 7am starts for open acreage where nobody is affected.</p>"),
        ("What are the fines for mowing outside the allowed hours in QLD?", "<p>Councils can issue a direction notice for noise from a regulated device outside the permitted mowing hours, and on-the-spot fines can follow if the direction is ignored. In practice, a first complaint almost always results in a warning. Repeated breaches, particularly early Sunday starts, are what lead to penalties.</p>"),
        ("What hours does Green Estates Gardening work?", "<p>Monday to Saturday, 7am to 4pm, across Moreton Bay and Somerset, well inside Queensland's mowing hours. We do not start powered equipment before 7am on residential properties, we rarely work Sundays, and we plan rounds so the noisiest part of a visit falls in the mid-morning window when it bothers the fewest people.</p>"),
    ],
    cta_heading="Mowed inside the mowing hours, on a day you don't have to think about",
    cta_text="Our fortnightly and monthly rounds across Moreton Bay and Somerset run 7am to 4pm, Monday to Saturday, well inside Queensland's noise hours. Fixed price per visit, and you never have to be home.",
),
# ---------------------------------------------------------------- 5
dict(
    slug="ride-on-vs-push-mowing", date="2026-09-10", short="Ride-on vs push", category="lawn",
    image="ride-on-mowing-acreage-moreton-bay",
    alt="Zero-turn ride-on mower on Moreton Bay acreage next to a push mower, comparing ride on vs push mowing",
    title="Ride-On vs Push Mowing: Which Does Your Moreton Bay Block Need?",
    h1="Ride-On vs Push Mowing: Which Does Your Moreton Bay Block Need?", h1_plain="Ride-On vs Push Mowing: Which Does Your Moreton Bay Block Need?",
    meta_title="Ride-On vs Push Mowing: Which Do You Need? | Green Estates",
    description="Ride-on vs push mowing for Moreton Bay blocks: the size cut-off, slopes, finish quality, mulching vs catching, and why most properties get both.",
    keyword="ride-on vs push mowing",
    excerpt="The block-size cut-off, what each machine does to the finish, mulching versus catching, and why most properties get both on one visit.",
    lead="The ride-on vs push mowing decision comes up on almost every acreage quote we do, and on plenty of larger suburban blocks in Burpengary and Narangba too. Each machine does one job brilliantly and the other badly. This guide covers the block-size cut-off, what each does to the finish, the mulching versus catching question, and why most Moreton Bay properties end up getting both on the same visit.",
    quick="Ride-on vs push mowing comes down to block size and shape. As a rule, blocks under about 800 square metres with beds, paths and a pool fence are better push-mowed, while open blocks above that and anything called acreage are ride-on territory. Most Moreton Bay properties get both on one visit: a zero-turn for the open ground and a push mower for the tight areas around the house.",
    body=f'''
<h2 id="cutoff">Ride-on vs push mowing: at what block size does a ride-on make sense?</h2>
<p>Around 800 to 1,000 square metres of actual lawn is the point where a ride-on starts to save real time, provided the shape is open. Below that, the time spent turning, backing out of corners and swapping to a push mower for the edges cancels the speed advantage. Above about 2,500 square metres, which is where lifestyle blocks around Wamuran, Elimbah, Bracalba and D'Aguilar begin, push mowing stops being practical at all.</p>
<p>Shape matters as much as area in the ride-on vs push mowing decision. A long, narrow 1,200 square metre block in Morayfield with a house in the middle, two garden beds and a clothesline may be quicker with a wide push mower than with a ride-on that has to three-point-turn at every obstacle. A square 900 square metre back paddock in Woodford with nothing in it is ride-on work all day.</p>

<h2 id="compare">Ride-on vs push mowing: how do they compare?</h2>
<div class="tbl-wrap"><table>
<thead><tr><th></th><th>Ride-on / zero-turn</th><th>Push mower</th></tr></thead>
<tbody>
<tr><td>Best for</td><td>Open blocks over ~800 m², acreage, paddocks, dam surrounds</td><td>Standard suburban lawns, tight spaces, soft buffalo</td></tr>
<tr><td>Speed</td><td>Very fast on open ground</td><td>Slow on area, fast around obstacles</td></tr>
<tr><td>Finish</td><td>Even, striped, mulched</td><td>Neatest in tight spaces, catches clippings</td></tr>
<tr><td>Slopes</td><td>Gentle to moderate; risky when steep or wet</td><td>Handles steeper banks safely</td></tr>
<tr><td>Soft ground</td><td>Ruts and compacts when wet</td><td>Light footprint</td></tr>
<tr><td>Clippings</td><td>Usually mulched back in</td><td>Caught and removed, or mulched</td></tr>
<tr><td>Access</td><td>Needs a wide gate (1.2 m+)</td><td>Fits any side gate</td></tr>
</tbody></table></div>
<p>That is ride-on vs push mowing in one table; the detail behind each row is below.</p>

<h2 id="finish">Ride-on vs push mowing: which gives the better finish?</h2>
<p>On open ground, a commercial zero-turn gives the better finish: a wide deck at a constant height, no wheel marks from repeated turns, and the classic striped look on couch and kikuyu. Around buildings, beds and fences, a push mower wins because it gets closer, turns tighter and does not scalp the crowns of small humps. That is why a professionally mowed property rarely looks like it was done with one machine. The ride-on does 90 percent of the area in 40 percent of the time; the push mower and line trimmer make it look finished.</p>
{callout("<strong>Soft buffalo lawns:</strong> a heavy ride-on can bruise and rut a lush Sir Walter lawn in a wet summer, especially on the same turning points each visit. For premium residential lawns in North Lakes and Redcliffe we push-mow even when a ride-on would fit; ride-on vs push mowing is settled by the turf, not the area.")}

<h2 id="mulch">Should you mulch or catch the clippings?</h2>
<p>This is the second half of the ride-on vs push mowing question, because ride-ons mulch by default and push mowers usually catch. Mulching chops clippings finely and drops them back into the lawn, where they break down within days and return nitrogen and moisture. On acreage it is the only sensible option: nobody is carting away a trailer of clippings from two acres every fortnight.</p>
<p>Catching makes sense when the grass is long and the clippings would clump, when the lawn borders a pool or entertaining area that has to stay clean, or when weeds are seeding and you do not want the seed spread. On regular residential rounds we generally catch; on acreage we generally mulch; and on the first cut of an overgrown block we catch or rake regardless, because a mat of long wet clippings will kill what is underneath. That is why ride-on vs push mowing usually means mulch on acreage and catch in suburbia.</p>

<h2 id="acreage">What does professional acreage mowing involve that a domestic ride-on does not?</h2>
<p>The difference between a domestic ride-on from the hardware store and a commercial zero-turn is not comfort, it is capability. A commercial machine has a fabricated deck that cuts thick, wet kikuyu without bogging, blades that stay sharp for a full round, and the power to run at a consistent height across uneven paddocks. It also turns on the spot, so trees, fence posts and dam edges get mowed to the edge rather than left as islands for the line trimmer.</p>
<p>Just as importantly, a professional brings the second machine. Every acreage visit from Green Estates includes a push mower and line trimmer for the house surrounds, sheds, tank stands and gardens, so the whole block is finished, not just the paddock. For most clients the ride-on vs push mowing question ends there: a professional brings both. See what is included on our <a href="/acreage-mowing-moreton-bay/">acreage and ride-on mowing</a> page.</p>

<h2 id="buy">Ride-on vs push mowing for owners: should you buy a ride-on?</h2>
<p>If you have more than an acre of open lawn, mow it yourself fortnightly through summer, and have a shed to keep it in, a good ride-on earns its keep. If you have a lifestyle block you bought for the lifestyle, the ride-on vs push mowing maths changes: be honest about how many Saturdays you want to spend on it. A quality zero-turn is a significant purchase, needs servicing, blade sharpening and a trailer to get it repaired, and still leaves you with the edges, the slopes and the tip run. For most owners in the Somerset region and the Wamuran acreage belt, a fixed-price fortnightly round costs less than the machine over its life and gets the whole block done, every time.</p>

<h2 id="takeaways">Key takeaways</h2>
<ul><li><strong>Ride-on vs push mowing by size:</strong> under 800 m² push, over 2,500 m² ride-on, in between it depends on shape and access.</li><li><strong>Finish:</strong> ride-on wins on open ground, push mower wins around the house.</li><li><strong>Ride-on vs push mowing on slopes and soft ground:</strong> the push mower wins.</li><li><strong>Most properties get both</strong> on one visit, which is how professional acreage mowing works.</li></ul>
''',
    faqs=[
        ("Is a ride-on mower worth it for a 1,000 square metre block?", "<p>Only if the block is open and you can get the machine through the gate; the ride-on vs push mowing cut-off is really about shape at this size. On a 1,000 square metre suburban block with beds, paths and a pool fence, a wide push mower is often as quick and leaves a neater finish. Ride-ons pay off clearly from about 2,500 square metres, which is typical lifestyle-block size around Wamuran and Woodford.</p>"),
        ("Can a ride-on mower be used on slopes?", "<p>Ride-on vs push mowing on slopes favours the push mower. Zero-turn and ride-on mowers handle gentle to moderate slopes when the ground is dry, and should be driven up and down rather than across steep ground. Very steep banks, dam edges and anything wet or boggy are safer with a push mower or line trimmer. This is why professional acreage mowing in the Somerset region uses both.</p>"),
        ("Is mulching better than catching grass clippings?", "<p>Mulching is the other half of ride-on vs push mowing. For a healthy lawn on a regular schedule, yes: mulched clippings return nitrogen and moisture to the soil and save carting green waste. Catching is better when the grass is long, when weeds are seeding, or around pools and paved entertaining areas where clippings make a mess. Most Moreton Bay lawns get mulched on acreage and caught in suburbia.</p>"),
        ("What size mower do you use for acreage mowing in Moreton Bay?", "<p>Green Estates Gardening runs commercial zero-turn mowers for open ground on lifestyle blocks, paddocks and large yards from Wamuran and Elimbah out to Kilcoy and Esk, and settles ride-on vs push mowing by bringing a push mower and line trimmer on every visit for the areas around the house, sheds and gardens. The block is quoted as one fixed price per cut.</p>"),
        ("Do I need a ride-on or push mower for a new estate lawn in North Lakes?", "<p>Ride-on vs push mowing for a new estate lawn is an easy call: a push mower. New estate lawns in North Lakes, Narangba and Burpengary are typically 300 to 600 square metres of soft buffalo with paths, beds and a small back yard. A ride-on would not fit through the gate and would rut the young turf. A fortnightly push-mow with edging is the right service for these blocks.</p>"),
    ],
    cta_heading="Not sure which your block needs? Describe it and we'll bring the right gear",
    cta_text="Tell us the address, rough size and access, and Green Estates will settle ride-on vs push mowing for you and quote acreage, ride-on or push mowing across Moreton Bay and Somerset as one fixed price per visit.",
),
]
