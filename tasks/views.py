from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NewTaskForm
# from .models import TodoList


# Create your views here.
@login_required
def tasks(request):
    # task_name = TodoList.objects.all[]
    

@login_required
def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task_title"]
            request.session["todos"] += [task]
            messages.success(request, "Task added successfully.")
            form.save()
            return HttpResponseRedirect(reverse("add-task"))
        else:
            return render(request, "tasks/add_task.html", {"form": form})

    form = NewTaskForm()
    # return HttpResponse("Done!")
    if "todos" not in request.session:
        request.session["todos"] = []
    context = {"todos": request.session["todos"], "form": form,}
    return render(request, "tasks/add_task.html", context)
    # if request.method == "POST":

    # return render(request, "tasks/add_task.html")
