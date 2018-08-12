from django.db import models

from apps.usuario.models import Usuario

# Create your models here.

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha = models.DateTimeField('fecha de solicitud')
    fecha_confirmacion = models.DateTimeField('fecha de confirmación')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    confirmacion = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
