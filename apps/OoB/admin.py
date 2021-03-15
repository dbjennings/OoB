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
    list_display = ('task','section','project','completed','user','created_date',)
    fieldsets = (
        (None, {'fields': ('task','project','section')}),
        ('Scheduling', {'fields': ('scheduled_date','completed_date')}),
        ('Generation/Modification', {'classes':('wide',),'fields':('user',)}),
        )
    inlines = [TagInLine]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    add_form = AdminProjectAddForm
    form = AdminProjectChangeForm
    list_display = ('project','user','created_date',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    add_form = AdminAddSectionForm
    list_display = ('section','user','created_date')