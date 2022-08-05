from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesPage.as_view(), name='statuses'),
]
