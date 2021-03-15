from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.tag_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)

    @property
    def tasks_completed(self):
        '''
        Returns the total number of completed tasks within the section
        '''
        return self.task_set.exclude(completed_date=None).count()

    def __str__(self) -> str:
        return self.project_name


class Section(models.Model):
    section_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)

    @property
    def tasks_completed(self):
        '''
        Returns the total number of completed tasks within the section
        '''
        return self.task_set.exclude(completed_date=None).count()

    def __str__(self) -> str:
        return self.section_name


class Task(models.Model):
    task = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)
    scheduled_date = models.DateTimeField('date_scheduled', null=True, blank=True)
    completed_date = models.DateTimeField('date_completed', null=True, blank=True)

    @property
    def completed(self):
        return not (self.completed_date==None)

    def __str__(self) -> str:
        return self.task