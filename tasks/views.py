from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskCreateForm  # , TaskUpdateForm
from django.contrib.auth.decorators import login_required


@login_required
def list_tasks(request):
    tasks_list = Task.objects.filter(assignee=request.user)
    context = {
        "tasks_list": tasks_list,
    }
    return render(request, "tasks/list.html", context)


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save()
        return redirect("show_project", pk=task.project.id)
    else:
        form = TaskCreateForm()

    context = {"form": form}

    return render(request, "tasks/create.html", context)


@login_required
def complete_task(request, pk):
    # Get is_completed value from template
    completed = request.POST.get("is_completed")

    # Update is_completed value for instance (filtered)
    Task.objects.filter(id=pk).update(is_completed=completed)

    return redirect("show_my_tasks")
