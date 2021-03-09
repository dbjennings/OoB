from django.contrib.auth.views import LogoutView
from . import views as local_views
from django.urls import path, include

urlpatterns = [
    path('', local_views.LandingView.as_view(), name='landing'),
    path('login', local_views.OobLoginView.as_view(), name='login'),
    path('register', local_views.OobRegisterNewUserView.as_view(), name='register'),
    path('home', local_views.OobUserHomeView.as_view(), name='home'),
    path('inbox', local_views.InboxView.as_view(), name='inbox'),
    path('project/<int:id>', local_views.ProjectView.as_view(), name='project'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('post', local_views.CreateNewTaskView.as_view(), name='post'),
]