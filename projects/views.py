from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    projects_list = Project.objects.filter(members=request.user)
    context = {
        "projects_list": projects_list,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, pk):
    project_detail = Project.objects.get(pk=pk)
    context = {
        "project_detail": project_detail,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
        return redirect("show_project", pk=project.id)
    else:
        form = ProjectForm()

    context = {"form": form}

    return render(request, "projects/create.html", context)
