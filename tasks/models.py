from django.db import models
from django.db.models.base import Model

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=18)
