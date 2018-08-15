from django.shortcuts import render, redirect

from apps.usuario.forms import UsuarioForm
from apps.principal.models import Banner

def index(request):
    if request.method=='POST':
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('principal:index')
    else:
        form=UsuarioForm()

    banner = Banner.objects.all()

    return render(request, 'principal/index.html',{'form':form,'banner':banner})
