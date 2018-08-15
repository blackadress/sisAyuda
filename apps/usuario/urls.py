from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('editar/', views.editar_usuario, name='editar_usuario '),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
