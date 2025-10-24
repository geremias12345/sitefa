from datetime import date, timezone
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.estudiante.models import Estudiante
from apps.materia.models import Materia
from .models import Calificacion
from django.db.models import Avg

class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificacion/leer.html'
    context_object_name = 'calificaciones'
    paginate_by = 10  # opcional, para paginación

    def get_queryset(self):
        qs = super().get_queryset().select_related('materia', 'estudiante')
        materia = self.request.GET.get('materia')
        estudiante = self.request.GET.get('estudiante')
        fecha = self.request.GET.get('fecha')

        if materia:
            qs = qs.filter(materia_id=materia)
        if estudiante:
            qs = qs.filter(estudiante_id=estudiante)
        if fecha:
            qs = qs.filter(fecha=fecha)

        return qs.order_by('-fecha')  # opcional, ordenar por fecha descendente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Para los filtros
        context['materias'] = Materia.objects.all()
        context['estudiantes'] = Estudiante.objects.all()
        context['selected_materia'] = self.request.GET.get('materia', '')
        context['selected_estudiante'] = self.request.GET.get('estudiante', '')
        context['selected_fecha'] = self.request.GET.get('fecha', '')

        # Estadísticas
        calificaciones = self.get_queryset()
        context['total_calificaciones'] = calificaciones.count()
        context['promedio_general'] = calificaciones.aggregate(Avg('nota'))['nota__avg']
        context['bajas'] = calificaciones.filter(nota__lt=6).count()  # notas menores a 6

        return context

class CalificacionCreateView(View):
    template_name = 'calificacion/crear.html'

    def get(self, request):
        materias = Materia.objects.all()
        selected_materia = request.GET.get('materia')
        estudiantes = Estudiante.objects.filter(materias__id=selected_materia).distinct() if selected_materia else []

        context = {
            'materias': materias,
            'selected_materia': int(selected_materia) if selected_materia else None,
            'estudiantes': estudiantes,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        selected_materia = request.POST.get('materia')
        estudiantes = Estudiante.objects.filter(materias__id=selected_materia).distinct()
        for est in estudiantes:
            nota_valor = request.POST.get(f'notas_{est.id}')
            if nota_valor:
                Calificacion.objects.create(
                    estudiante=est,
                    materia_id=selected_materia,
                    nota=nota_valor
                )
        return redirect('calificacion:calificacion_leer')

class CalificacionUpdateView(UpdateView):
    model = Calificacion
    fields = ['estudiante', 'materia', 'nota']
    template_name = 'calificacion/actualizar.html'
    success_url = reverse_lazy('calificacion:calificacion_leer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias'] = Materia.objects.all()
        selected_materia = self.object.materia.id if self.object.materia else None
        context['selected_materia'] = selected_materia
        context['estudiantes'] = Estudiante.objects.filter(materias__id=selected_materia).distinct() if selected_materia else []
        return context

class CalificacionDeleteView(DeleteView):
    model = Calificacion
    template_name = 'calificacion/eliminar.html'
    success_url = reverse_lazy('calificacion:calificacion_leer')