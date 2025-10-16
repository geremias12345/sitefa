from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.materia.models import Materia
from .models import Asistencia

class AsistenciaLeerView(ListView):
    model = Asistencia
    template_name = 'asistencia/leer.html'
    context_object_name = 'asistencias'
    paginate_by = 10

    def get_queryset(self):
        queryset = Asistencia.objects.select_related('estudiante', 'materia').all().order_by(
            'materia__anio', 'materia', '-fecha'
        )

        # Filtrado por año (de la materia)
        anio = self.request.GET.get('anio')
        if anio not in [None, '']:
            queryset = queryset.filter(materia__anio=anio)

        # Filtrado por materia
        materia_id = self.request.GET.get('materia')
        if materia_id not in [None, '']:
            queryset = queryset.filter(materia_id=materia_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anios'] = range(1, 5)  # 1º a 4º año
        context['materias'] = Materia.objects.all()
        context['selected_anio'] = self.request.GET.get('anio', '')
        context['selected_materia'] = self.request.GET.get('materia', '')
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Datos para los filtros
        context['anios'] = range(1, 5)  # 1º a 4º año
        context['materias'] = Materia.objects.all()
        context['selected_anio'] = self.request.GET.get('anio', '')
        context['selected_materia'] = self.request.GET.get('materia', '')
        return context
    
class AsistenciaCrearView(CreateView):
    model = Asistencia
    fields = '__all__'
    template_name = 'asistencia/crear.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')

class AsistenciaActualizarView(UpdateView):
    model = Asistencia
    fields = '__all__'
    template_name = 'asistencia/actualizar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')
    
class AsistenciaEliminarView(DeleteView):
    model = Asistencia
    fields = '__all__'
    template_name = 'asistencia/eliminar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')

