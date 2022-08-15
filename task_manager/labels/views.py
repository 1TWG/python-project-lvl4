from django.views.generic.base import TemplateView
from django.shortcuts import render
from task_manager.labels.models import Labels
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.

class LabelsPage(LoginRequiredMixin, TemplateView):
    "Users list page."
    # login_url = '/login/'
    template_name = 'labels.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'labels': Labels.objects.all(),
        })

    def test_func(self, request):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                'Авторизируйтесь'
            )
        return request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('/login')


class LabelCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'label-create.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно создана'
    fields = ['name']


class LabelUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    login_url = '/login/'
    template_name = 'label-update.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно изменёна'
    fields = ['name']


class LabelRemove(LoginRequiredMixin, SuccessMessageMixin, DeleteView):  # noqa: E501
    login_url = '/login/'
    template_name = 'label-remove.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно удаленв'
