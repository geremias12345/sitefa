from django.db import models
from apps.estudiante.models import Estudiante
from apps.materia.models import Materia

class Asistencia(models.Model):
    fecha = models.DateField(auto_now_add=True)  # se carga automáticamente
    presente = models.BooleanField(default=True)  # por defecto presente
    justificacion = models.CharField(max_length=100, blank=True, null=True)  # opcional
    estudiante = models.ForeignKey(
        Estudiante, 
        on_delete=models.CASCADE, 
        related_name="asistencias"
    )
    materia = models.ForeignKey(
        Materia, 
        on_delete=models.CASCADE, 
        related_name="asistencias"
    )

    def __str__(self):
        return f"{self.estudiante} - {self.materia} - {self.fecha}"


# Create your models here.