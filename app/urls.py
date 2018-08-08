from django.urls import path

from . import views

urlpatterns = [
    path('Pago/confirmar/', views.confirmar_pago, name='confirmar pago'),
    path('Pago/registrar/', views.registrar_pago, name='registrar pago'),
    path('Solicitud/editar/', views.editar_solicitud, name='editar solicitud '),
    path('Solicitud/registrar/', views.registrar_solicitud, name='registrar solicitud'),
    path('Usuario/editar/', views.editar_usuario, name='editar usuario '),
    path('Usuario/registrar/', views.registrar_usuario, name='registrar usuario'),
]
