from django.contrib import admin
from .models import Asistencia

# Register your models here.
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('fecha',)
    search_fields = ('fecha',)
    list_filter = ('fecha',)
    ordering = ('fecha',)