# 📐 Layout & Navigation

## 1. Grid System (Bento Box)
The layout uses an asymmetric modular grid (CSS Grid). Each service or feature block is presented as a standalone widget (Bento-box) with a `24px` border-radius.

### Breakpoints
* **Mobile (xs):** `< 640px` — 4 columns, 16px margins.
* **Tablet (sm/md):** 640px - 1024px — 8 columns, 24px margins.
* **Desktop (lg):** 1024px - 1440px — 12 columns, 32px margins.
* **Ultrawide (xl):** `> 1440px` — Max-width container of `1440px` centered.

## 2. Navigation (Floating Dock)
Instead of a traditional top header, a "Floating Dock" is positioned at the bottom of the screen.

* **Position:** `fixed`, `bottom: 24px`, `left: 50%`, `transform: translateX(-50%)`.
* **Visual:** Pill-shape (100px radius), Glassmorphism background, thin semi-transparent border.
* **Items:**
    * Home (CD Logo).
    * Services (Gear Icon).
    * Portfolio (Grid Icon).
    * Contact (Cyber Blue Button).
* **Behavior:** Shrinks or increases transparency on scroll. Highlights on hover.

## 3. Top Bar (Minimalist)
The top area is kept clean for branding and utility. `position: absolute`, full width, `z-index: 10`.
* **Left:** `Codex` + `DLC` (cyber-blue accent) — `Space Grotesk`, 24px, bold.
* **Right (flex row):** Theme toggle button + Language switcher.

## 4. Z-Pattern Layout
Alternating two-column rows for the Services section (Block 3). Each row presents one service.

### Structure
```
.z-section        — wrapper, padding: 96px 0
.z-row            — CSS Grid 1fr / 1fr, gap: 80px, align-items: center
.z-row.reverse    — direction: rtl (swaps columns without reordering DOM)
.z-row.reverse>*  — direction: ltr (restores text/content direction)
.z-text-block     — flex column, gap: 20px (label + h2 + p + list + z-link)
.z-visual         — glassmorphism card, min-height: 340px, overflow: hidden
.z-visual-accent  — absolute overlay: purple or blue glow (pointer-events: none)
```

### Visual Accents
* Default `.z-visual`: purple accent via `var(--glass-glow-purple)`.
* `.z-visual.blue-accent`: swaps to `var(--glass-glow-blue)`.

### Responsive (≤768px)
Both `.z-row` and `.z-row.reverse` collapse to single column (`direction: ltr`, `gap: 40px`).

## 5. Theme Toggle
A terminal-style button in the top bar switches between dark and light CSS bundles.

### HTML
```html
<button class="theme-toggle" onclick="toggleTheme()" id="theme-btn">[ L ]</button>
```
Label shows `[ L ]` when in dark mode (click to go Light), `[ D ]` when in light mode.

### JS Logic
```javascript
var DARK_CSS  = 'src/backend_django/static/css/app.css';
var LIGHT_CSS = 'src/backend_django/static/css/app-light.css';

function applyTheme(theme) {
    document.getElementById('theme-css').href = theme === 'light' ? LIGHT_CSS : DARK_CSS;
    localStorage.setItem('codex-theme', theme);
}
function toggleTheme() { applyTheme(getTheme() === 'dark' ? 'light' : 'dark'); }
```

### Anti-Flash
Inline `<script>` in `<head>` runs before stylesheets render. Reads `localStorage` and sets `data-theme="light"` attribute on `<html>` if needed, so the correct CSS bundle is applied server-side-like, before any repaint.
