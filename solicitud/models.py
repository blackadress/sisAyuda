from django.db import models

from usuario.models import Usuario
# Create your models here.

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField('fecha de solicitud')
    monto = models.DecimalField(max_digits =10 ,decimal_places=2)
    estado = models.BooleanField(default=False)
