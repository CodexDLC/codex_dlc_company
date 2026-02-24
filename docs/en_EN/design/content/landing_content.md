# Version: 1.0 | Language: EN | Mode: research → sales

---

## MODE ARCHITECTURE

# In the SiteConfig model, there is a site_mode field:
# - 'research' → landing collects email/survey, no sales
# - 'sales' → landing sells, buttons lead to pricing and order form

# All buttons and CTAs have TWO text variants.
# Agent DOES NOT change logic — only substitutes the correct variant based on the mode.
# Other blocks (Hero, services, trust) are the same in both modes.

---

## BLOCK 1 — HERO

# Same in both modes

kicker: DIGITAL SOLUTIONS FOR SMALL BUSINESS
title: Your Business. Our IT Engine.
subtitle: Full IT outsourcing for local companies: premium websites, automated client booking, and 24/7 server support. No huge one-time bills — fixed monthly fee, all-inclusive.

# [research]
cta_primary: I want this service
cta_secondary: Take the survey

# [sales]
cta_primary: View pricing
cta_secondary: Get a free consultation

---

## BLOCK 2 — PROBLEM / SOLUTION

# Same in both modes

title: Why Subscription Works Better Than One-Time Orders

col_problem_title: CLASSIC AGENCIES
col_problem_1: Huge one-time checks (often from 3,000 €)
col_problem_2: Every text edit is a separate bill
col_problem_3: Slow WordPress and constant crashes
col_problem_4: Hosting, domain, updates — your headache

col_solution_title: CODEXDLC
col_solution_1: One honest payment per month — no surprises
col_solution_2: Edits included — turnaround depends on complexity, always agreed in advance
col_solution_3: Fast, secure, modern stack
col_solution_4: 100% technical responsibility on us

---

## BLOCK 3 — SERVICES (Z-blocks)

# Same in both modes
# "Learn more" button leads to individual service pages:
# /services/waas/ | /services/automation/ | /services/solutions/

### 01 // WEBSITE AS A SERVICE
label: 01 // WEBSITE AS A SERVICE
title: Your Digital Branch. All-Inclusive.
text: We don't just build a website — we take it for ongoing maintenance. Custom design, corporate email, local SEO, and full GDPR compliance from day one.
feat_1: Design for your niche — no templates
feat_2: Local SEO: your business on the map — customers find you themselves
feat_3: Domain, hosting, and email already included
feat_4: Impressum and GDPR set up from day one

### 02 // AUTOMATION
label: 02 // AUTOMATION
title: Client Booking Without Your Involvement
text: A busy phone and missed inquiries are lost money. Our system accepts bookings 24/7, filters spam, and sends reminders to clients. Your business works even while you sleep.
feat_1: 24/7 online booking — without your involvement
feat_2: Integration with WhatsApp, Telegram, and website
feat_3: Automatic reminders reduce no-shows
feat_4: Instant notifications to you in your preferred messenger

### 03 // INDUSTRY SOLUTIONS
label: 03 // INDUSTRY SOLUTIONS
title: Ready-Made Concepts for Your Niche.
# IMPORTANT: 48 hours = prototype only (clickable, no forms or booking)
# Full launch = 7–14 days after prototype approval
# Agent NEVER confuses these two terms
text: No long-drawn-out IT projects. You choose the direction — we show a clickable prototype of your site in 48 hours. After approval — full launch in 7–14 days.
feat_1: Ready-made solutions for niches: salons, auto services, cafes, masters
feat_2: Your colors, logo, and content from the first demo
feat_3: Prototype can be touched and clicked before payment
feat_4: Full launch after approval — 7–14 days

---

## BLOCK 4 — TRUST / ARCHITECTURE

# Same in both modes

kicker: RELIABLE ARCHITECTURE
title: Security and Speed You Can Feel
text: No heavy builders. Every project is clean custom code: maximum visibility in Google, flawless data protection, and stability at any moment.

metric_1_value: 100% GDPR
metric_1_label: No fear of Abmahnung

metric_2_value: 99.9% Uptime
metric_2_label: Site doesn't go down during peak season

metric_3_value: Max Speed
metric_3_label: Google loves fast sites

metric_4_value: Hosting in Europe
metric_4_label: Highest data protection standard

---

## BLOCK 5 — FINAL CTA

# Two variants — depends on site_mode

kicker: READY TO GET RID OF IT ROUTINE?

# [research]
title: Help Us Become Better
text: We are preparing a service for small businesses in Germany and want to understand what is important to you. Take a short survey — it takes 2 minutes and helps us build a product for your needs.
cta_primary: Take the survey (2 minutes)
cta_secondary: I want to be the first to know about the launch

# [sales]
title: First Prototype — 48 Hours After Request.
text: Focus on your business — we'll handle all the tech. Choose a plan or let's figure out together what your company needs.
cta_primary: View pricing
cta_secondary: Request a consultation

---

## BLOCK 8 — TECH STACK (footer)

# Same in both modes
# Shown last — for technically savvy clients
# Agent DOES NOT touch this block — texts are hardcoded in the template

section_title: Zuverlässige Architektur
section_text: Wir verwenden keine langsamen Baukastensysteme. Jedes Projekt ist ein individueller Stack mit 99,9% Uptime und blitzschnellem Laden.

# Stack badges: Python, Django, FastAPI, HTMX, Docker,
# PostgreSQL, Redis, Aiogram, Nginx, CI/CD
# Metrics: <200ms TTFB | 99.9% Uptime | 100 Lighthouse
# Signature: DACH_REGION // EST. 2024
