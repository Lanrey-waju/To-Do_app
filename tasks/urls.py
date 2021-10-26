from django.urls import path

from . import views

# create routes here
urlpatterns = [
    path("add-task/", views.add_task, name="add-task"),
]
