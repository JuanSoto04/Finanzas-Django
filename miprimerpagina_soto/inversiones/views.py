from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def home(request):
    # Calculamos el total invertido
    total_inversion = Transaccion.objects.aggregate(total=Sum('precio'))['total']
    # Contamos la cantidad de operaciones
    cantidad_operaciones = Transaccion.objects.count()
    # Obtenemos la última transacción realizada
    ultimas_operaciones = Transaccion.objects.order_by('-fecha')[:5]
    # Si no hay inversiones, aseguramos que total_inversion sea 0
    if total_inversion is None:
        total_inversion = 0

    
    context = {
        'total_inversion': total_inversion,
        'cantidad_operaciones': cantidad_operaciones,
        'ultimas_operaciones': ultimas_operaciones,
    }
    return render(request, 'inversiones/index.html', context)

# --------------- TRANSACCIONES ---------------

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = TransaccionForm # Usamos el form que tiene los estilos CSS
    template_name = 'inversiones/nueva_operacion.html'
    success_url = reverse_lazy('home')