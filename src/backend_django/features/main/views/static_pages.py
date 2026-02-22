from django.views.generic import TemplateView

ContactsView = TemplateView.as_view(template_name="main/contacts.html")
FaqView = TemplateView.as_view(template_name="main/faq.html")
ImpressumView = TemplateView.as_view(template_name="main/impressum.html")
DatenschutzView = TemplateView.as_view(template_name="main/datenschutz.html")

# AI-context files — served as plain text, no i18n prefix needed
LlmsRuView = TemplateView.as_view(template_name="llms_ru.txt", content_type="text/plain; charset=utf-8")
LlmsEnView = TemplateView.as_view(template_name="llms_en.txt", content_type="text/plain; charset=utf-8")
LlmsDeView = TemplateView.as_view(template_name="llms_de.txt", content_type="text/plain; charset=utf-8")
