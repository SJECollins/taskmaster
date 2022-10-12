from django.shortcuts import render
from django.views import generic
from .models import Project


class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('-created_on')
    template_name = 'index.html'
