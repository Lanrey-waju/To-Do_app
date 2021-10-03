from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

from .forms import NewTaskForm
from .models import TodoList


# Create your views here.
def tasks(request):
    # task_name = TodoList.objects.all[]
    if "todos" not in request.session:
        request.session["todos"] = []
    context = {"todos": request.session["todos"]}
    return render(request, "tasks/tasks.html", context)


def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task_title"]
            request.session["todos"] += [task]
            messages.success(request, "Task added successfully.")
            form.save()
            return HttpResponseRedirect(reverse("tasks"))
        else:
            return render(request, "tasks/add_task.html", {"form": form})

    form = NewTaskForm()
    # return HttpResponse("Done!")
    context = {
        "form": form,
    }
    return render(request, "tasks/add_task.html", context)
    # if request.method == "POST":

    # return render(request, "tasks/add_task.html")
