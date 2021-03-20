from django.contrib import admin

from .forms import *
from .models import Task, Tag

class TagInLine(admin.TabularInline):
    model = Task.tags.through
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    add_form = AdminTagAddForm

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    add_form = AdminTaskAddForm
    form = AdminTaskChangeForm
    list_display = ('task','project','completed','user','created_date',)
    fieldsets = (
        (None, {'fields': ('task','project')}),
        ('Scheduling', {'fields': ('scheduled_date','completed_date')}),
        ('Generation/Modification', {'classes':('wide',),'fields':('user',)}),
        )
    inlines = [TagInLine]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    add_form = AdminProjectAddForm
    form = AdminProjectChangeForm
    list_display = ('name','user','created_date',)