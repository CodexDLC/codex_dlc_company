from django.urls import path

from .views import home, services
from .views.static_pages import ContactsView, DatenschutzView, FaqView, ImpressumView

app_name = "main"

urlpatterns = [
    path("", home.index, name="index"),
    path("services/waas/", services.waas_view, name="services_waas"),
    path("services/automation/", services.automation_view, name="services_automation"),
    path("services/prototype/", services.solutions_view, name="services_prototype"),
    path("contacts/", ContactsView, name="contacts"),
    path("faq/", FaqView, name="faq"),
    path("impressum/", ImpressumView, name="impressum"),
    path("datenschutz/", DatenschutzView, name="datenschutz"),
]
