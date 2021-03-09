from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms

from .models import OobUser, Task, Tag


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
