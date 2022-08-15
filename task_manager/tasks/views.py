from django.views.generic.base import TemplateView
from django.shortcuts import render
from task_manager.statuses.models import Statuses
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


# Create your views here.
class TasksPage(LoginRequiredMixin, TemplateView):
    "Users list page."
    # login_url = '/login/'
    template_name = 'tasks.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'statuses': Statuses.objects.all(),
        })

    def test_func(self):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                'Авторизируйтесь'
            )
        return request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('/login')


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'task-create.html'
    model = Statuses
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно создана'
