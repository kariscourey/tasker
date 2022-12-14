from django import forms
from tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "notes"
        ]

    def __init__(self, *args, **kwargs):

        current_user = kwargs.pop("current_user", None)

        super(TaskCreateForm, self).__init__(*args, **kwargs)

        if current_user:
            self.fields["project"].queryset = self.fields[
                "project"
            ].queryset.filter(members=current_user)

        self.fields["notes"].required = False
        self.fields["assignee"].required = False


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "notes"
        ]

    def __init__(self, *args, **kwargs):

        current_project = kwargs.pop("current_project", None)
        current_user = kwargs.pop("current_user", None)

        super(TaskUpdateForm, self).__init__(*args, **kwargs)

        if current_project:
            self.fields["assignee"].queryset = self.fields[
                "assignee"
            ].queryset.filter(projects=current_project)

            self.fields["project"].queryset = self.fields[
                "project"
            ].queryset.filter(members=current_user)

        self.fields["notes"].required = False
        self.fields["assignee"].required = False


class TaskNotesForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["notes"]

    def __init__(self, *args, **kwargs):
        super(TaskNotesForm, self).__init__(*args, **kwargs)
        self.fields["notes"].required = False


class TaskAssigneeForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["assignee"]

    def __init__(self, *args, **kwargs):
        super(TaskAssigneeForm, self).__init__(*args, **kwargs)
        self.fields["assignee"].required = False
