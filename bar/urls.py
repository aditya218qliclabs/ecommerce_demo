from django.urls import path
from .views import start_task, get_task_progress

urlpatterns = [
    path('start_task/', start_task, name='start_task'),
    path('get_task_progress/', get_task_progress, name='get_task_progress'),
]