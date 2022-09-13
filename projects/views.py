from django.shortcuts import render
from projects.models import Project
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
