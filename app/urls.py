from .views import *
from django.urls import path, include

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('login', LoginView.as_view(), name='login'),
    path('register', register_user, name='register'),
    path('home', HomeView.as_view(), name='home'),
    path('inbox', InboxView.as_view(), name='inbox'),
    path('project/<int:id>', ProjectView.as_view(), name='project')
]

