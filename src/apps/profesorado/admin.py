from django.contrib import admin
from .models import Profesorado


# Register your models here.
@admin.register(Profesorado)
class ProfesoradoAdmin(admin.ModelAdmin):
    list_display = ['nombre_instituto','ciclo_lectivo']
    search_fields = ['nombre_instituto','ciclo_lectivo']
    list_filter = ['nombre_instituto','ciclo_lectivo']
    ordering = ['nombre_instituto','ciclo_lectivo']