from django.db import models

class TaskMeta(models.Model):
    progress = models.IntegerField(default=0)