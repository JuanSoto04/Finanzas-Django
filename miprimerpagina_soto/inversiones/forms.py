from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['activo', 'cuenta', 'tipo', 'cantidad', 'precio', 'fecha'] 
        widgets = {
            'activo': forms.Select(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cripto, Acciones...'}),
        }

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ['simbolo', 'nombre', 'categoria'] # Pedimos Símbolo, Nombre y su Categoría
        widgets = {
            'simbolo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: AAPL, BTC'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Apple Inc., Bitcoin'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}), # Lista desplegable
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Binance, Banco Galicia, Caja Fuerte...'}),
        }

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']