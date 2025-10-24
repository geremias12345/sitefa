from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from apps.estudiante.models import Estudiante
from django.urls import reverse_lazy 
from django.views import generic
from django.db.models import Q

from apps.materia.models import Materia

class EstudianteCrearVista(generic.CreateView):
    model = Estudiante 
    fields = '__all__' 
    template_name = 'estudiante/crear.html' 
    success_url = reverse_lazy('estudiante:estudiante_leer')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lista de materias activas
        context['materias'] = Materia.objects.all()
        return context

class EstudianteActualizarVista(generic.UpdateView):
    model = Estudiante 
    fields = '__all__' 
    template_name = 'estudiante/actualizar.html' 
    success_url = reverse_lazy('estudiante:estudiante_leer')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lista de materias activas
        context['materias'] = Materia.objects.all()
        return context

class EstudianteEliminarVista(generic.DeleteView):
    model = Estudiante  
    template_name = 'estudiante/eliminar.html' 
    success_url = reverse_lazy('estudiante:estudiante_leer')

class EstudianteLeerVista(generic.ListView):
    model = Estudiante 
    fields = '__all__' 
    template_name = 'estudiante/leer.html' 
    context_object_name = 'estudiantes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar  = self.request.GET.get('buscar')
     
        if buscar:
            queryset = queryset.filter(
                Q(nombre__icontains=buscar) |
                Q(apellido__icontains=buscar)
            )
        return queryset.order_by('apellido', 'nombre')
