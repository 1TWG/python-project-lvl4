from django.views.generic.base import TemplateView
from django.shortcuts import render
from task_manager.statuses.models import Statuses
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.shortcuts import redirect


class StatusesPage(LoginRequiredMixin, TemplateView):
    "Statuses list page."
    template_name = 'statuses.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'statuses': Statuses.objects.all(),
        })

    def handle_no_permission(self):
        return redirect('/login')


class StatusCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    "Statuse create page."
    login_url = '/login/'
    template_name = 'status-create.html'
    model = Statuses
    success_url = reverse_lazy('statuses')
    success_message = 'Статус успешно создан'
    fields = ['name']


class StatusUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    "Statuse update page."
    login_url = '/login/'
    template_name = 'status-update.html'
    model = Statuses
    success_url = reverse_lazy('statuses')
    success_message = 'Статус успешно изменён'
    fields = ['name']


class StatusRemove(LoginRequiredMixin, SuccessMessageMixin, DeleteView):  # noqa: E501
    "Statuse remove page."
    login_url = '/login/'
    template_name = 'status-remove.html'
    model = Statuses
    success_url = reverse_lazy('statuses')
    success_message = 'Статус успешно удалён'
