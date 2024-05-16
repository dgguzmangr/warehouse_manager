from django.contrib import admin

from .models.warehouse import Warehouse
from .models.building import Building

admin.site.register(Warehouse)
admin.site.register(Building)
# Register your models here.
