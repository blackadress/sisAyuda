from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Usuario(models.Model):
    dni = models.IntegerField(
        primary_key=True,
        validators=[MinValueValidator(10000000), MaxValueValidator(99999999)],
        )
    dni_referido = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    contraseña = models.CharField(max_length=100)
    foto_perfil = models.ImageField(blank=True, upload_to='usuario')

    def __str__(self):
        return self.nombres


class Entidad_bancaria(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, upload_to='entidades_bancarias')

    def __str__(self):
        return self.nombre


class Cuenta_usuario(models.Model):
    numero_cuenta = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    entidad_bancaria = models.ForeignKey(Entidad_bancaria, on_delete=models.PROTECT)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return str(self.numero_cuenta)
