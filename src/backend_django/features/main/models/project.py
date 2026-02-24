from django.db import models
from django.utils.translation import gettext_lazy as _
from features.system.models.mixins import ActiveMixin, SeoMixin, TimestampMixin


class Project(TimestampMixin, ActiveMixin, SeoMixin, models.Model):
    """
    Portfolio project shown on landing page and service pages.
    Used in bento grid with adaptive col-span logic (see content_rules.md).
    """

    STATUS_LIVE = "live"
    STATUS_TAKEN = "taken"
    STATUS_FREE = "free"
    STATUS_CHOICES = [
        (STATUS_LIVE, _("Live")),
        (STATUS_TAKEN, _("Taken")),
        (STATUS_FREE, _("Free")),
    ]

    name = models.CharField(_("Name"), max_length=255)
    niche = models.CharField(_("Niche"), max_length=100)
    city = models.CharField(_("City"), max_length=100, blank=True)
    status = models.CharField(
        _("Status"),
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_FREE,
    )
    preview_url = models.URLField(
        _("Prototype URL"),
        blank=True,
        help_text=_("Clickable prototype link (48h version)"),
    )
    site_url = models.URLField(
        _("Live Site URL"),
        blank=True,
        help_text=_("Link to the live production site"),
    )
    thumbnail = models.ImageField(
        _("Thumbnail"),
        upload_to="projects/",
        blank=True,
        null=True,
        help_text=_("Preview image for bento card"),
    )
    has_automation = models.BooleanField(
        _("Has Automation"),
        default=False,
        help_text=_("If True, shown on /services/automation/ page"),
    )
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return self.name
