from django.urls import path
from . import views

urlpatterns = [
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
]

