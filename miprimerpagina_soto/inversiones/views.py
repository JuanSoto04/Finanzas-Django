from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
import datetime
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

    hoy = datetime.date.today()
    inversion_mes = Transaccion.objects.filter(
        tipo='COMPRA',
        fecha__year=hoy.year,
        fecha__month=hoy.month
    ).aggregate(total=Sum('precio'))['total'] or 0

    # DATOS PARA EL GRÁFICO (Cripto vs Acciones vs Bonos Vs Etfs) ---
    # Se crean dos listas: una con los nombres y otra con los montos
    nombres_grafico = []
    monto_grafico = []
    categorias = Categoria.objects.all()

    for cat in categorias:
        # Sumamos las compras por categoría
        total_cat = Transaccion.objects.filter(activo__categoria=cat, tipo='COMPRA').aggregate(total=Sum('precio'))['total'] or 0
        
        # Solo se agrega al gráfico si hay dinero invertido
        if total_cat > 0:
            nombres_grafico.append(cat.nombre)
            monto_grafico.append(float(total_cat))

    context = {
        'total_invertido': total_inversion,
        'cantidad_operaciones': cantidad_operaciones,
        'inversion_mes': inversion_mes,      
        'ultimas_operaciones': ultimas_operaciones,
        'labels_grafico': nombres_grafico,    
        'data_grafico': monto_grafico,        
    }
    return render(request, 'inversiones/index.html', context)

# --------------- TRANSACCIONES ---------------

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = TransaccionForm # Usamos el form que tiene los estilos CSS
    template_name = 'inversiones/nueva_operacion.html'
    success_url = reverse_lazy('home')