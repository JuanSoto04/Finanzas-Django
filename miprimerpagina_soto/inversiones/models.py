from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Categoria(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Cripto, Acciones
    
    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.usuario.username if self.usuario else 'Sin usuario'})"

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
    

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='perfil_default.png', upload_to='fotos_perfil')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()
