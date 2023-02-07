from celery import shared_task
from .models import TaskMeta

@shared_task
def long_running_operation(task_id):
    task = TaskMeta.objects.get(id=task_id)
    for i in range(100):
        # Perform a long-running operation here
        task.progress = i
        task.save()
    return 'Task completed!'