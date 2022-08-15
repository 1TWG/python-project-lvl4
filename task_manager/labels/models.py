from django.db import models


class Labels(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Имя', max_length=100, unique=True)

    def __str__(self):
        return self.name
