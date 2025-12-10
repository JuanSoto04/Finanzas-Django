from django import forms
from .models import Transaccion

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