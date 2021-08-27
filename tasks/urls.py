from django.urls import path

from . import views


# create routes here
urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("add-task/", views.add_task, name="add-task"),
]