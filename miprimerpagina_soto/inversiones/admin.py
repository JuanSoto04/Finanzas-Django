from django.contrib import admin
from .models import Categoria, Activo, Cuenta, Transaccion

# Esto hace que aparezcan en el panel de admin
admin.site.register(Categoria)
admin.site.register(Activo)
admin.site.register(Cuenta)
admin.site.register(Transaccion)