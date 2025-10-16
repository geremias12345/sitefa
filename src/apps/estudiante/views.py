from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from apps.estudiante.models import Estudiante
from django.urls import reverse_lazy 
from django.views import generic
class EstudianteCrearVista(generic.CreateView):
    model = Estudiante 
    fields = '__all__' 
    template_name = 'estudiante/crear.html' 
    success_url = reverse_lazy('estudiante:estudiante_leer')

class EstudianteActualizarVista(generic.UpdateView):
    model = Estudiante 
    fields = '__all__' 
    template_name = 'estudiante/actualizar.html' 
    success_url = reverse_lazy('estudiante:estudiante_leer')

class EstudianteEliminarVista(generic.DeleteView):
    model = Estudiante  
    template_name = 'estudiante/eliminar.html' 
    success_url = reverse_lazy('estudiante:estudiante_leer')

class EstudianteLeerVista(generic.ListView):
    model = Estudiante 
    fields = '__all__' 
    template_name = 'estudiante/leer.html' 
    context_object_name = 'estudiantes'
