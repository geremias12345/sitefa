from django.contrib import admin
from .models import Materia
# Register your models here.
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "profesorado"]
    search_fields = ["nombre", "profesorado"]
    list_filter = ["nombre","profesorado"]
    ordering = ["nombre"]
