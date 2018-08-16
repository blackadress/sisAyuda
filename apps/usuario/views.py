from django.shortcuts import render, redirect

from .forms import NuevoUsuarioForm

# Create your views here.

def login_usuario(request):
    return render(request, 'usuario/login.html')

def editar_usuario(request):
    return render(request, 'usuario/editar.html')


def registrar_usuario(request):
    if request.method == 'POST':
        formUsuario = NuevoUsuarioForm(request.POST, request.FILES)
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect('login')
    else:
        formUsuario = NuevoUsuarioForm()

    context = {
        'formUsuario': formUsuario,
    }

    return render(request, 'usuario/registrar.html', context=context)


# def buscar_usuario(request):
#     if request.method == 'POST':
#         busqueda = 

#     return render(request, 'usuario/buscar.html')