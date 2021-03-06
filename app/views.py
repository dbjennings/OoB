from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'app/home.html'

class LoginView(TemplateView):
    template_name = 'app/login.html'

class RegisterView(TemplateView):
    template_name = 'app/register.html'

class InboxView(TemplateView):
    template_name = 'app/inbox.html'

class ProjectView(TemplateView):
    template_name = 'app/project.html'

class LandingView(TemplateView):
    template_name = 'app/landing.html'
