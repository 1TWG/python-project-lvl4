# Generated by Django 4.0.6 on 2022-08-15 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuses',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
