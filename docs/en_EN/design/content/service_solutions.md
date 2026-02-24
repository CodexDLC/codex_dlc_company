# Page: /services/solutions/
# Language: EN | Mode: research → sales (same rules)

# AGENT: cards are pulled from the Project model
# Card status: 'live' | 'taken' | 'free'
# Bento logic: same as on the homepage (bento_span templatetag)

---

## PAGE HERO

kicker: 03 // INDUSTRY SOLUTIONS
title: Ready-Made Concepts for Your Niche.
text: We don't wait for clients to start working — we study niches and create ready-made solutions in advance. Each concept is designed for a specific business. Some have already found their owners. Others are waiting for you.

---

## CARD STATUSES

# AGENT: three visual states for the card

# [live] — real client, website is running
badge: LIVE
badge_color: status-green
show_url: yes
cta: View Website →

# [taken] — concept is taken, client exists
badge: TAKEN
badge_color: electric-purple
show_url: no
cta: Take in Another City →

# [free] — concept is free, looking for an owner
badge: FREE
badge_color: cyber-blue
show_url: yes (link to prototype)
cta: Claim This Concept →

---

## SUBTITLE ABOVE THE GRID

title: Each concept is developed for a niche. If it didn't fit one — it will find another owner.
text: When a concept is taken by a client — it is adapted to their city, colors, and content. A free concept is already ready for launch — all that's left is to add your data.

---

## PROJECTS GRID

# AGENT: adaptive bento grid (bento_span templatetag)
# Card fields from Project model:
# name — concept name
# niche — niche (beauty / construction / auto / cafe / etc)
# city — client's city (if live/taken)
# status — live | taken | free
# preview_url — link to prototype.codexdlc.com/slug/
# site_url — link to live site (only for live)
# thumbnail — preview image

# Current projects:
# 1. Lily Beauty Salon | beauty | Köthen | live | lily-salon.de
# 2. DLC Montage | construction | — | free | prototype.codexdlc.com/dlc-montage/

---

## "HOW IT WORKS" BLOCK

title: From Concept to Live Website — in 7–14 Days

step_1_num: 01
step_1_title: Choose a Concept
step_1_text: View the live prototype right here — click, scroll, check on your phone.

step_2_num: 02
step_2_title: We Add Your Data
step_2_text: Your logo, colors, content, and city. The concept becomes your unique website.

step_3_num: 03
step_3_title: We Launch
step_3_text: Domain, hosting, GDPR — everything is set up. The site lives and works for you.

# AGENT: this block is static, not from the DB

---

## FINAL CTA

# Two variants — depends on site_mode

kicker: DIDN'T FIND YOUR NICHE?

# [research]
title: Tell Us About Your Business — We'll Develop a Concept for You.
text: Take a short survey — we'll study your niche and add a new concept to the catalog. You'll be the first to know when it's ready.
cta_primary: Suggest a Niche
cta_secondary: Take the Survey

# [sales]
title: We'll Develop a Concept Specifically for Your Niche.
text: Prototype in 48 hours. Full launch in 7–14 days.
cta_primary: Discuss Project
cta_secondary: View Pricing
