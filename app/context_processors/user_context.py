from ..models import Project, Task
from ..forms import UserTaskAddForm, UserProjectAddForm

def user_context(request):
    context = {}
    if request.user.is_authenticated:
        context = {
            'projects': Project.objects.filter(created_by=request.user),
            'inbox_count': Task.objects.filter(created_by=request.user, project=None, section=None, completed_date=None).count(),
            'quick_task_form': UserTaskAddForm(),
            'project_form': UserProjectAddForm(),
        }
    return context