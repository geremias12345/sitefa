from django.contrib import admin
from .models import Calificacion
# Register your models here.
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
	list_display = ('nota',)
	search_fields = ('nota',)
	list_filter = ('nota',)
	ordering = ('nota',)