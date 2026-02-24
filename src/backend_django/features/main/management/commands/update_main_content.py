import json

from django.conf import settings
from django.core.management.base import BaseCommand
from features.main.models import PricingPlan, Project


class Command(BaseCommand):
    help = "Upsert Projects and PricingPlans from fixtures (features/main/fixtures/)"

    def handle(self, *args, **options):
        self._load_projects()
        self._load_pricing_plans()

    def _load_projects(self):
        fixture_path = settings.BASE_DIR / "features" / "main" / "fixtures" / "projects.json"
        if not fixture_path.exists():
            self.stdout.write(self.style.WARNING(f"Fixture not found: {fixture_path}"))
            return

        with open(fixture_path, encoding="utf-8") as f:
            items = json.load(f)

        created = updated = 0
        for item in items:
            pk = item.get("pk")
            fields = item.get("fields", {})
            obj, is_new = Project.objects.update_or_create(pk=pk, defaults=fields)
            if is_new:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"  [CREATE] Project #{pk}: {obj.name}"))
            else:
                updated += 1
                self.stdout.write(f"  [SKIP]   Project #{pk}: {obj.name} (already exists)")

        self.stdout.write(self.style.SUCCESS(f"✓ Projects: {created} created, {updated} skipped"))

    def _load_pricing_plans(self):
        fixture_path = settings.BASE_DIR / "features" / "main" / "fixtures" / "pricing_plans.json"
        if not fixture_path.exists():
            self.stdout.write(self.style.WARNING(f"Fixture not found: {fixture_path}"))
            return

        with open(fixture_path, encoding="utf-8") as f:
            items = json.load(f)

        created = updated = 0
        for item in items:
            pk = item.get("pk")
            fields = item.get("fields", {})
            obj, is_new = PricingPlan.objects.update_or_create(pk=pk, defaults=fields)
            if is_new:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"  [CREATE] PricingPlan #{pk}: {obj}"))
            else:
                updated += 1
                self.stdout.write(f"  [SKIP]   PricingPlan #{pk}: {obj} (already exists)")

        self.stdout.write(self.style.SUCCESS(f"✓ PricingPlans: {created} created, {updated} skipped"))
