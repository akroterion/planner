import datetime
from django import forms
from .models import Category, Project, Task


class CategoryForm(forms.Form):
    name = forms.CharField(label="category", max_length=120)


class ProjectForm(forms.Form):
    title = forms.CharField(label="project", max_length=120)

class TaskForm(forms.Form):
    desc = forms.CharField(label="task", max_length=120)
    due_date = forms.DateTimeField(label="due date",)



