from django import forms
from tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "start_date", "due_date", "project", "assignee"]


# class TaskUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ["is_completed"]
