from django import forms
from django.core.files.images import ImageFile

from .models import Usuario, Cuenta_usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        
        fields = [
            'dni',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'foto_perfil',
            'dni_referido',
            'contraseña',
        ]

        labels = {
            'dni': 'DNI',
            'nombres': 'Nombre(s)',
            'apellido_paterno': 'Apellido paterno',
            'apellido_materno': 'Apellido materno',
            'foto_perfil': 'Foto de perfil',
            'dni_referido': 'DNI del referente',
            'contraseña': 'Contraseña',            
        }

        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.FileInput(),
            'dni_referido': forms.NumberInput(attrs={'class': 'form-control'}),
            'contraseña': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
        }


class CuentaUsuarioForm(forms.ModelForm):

    class Meta:
        model = Cuenta_usuario

        fields = [
            'numero_cuenta',
            'entidad_bancaria',
        ]

        labels = {
            'numero_cuenta': 'Numero de cuenta',
            'entidad_bancaria': 'Entidad bancaria',
        }

        widgets = {
            'numero_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'entidad_bancaria': forms.Select(attrs={'class': 'form-control'}),
        }