from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class TodoList(models.Model):
    # name of the user is designated 'productiver'
    productiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks")
    task_title = models.CharField(max_length=50, null=True)
    task_description = models.CharField(max_length=200, blank=True, null=True)
    priority = models.PositiveBigIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.task_title.title()} with priority {self.priority}'

    class Meta:
        ordering = ['completed']
