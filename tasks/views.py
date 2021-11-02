from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NewTaskForm
from .models import TodoList
# from .models import TodoList


# Create your views here.
@login_required
def add_task(request):
    productiver = request.user
    todos = TodoList.objects.filter(productiver=productiver)
    if request.method != "POST":
        form = NewTaskForm()

    else:
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # Bind the logged in user as the 'productiver'
            new_form = form.save(commit=False)
            new_form.productiver = productiver
            new_form.save()
            messages.success(request, "Task added successfully.")
            return HttpResponseRedirect(reverse("add-task"))

    context = {"todos": todos, "form": form, "productiver": productiver}
    return render(request, "tasks/add_task.html", context)


# View to handle update of tasks
@login_required
def update_task(request, todos_id):
    productiver = request.user
    todo = TodoList.objects.get(id=todos_id)
    if request.method != "POST":
        form = NewTaskForm(instance=todo)
    else:
        form = NewTaskForm(instance=todo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-task')    

    context = {"todo": todo, "form": form, "productiver": productiver}
    return render(request, "tasks/update_task.html", context)


# View function to handle tasks deletion
@login_required
def delete_task(request, todos_id):
    todos = TodoList.objects.get(id=todos_id)
    if request.method == 'POST':
        todos.delete()
    return HttpResponseRedirect(reverse('add-task'))