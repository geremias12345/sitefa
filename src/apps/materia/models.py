from django.db import models
from apps.profesorado.models import Profesorado

class Materia(models.Model):
    DURACION = [
        ('Anual', 'Anual'),
        ('Primer Cuatrimestre', 'Primer Cuatrimestre'),
        ('Segundo Cuatrimestre', 'Segundo Cuatrimestre'),
    ]

    nombre = models.CharField(max_length=100)
   
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

    duracion = models.CharField(max_length=30, choices=DURACION, default='Anual')
    def __str__(self):
        return f"{self.nombre} - {self.duracion} - {self.anio}º Año"

# Create your models here.
