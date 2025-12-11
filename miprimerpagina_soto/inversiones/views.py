from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum, F, Case, When, DecimalField
import datetime
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

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

    # LÓGICA GRÁFICO DE EVOLUCIÓN (Línea de tiempo) ---

    # Agrupamos por fecha y sumamos las compras y ventas
    evolucion_data = Transaccion.objects.values('fecha').annotate(
        neto=Sum(
            Case(
                When(tipo='COMPRA', then=F('precio')),
                When(tipo='VENTA', then=-F('precio')), # Restamos si es venta
                output_field=DecimalField()
            )
        )
    ).order_by('fecha')

    # Calculamos el acumulado día a día
    fechas_evolucion = []
    montos_evolucion = []
    acumulado = 0

    for dato in evolucion_data:
        acumulado += float(dato['neto'])
        # Formateamos la fecha a día/mes
        fechas_evolucion.append(dato['fecha'].strftime("%d/%m"))
        montos_evolucion.append(acumulado)

    context = {
        'total_inversion': total_inversion,
        'cantidad_operaciones': cantidad_operaciones,
        'inversion_mes': inversion_mes,      
        'ultimas_operaciones': ultimas_operaciones,
        'nombres': nombres_grafico,
        'montos': monto_grafico,
        'fechas_evolucion': fechas_evolucion,
        'montos_evolucion': montos_evolucion,        
    }
    return render(request, 'inversiones/index.html', context)

# --------------- TRANSACCIONES ---------------

class TransaccionListView(ListView):
    model = Transaccion
    template_name = 'inversiones/transaccion_list.html'
    context_object_name = 'transacciones'
    ordering = ['-fecha']  # Ordenamos por fecha descendente
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Historial de Operaciones"
        context['create_url'] = reverse_lazy('nueva_operacion') 
        return context

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = TransaccionForm # Usamos el form que tiene los estilos CSS
    template_name = 'inversiones/nueva_operacion.html'
    success_url = reverse_lazy('home')

class TransaccionUpdateView(UpdateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = 'inversiones/nueva_operacion.html'
    success_url = reverse_lazy('home')

class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = 'inversiones/eliminar_operacion.html'
    success_url = reverse_lazy('home')

# --------------- CATEGORIAS ---------------

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'inversiones/categoria_list.html'
    context_object_name = 'categorias'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Gestión de Categorías"
        context['create_url'] = reverse_lazy('crear_categoria') 
        return context

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inversiones/generico_form.html'
    success_url = reverse_lazy('categoria_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Categoría"
        context['cancel_url'] = reverse_lazy('categoria_list')
        return context

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inversiones/generico_form.html'
    success_url = reverse_lazy('categoria_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Categoría"
        context['cancel_url'] = reverse_lazy('categoria_list')
        return context

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'inversiones/eliminar_generico.html'
    success_url = reverse_lazy('categoria_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Categoría"
        context['cancel_url'] = reverse_lazy('categoria_list')
        return context
    
# --------------- ACTIVOS ---------------
# --- CRUD DE ACTIVOS ---

class ActivoListView(ListView):
    model = Activo
    template_name = 'inversiones/activos_list.html'
    context_object_name = 'activos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Gestión de Activos"
        context['create_url'] = reverse_lazy('crear_activo')
        return context


class ActivoCreateView(CreateView):
    model = Activo
    form_class = ActivoForm
    template_name = 'inversiones/generico_form.html'
    success_url = reverse_lazy('activos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Activo"
        context['cancel_url'] = reverse_lazy('activos_list')
        return context


class ActivoUpdateView(UpdateView):
    model = Activo
    form_class = ActivoForm
    template_name = 'inversiones/generico_form.html'
    success_url = reverse_lazy('activos_list')
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Activo"
        context['cancel_url'] = reverse_lazy('activos_list')
        return context


class ActivoDeleteView(DeleteView):
    model = Activo
    template_name = 'inversiones/eliminar_generico.html'
    success_url = reverse_lazy('activos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Activo"
        context['cancel_url'] = reverse_lazy('activos_list')
        return context

# --------------- CUENTAS ---------------

class CuentaListView(ListView):
    model = Cuenta
    template_name = 'inversiones/cuentas_list.html'
    context_object_name = 'cuentas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Gestión de Cuentas"
        context['create_url'] = reverse_lazy('crear_cuenta')
        return context

class CuentaCreateView(CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'inversiones/generico_form.html' 
    success_url = reverse_lazy('cuentas_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Cuenta"
        context['cancel_url'] = reverse_lazy('cuentas_list')
        return context

class CuentaUpdateView(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'inversiones/generico_form.html' 
    success_url = reverse_lazy('cuentas_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Cuenta"
        context['cancel_url'] = reverse_lazy('cuentas_list')
        return context

class CuentaDeleteView(DeleteView):
    model = Cuenta
    template_name = 'inversiones/eliminar_generico.html'   
    success_url = reverse_lazy('cuentas_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Cuenta"
        context['cancel_url'] = reverse_lazy('cuentas_list')
        return context


# SOBRE MI
class SobreMiView(TemplateView): # USE TEMPLATEVIEW PORQUE SE RECOMIENDA PARA PÁGINAS ESTÁTICAS
    template_name = "inversiones/sobre_mi.html"