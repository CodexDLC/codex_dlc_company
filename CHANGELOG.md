# Changelog

All notable changes to the **CodexDLC** project will be documented in this file.

## [0.2.0] - 2026-02-22
### Core Architecture & Dual Mode UI
*   **Architecture:** Streamlined project by removing FastAPI-related documentation and focusing on a robust Django-centric stack.
*   **Dual Mode UI:** Implemented a comprehensive theme system with two modes:
    *   **Dark (High-Tech Gadget):** Neon accents, Glassmorphism, Deep Space aesthetics.
    *   **Light (Premium Studio):** Clean, Mac-style surfaces with adapted color tokens.
*   **CSS Pipeline:** Integrated a custom CSS compiler with support for `compiler_config.json` and recursive `@import` resolution.
*   **Template System:** Reorganized templates into a modular structure:
    *   Added `includes/` for reusable components (Floating Dock, Header, Footer, Meta).
    *   Implemented `Critical CSS` inlining for performance optimization.
    *   Created dedicated views and templates for static pages (Contacts, FAQ, Legal).
*   **Localization (i18n):** 
    *   Configured Gettext for UI strings with full support for DE, EN, and RU.
    *   Integrated `django-modeltranslation` for database-driven content.
    *   Added initial fixtures for static translations.
*   **SEO & AI Optimization:** 
    *   Implemented JSON-LD `LocalBusiness` schema.
    *   Added automated `hreflang` and `canonical` tag generation.
    *   Optimized meta-structure for both human search engines and AI agents.
*   **UX & Reliability:** Created custom error pages (400, 403, 404, 500) and implemented a "no-flash" theme switcher.

## [0.1.0] - 2026-02-22
### Foundation
*   **Added:** Project initialization: `codex_dlc_company`.
*   **Added:** Template snapshot transfer and activation (all modules).
