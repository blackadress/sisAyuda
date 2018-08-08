from django.db import models

# Create your models here.
class Usuario(models.Model):
    # Columnas sujetas a cambiar
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField('fecha de solicitud')
    monto = models.DecimalField(max_digits =10 ,decimal_places=2)
    estado = models.BooleanField(default=False)

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
