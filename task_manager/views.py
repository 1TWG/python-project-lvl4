from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin


class IndexPage(TemplateView):
    "Main page."
    template_name = 'index.html'


class LogIn(UserPassesTestMixin, SuccessMessageMixin, LoginView):
    "Log In page."
    success_message = 'Вы залогинены'

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('/users')


class LogOut(LogoutView):
    "Log Out page."
    pass
