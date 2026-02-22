# 🗺️ Page Flow & Logic

## 1. HOME PAGE (The Factory)
Goal: Sell the "Website as a Service (Subscription)" concept to local businesses.

### Block 1: Hero Section
* **Visual:** Deep Space background with Purple/Blue radial glow + subtle grid overlay (`.hero-bg`). Full viewport height.
* **Content:**
    * *Tech Label:* `SYSTEM_ONLINE // V.1.0`
    * *H1:* "Your Business. Our IT Engine."
    * *Subheading:* "Development, hosting, and support of premium subscription-based websites. No technical worries — we handle everything."
    * *CTA Primary:* "CALCULATE COST" (Cyber Blue, terminal style).
    * *CTA Secondary:* "VIEW SERVICES" (glass surface, links to `#services`).

### Block 2: Contrast Grid (Problem vs Solution)
Two-column grid of contrast cards (`.contrast-grid` / `.contrast-card`):
* **Left — `CLASSIC_AGENCIES`** (inactive state): Huge one-time invoices, hidden change fees, slow WordPress/builders, owner self-manages hosting.
* **Right — `CODEXDLC_SUBSCRIPTION`** (active state, cyber-blue glow): Comfortable monthly payment, all-inclusive, lightning-fast custom code, 24/7 monitoring and support.

Active card has `border-color: var(--cyber-blue)` and box-shadow glow. List items show `→` arrows in cyber-blue instead of `—` dashes.

### Block 3: Z-Pattern Services (id="services")
Tech Label: `CORE_OFFERINGS`. H2: "What We Do."

Three alternating rows (`.z-row` / `.z-row.reverse`) with text block + visual placeholder:

**01 // WEBSITE AS A SERVICE — "Subscription Websites"**
Text left, visual right. Purple accent on visual.
- Custom design per niche
- SEO optimization from day one
- Domain, hosting, email included
- Unlimited revisions within subscription
- Z-link: `LEARN ABOUT SUBSCRIPTION →`

**02 // AUTOMATION — "Telegram Bots & Automation"**
Visual left (reversed layout), text right. Blue accent on visual.
- FSM-based lead qualification
- Online booking via Telegram Web App
- Real-time admin notifications
- CRM & database integration
- Z-link: `LEARN ABOUT AUTOMATION →`

**03 // PLUG & PLAY — "Prototype in 48 Hours"**
Text left, visual right. Purple accent. Grid of template cards: LILY SALON, DLC MONTAGE, AUTO HUB, BUILDER PRO.
- Beauty Salon / Barbershop
- Construction & Repair
- Auto Service / Local Services
- Customized to your branding
- Z-link: `VIEW PROTOTYPES →`

### Block 4: Bento Grid (Subscription Value)
Tech Label: `SUBSCRIPTION_VALUE`. H2: "What's Included."

12-column bento grid (`.bento-grid`):
* *Card 1 (span-8, 2 rows):* "Custom Development" — layout preview placeholder.
* *Card 2 (span-4):* "SEO & Analytics" — Core Web Vitals 100/100.
* *Card 3 (span-4):* "Domain & Email" — corporate mail included.
* *Card 4 (span-12, row):* "24/7 Tech Support" — pulsing green `UPTIME 99.9%` status dot.

### Block 5: Tech Corner
Tech Label: `UNDER_THE_HOOD`. H2: "Reliable Architecture."

12-column tech bento (`.tech-bento`):
* *Card (span-5):* `SYSTEM_ARCHITECT` — Full-Stack & System Design description. Footer: `DACH_REGION // EST. 2024`.
* *Card (span-7):* `TECH_STACK` — Tech badges (Python, Django, FastAPI, HTMX, Docker, PostgreSQL, Redis, Aiogram, Nginx, CI/CD). Benchmark panel: `<200ms` TTFB, `99.9%` Uptime SLA, `100` Lighthouse Score.

### Block 6: Portfolio Marquee
Infinite horizontal scrolling ticker (`.marquee`) — project names separated by `//`:
`LILY SALON // DLC MONTAGE // BUILDER PRO // AUTO SERVICE HUB`

### Block 7: Final Funnel (Lead Capture)
Tech Label: `EXECUTE_DEPLOYMENT`. H2: "Ready to Automate Leads?"
Glass-surface form panel: terminal email/phone input + full-width primary CTA "INITIATE PROJECT".

---

## 2. SERVICES: AUTOMATION & BOTS
Goal: Sell Telegram bots as virtual employees.

### Block 1: Hero (The 24/7 Employee)
* **Visual:** Interactive phone mockup showing a Telegram bot accepting a request and sending data to CRM.
* **Content:**
    * *H1:* Your business no longer sleeps.
    * *Subheading:* Smart Telegram bots for lead capture, automated booking, and database integration.
    * *CTA Button:* Order Automation ->

### Block 2: Problem vs Solution
* **Manual Labor:** Long WhatsApp chats, lost contacts, no responses on weekends.
* **CodexDLC Automation:** Instant 24/7 response, FSM-based lead warming, automated visit reminders.

### Block 3: Automation Modules (Bento Grid)
* **Lead Gen Module:** Quiz bot for gathering needs.
* **Booking Module:** Telegram Web App (TMA) integration with a calendar.
* **Notification Module:** Real-time admin alerts via Redis.

---

## 3. PORTFOLIO: PROTOTYPES SHOWCASE
Goal: Let the client "touch" the product.

### Block 1: Hero
* **H1:** Business Solutions Showcase.
* **Subheading:** Choose a ready-made architecture. We adapt the design, texts, and launch the system.

### Block 2: Interactive Grid
* **Card 1: Beauty Salon / Barbershop** (LILY Booking Engine).
* **Card 2: Local Services / Repair** (Builder Pro).
