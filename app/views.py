from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import HttpRequest
from django.contrib import messages

from .forms import OobUserCreationForm, OobUserLoginForm
from .models import OobUser

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

def user_login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = OobUserLoginForm(request=request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, f'{email} - {password}')
                messages.error(request, "Invalid E-mail/Password Combination 1")

        else:
            messages.error(request, "Invalid E-mail/Password Combination 2")
    
    form = OobUserLoginForm()
    context = {'form': form, 'messages': messages.get_messages(request)}
    return render(request, 'app/login.html', context)

def user_home(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect('landing')
    
    user = OobUser.objects.get(pk=request.user.pk)
    context = {'user':user}

    return render(request, 'app/home.html', context)

def user_logout(request: HttpRequest):
    logout(request)
    return redirect('landing')

class RegisterView(TemplateView):
    template_name = 'app/register.html'

class InboxView(TemplateView):
    template_name = 'app/inbox.html'

class ProjectView(TemplateView):
    template_name = 'app/project.html'

class LandingView(TemplateView):
    template_name = 'app/landing.html'
