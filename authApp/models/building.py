from django.db import models
from .warehouse import Warehouse

class Building(models.Model):
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='building')

    class Meta:
        app_label = 'authApp'