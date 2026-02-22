from django.test import TestCase
from features.system.models.site_settings import SiteSettings


class SiteSettingsModelTest(TestCase):
    def test_site_settings_singleton(self):
        """Test that SiteSettings always uses pk=1 (Singleton)."""
        SiteSettings.objects.create(company_name="First")
        SiteSettings.objects.create(company_name="Second")

        # There should be only one record in the database
        self.assertEqual(SiteSettings.objects.count(), 1)
        # The record should have the data from the last save
        self.assertEqual(SiteSettings.objects.get(pk=1).company_name, "Second")

    def test_site_settings_load(self):
        """Test the load() classmethod."""
        # Should create a new one if none exists
        settings = SiteSettings.load()
        self.assertIsNotNone(settings)
        self.assertEqual(settings.pk, 1)

        # Should return existing one
        settings.company_name = "Test Company"
        settings.save()

        loaded_settings = SiteSettings.load()
        self.assertEqual(loaded_settings.company_name, "Test Company")

    def test_site_settings_to_dict(self):
        """Test the to_dict() method."""
        settings = SiteSettings.load()
        settings.company_name = "CodexDLC"
        settings.email = "test@example.com"
        settings.save()

        data = settings.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["company_name"], "CodexDLC")
        self.assertEqual(data["email"], "test@example.com")
        self.assertIn("site_base_url", data)
