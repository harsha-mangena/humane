from django.contrib import admin
from .models import CookingSchedule, CleaningTask, KitchenInventory

admin.site.register(CookingSchedule)
admin.site.register(CleaningTask)
admin.site.register(KitchenInventory)