from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Labels


class Tasks(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Имя', max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    creator = models.ForeignKey(
        get_user_model(),
        verbose_name='Автор',
        on_delete=models.PROTECT,
        related_name='creator'
    )
    executor = models.ForeignKey(
        get_user_model(),
        verbose_name='Исполнитель',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='executor'
    )
    status = models.ForeignKey(
        Statuses,
        verbose_name='Статус',
        on_delete=models.PROTECT
    )
    labels = models.ManyToManyField(
        Labels,
        through='TaskLabels',
        verbose_name='Метки',
        blank=True
    )

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    labels = models.ForeignKey(Labels, on_delete=models.PROTECT)
