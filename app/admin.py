from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import OobUser, Task, Tag

@admin.register(OobUser)


class CoreUserAdmin(UserAdmin):
    add_form = CoreUserAddForm
    form = CoreUserChangeForm
    model = OobUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

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
    list_display = ('task','section','project','completed','created_by','created_date',)
    fieldsets = (
        (None, {'fields': ('task','project','section')}),
        ('Scheduling', {'fields': ('scheduled_date','completed_date')}),
        ('Generation/Modification', {'classes':('wide',),'fields':('created_by',)}),
        )
    inlines = [TagInLine]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    add_form = AdminProjectAddForm
    form = AdminProjectChangeForm
    list_display = ('project_name','created_by','created_date',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    add_form = AdminAddSectionForm
    list_display = ('section_name','created_by','created_date')