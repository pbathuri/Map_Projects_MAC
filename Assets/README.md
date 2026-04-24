# Assets

Static imagery used by the [profile README](https://github.com/pbathuri/pbathuri) and per-repo social previews across [@pbathuri](https://github.com/pbathuri)'s portfolio.

Served raw from GitHub via:

```
https://raw.githubusercontent.com/pbathuri/Map_Projects_MAC/main/Assets/<filename>
```

---

## Index

| File | Role | Size | Notes |
|------|------|------|-------|
| `profile-hero.png` | Profile README hero banner | 1584 × 396 | Top of `pbathuri/pbathuri/README.md` |
| `profile-hero.gif` | Animated hero (optional replacement) | 1584 × 396, ≤ 4 MB | Looped phase-transition drawing |
| `research-cluster.png` | Social preview + inline card | 1280 × 640 | `finance-cache-hpc` + research section |
| `portfolio-constellation.png` | Social preview for `Map_Projects_MAC` | 1280 × 640 | - |
| `kory-social.png` | Social preview | 1280 × 640 | `Kory_The_Cat-NCAA` |
| `resumeforge-social.png` | Social preview | 1280 × 640 | `ResumeForge` |
| `claude-hackathon-social.png` | Social preview | 1280 × 640 | `Claude_Hackathon` |
| `entrepreneur-persona-social.png` | Social preview | 1280 × 640 | `entrepreneur-persona-skill` + `-llm` |
| `convo-ai-social.png` | Social preview | 1280 × 640 | `convo-ai` + `-demo` |
| `deskflow-social.png` | Social preview | 1280 × 640 | `deskflow-native` |

---

## Generation source

See [`GIF_PROMPT.md`](GIF_PROMPT.md) for the frame-by-frame prompt used with Gemini Nano Banana to produce `profile-hero.gif`.

Static PNGs were generated from the design brief in the root [`README.md`](../README.md) § **Nano-banana asset list**.

---

## House style - so new assets stay coherent

- **Background**: `#0D1117` (GitHub dark default)
- **Primary accent (finance / research)**: `#FFA657` amber
- **Secondary accent (tech / systems)**: `#58A6FF` electric blue
- **Neutral**: `#8B949E` grey
- **Type - serif (titles)**: Tiempos, Spectral, or equivalent editorial serif
- **Type - sans (metadata)**: Inter, IBM Plex Sans
- **No stock people, no 3D renders, no gradient decoration.** Aesthetic target: *Nature* / *Quanta Magazine* / *Bloomberg Terminal*, not marketing-landing.
- **Safe-zone rule**: keep text > 120 px inset from any edge so GitHub's card-crop doesn't truncate.
