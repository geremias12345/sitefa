from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.materia.models import Materia
from apps.asistencia.models import Asistencia
from apps.calificacion.models import Calificacion
from apps.horario.models import Horario
from apps.estudiante.models import Estudiante
from apps.docente.models import Docente
from apps.profesorado.models import Profesorado

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/resumen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = getattr(self.request.user, 'perfil', None)
        rol = perfil.rol if perfil else None

        #variables
        profesorado = None
        materias = Asistencia.objects.none()
        asistencias = Asistencia.objects.none()
        calificaciones = Calificacion.objects.none()
        horarios = Horario.objects.none()
        estudiantes = Estudiante.objects.none()
        docentes = Docente.objects.none()

        # Si es Bedel, mostrar solo su profesorado
        if rol == 'bedel' and perfil.profesorado:
            profesorado = perfil.profesorado
            materias = Materia.objects.filter(profesorado=profesorado)
            asistencias = Asistencia.objects.filter(materia__profesorado=profesorado)
            calificaciones = Calificacion.objects.filter(materia__profesorado=profesorado)
            horarios = Horario.objects.filter(materia__profesorado=profesorado)
            estudiantes = Estudiante.objects.filter(materias__profesorado=profesorado).distinct()
            docentes = Docente.objects.filter(materia__profesorado=profesorado).distinct()

        # Si es Directivo, mostrar todos los profesorados
        elif rol == 'directivo':
            materias = Materia.objects.all()
            asistencias = Asistencia.objects.all()
            calificaciones = Calificacion.objects.all()
            horarios = Horario.objects.all()
            estudiantes = Estudiante.objects.all()
            docentes = Docente.objects.all()
            profesorados = Profesorado.objects.all()
            context['profesorados'] = profesorados

        # Totales
        context['rol'] = rol
        context['profesorado'] = profesorado
        context['materias'] = materias
        context['estudiantes'] = estudiantes
        context['docentes'] = docentes
        context['total_materias'] = materias.count()
        context['total_asistencias'] = asistencias.count()
        context['total_calificaciones'] = calificaciones.count()
        context['total_horarios'] = horarios.count()
        context['total_estudiantes'] = estudiantes.count()
        context['total_docentes'] = docentes.count() if docentes else 0

        return context
