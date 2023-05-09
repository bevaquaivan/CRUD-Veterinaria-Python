from django.urls import path
from . import views

app_name = 'Veterinaria'


urlpatterns = [
    path('', views.home, name= "home"),
    path('cliente', views.cliente, name= "cliente"),
    path('editarcliente/<int:id>', views.editarcliente, name='editarcliente'),
    ]