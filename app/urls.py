from .views import HomeView, InboxView, LoginView, ProjectView, RegisterView
from django.urls import path, include

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('home', HomeView.as_view(), name='home'),
    path('inbox', InboxView.as_view(), name='inbox'),
    path('project/<int:id>', ProjectView.as_view(), name='project')
]

