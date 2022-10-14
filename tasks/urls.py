from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='index'),
    path('project/<int:project_id>', views.project_view, name='project'),
    path('add-project/', views.add_project, name='add_project'),
    path('edit-project/<int:project_id>', views.edit_project, name='edit_project'),
    path('delete-project/<int:project_id>', views.delete_project, name='delete_project'),
    path('task-list/<int:project_id>', views.task_list, name='task_list'),
    path('add_task/<int:project_id>', views.add_task, name='add_task'),
    path('edit-task/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>', views.delete_task, name='delete_task'),
]
