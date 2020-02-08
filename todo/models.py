import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name="name")
   
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    
class Project(models.Model):
    title = models.CharField(max_length=120, verbose_name="title")
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class Task(models.Model):
    desc = models.CharField(max_length=400, verbose_name="description")
    due_date = models.DateTimeField(
        verbose_name="due date", default=timezone.now,)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    projects = models.ManyToManyField(Project)
    done_task = models.BooleanField(verbose_name="done task", default=False)
    def __str__(self):
        return f"{self.desc} {self.due_date} {self.category} {self.projects} {self.done_task}"


