from django.db.models import QuerySet
from features.main.models import PricingPlan


def get_pricing_plans_for_service(service: str) -> QuerySet:
    """Returns active pricing plans for a given service ('waas' or 'automation')."""
    return PricingPlan.objects.filter(service=service, is_active=True)
