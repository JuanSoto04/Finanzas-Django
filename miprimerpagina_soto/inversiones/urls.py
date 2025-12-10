from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),

    # Rutas para las transacciones
    path('nueva/', TransaccionCreateView.as_view(), name='nueva_operacion')
]