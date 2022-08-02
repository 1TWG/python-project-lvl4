from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    "Main page."
    template_name = 'index.html'
