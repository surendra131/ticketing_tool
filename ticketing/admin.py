from django.contrib import admin

# Register your models here.
from .models import Project, Issue, Sprint

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    search_fields = ("name", "owner")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "status", "project")
    search_fields = ("id", "type", "status", "project")


class SprintAdmin(admin.ModelAdmin):
    list_display = ("name", "start", "end", "project")
    search_fields = ("name", "start", "end", "project")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Sprint, SprintAdmin)


