from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .forms import UserProjectAddForm, UserTaskAddForm, UserAddSectionForm, UserTaskCompletedForm
from .models import Project, Section, Task


class UserTaskAddView(CreateView, LoginRequiredMixin):
    template_name = 'app/blank.html'
    form_class = UserTaskAddForm

    def get_success_url(self):
        return self.request.POST.get('next')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserTaskCompleteToggleView(UpdateView, LoginRequiredMixin):
    template_name = "app/blank.html"
    model = Task
    form_class = UserTaskCompletedForm

    def form_valid(self, form):
        '''
        Toggles the completed date between None and timezone.now()
        '''
        form_complete = self.model.objects.get(pk=form.instance.pk)
        if not form_complete.completed:
            form.instance.completed_date = timezone.now()
        else:
            form.instance.completed_date = None
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.request.POST.get('next')

class UserProjectAddView(CreateView, LoginRequiredMixin):
    ''' 
    User view for creating a new project
    '''
    template_name = "app/blank.html"
    form_class = UserProjectAddForm

    def form_valid(self, form):
        '''
        Sets the value of Project.user to the current user
        '''
        form.instance.user = self.request.user
        return super(UserProjectAddView, self).form_valid(form)
    
    def get_success_url(self):
        '''
        Returns the url of the project created
        '''
        return reverse_lazy('project', kwargs={'pk': self.object.pk})

class UserHomeView(TemplateView, LoginRequiredMixin):
    template_name = 'app/user_home.html'    

class UserInboxView(ListView, LoginRequiredMixin):
    template_name = 'app/inbox.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        '''
        Returns a queryset of all user tasks that aren't in a section or project
        '''
        return Task.objects.filter(user=self.request.user, project=None, section=None
                          ).order_by('completed_date', 'created_date')

class UserProjectView(DetailView, LoginRequiredMixin):
    template_name = 'app/user_project.html'
    model = Project
    extra_context = {'section_form': UserAddSectionForm(),
    'task_form': UserTaskAddForm(),
    }

class UserAddSectionView(CreateView, LoginRequiredMixin):
    template_name = "app/blank.html"
    form_class = UserAddSectionForm

    def get_success_url(self):
        return reverse('project', kwargs={'pk':self.kwargs['prj']})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = Project.objects.get(pk=self.kwargs['prj'])
        return super().form_valid(form)

class UserTaskAddToSectionView(CreateView, LoginRequiredMixin):
    template_name = "app/blank.html"
    form_class = UserTaskAddForm

    def get_success_url(self):
        return self.request.POST.get('next')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.section = Section.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class UserTaskAddToProjectView(CreateView, LoginRequiredMixin):
    template_name = "app/blank.html"
    form_class = UserTaskAddForm

    def get_success_url(self):
        return self.request.POST.get('next')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = Project.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)