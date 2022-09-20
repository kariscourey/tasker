from django.urls import path

from tasks.views import (
    create_task,
    list_tasks,
    complete_task,
    add_notes,
)

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("<int:pk>/complete/", complete_task, name="complete_task"),
    path("<int:pk>/notes/", add_notes, name="add_notes"),
]
