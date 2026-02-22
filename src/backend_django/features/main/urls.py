from django.urls import path

from .views import home
from .views.static_pages import ContactsView, DatenschutzView, FaqView, ImpressumView

app_name = "main"

urlpatterns = [
    path("", home.index, name="index"),
    path("contacts/", ContactsView, name="contacts"),
    path("faq/", FaqView, name="faq"),
    path("impressum/", ImpressumView, name="impressum"),
    path("datenschutz/", DatenschutzView, name="datenschutz"),
]
