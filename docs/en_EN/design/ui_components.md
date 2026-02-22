# 🧩 UI Components & Interaction

## 1. Buttons (Tactile Terminal Style)
Buttons feel like physical hardware triggers or strict console commands. No soft shadows.

* **Primary Action (Cyber Blue):**
    * *Default:* Background `transparent`, Border `1px solid #00F0FF`, Text `#00F0FF`, `0px` border-radius.
    * *Hover:* Background `#00F0FF`, Text `#050505`. Instant transition (`75ms`).
    * *Active:* Background `#00C4D1`, transform `scale(0.98)`.
* **Secondary Action (Surface):**
    * *Default:* Background `rgba(255, 255, 255, 0.05)`, Border `1px solid rgba(255, 255, 255, 0.1)`, Text `#FFFFFF`.
    * *Hover:* Background `rgba(255, 255, 255, 0.1)`, Border `1px solid #A1A1AA`.

## 2. Forms & Inputs (Command Line Aesthetic)
Inputs mimic a command prompt, stripping away standard web form styling.

* **Default Input Field:**
    * Background `transparent`, Border-bottom `1px solid rgba(255, 255, 255, 0.1)` only.
    * Text `#FFFFFF`, Font `JetBrains Mono`.
* **Focus State:**
    * Border-bottom `1px solid #00F0FF`. Caret color `#00F0FF`.
* **Error State:**
    * Border-bottom `1px solid #EF4444`. Validation text in `12px JetBrains Mono`.

## 3. Bento Cards (Glassmorphism)
Used for service modules and feature highlights.

* **Structure (dark theme):**
    * Background: `linear-gradient(135deg, rgba(255,255,255,0.10), rgba(255,255,255,0.07))`.
    * Backdrop-filter: `blur(12px)` via `var(--glass-blur)`.
    * Border: `1px solid rgba(255,255,255,0.12)` via `var(--glass-border)`.
    * Border-radius: `24px` via `var(--radius-bento)`.
    * Inset shadow: `inset 0 1px 0 rgba(255,255,255,0.06)`.
* **Hover Effect:** Border → `var(--glass-border-hover)` = `rgba(0,240,255,0.25)`.

## 4. Status Dot
Pulsing green indicator for uptime / online state.
```css
.status-dot { width: 8px; height: 8px; background: var(--status-green); border-radius: 50%; animation: status-pulse 2s ease-in-out infinite; }
@keyframes status-pulse { 0%,100% { box-shadow: 0 0 4px var(--status-green); } 50% { box-shadow: 0 0 12px var(--status-green), 0 0 24px rgba(0,255,102,0.25); } }
```

## 5. Tech Label
Mono uppercase tag used as section identifier.
* Font: `var(--font-mono)` (JetBrains Mono), `11px`, uppercase, `letter-spacing: 2px`.
* Color: `var(--cyber-blue)`.
* Display: `block`, `margin-bottom: 16px`.

## 6. Z-Visual Block
Glassmorphism placeholder card inside Z-Pattern rows. Contains an absolute accent overlay.

```html
<div class="z-visual blue-accent">
    <div class="z-visual-accent"></div>
    <!-- content at z-index: 1 -->
</div>
```

* `.z-visual` — glass card, `min-height: 340px`, centered flex, mono font.
* `.z-visual-accent` — `position: absolute; inset: 0` — purple or blue glow gradient.
* `.z-visual.blue-accent .z-visual-accent` — overrides to `var(--glass-glow-blue)`.

## 7. Z-Link
Mono arrow link used at the bottom of Z-Pattern text blocks.
```html
<a href="#" class="z-link">LEARN MORE &nbsp;→</a>
```
* No underline. `gap` animates from `8px` to `16px` on hover (`transition: gap 0.2s ease`).
* Color: `var(--cyber-blue)`, size: `12px`, uppercase, mono.

## 8. Tech Badge
Mono pill label for tech stack display.

```html
<span class="tech-badge">Docker</span>
<span class="tech-badge active">Python</span>
```

* Default: `var(--glass-bg)` background, `var(--glass-border)` border, `var(--gray-400)` text.
* `.active`: `border-color: var(--cyber-blue)`, `color: var(--cyber-blue)`.

## 9. Contrast Cards
Used in Block 2 (Problem vs Solution).

```html
<div class="contrast-card">          <!-- inactive -->
<div class="contrast-card active">   <!-- active/solution -->
```

* Default: glass bg, standard border. Hover: `border-color: rgba(138,43,226,0.3)`.
* `.active`: `border-color: var(--cyber-blue)`, `box-shadow: 0 0 32px rgba(0,240,255,0.06)`, gradient background.
* `.contrast-list li::before` — `—` (inactive) vs `→` in cyber-blue (active).

## 10. Marquee
Infinite horizontal ticker for portfolio names.
```html
<div class="marquee">
    <div class="marquee-content">
        <span class="marquee-item">LILY SALON</span>
        <span class="marquee-item">//</span>
        <!-- repeated twice for seamless loop -->
    </div>
</div>
```
Animation: `marquee-scroll 30s linear infinite` — translates `-50%` on X axis.

## 11. Island Footer
Rounded glassmorphism footer block with 24px margin from page edges.
```css
.island-footer { margin: 0 24px 24px; padding: var(--space-2xl); border-radius: 40px; }
```
Bottom row (`.island-footer-bottom`): flex space-between, mono 10px, copyright + version string.
