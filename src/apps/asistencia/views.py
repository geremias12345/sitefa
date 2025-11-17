from datetime import date
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.estudiante.models import Estudiante
from apps.materia.models import Materia
from .models import Asistencia

class AsistenciaLeerView(ListView):
    model = Asistencia
    template_name = 'asistencia/leer.html'
    context_object_name = 'asistencias'
    paginate_by = 10

    def get_queryset(self):
        perfil = getattr(self.request.user, 'perfil', None)
        queryset = Asistencia.objects.select_related('estudiante', 'materia').all()

        # Filtrar por profesorado de la Bedel
        if perfil and perfil.rol == 'bedel' and perfil.profesorado:
            queryset = queryset.filter(materia__profesorado=perfil.profesorado)

        # Filtros GET
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

        return queryset.order_by('materia__anio', 'materia', 'estudiante__apellido', '-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = getattr(self.request.user, 'perfil', None)
        profesorado = perfil.profesorado if perfil and perfil.rol == 'bedel' else None

        # Filtrar materias y estudiantes por profesorado
        context['materias'] = Materia.objects.filter(profesorado=profesorado).order_by('nombre') if profesorado else Materia.objects.all()
        context['estudiantes'] = Estudiante.objects.filter(
            materias__profesorado=profesorado
        ).distinct().order_by('apellido', 'nombre') if profesorado else Estudiante.objects.all()
        context['anios'] = range(1, 5)

        context['selected_anio'] = self.request.GET.get('anio', '')
        context['selected_materia'] = self.request.GET.get('materia', '')
        context['selected_estudiante'] = self.request.GET.get('estudiante', '')
        context['selected_estado'] = self.request.GET.get('estado', 'todos')

        full_queryset = self.get_queryset()
        context['total_registros'] = full_queryset.count()
        context['total_ausencias'] = full_queryset.filter(presente=False).count()
        context['porcentaje_asistencia'] = round(
            (context['total_registros'] - context['total_ausencias']) / full_queryset.count() * 100, 1
        ) if full_queryset.count() > 0 else 0

        return context


class AsistenciaCrearView(CreateView):
    model = Asistencia
    fields = ['justificacion']
    template_name = 'asistencia/crear.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = getattr(self.request.user, 'perfil', None)
        profesorado = perfil.profesorado if perfil and perfil.rol == 'bedel' else None

        # Filtrar materias por profesorado
        context['materias'] = Materia.objects.filter(profesorado=profesorado) if profesorado else Materia.objects.all()
        context['today'] = date.today().isoformat()
        context['estudiantes'] = []
        context['selected_materia'] = None

        materia_id = self.request.GET.get('materia')
        if materia_id:
            try:
                materia = Materia.objects.get(id=materia_id)
                if not profesorado or materia.profesorado == profesorado:
                    context['estudiantes'] = materia.estudiantes.all()
                    context['selected_materia'] = str(materia.id)
            except Materia.DoesNotExist:
                pass

        return context

    def post(self, request, *args, **kwargs):
        perfil = getattr(self.request.user, 'perfil', None)
        profesorado = perfil.profesorado if perfil and perfil.rol == 'bedel' else None

        materia_id = request.POST.get('materia')
        justificacion = request.POST.get('justificacion', '')
        ausentes_ids = set(request.POST.getlist('ausentes'))

        if not materia_id:
            return redirect(self.success_url)

        try:
            materia = Materia.objects.get(id=materia_id)
            # Evita que la Bedel cree asistencias fuera de su profesorado
            if profesorado and materia.profesorado != profesorado:
                return redirect(self.success_url)
        except Materia.DoesNotExist:
            return redirect(self.success_url)

        todos_estudiantes = materia.estudiantes.all()
        presentes_ids = [str(est.id) for est in todos_estudiantes if str(est.id) not in ausentes_ids]

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
    template_name = 'asistencia/eliminar.html'
    success_url = reverse_lazy('asistencia:asistencia_leer')
