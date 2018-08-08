from django.db import models

from usuario.models import Usuario
# Create your models here.

class Pago(models.Model):
    usuario_asignado = models.ForeignKey(Usuario, related_name = 'usuarioAsignado',on_delete=models.PROTECT)
    usuario_paga = models.ForeignKey(Usuario, related_name = 'usuarioPaga',on_delete=models.PROTECT)
    fecha = models.DateTimeField('fecha de pago')
    estado = models.BooleanField(default=False)

class Requisitos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField('fecha de creación')
    fecha_ultima_modificacion = models.DateTimeField('última modificación')
    estado = models.BooleanField(default=False)
