from django.shortcuts import render, redirect

from apps.usuario.forms import UsuarioForm

def index(request):
    if request.method=='POST':
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('principal:index')
    else:
        form=UsuarioForm()
    return render(request, 'principal/index.html',{'form':form})
