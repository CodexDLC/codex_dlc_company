# Changelog

All notable changes to the **CodexDLC** project will be documented in this file.

## [0.2.0] - 2026-02-22
### Design System & Frontend Implementation
*   **Dual Mode UI:** Implemented "High-Tech Gadget" (Dark) and "Premium Studio" (Light) themes with a custom CSS compiler and no-flash theme switcher.
*   **Interactive Effects:** 
    *   Added **Hero Torch** effect (mouse-following glow).
    *   Implemented **Z-Row Parallax** for service visual blocks.
    *   Created **Fluid Branding Animation** for the logo (cycling through DLC meanings).
*   **Typography:** Switched to local variable fonts (Inter, Space Grotesk, JetBrains Mono) for better performance and privacy.
*   **Layout:** Implemented Z-Pattern for service sections and Bento Grid for technical specifications.
*   **Components:** Created reusable components: Floating Dock (pill-shape), Glassmorphism cards, and tactile terminal-style buttons.
*   **SEO & AI:** Added JSON-LD structured data, automated hreflang tags, and `llms_*.txt` context files for AI agents.
*   **Performance:** Implemented Critical CSS inlining and font preloading.

## [0.1.5] - 2026-02-22
### Infrastructure & Template Hardening
*   **Docker:** Created `docker-compose.test.yml` and integrated **Mailpit** for local email testing.
*   **Hardening:** Fixed critical bugs in the base template (missing imports, incorrect Docker paths, entrypoint script).
*   **Testing:** Established a dedicated test environment with SQLite in-memory and optimized settings.
*   **QA Tools:** Overhauled `tools/dev/check.py` with dynamic container monitoring and automated linting (Ruff/Mypy).
*   **Migrations:** Initial system migrations for SEO, analytics, and geo-location fields.

## [0.1.0] - 2026-02-22
### Foundation
*   **Added:** Project initialization: `codex_dlc_company`.
*   **Added:** Template snapshot transfer and activation (all modules).
