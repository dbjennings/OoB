from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .project import Project
from .section import Section
from .tag import Tag

class Task(models.Model):
    task = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)
    scheduled_date = models.DateTimeField('date_scheduled', null=True, blank=True)
    completed_date = models.DateTimeField('date_completed', null=True, blank=True)

    @property
    def completed(self):
        return not (self.completed_date==None)

    def __str__(self) -> str:
        return self.task