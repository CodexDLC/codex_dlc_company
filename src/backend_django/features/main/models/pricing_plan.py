from django.db import models
from django.utils.translation import gettext_lazy as _
from features.system.models.mixins import ActiveMixin, TimestampMixin


class PricingPlan(TimestampMixin, ActiveMixin, models.Model):
    """
    Subscription pricing plan shown on WaaS and Automation service pages.
    Pulled from DB — never hardcoded in templates (content_rules.md).
    Note: §19 UStG footnote is rendered by the template, not stored here.
    """

    SERVICE_WAAS = "waas"
    SERVICE_AUTOMATION = "automation"
    SERVICE_CHOICES = [
        (SERVICE_WAAS, _("Website as a Service")),
        (SERVICE_AUTOMATION, _("Automation")),
    ]

    service = models.CharField(_("Service"), max_length=20, choices=SERVICE_CHOICES)
    name = models.CharField(_("Plan Name"), max_length=100)
    price_label = models.CharField(
        _("Price"),
        max_length=100,
        help_text=_("Display price string, e.g. 'от €59 / мес'"),
    )
    feat_1 = models.CharField(_("Feature 1"), max_length=255, blank=True)
    feat_2 = models.CharField(_("Feature 2"), max_length=255, blank=True)
    feat_3 = models.CharField(_("Feature 3"), max_length=255, blank=True)
    cta_label = models.CharField(_("CTA Label"), max_length=100, default=_("Choose"))
    is_featured = models.BooleanField(
        _("Featured"),
        default=False,
        help_text=_("Highlighted plan (e.g. most popular)"),
    )
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Pricing Plan")
        verbose_name_plural = _("Pricing Plans")
        ordering = ["service", "order"]

    def __str__(self) -> str:
        return f"{self.get_service_display()} — {self.name}"
