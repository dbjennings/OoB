from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddProjectForm, AddTaskForm, OobRegisterNewUserForm, CreateNewTaskForm, ProjectAddForm, UserAddSectionForm
from .models import OobUser, Project, Section, Task


class UserAddTaskView(CreateView, LoginRequiredMixin):
    template_name = 'app/post.html'
    form_class = CreateNewTaskForm
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UserAddProjectView(CreateView, LoginRequiredMixin):
    ''' 
    User view for creating a new project
    '''
    template_name = "app/blank.html"
    form_class = AddProjectForm

    def form_valid(self, form):
        '''
        Sets the value of Project.created_by to the current user
        '''
        form.instance.created_by = self.request.user
        return super(ProjectAddView, self).form_valid(form)
    
    def get_success_url(self):
        '''
        Returns the url of the project created
        '''
        return reverse_lazy('project', kwargs={'pk': self.object.pk})

class UserHomeView(TemplateView, LoginRequiredMixin):
    template_name = 'app/user_home.html'
    
class CoreRegisterUserView(CreateView):
    template_name = 'app/register.html'
    form_class = OobRegisterNewUserForm
    success_url = reverse_lazy('login')
    redirect_authenticated_user = True

class CoreLoginView(LoginView):
    template_name = 'app/login.html'
    success_url = 'home'
    redirect_authenticated_user = True
    
    class Meta:
        pass

class UserInboxView(ListView, LoginRequiredMixin):
    template_name = 'app/inbox.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        '''
        Returns a queryset of all user tasks that aren't in a section or project
        '''
        return Task.objects.filter(created_by=self.request.user, project=None, section=None
                          ).order_by('completed_date', 'created_date')

class UserProjectView(DetailView, LoginRequiredMixin):
    template_name = 'app/user_project.html'
    model = Project
    extra_context = {'section_form': UserAddSectionForm(),
    'task_form': CreateNewTaskForm(),
    }

class CoreLandingView(TemplateView):
    template_name = 'app/landing.html'

class UserAddSectionView(CreateView, LoginRequiredMixin):
    template_name = "app/blank.html"
    form_class = UserAddSectionForm

    def get_success_url(self):
        return reverse('project', kwargs={'pk':self.kwargs['prj']})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.project = Project.objects.get(pk=self.kwargs['prj'])
        return super().form_valid(form)

class UserAddTaskToSection(CreateView, LoginRequiredMixin):
    template_name = "app/blank.html"
    form_class = CreateNewTaskForm

    def get_success_url(self):
        return reverse('project', kwargs={'pk':self.kwargs['prj']})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.section = Section.objects.get(pk=self.kwargs['sec'])
        return super().form_valid(form)
