from django import forms
from .models import Project, Task, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'due_date']
        widgets = {'due_date': DateInput()}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'content', 'priority', 'status']
        widgets = {
            'priority': forms.RadioSelect(),
            'status': forms.RadioSelect()
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]
