"""
Sitemaps for CodexDLC.
Generates multilingual XML sitemap via django.contrib.sitemaps.
All pages are wrapped in i18n_patterns, so we generate one entry per (page, language).
"""

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticPageSitemap(Sitemap):
    """Sitemap for static pages (home, contacts, faq, impressum, datenschutz)."""

    protocol = "https"

    # (url_name, priority, changefreq)
    _pages = [
        ("main:index", 1.0, "weekly"),
        ("main:contacts", 0.8, "monthly"),
        ("main:faq", 0.7, "monthly"),
        ("main:impressum", 0.3, "yearly"),
        ("main:datenschutz", 0.3, "yearly"),
    ]

    def items(self):
        """Return list of (lang_code, url_name, priority, changefreq) tuples."""
        result = []
        for lang_code, _ in settings.LANGUAGES:
            for url_name, priority, freq in self._pages:
                result.append((lang_code, url_name, priority, freq))
        return result

    def location(self, item):
        lang_code, url_name, _, _ = item
        return f"/{lang_code}/{self._get_path(url_name)}"

    def priority(self, item):
        return item[2]

    def changefreq(self, item):
        return item[3]

    def _get_path(self, url_name):
        """Return the path segment after the language prefix."""
        full = reverse(url_name)
        # reverse() includes the lang prefix via i18n_patterns when activated;
        # strip leading slash for clean concatenation
        return full.lstrip("/")


SITEMAPS = {
    "static": StaticPageSitemap,
}
