from django.db import models
from apps.estudiante.models import Estudiante
from apps.materia.models import Materia

class Calificacion(models.Model):
    SITUACIONES = [
        ('En curso', 'En curso'),
        ('Promocionó', 'Promocionó'),
        ('Abandonó', 'Abandonó'),
        ('Aprobó', 'Aprobó'),
        ('Desaprobó', 'Desaprobó'),
        ('AEF', 'AEF'),
        ('AT', 'AT'),
    ]

    NUMEROS_A_LETRAS = {
        1: 'uno',
        2: 'dos',
        3: 'tres',
        4: 'cuatro',
        5: 'cinco',
        6: 'seis',
        7: 'siete',
        8: 'ocho',
        9: 'nueve',
        10: 'diez',
    }

    nota = models.CharField(max_length=10)
    nota_letra = models.CharField(max_length=10, blank=True, editable=False)
    fecha = models.DateField(auto_now_add=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='calificaciones')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificaciones')
    situacion = models.CharField(max_length=20, choices=SITUACIONES, default='En curso')

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.materia.nombre}: {self.nota} ({self.nota_letra}) - {self.situacion}"
