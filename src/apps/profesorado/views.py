from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.profesorado.models import Profesorado
# Create your views here.
class ProfesoradoLeerVista(ListView):
    model = Profesorado
    template_name = 'profesorado/leer.html'
    context_object_name = 'profesorados'
    
class ProfesoradoCrearVista(CreateView):
    model = Profesorado
    fields = '__all__'
    template_name = 'profesorado/crear.html'
    success_url = reverse_lazy('profesorado:profesorado_leer')
    
class ProfesoradoActualizarVista(UpdateView): 
    model = Profesorado
    fields = '__all__'
    template_name = 'profesorado/actualizar.html'
    success_url = reverse_lazy('profesorado:profesorado_leer')

    
class ProfesoradoEliminarVista(DeleteView):
    model = Profesorado
    fields = '__all__'
    template_name = 'profesorado/eliminar.html'
    success_url = reverse_lazy('profesorado:profesorado_leer')
