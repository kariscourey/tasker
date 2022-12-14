# Generated by Django 4.1.1 on 2022-09-20 19:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0003_alter_project_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "project",
                    models.ManyToManyField(
                        null=True,
                        related_name="companies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
