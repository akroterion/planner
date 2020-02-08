from django.urls import path
from . import views
from .views import TaskDayArchiveView

urlpatterns = [
    path('', views.index, name="index"),
    path('tasks/', views.task, name="tasks"),
    path('projects/', views.project, name="projects"),
    path('category/<int:pk>/', views.CategoryDetails.as_view(), name='category_details'),
    path('category/new', views.CategoryCreateView.as_view(),
         name='category_create'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(),
         name='category_update'),
          path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(),
         name='category_delete'), 
    path('tasks_list/', views.TasksList.as_view(), name='tasks_list'), 
    path ('project/<int:pk>/', views.ProjectDetails.as_view(), name='project_details'),
    path('<int:year>/<str:month>/<int:day>/',
         TaskDayArchiveView.as_view(),
         name="task_day"),
    path('project/new', views.ProjectCreateView.as_view(),
         name='project_create'),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(),
         name='project_update'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(),
         name='project_delete'), 

    path ('task/<int:pk>/', views.TaskDetails.as_view(), name='task_details'),
    path('task/new', views.TaskCreateView.as_view(),
         name='task_create'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(),
         name='task_update'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(),
         name='task_delete'), 

         
    # path('create_category/', views.createCategory, name="create_category" )
    # path('category/add/', views.CategoryCreate.as_view(), name="category_create"),

]

