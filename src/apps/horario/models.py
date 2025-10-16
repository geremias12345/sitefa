from django.db import models

from apps.materia.models import Materia

class Horario(models.Model):

    DIAS_SEMANA = [('LUN', 'Lunes'),('MAR', 'Martes'),('MIE', 'Miércoles'),('JUE', 'Jueves'),('VIE', 'Viernes'),('SAB', 'Sábado'),]

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    def __str__(self):
        return f"{self.materia}, {self.dia_semana}"
# Create your models here.
