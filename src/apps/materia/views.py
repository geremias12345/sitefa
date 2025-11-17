from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.horario.models import Horario
from apps.profesorado.models import Profesorado
from .models import Materia


class MateriaLeerVista(ListView):
    model = Materia
    template_name = 'materia/leer.html'
    context_object_name = 'materias'
    paginate_by = 10  # cantidad de registros por página

    def get_queryset(self):
        """
        Retorna la lista de materias filtrada por año y/o nombre.
        """
        queryset = super().get_queryset()
        selected_anio = self.request.GET.get('anio')
        search_query = self.request.GET.get('q')

        if selected_anio:
            queryset = queryset.filter(anio=selected_anio)

        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)

        return queryset.order_by('anio', 'nombre')

    def get_context_data(self, **kwargs):
        """
        Agrega variables adicionales al contexto: lista de años,
        año seleccionado y texto de búsqueda.
        """
        context = super().get_context_data(**kwargs)
        anios = Materia.objects.values_list(
            'anio', flat=True).distinct().order_by('anio')

        context['anios'] = anios
        context['selected_anio'] = self.request.GET.get('anio', '')
        context['search_query'] = self.request.GET.get('q', '')

        return context


class MateriaCrearVista(CreateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/crear.html'
    success_url = reverse_lazy('materia:materia_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Lista de años disponibles
        context['anios'] = ['1', '2', '3', '4']

        # Lista de profesorados
        context['profesorados'] = Profesorado.objects.all()

        # Lista de duraciones según el modelo
        context['DURACION'] = Materia.DURACION

        # Valores seleccionados
        context['selected_anio'] = self.request.GET.get('anio', None)
        context['selected_profesorado'] = self.request.GET.get('profesorado', None)
        context['selected_duracion'] = self.request.GET.get('duracion', 'Anual')

        return context


class MateriaActualizarVista(UpdateView):
    model = Materia
    fields = '__all__'
    template_name = 'materia/actualizar.html'
    success_url = reverse_lazy('materia:materia_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anios'] = ['1', '2', '3', '4']
        context['profesorados'] = Profesorado.objects.all()
        # Valores seleccionados para mantener selección
        if self.object:
            context['selected_anio'] = self.object.anio
            context['selected_profesorado'] = self.object.profesorado.id
        return context


class MateriaEliminarVista(DeleteView):
    model = Materia
    template_name = 'materia/eliminar.html'
    success_url = reverse_lazy('materia:materia_leer')


class MateriaDetalleVista(DetailView):
    model = Materia
    template_name = 'materia/detalle.html'
    context_object_name = 'materia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Horarios asociados a esta materia
        context['horarios'] = Horario.objects.filter(materia=self.object)
        return context
