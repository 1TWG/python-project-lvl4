# Generated by Django 4.0.6 on 2022-08-20 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),  # noqa: E501
        ),
        migrations.AddField(
            model_name='tasks',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),  # noqa: E501
        ),
        migrations.AddField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.TaskLabels', to='labels.labels', verbose_name='Метки'),  # noqa: E501
        ),
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='statuses.statuses', verbose_name='Статус'),  # noqa: E501
        ),
        migrations.AddField(
            model_name='tasklabels',
            name='labels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labels.labels'),  # noqa: E501
        ),
        migrations.AddField(
            model_name='tasklabels',
            name='tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks'),  # noqa: E501
        ),
    ]
