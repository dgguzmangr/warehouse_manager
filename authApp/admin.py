from django.contrib import admin

from .models.warehouse import Warehouse
from .models.building import Building
from .models.location import Location

admin.site.register(Warehouse)
admin.site.register(Building)
admin.site.register(Location)
# Register your models here.
