from django.contrib.auth.views import LogoutView
from . import views as core_views
from django.urls import path, include

urlpatterns = [
    path('', core_views.CoreLandingView.as_view(), name='landing'),
    path('login', core_views.CoreLoginView.as_view(), name='login'),
    path('register', core_views.CoreRegisterUserView.as_view(), name='register'),
]