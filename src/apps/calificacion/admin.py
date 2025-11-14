from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante',
        'materia',
        'nota',
        'nota_letra',
        'situacion',
        'fecha',
    )
    search_fields = (
        'estudiante__nombre',
        'estudiante__apellido',
        'estudiante__dni',
        'materia__nombre',
    )

    list_filter = (
        'situacion',
        'materia',
        'fecha',
    )

    ordering = ('-fecha',)

    fields = (
        'estudiante',
        'materia',
        'nota',
        'situacion',
    )

    readonly_fields = ('nota_letra', 'fecha')

    date_hierarchy = 'fecha'
