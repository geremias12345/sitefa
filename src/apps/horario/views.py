from django.shortcuts import render
from .models import Horario, Materia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HorarioCrearVista(CreateView):
    model = Horario
    fields = '__all__'
    template_name = 'horario/crear.html'
    success_url = reverse_lazy('horario:horario_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Lista de materias disponibles
        context['materias'] = Materia.objects.all()

        return context

class HorarioLeerVista(ListView):
    model = Horario
    template_name = 'horario/leer.html'
    context_object_name = 'horarios' #Esta es la variable que se usará en el template con {% for curso in cursos %} para mostrar los cursos

class HorarioActualizarVista(UpdateView):
    model = Horario
    fields = '__all__'
    template_name = 'horario/actualizar.html'
    success_url = reverse_lazy('horario:horario_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Todas las materias disponibles
        context['materias'] = Materia.objects.all()

        # El horario actual (el objeto que se está editando)
        horario = self.object

        # Valores actuales del horario (para mostrarlos como default)
        context['selected_materia'] = horario.materia.id if horario.materia else None
        context['selected_dia'] = horario.dia_semana
        context['hora_inicio'] = horario.hora_inicio.strftime("%H:%M") if horario.hora_inicio else ""
        context['hora_fin'] = horario.hora_fin.strftime("%H:%M") if horario.hora_fin else ""

        return context


class HorarioEliminarVista(DeleteView):
    model = Horario
    template_name = 'horario/eliminar.html'
    success_url = reverse_lazy('horario:horario_leer')

# Create your views here.

