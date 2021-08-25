from django.urls import path

from . import views

# create routes here
urlpatterns = [
    path("", views.index, name="index"),
]
