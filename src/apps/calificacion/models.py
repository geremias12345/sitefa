from django.db import models
from apps.estudiante.models import Estudiante
from apps.materia.models import Materia

from apps.estudiante.models import Estudiante
from apps.materia.models import Materia

#Crea tus modelos aquí.
class Calificacion(models.Model):
    nota = models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='calificacion')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificacion')

    # Agrega más campos según sea necesario
    def __str__ (self):
        return f"{self.estudiante.nombre} - {self.materia.nombre}: {self.nota}"