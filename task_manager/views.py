from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


class IndexPage(TemplateView):
    "Main page."
    template_name = 'index.html'


@login_required
def my_view(request):
    pass
