from django.shortcuts import render, redirect
from projects.models import Project, Company
from projects.forms import ProjectForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
# from django.core.paginator import Paginator, EmptyPage


@login_required
def list_projects(request):  #, page=1):

    # paginator = Paginator(projects_list, 10)

    # try:
    #     projects_list = paginator.page(page)
    # except EmptyPage:
    #     projects_list = paginator.page(paginator.num_pages)

    bad_search = False
    companies_list = Company.objects.all()
    filter = "name"

    if request.method == "POST":

        company_name = request.POST.get("company_name")
        show_all = request.POST.get("show_all")
        bad_search = False

        # TODO figure out filtering, company selection

        if request.POST.get("filter") is not None:
            filter = request.POST.get("filter")

        if show_all:
            projects_list = Project.objects.filter(members=request.user)

        else:
            try:
                # functionality added in if select field not hidden, but currently is
                company_id = Company.objects.get(name=company_name).id
                projects_list = Project.objects.filter(members=request.user, company_id=company_id)
            except ObjectDoesNotExist:
                bad_search = True
                projects_list = Project.objects.filter(members=request.user)

    else:
        projects_list = Project.objects.filter(members=request.user)

    projects_list = projects_list.order_by(filter)


    context = {
        "projects_list": projects_list,
        "bad_search": bad_search,
        "companies_list": companies_list,
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
            project_form = form.save()

            if request.user in project_form.members.all():
                return redirect("show_project", pk=project_form.id)
            else:
                return redirect("list_projects")

    else:
        form = ProjectForm()

    context = {"form": form}

    return render(request, "projects/create.html", context)


@login_required
def update_project(request, pk):

    project_instance = Project.objects.get(id=pk)

    if request.method == "POST":

        form = ProjectForm(request.POST, instance=project_instance)

        if form.is_valid():

            project_form = form.save()

            print(project_form.members.all())

            if request.user in project_form.members.all():
                return redirect("show_project", pk=project_instance.id)

            else:
                project_instance.tasks.filter(assignee_id=request.user.id).update(assignee_id=None)
                return redirect("list_projects")

        return redirect("show_project", pk=project_instance.id)
    else:
        form = ProjectForm(instance=project_instance)

    context = {
            "form": form,
            "project_instance": project_instance,
        }

    return render(request, "projects/update.html", context)
