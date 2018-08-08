from django.shortcuts import render

# Create your views here.

# Pago
def confirmar_pago(request):
    return render(request, 'pago/confirmar.html')

def registrar_pago(request):
    return render(request, 'pago/registrar.html')

# Solicitud
def editar_solicitud(request):
    return render(request, 'solicitud/editar.html')

def registrar_solicitud(request):
    return render(request, 'solicitud/registrar.html')

# Usuario
def editar_usuario(request):
    return render(request, 'usuario/editar.html')

def registrar_usuario(request):
    return render(request, 'usuario/registrar.html')
