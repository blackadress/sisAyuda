from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.registrar_solicitud, name='registrar solicitud'),
    path('editar/', views.editar_solicitud, name='editar solicitud'),
]
