from django.db import models
from accounts.models import CustomUser


PRIORITIES = (('!', '!'), ('!!', '!!'), ('!!!', '!!!'))
STATUSES = (('ToDo', 'ToDo'), ('In Progress', 'In Progress'), ('Done', 'Done'))


class Project(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    edited_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=240)
    added_on = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=12, choices=PRIORITIES, default='!')
    status = models.CharField(max_length=12, choices=STATUSES, default='ToDo')
    edited_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    body = models.CharField(max_length=180)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'"{self.body}"\nby {self.author} on {self.added_on}'
