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
from django.views.generic.edit import DeleteView
from django.contrib import messages


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
    success_url = reverse_lazy('user-login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    template_name = 'user-update.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно изменен'

    def test_func(self):
        if not self.request.user.id == self.kwargs.get('pk'):
            messages.error(
                self.request,
                'У вас нет прав для изменения другого пользователя.'
            )
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        return redirect('/login')


class UserRemove(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):  # noqa: E501
    # login_url = '/login/'
    template_name = 'user-remove.html'
    model = get_user_model()
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно удален'

    def test_func(self):
        if not self.request.user.id == self.kwargs.get('pk'):
            messages.error(
                self.request,
                'У вас нет прав для изменения другого пользователя.'
            )
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        return redirect('/login')
