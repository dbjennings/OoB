from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView

from .forms import CoreUserAddForm

class CoreLoginView(LoginView):
    template_name = 'core/login.html'
    success_url = 'home'
    redirect_authenticated_user = True
    
    class Meta:
        pass

class CoreRegisterUserView(CreateView):
    template_name = 'core/register.html'
    form_class = CoreUserAddForm
    success_url = reverse_lazy('login')
    redirect_authenticated_user = True

class CoreLandingView(TemplateView):
    template_name = 'core/landing.html'