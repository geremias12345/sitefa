from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
# Modelos importados desde otras aplicaciones
from apps.horario.models import Horario
from apps.profesorado.models import Profesorado
from apps.seguridad.models import Perfil # <-- ¡IMPORTACIÓN CRUCIAL DEL MODELO PERFIL!
# Modelos de la aplicación actual
from .models import Materia


class MateriaLeerVista(ListView):
    model = Materia
    template_name = 'materia/leer.html'
    context_object_name = 'materias'
    paginate_by = 10  # cantidad de registros por página

    def get_queryset(self):
        """
        Retorna la lista de materias filtrada:
        1. Por el Profesorado si el usuario tiene el rol 'Bedel'.
        2. Por año y/o nombre (filtros existentes).
        """
        # 1. Obtiene el queryset inicial (todas las materias)
        queryset = super().get_queryset()
        
        usuario_actual = self.request.user
        
        # --- LÓGICA DE FILTRADO POR PROFESORADO (SOLO PARA BEDELES) ---
        
        # Intenta obtener el Perfil asociado al usuario logueado
        try:
            # Acceso al perfil usando el related_name='perfil'
            perfil = usuario_actual.perfil
            
            # 2. Comprobar si tiene el rol 'bedel' Y tiene un profesorado asignado
            if perfil.rol == 'bedel' and perfil.profesorado:
                
                # 3. Aplicar el filtro: solo materias con el mismo Profesorado
                # Se asume que Materia tiene un campo 'profesorado'
                queryset = queryset.filter(profesorado=perfil.profesorado)
                
            # Si el rol NO es 'bedel' (ej. 'secretaria', 'directivo'), el queryset NO se filtra aquí.
                
        except Perfil.DoesNotExist:
            # Maneja el caso en que el usuario no tiene objeto Perfil asociado
            pass
        except AttributeError:
             # Maneja si usuario_actual no existe o no tiene el atributo 'perfil'
             pass
        
        # --- LÓGICA DE FILTRADO EXISTENTE (por URL) ---
        selected_anio = self.request.GET.get('anio')
        search_query = self.request.GET.get('q')

        if selected_anio:
            queryset = queryset.filter(anio=selected_anio)

        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)

        return queryset.order_by('anio', 'nombre')


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