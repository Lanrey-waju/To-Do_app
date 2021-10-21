from django import forms
from django.db.models import fields

from .models import TodoList

# Create your forms here
class NewTaskForm(forms.ModelForm):
    # Check if data doesnt contain just integers

    class Meta:
        model = TodoList
        exclude = ('productiver',)
        labels = {"task_title": "Title", "task_description": "Description"}
        help_text = {"task_title": "Enter the title of your task"}
