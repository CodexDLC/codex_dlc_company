from features.main.models import Project


def get_all_projects() -> list[Project]:
    """Returns all active projects ordered by order, name."""
    return list(Project.objects.filter(is_active=True))


def get_automation_projects() -> list[Project]:
    """Returns active projects that have automation (shown on /services/automation/)."""
    return list(Project.objects.filter(is_active=True, has_automation=True))
