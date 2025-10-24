from datetime import date
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.estudiante.models import Estudiante
from apps.materia.models import Materia
from .models import Asistencia
from django.shortcuts import redirect


class AsistenciaLeerView(ListView):
    model = Asistencia
    template_name = 'asistencia/leer.html'
    context_object_name = 'asistencias'
    paginate_by = 10 # cantidad de registros por página

    def get_queryset(self):
        queryset = Asistencia.objects.select_related('estudiante', 'materia').all().order_by(
            'materia__anio', 'materia', 'estudiante__apellido', '-fecha' 
        )

        anio = self.request.GET.get('anio')
        if anio:
            queryset = queryset.filter(materia__anio=anio)

        materia_id = self.request.GET.get('materia')
        if materia_id:
            queryset = queryset.filter(materia_id=materia_id)

        
        estudiante_id = self.request.GET.get('estudiante')
        if estudiante_id:
            queryset = queryset.filter(estudiante_id=estudiante_id)

        estado = self.request.GET.get('estado')
        if estado == 'ausente':
            queryset = queryset.filter(presente=False)
        elif estado == 'presente':
            queryset = queryset.filter(presente=True)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
   
        context['anios'] = range(1, 5) 
        context['materias'] = Materia.objects.all().order_by('nombre')
        context['estudiantes'] = Estudiante.objects.all().order_by('apellido', 'nombre')
        

        context['selected_anio'] = self.request.GET.get('anio', '')
        context['selected_materia'] = self.request.GET.get('materia', '')
        context['selected_estudiante'] = self.request.GET.get('estudiante', '')
        context['selected_estado'] = self.request.GET.get('estado', 'todos')

        full_queryset = self.get_queryset()
        
        total_registros = full_queryset.count()
        total_ausencias = full_queryset.filter(presente=False).count()
        
        context['total_registros'] = total_registros
        context['total_ausencias'] = total_ausencias
        
        if total_registros > 0:
            context['porcentaje_asistencia'] = round(
                (total_registros - total_ausencias) / total_registros * 100, 1
            )
        else:
            context['porcentaje_asistencia'] = 0

        return context
    

class AsistenciaCrearView(CreateView):
    model = Asistencia
    fields = ['justificacion'] 
    template_name = 'asistencia/crear.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias'] = Materia.objects.all()
        context['today'] = date.today().isoformat()

        # Filtrar estudiantes según la materia seleccionada
        materia_id = self.request.GET.get('materia')
        context['estudiantes'] = []
        context['selected_materia'] = None

        if materia_id:
            try:
                materia = Materia.objects.get(id=materia_id)
                context['estudiantes'] = materia.estudiantes.all()
                context['selected_materia'] = str(materia.id)
            except Materia.DoesNotExist:
                pass

        return context

    def post(self, request, *args, **kwargs):
        materia_id = request.POST.get('materia')
        justificacion = request.POST.get('justificacion', '')
        
 
        ausentes_ids = set(request.POST.getlist('ausentes')) 
        
        if not materia_id:
          
            return redirect(self.success_url) 
        
        try:
            materia = Materia.objects.get(id=materia_id)
        except Materia.DoesNotExist:
           
            return redirect(self.success_url)
            
        todos_estudiantes = materia.estudiantes.all()
        
        presentes_ids = [
            str(est.id) for est in todos_estudiantes 
            if str(est.id) not in ausentes_ids
        ]

        for est_id in ausentes_ids:
            Asistencia.objects.create(
                estudiante_id=est_id,
                materia_id=materia_id,
                presente=False,  
                justificacion=justificacion
            )

        for est_id in presentes_ids:
            Asistencia.objects.create(
                estudiante_id=est_id,
                materia_id=materia_id,
                presente=True,  
                justificacion='' 
            )
        return redirect(self.success_url)

    
class AsistenciaActualizarView(UpdateView):
    model = Asistencia
    fields = ['presente', 'justificacion']
    template_name = 'asistencia/actualizar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')
    
class AsistenciaEliminarView(DeleteView):
    model = Asistencia
    fields = '__all__'
    template_name = 'asistencia/eliminar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')

