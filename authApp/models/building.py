from django.db import models
from .location import Location

class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='building')

    class Meta:
        app_label = 'authApp'