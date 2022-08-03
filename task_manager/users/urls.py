from django.urls import path, include
from task_manager.users import views

urlpatterns = [
    path('', views.UsersPage.as_view(), name='users'),
    path('create/', views.CreateUserPage.as_view(), name='create'),
]
