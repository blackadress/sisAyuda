from django.urls import path

from apps.principal import views

app_name='principal'
urlpatterns = [
    path('index/', views.index, name='index'),

]
