from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User


class UsersPage(TemplateView):
    "Users list page."
    template_name = 'users.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'users': User.objects.all(),
        })


class CreateUserPage(TemplateView):
    "Create user page."
    template_name = 'create.html'


