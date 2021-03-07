from django.db import models
from django.utils import timezone
from django.conf import settings

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
    # !!! Remove null=True when user functionality added
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date created')
    modified_date = models.DateTimeField('date modified')
    scheduled_date = models.DateTimeField('date scheduled', null=True)
    completed_date = models.DateTimeField('date completed', null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Task, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.task_name