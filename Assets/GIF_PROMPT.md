# GIF generation prompt — `profile-hero.gif`

Place the resulting file at `Assets/profile-hero.gif`. It replaces (or loops above) the static `profile-hero.png` at the top of `pbathuri/pbathuri/README.md`.

The entire brief below is designed to be pasted verbatim into **Gemini Nano Banana** (or equivalent image-to-video / text-to-video tooling). It's written to be unambiguous about timing, palette, safe-zones, and loop behaviour so a non-artist operator can reproduce the exact asset.

---

## Purpose

This GIF is the first pixel a recruiter, academic, or collaborator sees on the GitHub profile. It has to land the positioning in under 4 seconds without being a stock-animation cliché. The visual argument: *empirical, editorial, quant-research-flavoured, systems-aware, curious* — not marketing.

The motif is a **phase-transition curve drawing itself** over a dark editorial grid, with three annotated data-spikes (`28×`, `1,657×`, `500×`) — the actual headline results from `finance-cache-hpc`. So the banner doubles as a visible research claim.

---

## Technical spec

| Parameter | Value |
|---|---|
| Output | `profile-hero.gif` |
| Dimensions | **1584 × 396 px** (GitHub-optimal wide banner; 4:1 aspect-ish) |
| Duration | **4.0 s total** |
| Frame rate | **24 fps** → 96 frames |
| Loop | **Seamless**. Last frame must blend into first (hold 0.6 s at end, then fade opacity of drawn curve back to 0 over the hold, so the loop restart is imperceptible) |
| File size cap | **≤ 4 MB** (GitHub README inline limit is 10 MB; aim for < 4 for fast first paint) |
| Color profile | sRGB, 8-bit |
| Transparency | No alpha — solid `#0D1117` background |
| Compression | Lossy GIF OK; dithered palette of ≤ 64 colors |

---

## Palette (locked)

| Role | Hex | RGB | Usage |
|---|---|---|---|
| Background | `#0D1117` | 13, 17, 23 | Full canvas fill, no gradient |
| Grid lines | `#161B22` | 22, 27, 34 | Faint graph paper underlay |
| Primary (curve + amber spikes) | `#FFA657` | 255, 166, 87 | The drawing line, the three data-spike glow |
| Secondary (axis labels, callouts) | `#58A6FF` | 88, 166, 255 | Axis tick labels, the "cache boundary" vertical marker |
| Neutral text | `#8B949E` | 139, 148, 158 | Byline text |
| Title text | `#E6EDF3` | 230, 237, 243 | "PRADYOT BATHURI" wordmark |

**No other colours.** No reds, greens, purples, or neon. No gradient fills inside the curve — the curve is a 2px stroke line only.

---

## Composition (safe-zones matter — GitHub crops aggressively on mobile)

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│  [ 144 px safe inset ]                                              [ 144 px safe inset ]  │
│                                                                                             │
│   LEFT HALF (0 – 792 px)                    RIGHT HALF (792 – 1584 px)                     │
│                                                                                             │
│   ┌────────────────────────────┐           PRADYOT BATHURI                                 │
│   │                            │           (serif, 56 pt, #E6EDF3, tracking +20)           │
│   │     Phase-transition       │                                                           │
│   │     curve drawing          │           quantitative research · HPC systems             │
│   │     itself                 │           · shipping LLM tools                            │
│   │                            │           (sans, 22 pt, #8B949E)                          │
│   │     over graph-paper grid  │                                                           │
│   │                            │           ──── small horizontal rule in #FFA657 (120 px)  │
│   │     Y-axis: "speedup ×"    │                                                           │
│   │     X-axis: "problem size" │           IU Bloomington · building empirical tools       │
│   │     (#58A6FF tick labels)  │           (sans, 16 pt, #8B949E)                          │
│   │                            │                                                           │
│   └────────────────────────────┘                                                           │
│                                                                                             │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Title "PRADYOT BATHURI"** — editorial serif (Tiempos / Spectral / EB Garamond — pick closest available). Weight: regular. Size 56 pt. Color `#E6EDF3`. Letter-spacing +20 for the "magazine masthead" feel.
- **Subtitle** — Inter or IBM Plex Sans, regular 22 pt, color `#8B949E`. One line, em-dash separator.
- **Bottom line** — 16 pt, `#8B949E`, lowercase.
- **Horizontal rule** — 120 px wide, 2 px tall, `#FFA657`, anchored below the serif title.

All right-half text is **static** across every frame. Only the left-half curve animates.

---

## Animation timeline (t = time in seconds, beats on 24 fps)

| Window | What happens |
|---|---|
| **0.0 – 0.3 s** (frames 0–7) | Canvas appears. Graph-paper grid (`#161B22` 1px lines every 48 px) fades in from 0 % to 100 % opacity. No curve yet. |
| **0.3 – 0.5 s** (frames 8–12) | Axis tick labels (`#58A6FF`) fade in on left edge and bottom edge. Axis labels "speedup ×" (vertical, rotated 90°) and "problem size" (horizontal) appear in 14 pt `#8B949E`. |
| **0.5 – 2.5 s** (frames 12–60) | **The curve draws itself** left-to-right. A 2 px `#FFA657` stroke moves at non-linear ease-in-out — the flat low-speedup region covers the first 60 % of canvas width slowly, then the curve ramps dramatically into the phase-transition cliff. A 6 px radius glowing dot leads the stroke-head (same `#FFA657`, opacity 60 %, 2 px blur). |
| **1.3 s** mark (frame 31) | As the curve crosses the vertical cache-boundary marker at ~40 % canvas width, a thin 1 px `#58A6FF` dashed vertical line appears from top to bottom, labelled `L1 boundary` in 10 pt `#58A6FF` at the top (callout tucked into the upper-safe-zone). |
| **1.8 – 2.2 s** (frames 43–53) | First data-spike annotation pops in at the top of its peak: small `#FFA657` filled circle (4 px radius) + leader line angling up-right to a text block `28×` in 20 pt sans `#E6EDF3` with a `#FFA657` underline. Scale-from-80%-to-100% bounce ease over 6 frames. |
| **2.2 – 2.6 s** (frames 53–62) | Second annotation: `1,657×` same style, at the phase-transition peak. |
| **2.6 – 3.0 s** (frames 62–72) | Third annotation: `500×` at the third spike. |
| **3.0 – 3.4 s** (frames 72–82) | **Hold.** Full composition static. The leading-dot has parked at the curve's right end and pulses softly (opacity 60 % → 100 % → 60 %, 0.4 s cycle). |
| **3.4 – 4.0 s** (frames 82–95) | **Loop blend.** The drawn curve's opacity fades from 100 % to 0 % over 14 frames (non-linear, ease-out). Annotations fade with it. Grid + axis labels + right-half text STAY at full opacity — only the curve and its annotations disappear. Frame 95 matches frame 0 for seamless loop. |

Timing targets ±1 frame; exact easing is a judgment call but the **cliff must feel sudden** — this is the phase-transition moment and it should visually surprise.

---

## The curve itself — geometry

The curve is **not a smooth sigmoid**. It's deliberately shaped to mirror the real L1-cache empirical result — flat low-speedup region, then a cliff, then three distinct spikes:

Normalized coordinates (x: 0 at left graph edge, 1 at right; y: 0 at baseline, 1 at top):

```
(0.00, 0.05)  → (0.15, 0.06) → (0.30, 0.08)  slow rise
(0.40, 0.10)  → (0.42, 0.38)                 cliff begins (L1 boundary marker at x=0.40)
(0.45, 0.55)  → (0.50, 0.62)                 first spike → 28× label here
(0.55, 0.45)
(0.62, 0.92)  → (0.64, 0.95)                 second spike → 1,657× label here (peak)
(0.70, 0.60)
(0.80, 0.75)  → (0.82, 0.78)                 third spike → 500× label here
(0.90, 0.50)
(1.00, 0.45)
```

Stroke: catmull-rom or cubic-bezier through these points, 2 px thickness, rounded line caps, slight anti-aliasing. **No fill beneath the curve** (it's a plot line, not an area chart).

---

## What NOT to do (guardrails)

- ❌ No particle effects, sparkles, lens flares, or bokeh.
- ❌ No 3D perspective, depth of field, or camera tilt.
- ❌ No colour outside the six-hex palette above.
- ❌ No images of people, faces, hands, screens, or desks.
- ❌ No typography in Comic Sans, Times New Roman, or default Helvetica — must be editorial serif + geometric sans.
- ❌ No background texture beyond the flat grid.
- ❌ No motion blur on the curve — it's a clean plot, not a speed-line.
- ❌ The annotations must not overlap the curve itself — leader lines only.
- ❌ No easing that makes the curve "bounce" on arrival — scientific plots don't bounce.

---

## Delivery

Name the file **exactly** `profile-hero.gif` and place it at `/Assets/profile-hero.gif` in the `Map_Projects_MAC` repo. The profile README references the raw GitHub URL, so the moment the file is committed, the banner goes live.

Also generate the first frame as a standalone `profile-hero.png` (same path, `.png`) — this is the fallback used in dark-mode-unfriendly RSS feeds and when the GIF is still loading. Frame 95 (the grid + text, curve opacity 0) is the correct snapshot because it represents the banner at loop-reset.

---

## If you want to iterate

The single easiest lever is the **cliff steepness** (slope between `x=0.40` and `x=0.45`). Steeper = more dramatic but less readable. If the annotations fight for space, lower the first spike to `y=0.50` and lift the second to `y=0.98` to spread them vertically. Keep the three-annotation structure — it is the narrative.
