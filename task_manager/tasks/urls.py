from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('', views.TasksPage.as_view(), name='tasks'),
    path('create/', views.TaskCreate.as_view(), name='task-create'),
    # path('<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    # path('<int:pk>/delete/', views.TaskRemove.as_view(), name='task-remove'),
]
