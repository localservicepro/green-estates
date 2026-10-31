# Site build overview — Green Estates Gardening

How this website was built, end to end, written so it can be turned into a reusable skill for
building local service business websites. Everything here reflects the code in this repository
as of the last commit on `claude/gallant-archimedes-1gx521`.

Live site: https://www.greenestatesgardening.com.au · Client: Green Estates Gardening Pty Ltd,
Wamuran QLD 4512 · Agency: Local Service Pro.

---

## 1. What the build produces

A fast, static, SEO-first website for a local trade business that replaces an old Wix site.

| Output | Count / result |
|---|---|
| Pages generated | 40 (32 indexable in the sitemap) |
| Service pages | 6 |
| Suburb landing pages | 17 (14 live, 3 built but held back until the service radius is confirmed) |
| Blog articles | 10, AEO-structured, keyword density 1.3–1.5% |
| Lighthouse (mobile and desktop) | 100 / 100 / 100 / 100 on every page type tested |
| axe-core accessibility | 0 violations on every page at desktop and mobile width |
| Runtime dependencies | None. No framework, no CMS, no animation library |
| Form backend | None. The GoHighLevel tracking script captures submissions into the CRM |

---

## 2. Inputs the build needs

Collect these before starting. Items marked "required" block the build.

| Input | Required | Used for |
|---|---|---|
| SEO website strategy doc | Required | Page list, URL slugs, H1s, titles, meta descriptions, keyword map, suburb list, FAQs |
| Brand board | Required | Colours, fonts, logo rules, accent usage |
| Logo file (PNG/WebP with transparency) | Required | Header, footer, favicons, knockout version for dark backgrounds |
| Client photos (Google Drive folder) | Required | All imagery. Real job photos only, no stock |
| Business facts | Required | Legal name, phone, email, suburb/postcode, hours, owner name, years trading, ABN if wanted |
| Google reviews (screenshot or text) | Required | Review cards and rating stats, quoted verbatim |
| CRM tracking script + field keys | Required | Form capture (here: LeadConnector `external-tracking.js`, tracking ID, field names) |
| Facebook / GBP URLs | Optional | `sameAs` in schema, footer and review links |
| Old site URL list (old sitemap) | Required for a rebuild | 301 redirect map so rankings carry over |
| Live domain and which host is primary (`www` or apex) | Required before launch | Canonicals, sitemap, redirect rules |
| Keyword data access (DataForSEO, Ubersuggest) | Required for blog | Topic selection and volumes |
| Data-backed review (optional second pass) | Optional | Re-aiming pages at real search demand after launch |

---

## 3. Architecture

**Static site generator written in plain Python.** Content and templates live in Python modules
under `src/`. `src/build.py` renders every page to `public/` as `dir/index.html` (clean URLs with
trailing slashes) and runs SEO checks on each page. `public/` is the deployable artefact and is
committed, so any static host can serve it.

Why this approach:
- No build step on the host, no framework updates, nothing to break.
- Every page is plain HTML, so content is in the server response for search engines and AI crawlers.
- Shared components are Python functions, so the header, footer, form and schema stay consistent.
- Checks run on every build, so SEO rules are enforced, not remembered.

```
green-estates/
├── src/
│   ├── build.py            # renders all pages, sitemap, robots, manifest; runs per-page checks
│   ├── gesite.py           # SITE constants, services list, suburb lists, icons, components, schema, page shell
│   ├── pages_home.py       # homepage
│   ├── pages_mowing.py     # residential lawn mowing, acreage mowing, garden maintenance
│   ├── pages_services.py   # hedge trimming, garden cleanup, mulching + shared service hero
│   ├── pages_other.py      # about, contact, thank-you, 404
│   ├── blog.py             # blog index, post template, homepage teaser
│   ├── blog_posts_a.py/_b.py  # the 10 articles (content + FAQs + metadata)
│   ├── suburbs.py          # service-areas hub + suburb page template, cluster groups
│   ├── suburbs_data_a.py/_b.py  # suburb page content
│   ├── density.py          # keyword density report for blog posts
│   └── favicons.py         # favicon/apple-touch/manifest icons from the logo
├── scripts/
│   ├── build-images.py     # source photos -> named, sized, compressed WebP
│   ├── browser-check.mjs   # Playwright smoke test (desktop + mobile)
│   └── check-redirects.mjs # verifies every old URL 301s in one hop to a 200
├── assets-src/             # original client photos (source of truth)
├── public/                 # deployable site (HTML, assets, sitemap.xml, robots.txt)
├── design-system/<client>/MASTER.md   # tokens, type, motion, component rules
├── docs/                   # research notes and this overview
├── vercel.json, netlify.toml          # redirects + cache headers
└── .github/workflows/fetch-assets.yml # pulls Drive photos when the sandbox can't reach Drive
```

### Build commands

```bash
pip install pillow fonttools brotli
python3 scripts/build-images.py   # when photos change
python3 src/favicons.py           # when the logo changes
python3 src/build.py              # every content change; prints a check line per page
```

---

## 4. Site map and URL architecture

| URL pattern | Template | Purpose |
|---|---|---|
| `/` | Home | Brand hub. Links authority into service and suburb pages. Not a single-keyword page |
| `/<service>-<region>/` ×6 | Service | One page per service, keyword in slug, H1, title, description and first 100 words |
| `/service-areas/` | Hub | Every suburb page, grouped into 3 clusters, plus plain-text suburbs without pages |
| `/service-areas/<service>-<suburb>/` ×17 | Suburb | Local landing pages with unique local content |
| `/blog/` | Blog index | Articles only, grouped by service category |
| `/blog/<question-slug>/` ×10 | Post | AEO articles answering real search questions |
| `/about/`, `/contact/` | Other | Trust and conversion pages |
| `/thank-you/` | Other | Form redirect target, `noindex`, disallowed in robots.txt |
| `/404.html` | Other | Not-found page |

Rules that came out of this build:
- **One folder per page type.** Suburb pages live under `/service-areas/`, never `/blog/`. The blog is articles only.
- **Split pages by search intent, not by service list.** Residential mowing and acreage mowing are separate pages because they have different buyers, machines and suburbs. Each links to the other once, in context, and no paragraph is shared.
- **Every suburb page links up to its parent service page** and across to 2–3 neighbouring suburbs.
- **Suburbs with no search demand stay as plain text** on the hub until there is demand or unique content.
- **Hold back pages the client hasn't confirmed.** `CONFIRMED_RADIUS = False` in `suburbs.py` builds three outer suburbs but keeps them `noindex` and out of the nav, hub and sitemap.

---

## 5. Page templates

### Homepage (`pages_home.py`)
Hero (eyebrow, H1, lead, CTA buttons, trust strip, quote form on the right) → services grid
(6 cards) → why us (4 features + 4 count-up stats + branded photo) → before/after slider →
3-step process → suburbs we serve → recent work gallery (tiles link to suburb pages) →
Google reviews (4 verbatim cards) → blog teaser (3 latest posts) → FAQ (6) → CTA band.

### Service page (`pages_services.py`, `pages_mowing.py`)
Compact hero with breadcrumbs, H1, lead, CTA, trust strip and the inline quote form (service
preselected) → intro split with a `speakable` summary paragraph and checklist → "what's included"
cards → a differentiator section (types, process, ride-on vs push, who we work for) → gallery
whose tiles link to suburb pages → suburb links for that service → FAQ (4–6, `FAQPage` schema) →
related services → CTA band.

### Suburb page (`suburbs.py` + data modules)
Hero with breadcrumbs (Home › Service Areas › Suburb), suburb-specific H1 and lead, inline form
→ "In short" quick answer → link up to the parent service page → unique local body copy (soil,
grass types, estates, access, who we mow for) → 4 local FAQs → CTA. Sidebar: parent service
first, other services, nearby suburbs, all service areas.

### Service-areas hub (`suburbs.py`)
Intro with a `speakable` summary of the three rounds, map embed, suburb cards grouped into
Northern corridor / Coast and peninsula / Acreage and Somerset, plain-text "also on our rounds"
list, services grid, CTA.

### Blog post (`blog.py`)
Hero with category, H1, lead, byline (named owner), date and reading time → table of contents →
40–60 word quick answer (`speakable`) → body with question-phrased H2s, tables and callouts →
key takeaways → 5 FAQs → CTA → author box. Sidebar: service link and related posts.

### About, contact, thank-you
About: owner story, credentials, who we work with, reviews. Contact: full form, what happens
next, contact list, service areas. Thank-you: confirmation, what happens next, `noindex`.

---

## 6. Shared components (`gesite.py`)

| Component | Notes |
|---|---|
| `SITE` | Name, legal name, primary URL (with `www` if that's the live host), phone, email, address, hours, geo, owner, tracking ID |
| `SERVICES` | One dict per service: slug, card title, descriptor, icon, image, alt, blurb, points. Drives nav, footer, cards and related services |
| `MORETON_BAY`, `SOMERSET` | **The one suburb list.** Used by footer, homepage, service pages and hub. Names with a live page are linked automatically |
| `header()` | Logo (knockout on dark hero, normal when scrolled), Services mega-menu, Areas mega-menu (3 cluster columns), phone, CTA, mobile drawer with accordions |
| `footer()` | Logo, blurb, Facebook, services, company links, NAP, linked suburb list |
| `quote_form()` | CRM-mapped fields, inline validation, honeypot-free, works without JS |
| `quote_modal()` | Pop-up version of the same form, opened by header and hero CTAs, service preselected per page |
| `picture()` | Responsive WebP `<img>` with `srcset` at 400/600/800/1200/1600 and a `sizes` constant |
| `gallery()` | Tiles that can link to a suburb or service page with a caption |
| `faq_section()` | Native `<details>` FAQs, answers in server HTML |
| `schema_graph()` | One JSON-LD `@graph` per page (see section 7) |
| `shell()` | `<head>`: meta, canonical, Open Graph, preloads, inline CSS, JSON-LD, lazy CRM loader; then header, main, footer, modal, `site.js` |

---

## 7. SEO rules enforced

### Per-page checks (run by `build.py` on every build)
- Exactly one H1, containing service + location.
- Title ≤ 60 characters, description ≤ 160, both containing the page keyword.
- Keyword in the first 100 words of body copy.
- At least 650 words on keyword pages (blog posts run 1,600–2,000).
- Every image has alt text. JSON-LD parses. Headings never skip a level.
- No broken internal links across the whole site.

### Structured data
`LocalBusiness` (address, geo, hours, `areaServed` with every suburb, founder, `sameAs`),
`WebSite`, `WebPage` with `speakable`, `BreadcrumbList`, `Service` with an `OfferCatalog` and
page-specific `areaServed`, `FAQPage`, `BlogPosting` (named author, publisher, dates, word
count, section) and `Blog` on the index.

### Linking and architecture
- Nav: Services mega-menu (all services with suburb descriptors) and Areas mega-menu (every live suburb page by cluster).
- Homepage gallery tiles and service-page galleries link to the suburb they show.
- Suburb pages link up to their parent service and across to neighbours.
- Blog posts link to their service page; the homepage shows 3 posts.

### Sitemap, robots, redirects, canonicals
- `sitemap.xml` lists only indexable pages; priority 1.0 home, 0.9 service/suburb, 0.7 other, 0.6 posts.
- `robots.txt` disallows `/thank-you/` and points to the sitemap.
- Every old URL gets an explicit 301 to its new URL in **one hop** (`vercel.json`, `netlify.toml`), verified with `scripts/check-redirects.mjs`.
- Canonical, Open Graph and sitemap URLs use the **exact live host** (`https://www.…`), never a host that redirects.

---

## 8. Blog / AEO method

1. **Pick topics from data, not guesses.** DataForSEO Labs (Australia) and Ubersuggest (location 2036) for question-phrased, low-difficulty queries that map to a service. Record volumes and difficulty in `docs/blog-topic-research.md`.
2. **Structure every post for answer engines:** 40–60 word quick answer at the top marked `speakable`; question-phrased H2s; 5 FAQs with 40–60 word standalone answers and `FAQPage` schema; key takeaways; local specifics (suburbs, grass types, soils, climate, state regulations).
3. **Keyword density 1.3–1.5%**, measured by `src/density.py` over quick answer + body + FAQs + CTA.
4. **Spread publish dates** over the previous three months.
5. **Named author** (the owner) with a bio box, for E-E-A-T.
6. Each post links to its service page and related posts.

---

## 9. Design system

Built with ui-ux-pro-max and then constrained by the brand board. Brand board wins on colour and
type, ui-ux-pro-max on layout rhythm, motion and accessibility, the strategy doc on headings and copy.

| Token | Hex | Rule |
|---|---|---|
| Deep Lawn Green `--c-primary` | `#2D7A1E` | Section backgrounds, headings on light, footer |
| Vibrant Grass Green `--c-action` | `#4CAF28` | Buttons, icons, focus rings. Never body text on white |
| Sunburst Gold `--c-accent` | `#F5A800` | One moment per section only. Never a background or body text |
| Dark Forest `--c-dark` | `#1A3C0E` | Dark backgrounds and body text |
| Dark Forest ink `--c-dark-ink` | `#0F2A08` | Text on Vibrant Green buttons (5.5:1). Dark Forest only reaches 4.4:1 there |
| Sage White `--c-light` | `#F9FAF7` | Light backgrounds, and **all** text on green sections at full strength |

- Fonts: Montserrat (display, 600–800) and Source Sans 3 (body, 300–600), self-hosted.
- Logo used untouched on light backgrounds; a generated knockout version on dark ones.
- Pattern: hero → services → proof → process → areas → work → reviews → FAQ → CTA, with a quote form above the fold on every page.
- Motion: subtle fade-up reveals below the fold only; respects `prefers-reduced-motion`.

---

## 10. Forms and CRM (GoHighLevel / LeadConnector)

- Field names map to CRM contact fields: `full_name`, `phone`, `email`, `property_address`, `property_type` (custom field `{{contact.property_type}}`), `property_size`, `service_needed`, `job_notes`, plus hidden `source_page` (tagged `#popup` for the modal).
- **No endpoint.** The LeadConnector `external-tracking.js` script reads the submit event and creates the contact.
- `site.js` validates, lets the submit event fire so the tracker sees it, stops native navigation, then redirects to `/thank-you/`. Handlers run in the capture phase on `window` so no other script can swallow the event, with a click-hook backup.
- Without JS the form falls back to a GET to `/thank-you/`.
- **No honeypot field.** Browser autofill filled it, which silently blocked real submissions.
- The tracker is loaded lazily: on first tap, key, scroll or field focus, or 6 s after load. A visitor always focuses a field before submitting, so no submission is missed.

---

## 11. Performance rules (Lighthouse 100)

| Rule | Why |
|---|---|
| Inline all CSS into each page at build time | Removes the render-blocking stylesheet request |
| One variable font per family, subset to Latin and trimmed to used weights, preloaded | 5 font downloads (163 KB) became 2 (45 KB) |
| `font-display: optional` + metric-matched Arial fallback faces | No font-swap layout shift. Live desktop CLS went from 0.134 to 0 |
| No animation library | GSAP and ScrollTrigger cost ~115 KB and delayed the hero. Replaced by an IntersectionObserver reveal |
| Never hide above-the-fold content | Hidden-then-revealed hero text was the mobile LCP element |
| Read no layout at start-up | IntersectionObserver's first report decides what is below the fold, so no forced reflow |
| Third-party scripts load on interaction | The CRM tracker was 440 ms of render-blocking |
| Photos: WebP at 400/600/800/1200/1600, quality 56, 0.6 px denoise | Camera noise in grass and foliage was most of the file size. About 40% smaller, not visible |
| Hero photos: quality 50, 1.2 px blur, half-width file on phones | They sit under a 60–94% dark overlay, so the detail is invisible anyway |
| `sizes` constants measured against the real layout | Phones download phone-sized files |
| Logos as small WebP with 1x/2x `srcset`; hidden scrolled-header logo lazy | The PNG logo was 80 KB for a 76 px image |
| Preload the hero image only on pages that show it | Avoids wasted preloads |
| Versioned asset URLs (`?v=<content hash>`) | A deploy is never shadowed by cached files or cached redirects |
| Long-cache headers on `/assets/` | Repeat views are instant |

---

## 12. Accessibility rules (axe 0 violations)

- Body text ≥ 4.5:1. Check button text on the action colour, it often fails by a fraction.
- No translucent light text on coloured sections; use the full-strength light colour.
- White cards inside dark sections keep dark text. Watch inherited `a { color }` rules.
- Links inside text blocks are underlined, not colour-only.
- Footer and mega-menu labels are not `h4`/`h5`; use `h2` for footer headings and plain text for menu labels.
- Data tables have a header for every column; horizontally scrolling wrappers get `tabindex="0"`, `role="region"` and a label.
- All links with the same text go to the same place.
- Modal: focus moves in, Tab is trapped, Escape and backdrop close it, focus returns to the opener.

---

## 13. QA and verification

| Check | Tool | What passes |
|---|---|---|
| SEO rules | `python3 src/build.py` | Every page "OK", no broken internal links |
| Smoke test | `node scripts/browser-check.mjs` | No console errors, no horizontal scroll at 375 px, menus open, form validates and redirects |
| Form regression | Playwright | Redirect on valid submit from every form, with Enter key, with a hostile script cancelling submit, and without JS |
| Pop-up | Playwright | Opens from header and hero, focus trap, closes three ways, redirects on submit |
| Accessibility | axe-core over every sitemap URL at 1350 px and 412 px | 0 violations |
| Performance | Lighthouse 12 against a local **gzip** server, mobile and desktop | 100 on every page type |
| Real-world fonts | Same, with fonts delayed 150 ms | CLS 0. Local servers deliver fonts instantly and hide swap shifts |
| Redirects | `node scripts/check-redirects.mjs <url>` | Every old URL: 301, one hop, destination 200 |
| Visual | Full-page screenshots at desktop and phone | Reviewed by eye before every push |

---

## 14. Deployment

- Host: Vercel (Netlify config also included). Output directory `public/`. No build command needed.
- `vercel.json`: `cleanUrls`, `trailingSlash`, explicit 301s for every old URL, immutable cache on `/assets/`.
- **The apex/`www` redirect belongs in the host's Domains settings, not in `vercel.json`.** A rule in the opposite direction to the dashboard setting creates a redirect loop on every asset (pages still load, so it looks like "images are missing").
- Set `SITE["url"]` to the exact primary host before the launch build.
- After launch: submit the sitemap in Search Console, run the redirect checker against the live domain, and test one real form submission into the CRM.

---

## 15. Problems hit during this build, and the fix for each

| Problem | Cause | Fix now built in |
|---|---|---|
| Photos unreachable from the build sandbox | Google Drive and Wix CDN blocked by the network proxy | GitHub Actions workflow downloads Drive files into `assets-src/` |
| `site.py` broke Python | Shadowed the standard library `site` module | Never name a module `site.py` |
| Form submit did nothing on the live site | Browser autofill filled the hidden honeypot, which silently aborted submit | Honeypot removed; capture-phase submit handler; click-hook backup; no-JS fallback |
| Footer suburb lists inconsistent | Three separate lists in nav, footer and homepage | One list in `gesite.py` drives everything |
| Two pages fighting over one keyword | Homepage and service page both targeted "lawn mowing Moreton Bay" | Homepage became a hub; pages split by intent |
| Suburb pages mixed into the blog | Old Wix URLs were under `/blog/` | Moved to `/service-areas/` with one-hop 301s |
| Accessibility 91 | Button text 4.4:1, faint footer and form hints, heading skips, colour-only links | Rules in section 12 |
| Mobile performance 74 | Render-blocking tracker, GSAP, duplicate font downloads, oversized photos, hidden hero text | Rules in section 11 |
| Desktop dropped to 95 live | Font swap after first paint shifted the hero (CLS 0.134) | `font-display: optional` + metric-matched fallbacks |
| Literal `{SIZES_HERO}` shipped in HTML | Constant name put inside a quoted string in an f-string expression | Pass constants, not strings; build output scanned for leftover braces |
| Images and fonts missing on the live domain | `www`→apex rule in `vercel.json` fought the dashboard's apex→`www` redirect | Domain redirects only in the host dashboard; versioned asset URLs |
| Stale pages after moving URLs | Old HTML files stayed in `public/` | Build prunes any page it didn't generate |

---

## 16. Open items for this client

- Confirm the service radius for Deception Bay, Petrie and Kallangur, then set `CONFIRMED_RADIUS = True`.
- Confirm the full suburb list (including the Somerset towns) with the owner.
- Supply the Google Business Profile link and a higher-resolution logo.
- Test one real form submission end to end into GoHighLevel.
- Merge the open pull request so `main` matches the live site.
- Review moving to a single `/service-areas/` folder in three months once rankings settle (done early at the client's request).

---

## 17. Suggested structure for a reusable skill

A skill built from this should run in phases, each with a clear gate:

1. **Intake** — collect the inputs in section 2; refuse to start without the strategy doc, brand board, logo, photos, business facts and CRM details.
2. **Assets** — pull photos (workaround if the sandbox can't reach Drive), name them semantically, generate WebP sizes, knockout logo and favicons.
3. **Design system** — run ui-ux-pro-max, constrain it to the brand board, write `MASTER.md`, and check every text/background pair for contrast before writing CSS.
4. **Scaffold** — copy this generator structure (`gesite.py` components, `build.py` checks, page modules) and fill `SITE`, `SERVICES` and the suburb list.
5. **Pages** — homepage, service pages (split by intent), about, contact, thank-you, 404; copy follows the strategy doc's locked H1s, titles and descriptions.
6. **Local pages** — service-areas hub plus suburb pages with unique local content, parent and neighbour links; hold back unconfirmed suburbs.
7. **Blog** — keyword research with DataForSEO and Ubersuggest, 10 AEO posts at 1.3–1.5% density, dates spread over three months.
8. **CRM** — field mapping, lazy tracker loader, fail-safe redirect handler, pop-up form.
9. **Performance and accessibility** — apply sections 11 and 12 from the start, not as a fix-up pass.
10. **QA** — run every check in section 13; Lighthouse against a gzip server with delayed fonts; axe across every page.
11. **Launch** — set the primary host, write the redirect map, configure the host, verify redirects live, submit the sitemap, test a real lead.
12. **Report** — plain-English summary of what's built, what's verified and what the client still owes.

Reference files to bundle with the skill: `src/gesite.py` (components and schema), `src/build.py`
(checks), `public/assets/js/site.js` (form, modal, motion), `public/assets/css/site.css`
(design tokens and components), `scripts/build-images.py`, `scripts/check-redirects.mjs`,
`scripts/browser-check.mjs`, and `design-system/green-estates-gardening/MASTER.md` as a worked example.
