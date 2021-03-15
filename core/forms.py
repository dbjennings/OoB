from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import OobUser


class CoreUserAddForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = OobUser
        fields = ('email','name',)


class CoreUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = OobUser
        fields = ('email',)

