# 🎨 Identity & Style (High-Tech Gadget)

## 1. Color System (Dark Mode First)
The design mimics a premium electronic device interface. Deep dark backgrounds with vibrant neon accents and glassmorphism effects.

### Base Surfaces (Glassmorphism & Depth)
* **Deep Space (Main BG):** `#050505` — Core background for maximum contrast.
* **Glass Panel:** `rgba(255, 255, 255, 0.05)` with `backdrop-filter: blur(12px)` — Background for Bento-boxes and the floating dock.
* **Border Glow:** `rgba(255, 255, 255, 0.1)` — Subtle borders mimicking glowing glass edges.

### Accent Colors (Neon)
* **Cyber Blue (Primary Action):** `#00F0FF` — Main buttons, active states, and primary highlights.
* **Electric Purple (Secondary):** `#8A2BE2` — Icons, background gradients, and depth accents.
* **Status Green:** `#00FF66` — Uptime indicators (99.9%) and success states.

### Typography Colors
* **Primary Text:** `#FFFFFF` — Headings and primary information.
* **Secondary Text:** `#A1A1AA` — Descriptions, subheadings, and helper text.

## 2. Typography Scale
Technical, geometric fonts that balance engineering precision with business readability.

* **Font Families:**
    * **Headings / UI:** `Space Grotesk` (Geometric, modern, structural).
    * **Code / Stats:** `JetBrains Mono` (Monospace for technical data and badges).
    * **Body Text:** `Inter` (Maximum legibility).

* **Scale (Desktop):**
    * **H1 (Hero):** 56px / 64px line-height, Bold (700).
    * **H2 (Section):** 40px / 48px line-height, Semi-Bold (600).
    * **Body Large:** 18px / 28px line-height, Regular (400).
    * **Tech Labels:** 12px, Uppercase, Medium (500), JetBrains Mono.

## 3. Spacing & Geometry
* **Baseline Grid:** 8px (xs: 8px, sm: 16px, md: 24px, lg: 32px, xl: 48px).
* **Border Radius:**
    * **Bento Cards:** `24px` (Soft, premium gadget feel).
    * **Buttons/Inputs:** `0px` (Strict terminal/tactile feel).
    * **Floating Dock:** `100px` (Pill-shape).

---

## 4. Theme System (Dual Mode)

The design system supports two visual modes compiled as separate CSS bundles.

### Dark Theme — "High-Tech Gadget" (default)
The primary brand experience. Deep black background, neon cyan accents, glassmorphism panels.

| Token | Value | Purpose |
|-------|-------|---------|
| `--deep-space` | `#050505` | Page background |
| `--glass-bg` | `rgba(255,255,255,0.07)` | Card/surface background |
| `--glass-bg-elevated` | `rgba(255,255,255,0.10)` | Elevated surfaces, hover |
| `--glass-border` | `rgba(255,255,255,0.12)` | Card borders |
| `--glass-border-hover` | `rgba(0,240,255,0.25)` | Hover border glow |
| `--glow-btn` | dual box-shadow | Button neon glow on hover |
| `--dock-bg` | `rgba(15,15,15,0.88)` | Floating dock background |
| `--glass-glow-blue` | `rgba(0,240,255,0.08)` | Card hover glow |
| `--glass-glow-purple` | `rgba(138,43,226,0.07)` | Hero background depth |

### Light Theme — "Premium Studio"
Clean, airy, Mac-style surfaces. Same geometric structure, shadows replace glow effects.

| Token | Value | Purpose |
|-------|-------|---------|
| `--deep-space` | `#F2F2F7` | Page background (Apple light gray) |
| `--glass-bg` | `rgba(255,255,255,0.72)` | Frosted glass cards |
| `--glass-border` | `rgba(0,0,0,0.08)` | Subtle borders |
| `--dock-bg` | `rgba(255,255,255,0.85)` | White frosted dock |
| `--cyber-blue` | `#00838F` | Adjusted for light readability |
| `--electric-purple` | `#6B21D6` | Adjusted for light readability |
| `--status-green` | `#00964A` | Adjusted for light readability |

### Build Pipeline
```
base.css       → python tools/static/css_compiler.py → app.css       (dark)
base-light.css → python tools/static/css_compiler.py → app-light.css (light)
```

The compiler reads `compiler_config.json` and resolves all `@import` statements.

### Theme Switching (JS)
The active CSS bundle is switched dynamically via `<link id="theme-css">`.

- **Default:** Follows `prefers-color-scheme` system preference
- **Manual override:** Saved to `localStorage` key `codex-theme`
- **Anti-flash:** A small inline script in `<head>` applies the saved theme before render
- **Toggle button:** `[ ◗ ]` (dark) / `[ ☀ ]` (light) — terminal-style, in the top bar
