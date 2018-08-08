from django.shortcuts import render

# Create your views here.

def registrar_solicitud(request):
    return render(request, 'solicitud/registrar.html')

def editar_solicitud(request):
    return render(request, 'solicitud/editar.html')
