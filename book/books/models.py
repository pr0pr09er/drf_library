from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    annotations = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
