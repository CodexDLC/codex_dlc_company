import re

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
    # Force refresh from DB to fix empty buttons issue
    try:
        content = {obj.key: obj.text for obj in StaticTranslation.objects.all()}
    except Exception:
        content = {}

    return {"content": content}
