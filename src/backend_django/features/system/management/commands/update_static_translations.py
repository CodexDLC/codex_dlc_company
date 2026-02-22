import json

from django.conf import settings
from django.core.management.base import BaseCommand
from features.system.models import StaticTranslation


class Command(BaseCommand):
    help = "Update Static Translations from JSON fixture (supports per-language text fields)"

    def handle(self, *args, **options):
        fixture_path = settings.BASE_DIR / "features" / "system" / "fixtures" / "static_translations.json"

        if not fixture_path.exists():
            self.stdout.write(self.style.WARNING(f"Fixture not found: {fixture_path}"))
            return

        with open(fixture_path, encoding="utf-8") as f:
            data = json.load(f)

        count = 0
        for item in data:
            fields = item.get("fields", item)
            key = fields.get("key")
            if not key:
                continue

            defaults = {"description": fields.get("description", "")}

            # Support per-language format: {"text_ru": "...", "text_en": "...", "text_de": "..."}
            # as well as flat format: {"text": "..."}
            if any(f"text_{lang}" in fields for lang in settings.MODELTRANSLATION_LANGUAGES):
                for lang_code in settings.MODELTRANSLATION_LANGUAGES:
                    lang_field = f"text_{lang_code}"
                    if lang_field in fields:
                        defaults[lang_field] = fields[lang_field]
                # Base `text` = default language value
                default_lang = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
                defaults["text"] = fields.get(f"text_{default_lang}", fields.get("text", ""))
            else:
                defaults["text"] = fields.get("text", "")

            obj, created = StaticTranslation.objects.update_or_create(key=key, defaults=defaults)
            verb = "Created" if created else "Updated"
            self.stdout.write(f"  [{verb}] {key}")
            count += 1

        self.stdout.write(self.style.SUCCESS(f"✓ Processed {count} translations"))
