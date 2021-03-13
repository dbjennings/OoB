from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OobRegisterNewUserForm, CreateNewTaskForm
from .models import OobUser, Project, Task


class CreateNewTaskView(CreateView, LoginRequiredMixin):
    template_name = 'app/post.html'
    form_class = CreateNewTaskForm
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OobUserHomeView(TemplateView, LoginRequiredMixin):
    template_name = 'app/user_home.html'
    
class OobRegisterNewUserView(CreateView):
    template_name = 'app/register.html'
    form_class = OobRegisterNewUserForm
    success_url = reverse_lazy('login')
    redirect_authenticated_user = True

class OobLoginView(LoginView):
    template_name = 'app/login.html'
    success_url = 'home'
    redirect_authenticated_user = True
    
    class Meta:
        pass

class InboxView(ListView, LoginRequiredMixin):
    template_name = 'app/inbox.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user).order_by('completed_date', 'created_date')
    
    def get_context_data(self, **kwargs):
        context = super(InboxView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(created_by=self.request.user)
        return context

class ProjectView(TemplateView, LoginRequiredMixin):
    template_name = 'app/user_project.html'

class LandingView(TemplateView):
    template_name = 'app/landing.html'
