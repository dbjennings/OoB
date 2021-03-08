from . import views as local_views
from django.urls import path, include

urlpatterns = [
    path('', local_views.LandingView.as_view(), name='landing'),
    path('login', local_views.user_login, name='login'),
    path('register', local_views.register_user, name='register'),
    path('home', local_views.user_home, name='home'),
    path('inbox', local_views.InboxView.as_view(), name='inbox'),
    path('project/<int:id>', local_views.ProjectView.as_view(), name='project'),
    path('logout', local_views.user_logout, name='logout')
]

