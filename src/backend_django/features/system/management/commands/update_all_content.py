from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run all content update commands (SiteSettings, Translations, etc.)"

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(">>> Updating Site Settings..."))
        try:
            call_command("update_site_settings")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to update site settings: {e}"))

        self.stdout.write(self.style.MIGRATE_HEADING("\n>>> Updating Static Translations..."))
        try:
            call_command("update_static_translations")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to update static translations: {e}"))

        self.stdout.write(self.style.MIGRATE_HEADING("\n>>> Updating Main Content (Projects, Pricing)..."))
        try:
            call_command("update_main_content")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to update main content: {e}"))

        self.stdout.write(self.style.SUCCESS("\n✓ All system updates completed."))
