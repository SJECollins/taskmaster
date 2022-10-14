from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Task, Comment
from .forms import ProjectForm, TaskForm, CommentForm


class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('due_date')
    template_name = 'index.html'


def project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project).order_by('-status', '-priority')
    context = {'project': project, 'tasks': tasks}
    return render(request, 'tasks/project.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return HttpResponse(status=204)
        else:
            print(form.errors.as_data())
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'tasks/add_project.html', context)


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, instance=project)
        if form.is_valid():
            form.save()
            return redirect('tasks:project', project_id=project_id)
        else:
            print(form.errors.as_data())
    form = ProjectForm(request.POST or None, instance=project)
    context = {'form': form}
    return render(request, 'tasks/edit_project.html', context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('tasks:index')


def task_list(request, project_id):
    tasks = Task.objects.filter(project=project_id).all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                pass
            task.project = project
            task.author = request.user
            task.save()
            return HttpResponse(status=204)
        else:
            print(form.errors.as_data())
    form = TaskForm()
    context = {'project': project, 'form': form}
    return render(request, 'tasks/add_task.html', context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:project', project_id=task.project.id)
        else:
            print(form.errors.as_data())
    form = TaskForm(request.POST or None, instance=task)
    context = {'form': form}
    return render(request, 'tasks/edit_task.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks:project', project_id=task.project.id)
