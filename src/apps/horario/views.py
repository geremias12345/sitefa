from django.shortcuts import render
from apps.horario.models import Horario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HorarioCrearVista(CreateView):
    model = Horario
    fields = '__all__'
    template_name = 'horario/crear.html'
    success_url = reverse_lazy('horario:horario_leer')

class HorarioLeerVista(ListView):
    model = Horario
    template_name = 'horario/leer.html'
    context_object_name = 'horarios' #Esta es la variable que se usará en el template con {% for curso in cursos %} para mostrar los cursos

class HorarioActualizarVista(UpdateView):
    model = Horario
    fields = '__all__'
    template_name = 'horario/actualizar.html'
    success_url = reverse_lazy('horario:horario_leer')


class HorarioEliminarVista(DeleteView):
    model = Horario
    template_name = 'horario/eliminar.html'
    success_url = reverse_lazy('horario:horario_leer')

# Create your views here.

