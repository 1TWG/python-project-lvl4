import django_filters
from .models import Tasks
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Labels
from django import forms
from django.contrib.auth.models import User


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.filters.BooleanFilter(
        widget=forms.CheckboxInput,
        field_name='author',
        method='filter_self_tasks',
        label='Только свои задачи'
    )

    label = django_filters.filters.ModelChoiceFilter(
        queryset=Labels.objects.all(),
        field_name='labels',
        label='Метка'
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'label', 'self_tasks']
