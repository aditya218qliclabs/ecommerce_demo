from django.shortcuts import render
from .models import TaskMeta
from .tasks import long_running_operation

def start_task(request):
    task = TaskMeta.objects.create(progress=0)
    long_running_operation.delay(task.id)
    return render(request, 'import.html', {'task_id': task.id})

from django.http import JsonResponse

def get_task_progress(request):
    task_id = request.GET.get('task_id')
    task = TaskMeta.objects.get(id=task_id)
    return JsonResponse({'progress': task.progress})
