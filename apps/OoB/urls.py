from django.contrib.auth.views import LogoutView
from . import views as local_views
from django.urls import path, include

urlpatterns = [
    path('home', local_views.UserHomeView.as_view(), name='home'),
    path('inbox', local_views.UserInboxView.as_view(), name='inbox'),
    path('project/<int:pk>', local_views.UserProjectView.as_view(), name='project'),
    path('project/add', local_views.UserProjectAddView.as_view(), name='add_project'),
    path('section/add/<int:pk>', local_views.UserAddSectionView.as_view(), name='add_section'),
    path('task/add/<str:target>/<int:pk>', local_views.UserTaskAddView.as_view(), name='add_task'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('task/edit/<str:target>/<int:pk>', local_views.UserEditTaskView.as_view(), name='edit_task'),
]