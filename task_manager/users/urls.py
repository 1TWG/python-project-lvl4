from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.UsersPage.as_view(), name='users'),
    path('create/', views.UserCreate.as_view(), name='user-create'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
]
