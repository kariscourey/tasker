from django.urls import path

from projects.views import (
    list_projects,
    show_project,
    create_project,
    update_project,
)

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:pk>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("<int:pk>/update/", update_project, name="update_project"),

]
