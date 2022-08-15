from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesPage.as_view(), name='statuses'),
    path('create/', views.StatusCreate.as_view(), name='status-create'),
    path('<int:pk>/update/', views.StatusUpdate.as_view(), name='status-update'),  # noqa: E501
    path('<int:pk>/delete/', views.StatusRemove.as_view(), name='status-remove'),  # noqa: E501
]
