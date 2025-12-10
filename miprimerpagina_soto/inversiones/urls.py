from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),

    # --- RUTAS PARA OPERACIONES ---
    path('nueva/', TransaccionCreateView.as_view(), name='nueva_operacion'),
    path('editar/<int:pk>/', TransaccionUpdateView.as_view(), name='editar_operacion'),
    path('eliminar/<int:pk>/', TransaccionDeleteView.as_view(), name='eliminar_operacion'),

    # --- RUTAS PARA CATEGORÍAS ---
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nueva/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),
]