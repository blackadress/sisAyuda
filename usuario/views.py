from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registrar_usuario(request):

    return render(request, 'usuario/registrar.html')

def editar_usuario(request):
    return render(request, 'usuario/editar.html')
