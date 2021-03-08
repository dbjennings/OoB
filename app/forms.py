from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms
from django.db.models import fields
from django.forms import models

from .models import OobUser, Task, Tag

class OobUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = OobUser
        fields = ('email','name',)


class OobUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = OobUser
        fields = ('email',)


class OobUserLoginForm(AuthenticationForm):
    
    class Meta:
        model = OobUser
        fields = ()

class TaskAddForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'


class TaskChangeForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'


class TagAddForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ("tag_name",)
