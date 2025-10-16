from django.contrib import admin
from .models import Horario

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['materia']
    search_fields = ['materia']
    list_filter = ['materia']
    ordering = ['materia']


# Register your models here.

