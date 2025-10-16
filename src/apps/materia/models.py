from django.db import models
from apps.profesorado.models import Profesorado

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    # Año puede ser 1 a 4 (cuatrimestral o anual)
    anio = models.CharField(
        max_length=10,
        choices=[('1','1º Año'), ('2','2º Año'), ('3','3º Año'), ('4','4º Año')],
        default='1'
    )
    profesorado = models.ForeignKey(
        Profesorado,
        on_delete=models.CASCADE,
        related_name="materias"
    )

    def __str__(self):
        return f"{self.nombre} - {self.anio}"

# Create your models here.
