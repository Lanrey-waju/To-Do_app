from django.db import models
from django.db.models.base import Model
from django.forms.widgets import Widget

# Create your models here.
class TodoList(models.Model):
    task_title = models.CharField(max_length=50, null=True)
    task_description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.task_title
