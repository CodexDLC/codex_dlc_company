# 📜 Content Rules & Architecture

## 1. General Principles

This document establishes the architectural decisions and content rules for the CodexDLC platform. The Agent (AI assistant) and developers must follow these rules when creating, modifying, or translating content.

## 2. Site Modes

In the `SiteConfig` model, there is a `site_mode` field that determines the current landing page mode:
- **`'research'`**: Research mode. The landing page focuses on collecting email addresses and conducting surveys. No direct sales. CTA elements lead to survey or subscription forms.
- **`'sales'`**: Sales mode. The landing page focuses on direct service sales. CTA elements lead to pricing pages, order forms, or consultation requests.

**Rule for Agent/Developer:**
- All buttons and CTA elements dependent on the mode must have TWO text variants (for `research` and `sales`).
- The logic for switching text by mode is implemented at the template/backend level. The Agent DOES NOT change the logic, only provides the correct text variant.
- Other blocks (Hero, services, trust, Tech Stack) remain the same in both modes unless explicitly stated otherwise.

## 3. Content Constants and Important Notes

- **48 Hours vs Launch Rule:**
    - **48 Hours:** Refers only to the creation of a *clickable prototype* (no forms or booking).
    - **7–14 Days:** Refers to the *full launch* of the site after prototype approval.
    - The Agent/Developer NEVER confuses these two terms in communications and content.

- **§19 UStG (Small Business):**
    - Under prices, where applicable, there should be a footnote about the application of §19 UStG (VAT exemption for small businesses in Germany).

- **eRecht24 (GDPR/Impressum):**
    - All legal texts (Impressum, Datenschutzerklärung) must comply with eRecht24 and GDPR standards.
    - Content emphasizes full GDPR protection from day one.

## 4. Display Logic and Structure

- **Service Page Template:**
    - All service pages (`/services/waas/`, `/services/automation/`, `/services/solutions/`) must follow a unified block structure (Hero, Who It's For, How It Works/What's Included, Pricing, Projects, Final CTA).

- **Bento Logic for Projects (Adaptive Grid):**
    - An adaptive 12-column bento grid is used.
    - `col-span` class logic is calculated via `templatetag bento_span(index, total)`:
        - 1 project → `col-span-12`
        - 2 projects → `col-span-6`
        - 3 projects → first `col-span-6`, others `col-span-3`
        - 4 projects → `col-span-6` each (2x2)
        - 5 projects → first two `col-span-6`, others `col-span-4`
        - 6 projects → `col-span-4` each (3x2 standard)

- **Z-Blocks for Services:**
    - On the homepage, services are presented as Z-blocks, each leading to a separate service page.

## 5. Database (DB) Integration

- **Dynamic Content:**
    - Projects (on service and solution pages) are pulled from the `Project` model in the DB.
    - Pricing (on service pages) is pulled from the corresponding `PricingPlan` model or similar.
    - The Agent/Developer DOES NOT hardcode dynamic content.

- **Static Content:**
    - "How It Works" blocks (on the solutions page) and "TECH STACK" (in the footer) are static and not pulled from the DB. Texts for them are hardcoded in the template.

- **`Project` Model:**
    - Fields for project cards: `name`, `niche`, `city`, `status` (`live` | `taken` | `free`), `preview_url`, `site_url`, `thumbnail`.
    - For filtering projects by automation, the `has_automation = BooleanField` field is used.

## 6. Multilingualism

- **Supported Languages:** DE (German), RU (Russian), EN (English), UA (Ukrainian).
- **Technical Keys:** Keys like `cta_primary`, `feat_1`, `card_name`, etc., remain in English for consistency with code and DB models. Only the values of these keys are translated.
- **Synchronization:** When adding new content or changing existing content, it must be synchronized across all supported languages.

## 7. Rules for the Agent (AI Assistant)

- **Do Not Change Logic:** The Agent does not change the site's logic (e.g., mode switching), only provides content according to the rules.
- **Do Not Hardcode:** The Agent does not hardcode data that should be pulled from the DB.
- **Follow Structure:** The Agent follows the approved block structure and file naming.
- **Clarify:** If information is insufficient or there is uncertainty, the Agent must ask clarifying questions.
