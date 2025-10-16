from django.contrib import admin
from .models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']
    search_fields = ['nombre']
    list_filter =['dni']
    ordering = ['apellido']