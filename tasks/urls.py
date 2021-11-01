from django.urls import path

from . import views

# create routes here
urlpatterns = [
    path('', views.add_task, name='add-task'),
    path('delete-task/<int:todos_id>', views.delete_task, name='delete-task')
]
