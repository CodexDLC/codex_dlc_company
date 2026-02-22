import re

from django.core.cache import cache
from django.utils.translation import get_language

from .models.site_settings import SiteSettings
from .models.static_translation import StaticTranslation


def site_settings(request):
    """Makes site settings globally available in templates."""
    return {"site_settings": SiteSettings.load()}


def path_without_lang(request):
    """Provides current path stripped of language prefix for the language switcher."""
    path = request.path
    # Strip leading language prefix like /de/, /en/, /ru/
    stripped = re.sub(r"^/[a-z]{2}/", "/", path)
    return {"path_without_lang": stripped}


def static_content(request):
    """
    Injects all StaticTranslation keys as a dict into every template context.
    Uses caching to minimize database load.
    """
    lang = get_language()
    cache_key = f"static_content_{lang}"
    content = cache.get(cache_key)

    if content is None:
        try:
            content = {obj.key: obj.text for obj in StaticTranslation.objects.all()}
            # Cache for 1 hour (3600 seconds)
            cache.set(cache_key, content, 3600)
        except Exception:
            # Graceful degradation during migrations or cold start
            content = {}

    return {"content": content}
