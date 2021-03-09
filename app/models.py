from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from .managers import OobUserManager



class OobUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('first name'), max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = OobUserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    @property
    def first_name(self):
        return self.name.split(' ')[0]

    def __str__(self):
        return self.email

    
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.tag_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)

    def __str__(self) -> str:
        return self.project_name


class Section(models.Model):
    section_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)

    def __str__(self) -> str:
        return self.section_name


class Task(models.Model):
    task = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField('date_created', editable=False, auto_now_add=True)
    modified_date = models.DateTimeField('date_modified', auto_now=True)
    scheduled_date = models.DateTimeField('date_scheduled', null=True)
    completed_date = models.DateTimeField('date_completed', null=True)

    @property
    def completed(self):
        return not (self.completed_date==None)

    # def save(self, *args, **kwargs):

    def __str__(self) -> str:
        return self.task