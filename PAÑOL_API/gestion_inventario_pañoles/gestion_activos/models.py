from django.db import models

# Create your models here.
class Activo(models.Model):
    ELECCION_ESTADO = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    nombre_activo = models.CharField(max_length=100)
    cantidad_disponible = models.PositiveIntegerField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ELECCION_ESTADO)

    def __str__(self):
        return self.nombre_activo