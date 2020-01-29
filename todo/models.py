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
    desc = models.CharField(max_length=400, verbose_name=("Description"),)
    due_date = models.DateTimeField(
    verbose_name=("Task date"), default=datetime.now("due_date"))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.desc} {self.due_date} {self.category}"
    
class Projects(modelsModel)
    title =  models.CharField(max_length=120, verbose_name=("Title"),)
    task = models.ManyToManyField(Task, on_delete=models.PROTECT)

    def __str__(self):
        return self.title



