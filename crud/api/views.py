from rest_framework.viewsets import ModelViewSet
from .models import TaskModel
from .serializers import TaskSerializer

# Create your views here.

class TaskViewset(ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
