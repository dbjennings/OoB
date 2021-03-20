from django import forms

from .models import Project, Task, Tag

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

class UserTaskAddForm(forms.ModelForm):
    task = forms.CharField(max_length=200, 
                           widget=forms.TextInput(
                           attrs={'class': 'form-control',
                                  'placeholder': 'New Task'}))

    class Meta:
        model = Task
        fields = ('task',)

class UserTaskCompletedForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('completed_date',)

class UserProjectAddForm(forms.ModelForm):
    name = forms.CharField(max_length=100, 
                                   widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Your Project Name',}))

    class Meta:
        model = Project
        fields = ('name',)

