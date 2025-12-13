from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),

    # RUTAS PARA OPERACIONES
    path('transacciones/', TransaccionListView.as_view(), name='transacciones_list'),
    path('transacciones/nueva/', TransaccionCreateView.as_view(), name='nueva_operacion'),
    path('transacciones/editar/<int:pk>/', TransaccionUpdateView.as_view(), name='editar_operacion'),
    path('transacciones/eliminar/<int:pk>/', TransaccionDeleteView.as_view(), name='eliminar_operacion'),

    # RUTAS PARA CATEGORÍAS
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nueva/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),

    # RUTAS PARA ACTIVOS
    path('activos/', ActivoListView.as_view(), name='activos_list'),
    path('activos/nueva/', ActivoCreateView.as_view(), name='crear_activo'),
    path('activos/editar/<int:pk>/', ActivoUpdateView.as_view(), name='editar_activo'),
    path('activos/eliminar/<int:pk>/', ActivoDeleteView.as_view(), name='eliminar_activo'),

    # RUTAS PARA CUENTAS
    path('cuentas/', CuentaListView.as_view(), name='cuentas_list'),
    path('cuentas/nueva/', CuentaCreateView.as_view(), name='crear_cuenta'),
    path('cuentas/editar/<int:pk>/', CuentaUpdateView.as_view(), name='editar_cuenta'),
    path('cuentas/eliminar/<int:pk>/', CuentaDeleteView.as_view(), name='eliminar_cuenta'),

    # RUTA SOBRE MI
    path('sobre_mi/', SobreMiView.as_view(), name='sobre_mi'),

    # RUTAS LOGIN / LOGOUT
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
