from django.db import models

# Create your models here.
class Profesorado(models.Model):
    nombre_instituto = models.CharField(max_length=100)
    ciclo_lectivo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre_instituto}, {self.ciclo_lectivo}"