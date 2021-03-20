from ..models import Project, Task
from ..forms import UserTaskAddForm, UserProjectAddForm

def user_context(request):
    context = {}
    
    if request.user.is_authenticated:
        context = {
            'projects': Project.objects.filter(user=request.user, parent=None),
            'inbox_count': Task.objects.filter(user=request.user, project=None, completed_date=None).count(),
            'add_task_form': UserTaskAddForm(),
            'project_form': UserProjectAddForm(),
        }
    return context