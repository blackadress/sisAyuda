from django.db import models

from apps.usuario.models import Cuenta_usuario

# Create your models here.

class Pago(models.Model):
    cuenta_usuario_asignado = models.ForeignKey(Cuenta_usuario, related_name='CuentaUsuarioAsignado',on_delete=models.PROTECT)
    cuenta_usuario = models.ForeignKey(Cuenta_usuario, related_name='CuentaUsuarioPaga',on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=10, decimal_places=2) # Quizas? este monto es el mismo en solicitud
    fecha = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.cuenta_usuario + self.cuenta_usuario_asignado + self.monto