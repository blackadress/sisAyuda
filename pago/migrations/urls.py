from django.urls import paths

from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar usuario'),
    path('editar/', views.editar_usuario, name='editar usuario'),
]
