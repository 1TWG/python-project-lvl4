from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from task_manager.users.forms import UserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView
from django.shortcuts import redirect


class UsersPage(TemplateView):
    "Users list page."
    template_name = 'users.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'users': User.objects.all(),
        })


class UserCreate(SuccessMessageMixin, CreateView):
    template_name = 'create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    # login_url = '/login/'
    template_name = 'user-update.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно изменен'

    def test_func(self):
        return self.request.user.id == 1

    def handle_no_permission(self):
        return redirect('/login')
