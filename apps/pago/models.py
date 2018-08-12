from django.db import models

from apps.usuario.models import Cuenta_usuario

# Create your models here.

class Pago(models.Model):
    usuario_asignado = models.ForeignKey(Cuenta_usuario, related_name='CuentaUsuarioAsignado',on_delete=models.PROTECT)
    usuario_paga = models.ForeignKey(Cuenta_usuario, related_name='CuentaUsuarioPaga',on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=10, decimal_places=2) # Quizas? este monto es el mismo en solicitud
    fecha = models.DateTimeField('fecha de pago')
    estado = models.BooleanField(default=True)