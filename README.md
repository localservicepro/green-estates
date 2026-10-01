# Green Estates Gardening — website

Static, dependency-free website for Green Estates Gardening Pty Ltd (Wamuran QLD), built to the
SEO Website Strategy doc and the approved brand board. Replaces the Wix site at
https://greenestatesgardening.com.au (the old Wix site was on the .com).

## Layout

| Path | What |
|---|---|
| `public/` | **Deployable site.** Point any static host (Vercel, Netlify, cPanel, S3) at this folder. |
| `src/build.py` | Generates every page in `public/` from the content modules and runs SEO checks. |
| `src/gesite.py` | Shared components: header, mega-menu, footer, quote form, schema, page shell. |
| `src/pages_*.py` | Page copy, FAQs and metadata. `pages_mowing.py` holds the residential lawn page, the acreage page and the garden maintenance parent (review v2). |
| `src/blog.py`, `src/blog_posts_*.py` | Blog renderer and the ten articles. `src/density.py` reports keyword density. |
| `src/suburbs.py`, `src/suburbs_data_*.py` | Service-areas hub and the 17 suburb landing pages. |
| `scripts/build-images.py` | Turns `assets-src/` photos into named, optimised WebP files. |
| `assets-src/` | Client photos pulled from the shared Google Drive folder (source of truth for imagery). |
| `design-system/green-estates-gardening/MASTER.md` | Brand tokens, type, motion and component rules (ui-ux-pro-max + brand board). |
| `.github/workflows/fetch-assets.yml` | Re-downloads the Drive photos into `assets-src/` (manual trigger). |

## Build

```bash
pip install pillow
python3 scripts/build-images.py   # only needed when photos change
python3 src/favicons.py           # only needed when the logo changes
python3 src/build.py              # writes public/*.html, sitemap.xml, robots.txt, site.webmanifest
```

`build.py` prints a per-page check: one H1, title ≤ 60, description ≤ 160, primary keyword in
title/description/first 100 words, word count, FAQ count, valid JSON-LD, no broken internal links.

## Pages

| URL | Primary keyword |
|---|---|
| `/` | Lawn Mowing & Garden Care Moreton Bay (brand/hub page; natural keyword usage per review v2) |
| `/lawn-mowing-moreton-bay/` | Lawn Mowing Moreton Bay (residential push-mowing rounds) |
| `/acreage-mowing-moreton-bay/` | Acreage Mowing Moreton Bay & Somerset (ride-on, lifestyle blocks) |
| `/garden-maintenance-moreton-bay/` | Garden Maintenance Moreton Bay (light parent for the North Lakes and Redcliffe garden pages) |
| `/hedge-trimming-moreton-bay/` | Hedge Trimming Moreton Bay |
| `/garden-cleanup-moreton-bay/` | Garden Cleanup Moreton Bay |
| `/mulching-services-moreton-bay/` | Mulching Services Moreton Bay |
| `/about/` | Local Gardeners Moreton Bay |
| `/contact/` | Lawn Mowing Quote Moreton Bay |
| `/thank-you/` | noindex, form redirect target |
| `/blog/` + 10 posts | AEO articles (see `docs/blog-topic-research.md`) |
| `/service-areas/` | Hub linking every suburb page |
| `/blog/lawn-mowing-<suburb>/` ×7, `/blog/garden-maintenance-<suburb>/` ×2 | Existing suburb landing pages, URLs preserved per strategy doc |
| `/service-areas/lawn-mowing-<suburb>/` ×8 | New suburb pages. Deception Bay, Petrie and Kallangur are noindexed and unlisted until `CONFIRMED_RADIUS = True` in `src/suburbs.py` |

## Forms / CRM

Every quote form posts field names that map to the GoHighLevel contact fields:
`full_name`, `email`, `phone`, `property_address`, `property_type` (custom field `{{contact.property_type}}`),
`property_size`, `service_needed`, `job_notes` (+ hidden `source_page`). The LeadConnector `external-tracking.js` script in `<head>` captures the
submit event; `site.js` then redirects to `/thank-you/`. There is no server endpoint.

## Local preview

```bash
npx serve public   # or: python3 -m http.server -d public 8080
```

## Redirects

Old Wix URLs had no trailing slash. `vercel.json` and `netlify.toml` carry explicit 301 rules for all 18 old
sitemap URLs plus a `www` to apex redirect. Verify against a preview or the live domain with:

```
node scripts/check-redirects.mjs https://greenestatesgardening.com.au
```
