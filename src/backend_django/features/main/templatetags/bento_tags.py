from django import template

register = template.Library()


@register.simple_tag
def bento_span(index: int, total: int) -> str:
    """
    Returns CSS col-span class for bento grid based on item position and total count.

    Rules from content_rules.md:
      1  project  → col-span-12
      2  projects → col-span-6 each
      3  projects → first col-span-6, rest col-span-3
      4  projects → col-span-6 each (2×2)
      5  projects → first two col-span-6, rest col-span-4
      6+ projects → col-span-4 each

    Usage in templates:
        {% load bento_tags %}
        {% for project in projects %}
            {% bento_span forloop.counter projects_count as span %}
            <div class="bento-card {{ span }}">...</div>
        {% endfor %}

    Note: pass `projects_count` from view context (len(projects)),
    because simple_tag does not accept filter expressions as arguments.
    """
    if total == 1:
        return "col-span-12"
    if total == 2:
        return "col-span-6"
    if total == 3:
        return "col-span-4"
    if total == 4:
        return "col-span-6"
    if total == 5:
        return "col-span-6" if index <= 2 else "col-span-4"
    return "col-span-4"
