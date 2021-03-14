from django.contrib.auth.views import LogoutView
from . import views as local_views
from django.urls import path, include

urlpatterns = [
    path('', local_views.CoreLandingView.as_view(), name='landing'),
    path('login', local_views.CoreLoginView.as_view(), name='login'),
    path('register', local_views.CoreRegisterUserView.as_view(), name='register'),
    path('home', local_views.UserHomeView.as_view(), name='home'),
    path('inbox', local_views.UserInboxView.as_view(), name='inbox'),
    path('project/<int:pk>', local_views.UserProjectView.as_view(), name='project'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('post', local_views.UserAddTaskView.as_view(), name='post'),
    path('project_add', local_views.UserAddProjectView.as_view(), name='project_add'),
    path('create_section/<int:prj>', local_views.UserAddSectionView.as_view(), name='create_section'),
    path('section/<int:prj>/<int:sec>', local_views.UserTaskAddToSection.as_view(), name='task_to_section'),
]