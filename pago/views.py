from django.shortcuts import render

# Create your views here.

def registrar_usuario(request):
    return render(request, 'usuario/registrar.html')

def editar_usuario(request):
    return render(request, 'usuario/editar.html')
