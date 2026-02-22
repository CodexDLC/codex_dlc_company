"""
codex_dlc_company — URL Configuration.

Features auto-included via include().
API via Django Ninja at /api/.
"""

from api.urls import api
from core.sitemaps import SITEMAPS
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from features.main.views.static_pages import LlmsDeView, LlmsEnView, LlmsRuView

# Custom error handlers
handler400 = "features.main.views.errors.bad_request"
handler403 = "features.main.views.errors.permission_denied"
handler404 = "features.main.views.errors.page_not_found"
handler500 = "features.main.views.errors.server_error"

# Technical and non-localized patterns
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/", api.urls),
    path("", include("django_prometheus.urls")),
    # AI-context files — no i18n prefix, accessed directly by LLM crawlers
    path("llms_ru.txt", LlmsRuView, name="llms_ru"),
    path("llms_en.txt", LlmsEnView, name="llms_en"),
    path("llms_de.txt", LlmsDeView, name="llms_de"),
    # Sitemap
    path("sitemap.xml", sitemap, {"sitemaps": SITEMAPS}, name="django.contrib.sitemaps.views.sitemap"),
]

# Localized patterns
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("features.main.urls")),
)

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
