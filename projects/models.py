from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    members = models.ManyToManyField(USER_MODEL, related_name="projects")
    company = models.ForeignKey(
        "Company",
        related_name="projects",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    project = models.ManyToManyField(
        Project,
        related_name="companies",
    )

    def __str__(self):
        return self.name
