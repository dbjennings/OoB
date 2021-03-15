from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .project import Project



class Section(models.Model):
    section = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)

    @property
    def tasks_completed(self):
        '''
        Returns the total number of completed tasks within the section
        '''
        return self.task_set.exclude(completed_date=None).count()

    def __str__(self) -> str:
        return self.section