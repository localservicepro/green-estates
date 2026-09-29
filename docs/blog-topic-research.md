# Blog topic research — Green Estates Gardening

Data pulled 29 Sep 2026 via DataForSEO Labs (Google, Australia) and Ubersuggest (Australia, locId 2036).
Keyword difficulty (KD) is DataForSEO's 0–100 scale; SD is Ubersuggest's. Volumes are monthly, Australia-wide.
Question-phrased and answer-engine-friendly queries were preferred over head terms; every topic maps to a service page.

| # | Post (URL) | Primary query | Vol/mo (AU) | KD / SD | Signals |
|---|---|---|---|---|---|
| 1 | /blog/how-often-to-mow-lawn-moreton-bay/ | how often to mow lawn | 210 (DFS + US) | KD 0 / SD 18 | "how often should you mow your lawn" 140; peaks Nov–Mar; #2 FAQ on the old lawn mowing page |
| 2 | /blog/lawn-mowing-cost-moreton-bay/ | lawn mowing cost | 320 | KD 0 / SD 12 | "how much does lawn mowing cost" 260 (SD 11, CPC $5.04); top FAQ across service pages |
| 3 | /blog/can-you-mow-wet-grass/ | can you mow wet grass / mowing wet grass | 1,300 / 590 | KD 0 | Strongly seasonal, 2,400 in Mar 2026; informational, very low competition |
| 4 | /blog/what-time-can-you-mow-lawn-qld/ | what time can you start mowing | 590 | KD 0 | 1,600 in Dec 2025; "what time can i mow my lawn" 590 KD 3; QLD-specific answer wins the snippet |
| 5 | /blog/ride-on-vs-push-mowing/ | ride-on vs push mowing (+ mulching when mowing) | no data / 720 | KD 0 | #1 FAQ on the lawn mowing page; feeds the retargeted acreage page |
| 6 | /blog/best-time-to-trim-hedges-queensland/ | best time to trim hedges (+ how to trim a hedge) | 90 / 210 | KD 0 / SD 18; KD 12 | "when is the best time to trim hedges" 40; AU variant ignored by most competitors |
| 7 | /blog/best-hedge-plants-moreton-bay/ | best hedge plants australia | 320 (best plant for hedge 720) | KD 0 | Commercial-investigation query that pre-qualifies hedge trimming schedules |
| 8 | /blog/when-to-mulch-garden-queensland/ | when to mulch garden (+ how much mulch do I need) | no data / 210 | KD 0 | "best mulch to stop weeds" 170, "does mulch stop weeds" 170, "best mulch for garden" 480 |
| 9 | /blog/get-rid-of-lawn-weeds-queensland/ | how to get rid of weeds (in lawn) | 210 | KD 0 | "how do you kill weeds naturally" 320 KD 2, "does vinegar kill weeds" 720 KD 1, "how to get rid of onion weed" 390 |
| 10 | /blog/overgrown-garden-cleanup-guide/ | overgrown garden | 110 | KD 0 / SD 19 | CPC $6.70; highest-margin job type; supports the cleanup page |

Considered and parked: "tree lopping caboolture" (210/mo, $19 CPC, SD 12) — belongs on the planned /tree-work-moreton-bay/
service page rather than a blog post; "best hedge trimmer" and "how to sharpen hedge clippers" (product intent, not service intent);
"lawn mowing service brisbane" (720, commercial, outside the service area).

## AEO/GEO conventions applied to every post
- 40–60 word "Quick answer" block at the top, marked `speakable` in schema
- Question-phrased H2s that match how the query is spoken
- 5 FAQs per post with 40–60 word standalone answers, `FAQPage` schema, answers in server HTML
- `BlogPosting` schema with named author (Hamish Baggley), publisher, dates, word count and `articleSection`
- Local specificity: suburbs, grass types, soils, climate and Queensland regulations named in body copy
- Internal links: each post → its service page, related posts, contact; homepage teaser → 3 posts; nav + footer → /blog/
