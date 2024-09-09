from django.db import models

# Model for Cooking Schedule
class CookingSchedule(models.Model):
    meal_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.meal_name} at {self.time} on {self.date}"

# Model for Cleaning Schedule
class CleaningTask(models.Model):
    task_name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50, choices=[('daily', 'Daily'), ('weekly', 'Weekly')])

    def __str__(self):
        return self.task_name

# Model for Kitchen Inventory
class KitchenInventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    low_stock_alert = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} - {self.quantity}"