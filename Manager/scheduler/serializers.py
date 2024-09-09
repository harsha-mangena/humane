from rest_framework import serializers
from .models import CookingSchedule, CleaningTask, KitchenInventory

class CookingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingSchedule
        fields = '__all__'

class CleaningTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningTask
        fields = '__all__'

class KitchenInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenInventory
        fields = '__all__'