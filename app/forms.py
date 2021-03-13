from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms
from django.forms import fields

from .models import OobUser, Project, Task, Tag


class OobRegisterNewUserForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = OobUser
        fields = ('email','name',)


class OobUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = OobUser
        fields = ('email',)
      

class CreateNewTaskForm(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        fields = ('task',)


class TaskChangeForm(forms.ModelForm):
    
    class Meta:
        model = Task
        exclude = ('created_date', 'modified_date',)


class TagAddForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ("tag_name",)


class ProjectAddForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectChangeForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class AddTaskForm(forms.ModelForm):
    task = forms.CharField(max_length=200, 
                           widget=forms.Textarea(
                           attrs={'class': 'form-control',
                                  'placeholder': 'Type your new task here'}))

    class Meta:
        model = Task
        fields = ('task',)


class AddProjectForm(forms.ModelForm):
    project_name = forms.CharField(max_length=100, 
                                   widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Your Project Name',
                                          'cols': '200'}))

    class Meta:
        model = Project
        fields = ('project_name',)