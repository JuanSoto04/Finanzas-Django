from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Cripto, Acciones
    
    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Binance, IOL
    
    def __str__(self):
        return self.nombre

class Activo(models.Model):
    simbolo = models.CharField(max_length=10) # Ej: BTC
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.simbolo} - {self.nombre}"

class Transaccion(models.Model):
    TIPO_CHOICES = [('COMPRA', 'Compra'), ('VENTA', 'Venta')]
    
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)
    cantidad = models.DecimalField(max_digits=10, decimal_places=5)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.tipo} de {self.activo.simbolo}"
