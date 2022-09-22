from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskCreateForm, TaskNotesForm, TaskUpdateForm, TaskAssigneeForm
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
        form = TaskCreateForm(request.POST, current_user=request.user)
        if form.is_valid():
            task = form.save()
        return redirect("show_project", pk=task.project.id)
    else:
        # current_project = request.GET.get("current_project")
        form = TaskCreateForm(current_user=request.user)  # , initial={'project': current_project})  # , current_project=current_project)

    context = {"form": form}

    return render(request, "tasks/create.html", context)


@login_required
def complete_task(request, pk):
    # Get is_completed value from template
    completed = request.POST.get("is_completed")

    # Update is_completed value for instance (filtered)
    Task.objects.filter(id=pk).update(is_completed=completed)

    return redirect("show_my_tasks")


@login_required
def add_notes(request, pk):

    task_set = Task.objects.filter(id=pk)
    task_instance = Task.objects.get(id=pk)

    if request.method == "POST":

        form = TaskNotesForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            task_set.update(notes=instance.notes)
        return redirect("show_my_tasks")
    else:
        form = TaskNotesForm()

    # https://stackoverflow.com/questions/67544328/queryset-object-has-no-attribute-name-django
    # You're using .filter() which will return a QuerySet and not a instance of a model. You should use .get() for this scenario to access the name attribute.

    context = {
            "form": form,
            "task_name": task_instance.name,
        }

    return render(request, "tasks/update_notes.html", context)


@login_required
def update_task(request, pk):

    task_instance = Task.objects.get(id=pk)
    current_project = task_instance.project
    current_user = request.user


    if request.method == "POST":

        form = TaskUpdateForm(request.POST, instance=task_instance, current_project=current_project, current_user=current_user)

        if form.is_valid():
            form.save()
        return redirect("show_my_tasks")
    else:
        form = TaskUpdateForm(instance=task_instance, current_project=current_project, current_user=current_user)

    context = {
            "form": form,
            "task_instance": task_instance,
        }

    return render(request, "tasks/update.html", context)


@login_required
def add_assignee(request, pk):

    task_set = Task.objects.filter(id=pk)
    task_instance = Task.objects.get(id=pk)

    if request.method == "POST":

        form = TaskAssigneeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            task_set.update(assignee=instance.assignee)
        return redirect("show_project", pk=task_instance.project.id)
    else:
        form = TaskAssigneeForm()

    context = {
            "form": form,
            "task_name": task_instance.name,
        }

    return render(request, "tasks/update_assignee.html", context)
