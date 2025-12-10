from django import forms
from .models import Transaccion

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['activo', 'cuenta', 'tipo', 'cantidad', 'precio']
        widgets = {
            'activo': forms.Select(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }