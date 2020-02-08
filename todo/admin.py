from django.contrib import admin
from .models import Category, Task, Project


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = "due_date"
    list_display = ["desc", "due_date", "category", "done_task" ]
    list_filter = ["desc", "due_date", "category"]
    search_fields = ["desc", "category"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title"]
   

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)