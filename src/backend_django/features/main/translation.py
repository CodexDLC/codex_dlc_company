from modeltranslation.translator import TranslationOptions, register

from .models import PricingPlan, Project


@register(Project)
class ProjectTranslation(TranslationOptions):
    fields = ("name", "niche", "city")


@register(PricingPlan)
class PricingPlanTranslation(TranslationOptions):
    fields = ("name", "price_label", "feat_1", "feat_2", "feat_3", "cta_label")
