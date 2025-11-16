from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('productos/', views.productos, name='productos'),
    path('eventos/', views.eventos, name='eventos'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('contacto/', views.contacto, name='contacto'),
]
