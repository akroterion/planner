import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name=("Name"),)
   
   class Meta
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name



class Task(models.Model):
    desc = models.CharField(max_length=400, verbos_name=("Description"),)
    task_date = models.DateTimeField(
    verbose_name=("Task date"), unique_for_date="task_date")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.desc} {self.task_date} {self.category}"
    
    