from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import OobUser, Project, Section, Task, Tag


class CoreUserAddForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = OobUser
        fields = ('email','name',)

class CoreUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = OobUser
        fields = ('email',)



class AdminTaskAddForm(forms.ModelForm):
    task = forms.CharField(max_length=200, 
                           widget=forms.TextInput(
                           attrs={'class': 'form-control',
                                  'placeholder': 'New Task',}))
    class Meta:
        model = Task
        fields = ('task',)

class AdminTaskChangeForm(forms.ModelForm):
    
    class Meta:
        model = Task
        exclude = ('created_date', 'modified_date',)

class AdminTagAddForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ("tag_name",)

class AdminProjectAddForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

class AdminProjectChangeForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

class AdminAddSectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('section_name','project','created_by',)



class UserTaskAddForm(forms.ModelForm):
    task = forms.CharField(max_length=200, 
                           widget=forms.TextInput(
                           attrs={'class': 'form-control',
                                  'placeholder': 'New Task'}))

    class Meta:
        model = Task
        fields = ('task',)

class UserProjectAddForm(forms.ModelForm):
    project_name = forms.CharField(max_length=100, 
                                   widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Your Project Name',
                                          'cols': '200'}))

    class Meta:
        model = Project
        fields = ('project_name',)

class UserAddSectionForm(forms.ModelForm):
    section_name = forms.CharField(max_length=100, 
                                   widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Section Name',}))

    class Meta:
        model = Section
        fields = ('section_name',)