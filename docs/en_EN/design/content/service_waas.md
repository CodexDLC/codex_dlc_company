# Language: EN | Mode: research → sales (same rules as homepage)

---

## PAGE HERO

kicker: 01 // WEBSITE AS A SERVICE
title: A Website That Works for You. Not the Other Way Around.
text: Forget about huge one-time checks and agencies that disappear after project delivery. We build your site and stay by your side — every month, every year.

---

## WHO IT'S FOR

title: Your Niche — Our Expertise

card_1_title: Beauty Salons and Studios
card_1_text: Online booking, portfolio, price list, and Google Maps — all in one place.

card_2_title: Craftsmen and Handwerker
card_2_text: Business card site with an inquiry form, work examples, and a call button — customers find you themselves.

card_3_title: Cafes, Restaurants, Services
card_3_text: Menu, promotions, table booking, and reviews — your business online 24/7.

---

## WHAT'S INCLUDED

title: Everything You Need — Already Included in the Subscription

feat_1_title: Custom Design
feat_1_text: No templates — only your colors, logo, and style. A website that looks more expensive than it costs.

feat_2_title: Domain, Hosting, and Email
feat_2_text: We buy the domain, set up hosting in Europe, and corporate email. You don't pay separately.

feat_3_title: Local SEO
feat_3_text: We set up Google Business Profile, maps, and meta tags — your business is found in your local area.

feat_4_title: GDPR and Impressum
feat_4_text: Full legal protection from day one. No fear of Abmahnung.

feat_5_title: Edits and Support
feat_5_text: Minor edits — within 48 hours. Complex tasks — according to the agreed timeline. Always in touch.

feat_6_title: 24/7 Monitoring
feat_6_text: We monitor the server around the clock. 99.9% uptime — your site doesn't go down during peak season.

---

## PRICING (Cards)

# Each card: name + 3 key points + price + button
# Button leads to /pricing/ with the full table

card_1_name: Starter
card_1_price: from €59 / mo
card_1_feat_1: Up to 5 pages
card_1_feat_2: Hosting and domain included
card_1_feat_3: GDPR and Impressum
card_1_cta: Learn More

card_2_name: Business
card_2_price: from €119 / mo
card_2_feat_1: Up to 10 pages
card_2_feat_2: Google Business + Local SEO
card_2_feat_3: Online client booking
card_2_cta: Learn More

card_3_name: Premium
card_3_price: from €189 / mo
card_3_feat_1: Up to 20 pages + 2 languages
card_3_feat_2: E-commerce up to 50 products
card_3_feat_3: Online payment (Stripe / PayPal)
card_3_cta: Learn More

card_4_name: Enterprise
card_4_price: from €299 / mo
card_4_feat_1: No page limits
card_4_feat_2: Custom functionality
card_4_feat_3: SLA and priority support
card_4_cta: Discuss Project

---

## PROJECTS BLOCK

# AGENT: Adaptive 12-column bento grid implementation
# Span class logic calculated via templatetag bento_span(index, total):
# 1 project → col-span-12
# 2 projects → col-span-6
# 3 projects → first col-span-6, others col-span-3
# 4 projects → col-span-6 each (2x2)
# 5 projects → first two col-span-6, others col-span-4
# 6 projects → col-span-4 each (3x2 standard)

# Card contains: preview (screenshot or photo), name, niche, link
# All projects are pulled from the Project model in the database — do not hardcode

label: OUR PROJECTS
title: Real Websites. Real Business.

# Current projects in DB:
# 1. Lily Beauty Salon — beauty — lily-salon.de — LIVE
# 2. DLC Montage — construction — prototype — PREVIEW
# Others added via admin panel as they appear

card_cta: View Website

---

## FINAL CTA

# Two variants — depends on site_mode

# [research]
title: Would This Service Be Useful to You?
text: We are studying demand before launch. Take a short survey — 2 minutes, and you help us build the product specifically for your business.
cta_primary: Take the Survey
cta_secondary: I want to be the first to know

# [sales]
title: Ready to Launch Your Website?
text: Prototype in 48 hours after request. Full launch in 7–14 days.
cta_primary: Choose a Plan
cta_secondary: Get a Consultation
