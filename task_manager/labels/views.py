from django.views.generic.base import TemplateView
from django.shortcuts import render
from task_manager.labels.models import Labels
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect


class LabelsPage(LoginRequiredMixin, TemplateView):
    "Labels list page."
    template_name = 'labels.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'labels': Labels.objects.all(),
        })

    def handle_no_permission(self):
        return redirect('/login')


class LabelCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    "Label create page."
    login_url = '/login/'
    template_name = 'label-create.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно создана'
    fields = ['name']


class LabelUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    "Label update page."
    login_url = '/login/'
    template_name = 'label-update.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно изменена'
    fields = ['name']


class LabelRemove(LoginRequiredMixin, SuccessMessageMixin, DeleteView):  # noqa: E501
    "Label remove page."
    login_url = '/login/'
    template_name = 'label-remove.html'
    model = Labels
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно удалена'
