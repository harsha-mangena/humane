from rest_framework import viewsets
from .models import CookingSchedule, CleaningTask, KitchenInventory
from .serializers import CookingScheduleSerializer, CleaningTaskSerializer, KitchenInventorySerializer

class CookingScheduleViewSet(viewsets.ModelViewSet):
    queryset = CookingSchedule.objects.all()
    serializer_class = CookingScheduleSerializer

class CleaningTaskViewSet(viewsets.ModelViewSet):
    queryset = CleaningTask.objects.all()
    serializer_class = CleaningTaskSerializer

class KitchenInventoryViewSet(viewsets.ModelViewSet):
    queryset = KitchenInventory.objects.all()
    serializer_class = KitchenInventorySerializer