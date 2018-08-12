from django.db import models

# Create your models here.

class Usuario(models.Model):
    # Columnas sujetas a cambiar
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cuenta_usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    