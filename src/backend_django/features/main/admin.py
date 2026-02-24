from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from .models import PricingPlan, Project


class TranslationModelAdmin(ModelAdmin, TabbedTranslationAdmin):
    """Combines Unfold styling with modeltranslation language tabs."""

    pass


@admin.register(Project)
class ProjectAdmin(TranslationModelAdmin):
    list_display = ("name", "niche", "city", "status", "has_automation", "is_active", "order")
    list_filter = ("status", "has_automation", "is_active")
    list_editable = ("status", "is_active", "order")
    search_fields = ("name", "niche", "city")

    fieldsets = (
        (
            _("General"),
            {
                "fields": ("name", "niche", "city", "status"),
            },
        ),
        (
            _("Media"),
            {
                "fields": ("thumbnail",),
            },
        ),
        (
            _("Links"),
            {
                "fields": ("preview_url", "site_url"),
            },
        ),
        (
            _("Display"),
            {
                "fields": ("has_automation", "is_active", "is_available", "is_planned", "order"),
            },
        ),
        (
            _("SEO"),
            {
                "classes": ("collapse",),
                "fields": ("seo_title", "seo_description", "seo_image"),
            },
        ),
    )


@admin.register(PricingPlan)
class PricingPlanAdmin(TranslationModelAdmin):
    list_display = ("name", "service", "price_label", "is_featured", "is_active", "order")
    list_filter = ("service", "is_active")
    list_editable = ("is_featured", "is_active", "order")
    search_fields = ("name",)

    fieldsets = (
        (
            _("General"),
            {
                "fields": ("service", "name", "price_label"),
            },
        ),
        (
            _("Features"),
            {
                "fields": ("feat_1", "feat_2", "feat_3"),
            },
        ),
        (
            _("Display"),
            {
                "fields": ("cta_label", "is_featured", "is_active", "order"),
            },
        ),
    )
