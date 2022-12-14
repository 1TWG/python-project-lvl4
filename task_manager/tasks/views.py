from django.views.generic.base import TemplateView
from django.shortcuts import render
from task_manager.tasks.models import Tasks
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django_filters.views import FilterView
from task_manager.tasks.filter import TaskFilter


# Create your views here.
class TasksPage(LoginRequiredMixin, FilterView):
    model = Tasks
    template_name = 'tasks.html'
    filterset_class = TaskFilter


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'task-create.html'
    model = Tasks
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно создана'
    fields = ['name', 'description', 'status', 'executor', 'labels']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskPreview(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    login_url = '/login/'
    template_name = 'task-preview.html'
    success_url = reverse_lazy('tasks')

    def get(self, request, pk):
        return render(request, self.template_name, context={
            'task': Tasks.objects.filter(id=pk)[0],
        })


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    login_url = '/login/'
    template_name = 'task-update.html'
    model = Tasks
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно изменена'
    fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskRemove(LoginRequiredMixin, SuccessMessageMixin, DeleteView):  # noqa: E501
    login_url = '/login/'
    template_name = 'task-remove.html'
    model = Tasks
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно удалена'
