from .models.site_settings import SiteSettings
from .models.static_translation import StaticTranslation


def site_settings(request):
    """Makes site settings globally available in templates."""
    return {"site_settings": SiteSettings.load()}


def static_content(request):
    """
    Injects all StaticTranslation keys as a dict into every template context.
    Access via {{ content.home_hero_title }} — returns the language-aware `text` field
    resolved by modeltranslation (text_ru / text_en / text_de based on active language).
    Falls back to empty string when key is missing.
    """
    try:
        content = {obj.key: obj.text for obj in StaticTranslation.objects.all()}
    except Exception:
        # Graceful degradation during migrations or cold start
        content = {}

    return {"content": content}
