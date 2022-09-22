from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "members", "company"]

    def __init__(self, *args, **kwargs):

        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields["company"].required = False
