from django.db import models
from .building import Building

class Location(models.Model):
    AREAS = [
        ('Pasillo', 'Pasillo'),
        ('Estantería', 'Estantería'),
        ('Rack', 'Rack'),
        ('Slot', 'Slot'),
        ('Posición de Pallet', 'Posición de Pallet'),
        ('Ubicación de Contenedor', 'Ubicación de Contenedor'),
        ('Zona de Recolección', 'Zona de Recolección'),
        ('Área de Consolidación', 'Área de Consolidación'),
        ('Área de Recepción', 'Área de Recepción'),
        ('Área de Envío', 'Área de Envío'),
        ('Almacenamiento a Granel', 'Almacenamiento a Granel'),
        ('Almacenamiento en Frío', 'Almacenamiento en Frío'),
        ('Almacenamiento de Materiales Peligrosos', 'Almacenamiento de Materiales Peligrosos'),
        ('Área de Desbordamiento', 'Área de Desbordamiento'),
        ('Área de Devoluciones', 'Área de Devoluciones'),
    ]

    location_id = models.AutoField(primary_key=True)
    type = models.CharField('Type', max_length=70, choices=AREAS, blank=False, null=False)
    long = models.DecimalField('Long', max_digits=10, decimal_places=3, blank=False, null=False)
    high = models.DecimalField('High', max_digits=10, decimal_places=3, blank=False, null=False)
    width = models.DecimalField('Width', max_digits=10, decimal_places=3, blank=False, null=False)
    weight = models.DecimalField('Weight', max_digits=10, decimal_places=3, blank=False, null=False)
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=3, blank=True, null=True)
    description = models.CharField('Description', max_length=250, blank=False, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='location')

    def save(self, *args, **kwargs):
        self.volume = self.long * self.high * self.width
        super(Location, self).save(*args, **kwargs)

    class Meta:
        app_label = 'authApp'