# Green Estates Gardening — Design System (MASTER)

Generated with ui-ux-pro-max (`--design-system --variance 6 --motion 6 --density 4`) and then
constrained by the client's approved brand board. Where the two disagree, the brand board wins on
colour and type; ui-ux-pro-max wins on layout rhythm, motion timing, accessibility rules and the
pre-delivery checklist. SEO strategy doc wins on headings and copy.

## Pattern
Landing pattern: **Hero → Problem → Solution (services) → Social proof → CTA**, with a quote form
above the fold on every page (from ui-ux-pro-max `hero-testimonials-cta`, adapted for a local
service business). Style family: Minimalism & Swiss — spacious, grid-based, geometric sans, high
contrast, sharp type hierarchy. No glassmorphism except the frosted sticky header.

## Colour tokens (brand board — no new hues)
| Token | Hex | Role |
|---|---|---|
| `--c-primary` Deep Lawn Green | `#2D7A1E` | Section backgrounds, headings on light, footer, logo arc match |
| `--c-action` Vibrant Grass Green | `#4CAF28` | Buttons, links, hover, icons, active states, focus rings |
| `--c-accent` Sunburst Gold | `#F5A800` | ONE moment per section: rule, underline, stat, hover glow, stars. Never a background, never body text, never a primary button |
| `--c-dark` Dark Forest | `#1A3C0E` | Dark backgrounds, dark body text |
| `--c-light` Sage White | `#F9FAF7` | Light backgrounds, knockout text on dark |
| `--c-lime` (logo stripe tint) | `#90BA1A` | Gradient / illustration fills derived from the mark only. Never a standalone UI colour |
| Greys `--g-100…--g-600` | `#EEF0EC` `#DDE1DA` `#C5CBC1` `#8A918A` `#5C645B` `#3E463D` | Borders, dividers, muted text, form strokes |

Sampled from the supplied logo file (for reference, not new tokens): wordmark/arc green `#177D0E`,
lime stripe `#90BA1A`, sun gold `#EF9D0E`.

Contrast (WCAG AA, body ≥ 4.5:1): Dark Forest on Sage White 12.9:1 ✓ · Sage White on Deep Lawn
Green 5.6:1 ✓ · Sage White on Dark Forest 12.4:1 ✓ · Dark Forest on Vibrant Grass Green 5.2:1 ✓
(primary button label). Vibrant Grass Green on white 2.9:1 ✗ and Gold on white 1.9:1 ✗ → display
type, icons and fills only.

Gradient allowed: Deep Lawn Green → Vibrant Grass Green only.

Section rhythm: Sage White → Deep Lawn Green → Sage White. Hero is Dark Forest. Never two dark
sections back to back.

## Typography
- Display / H1 / nav / CTA: **Montserrat 800** (wide geometric, same family feel as the wordmark).
  Overrides the Oswald spec on the brand board.
- Body: **Source Sans 3** 300 / 400 / 600. Base 17px desktop, 16px mobile, line-height 1.6.
- Scale (clamp): H1 `clamp(2.25rem, 1.4rem + 3.2vw, 4rem)`, H2 `clamp(1.75rem, 1.2rem + 1.8vw, 2.75rem)`,
  H3 `1.25–1.5rem`, eyebrow `0.8rem` uppercase tracking `.12em`.
- Headings: Deep Lawn Green on light, Sage White on dark. Gold only as an underline rule.

## Spacing (density 4 — marketing, spacious)
`--space-1: 4px` `-2: 8px` `-3: 16px` `-4: 24px` `-5: 32px` `-6: 48px` `-7: 64px` `-8: 96px`
Section padding `clamp(64px, 8vw, 112px)`. Container max 1200px, gutter 16px mobile / 32px desktop.

## Components
- **Buttons**: primary = Vibrant Grass Green fill, Dark Forest label, pill radius 999px, hover
  darkens to Deep Lawn Green with Sage White label + 2px lift. Secondary = transparent, 2px Vibrant
  Grass Green border, label Dark Forest (light bg) or Sage White (dark bg). Min height 48px.
- **Cards**: white, radius 20px, 1px `--g-200` border, hover lift 4px + shadow `0 20px 40px rgba(26,60,14,.12)`.
- **Icon tiles**: 48px, radius 14px, Vibrant Grass Green at 12% background, 22px stroke icon in Vibrant Grass Green.
- **Header**: fixed, transparent over dark hero (Sage White links), frosted `rgba(249,250,247,.88)` +
  blur 14px on scroll with Dark Forest links. Services mega-dropdown with icon tile + name + suburb descriptor.
- **Focus ring**: 3px Vibrant Grass Green outline, offset 3px, everywhere.
- **Stars / rating**: Gold (the section's one gold moment).

## Motion (ui-ux-pro-max GSAP presets, Standard tier)
- Scroll reveal: `opacity 0→1, y 24→0, 0.5s, power2.out, start 'top 85%'`, children stagger 0.08 (max 8).
- Stagger grids: `scale .92→1, y 16→0, 0.4s, back.out(1.4), stagger.each .06 grid:auto`.
- Hero: headline words rise (0.6s expo.out, stagger .06), then subhead/CTA/form (0.5s).
- Counters: count-up on enter, 1.2s power1.out.
- Hover transitions 200–250ms. `prefers-reduced-motion: reduce` → all of the above render final state instantly.
- Never animate width/height; transforms and opacity only. Nothing below the fold is invisible without JS
  (reveal classes are added by JS, so no-JS renders full content).

## Logo usage
- Light sections: supplied logo as-is (`logo-green-estates-gardening.webp`).
- Dark sections: knockout (`logo-green-estates-gardening-knockout.png`) — greens and gold retained,
  stripe gaps + wordmark swapped to Sage White. Generated programmatically from the supplied file; not redrawn.
- Clear space = cap height of "GREEN"; min width 140px; never stretched, recoloured, cropped or rebuilt.

## Anti-patterns (from the brand rules + ui-ux-pro-max)
No emoji icons · no gold or grass-green body text on white · no green→gold gradients · no full-gold
backgrounds · no hover-only interactions · no layout-shifting hovers · no placeholder-only labels ·
no invented reviews or statistics · no tagline.
