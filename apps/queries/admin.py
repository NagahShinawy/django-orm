from django.contrib import admin
from .models import Developer, Task


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "developer")


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age")
    list_editable = ("age", )
