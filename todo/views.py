import random
from .forms import CategoryForm, ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Task, Project
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin #do widoków cbv
from django.contrib.auth.decorators import login_required #do widoków fbv
from django.views.generic import DateDetailView
from django.views.generic.dates import DayArchiveView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'title': "Kategorie",
        'categories': categories,
    }
    return render(request, "todo/index.html", context)


def task(request):
     tasks = Task.objects.all().order_by('due_date')
     context = {
        'title': "Zadania",
        'tasks': tasks,
        'data zadania': 'due_date',
    }
     return render(request, "todo/tasks.html", context)


def project(request):
    projects = Project.objects.all().order_by('title')
    context = {
        'title': "Projekty",
        'projects': projects,
    }
    return render(request, "todo/projects.html", context)


class CategoryDetails(DetailView):
        model = Category
        #queryset
        template_name = 'todo/category_details.html'
      


class TasksList(ListView):
    model = Task
    template_name = 'todo/tasks_list.html'
    # def get (self, request):
    #     tasks = task.objects.all().order_by('due_date')
    ordering = ['due_date']

class TaskDetails(DetailView):
    model = Task
    template_name = 'todo/task_details.html'


class ProjectDetails(DetailView):
        model = Project
        #queryset
        template_name = 'todo/project_details.html'


class TaskDayArchiveView(DayArchiveView):
    queryset = Task.objects.all()
    date_field = "due_date"
    allow_future = True
    template_name = 'todo/task_day.html'
    month_format = '%m' 


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'todo/category_create.html'
    fields = ('name',)
    success_url = reverse_lazy('index')   

class CategoryUpdateView(UpdateView):
    
    model = Category
    template_name = 'todo/category_update.html'
    fields = ('name',)
    def get_success_url(self):
        return reverse_lazy('category_details', kwargs={'pk': self.object.id})

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'todo/category_delete.html'
    success_url = reverse_lazy('index')

    
class ProjectCreateView(CreateView): 
    model = Project
    template_name = 'todo/project_create.html'
    fields = ('title',)
    success_url = reverse_lazy('index')   

class ProjectUpdateView(UpdateView):
    
    model = Project
    template_name = 'todo/project_update.html'
    fields = ('title',)
    def get_success_url(self):
        return reverse_lazy('project_details', kwargs={'pk': self.object.id})

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'todo/project_delete.html'
    success_url = reverse_lazy('index')


class TaskCreateView(CreateView): 
    model = Task
    template_name = 'todo/task_create.html'
    fields = ['desc', 'due_date', 'category', 'projects']
    success_url = reverse_lazy('index')   

class TaskUpdateView(UpdateView):
    
    model =Task
    template_name = 'todo/task_update.html'
    fields = ['desc', 'due_date', 'category', 'projects']
    def get_success_url(self):
        return reverse_lazy('task_details', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/tasj_delete.html'
    success_url = reverse_lazy('index')

    



