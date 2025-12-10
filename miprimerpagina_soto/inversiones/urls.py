from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),

    # Rutas para las transacciones
    path('nueva/', TransaccionCreateView.as_view(), name='nueva_operacion'),
    path('editar/<int:pk>/', TransaccionUpdateView.as_view(), name='editar_operacion'),
    path('eliminar/<int:pk>/', TransaccionDeleteView.as_view(), name='eliminar_operacion'),
]