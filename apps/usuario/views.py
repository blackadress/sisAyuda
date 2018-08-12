from django.shortcuts import render

# Create your views here.

def editar_usuario(request):
    return render(request, 'usuario/editar.html')


def registrar_usuario(request):
    return render(request, 'usuario/registrar.html')