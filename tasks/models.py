from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.forms.widgets import Widget

# Create your models here.
class TodoList(models.Model):
    # name of the user is designated 'productiver'
    productiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=50, null=True)
    task_description = models.CharField(max_length=200, null=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title

    class Meta:
        ordering = ['completed']
