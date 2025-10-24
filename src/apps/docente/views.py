from django.shortcuts import render
from apps.docente.models import Docente
from apps.materia.models import Materia
from .models import Docente
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

#Docente
class DocenteCrearVista(generic.CreateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/crear.html'
    success_url = reverse_lazy ('docente:docente_leer')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lista de materias activas
        context['materias'] = Materia.objects.all()
        return context
    
class DocenteActualizarVista(generic.UpdateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/actualizar.html'
    success_url = reverse_lazy ('docente:docente_leer')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lista de materias activas
        context['materias'] = Materia.objects.all()
        return context
    
    
class DocenteEliminarVista(generic.DeleteView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/eliminar.html'
    success_url = reverse_lazy ('docente:docente_leer')
    
class DocenteLeerVista(generic.ListView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/leer.html'
    context_object_name = 'docentes' # Esta es la variable que se utiliza para referenciar los objetos en la plantilla
    def get_queryset(self):
        queryset = super().get_queryset()
        buscar  = self.request.GET.get('buscar')
     
        if buscar:
            queryset = queryset.filter(
                Q(nombre__icontains=buscar) |
                Q(apellido__icontains=buscar)
            )
        return queryset.order_by('apellido', 'nombre')