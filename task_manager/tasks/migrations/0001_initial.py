# Generated by Django 4.0.6 on 2022-08-15 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('labels', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labels.labels')),  # noqa: E501
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('timestamp', models.DateTimeField(auto_now_add=True)),  # noqa: E501
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),  # noqa: E501
                ('description', models.TextField(blank=True, verbose_name='Описание')),  # noqa: E501
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),  # noqa: E501
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),  # noqa: E501
                ('labels', models.ManyToManyField(blank=True, through='tasks.TaskLabels', to='labels.labels', verbose_name='Метки')),  # noqa: E501
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.statuses', verbose_name='Статус')),  # noqa: E501
            ],
        ),
        migrations.AddField(
            model_name='tasklabels',
            name='tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks'),  # noqa: E501
        ),
    ]