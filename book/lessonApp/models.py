from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return f'{self.name}: {self.completed}'
