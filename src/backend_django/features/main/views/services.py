from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from features.main.selectors import (
    get_all_projects,
    get_automation_projects,
    get_pricing_plans_for_service,
)


def waas_view(request: HttpRequest) -> HttpResponse:
    """Website as a Service service page."""
    projects = get_all_projects()
    return render(
        request,
        "main/services/waas.html",
        {
            "projects": projects,
            "projects_count": len(projects),
            "plans": get_pricing_plans_for_service("waas"),
        },
    )


def automation_view(request: HttpRequest) -> HttpResponse:
    """Automation service page — shows only projects with has_automation=True."""
    projects = get_automation_projects()
    return render(
        request,
        "main/services/automation.html",
        {
            "projects": projects,
            "projects_count": len(projects),
            "plans": get_pricing_plans_for_service("automation"),
        },
    )


def solutions_view(request: HttpRequest) -> HttpResponse:
    """Industry solutions / prototype page."""
    projects = get_all_projects()
    return render(
        request,
        "main/services/solutions.html",
        {
            "projects": projects,
            "projects_count": len(projects),
        },
    )
