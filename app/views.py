from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.http import HttpRequest

from .forms import OobUserCreationForm

def register_user(request: HttpRequest):
    # Checks to see if a user is already logged in
    # !!! Change this functionality into a decorator
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = OobUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email,password=password)
            login(request, user)
            return redirect('home')
    else:
        form = OobUserCreationForm
        return render(request, 'app/register.html', {'form':form})

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
