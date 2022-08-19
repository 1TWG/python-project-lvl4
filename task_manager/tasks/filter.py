from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from .models import Tasks
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Labels
from django import forms


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(label='Статус', queryset=Statuses.objects.all())
    performer = ModelChoiceFilter(label='Исполнитель', queryset=User.objects.all())
    label = ModelChoiceFilter(label='Метка', queryset=Label.objects.all())
    self_tasks = BooleanFilter(label='Только свои задачи', method='self_tasks_filter', widget=forms.CheckboxInput)

    class Meta:
        model = Task
        fields = ['status', 'performer', 'label', 'self_tasks']

    def self_tasks_filter(self, queryset, name, value):
        if value:
            return queryset & self.request.user.created_tasks.all()
        return queryset & Task.objects.all()
