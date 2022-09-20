from django.contrib import admin

from projects.models import Project, Company


class ProjectAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Company, CompanyAdmin)
