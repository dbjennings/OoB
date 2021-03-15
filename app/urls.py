from django.contrib.auth.views import LogoutView
from . import views as local_views
from django.urls import path, include

urlpatterns = [
    path('home', local_views.UserHomeView.as_view(), name='home'),
    path('inbox', local_views.UserInboxView.as_view(), name='inbox'),
    path('project/<int:pk>', local_views.UserProjectView.as_view(), name='project'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('post', local_views.UserTaskAddView.as_view(), name='post'),
    path('project_add', local_views.UserProjectAddView.as_view(), name='project_add'),
    path('create_section/<int:prj>', local_views.UserAddSectionView.as_view(), name='create_section'),
    path('task/section/<int:pk>', local_views.UserTaskAddToSectionView.as_view(), name='task_to_section'),
    path('task/complete/<int:pk>', local_views.UserTaskCompleteToggleView.as_view(), name='task_complete'),
    path('task/project/<int:pk>', local_views.UserTaskAddToProjectView.as_view(), name='task_to_project')
]