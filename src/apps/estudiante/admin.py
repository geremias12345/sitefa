from django.contrib import admin
from .models import Estudiante 

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'dni', 'apellido']
    search_fields = ['nombre']
    list_filter = ['dni']
    ordering = ['nombre']

# Register your models here.
