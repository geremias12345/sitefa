from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.materia.models import Materia
from apps.asistencia.models import Asistencia
from apps.calificacion.models import Calificacion
from apps.horario.models import Horario
from apps.estudiante.models import Estudiante
from apps.docente.models import Docente
from apps.profesorado.models import Profesorado

class InicioView(TemplateView):
    template_name = 'inicio/resumen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Materias
        materias = Materia.objects.all()
        context['total_materias'] = materias.count()

        # Asistencias
        asistencias = Asistencia.objects.all()
        context['total_asistencias'] = asistencias.count()

        # Calificaciones
        calificaciones = Calificacion.objects.all()
        context['total_calificaciones'] = calificaciones.count()

        # Horarios
        horarios = Horario.objects.all()
        context['total_horarios'] = horarios.count()

        # Estudiantes
        estudiantes = Estudiante.objects.all()
        context['total_estudiantes'] = estudiantes.count()

        # Docentes
        docentes = Docente.objects.all()
        context['total_docentes'] = docentes.count()
        # Docentes
        Profesorados = Profesorado.objects.all()
        context['profesorados'] = Profesorados

        return context
