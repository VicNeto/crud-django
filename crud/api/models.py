from django.db import models

# Create your models here.

class TaskModel(models.Model):
    name = models.CharField(max_length=50, default="John")
    description = models.CharField(max_length=50, null=True)
    