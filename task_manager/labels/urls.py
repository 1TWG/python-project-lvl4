from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsPage.as_view(), name='labels'),
    path('create/', views.LabelCreate.as_view(), name='label-create'),
    path('<int:pk>/update/', views.LabelUpdate.as_view(), name='label-update'),
    path('<int:pk>/delete/', views.LabelRemove.as_view(), name='label-remove'),
]
