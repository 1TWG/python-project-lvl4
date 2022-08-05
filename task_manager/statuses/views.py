from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class StatusesPage(TemplateView):
    "Users list page."
    template_name = 'statuses.html'

