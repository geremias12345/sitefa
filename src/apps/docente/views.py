from django.shortcuts import render
from apps.docente.models import Docente
from .models import Docente
from django.views import generic
from django.urls import reverse_lazy

#Docente
class DocenteCrearVista(generic.CreateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/crear.html'
    success_url = reverse_lazy ('docente:docente_leer')
    
class DocenteActualizarVista(generic.UpdateView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/actualizar.html'
    success_url = reverse_lazy ('docente:docente_leer')
    
    
class DocenteEliminarVista(generic.DeleteView):
    model = Docente
    fields = '__all__'
    template_name = 'docente/eliminar.html'
    success_url = reverse_lazy ('docente:docente_leer')
    
class DocenteLeerVista(generic.ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        nombre = self.request.GET.get('nombre')
        apellido = self.request.GET.get('apellido')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        return queryset.order_by('apellido', 'nombre')
    model = Docente
    fields = '__all__'
    template_name = 'docente/leer.html'
    context_object_name = 'docentes' # Esta es la variable que se utiliza para referenciar los objetos en la plantilla

