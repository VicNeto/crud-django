from .models import TaskModel
from rest_framework.serializers import ModelSerializer

class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'name', 'description']

