from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import OobUser, Task, Tag

@admin.register(OobUser)
class OobUserAdmin(UserAdmin):
    add_form = OobRegisterNewUserForm
    form = OobUserChangeForm
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
    add_form = TagAddForm

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    add_form = CreateNewTaskForm
    form = TaskChangeForm
    list_display = ('task','section','project','completed','created_by','created_date',)
    fieldsets = (
        (None, {'fields': ('task',)}),
        ('Generation/Modification', {'classes':('wide',),'fields':('created_by',)}),
        ('Scheduling', {'fields':('scheduled_date','completed_date')})
    )
    inlines = [TagInLine]

