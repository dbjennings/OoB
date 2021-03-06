from django.db import models
from django.utils import timezone

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tag_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.project_name


class Section(models.Model):
    section_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.section_name


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField('completed',default=False)
    date_created = models.DateTimeField('date created', default='django.utils.timezone.now')
    date_scheduled = models.DateTimeField('date scheduled', null=True)
    date_completed = models.DateTimeField('date completed', null=True)
    
    def __str__(self) -> str:
        return self.task_name