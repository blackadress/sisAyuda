from django.urls import path

from . import views

urlpatterns = [
    path('editar/', views.editar_usuario, name='editar usuario '),
    path('registrar/', views.registrar_usuario, name='registrar usuario'),
]
