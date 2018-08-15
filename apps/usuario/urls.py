from django.urls import path

from . import views

urlpatterns = [
    path('', views.principal, name='principal'), #cambiar a 'login'
    path('editar/', views.editar_usuario, name='editar_usuario '),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
