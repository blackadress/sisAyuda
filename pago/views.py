from django.shortcuts import render

# Create your views here.

def registrar_pago(request):
    return render(request, 'pago/registrar.html')

def confirmar_pago(request):
    return render(request, 'pago/confirmar.html')
