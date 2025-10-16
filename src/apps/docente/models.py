from django.db import models

from apps.materia.models import Materia

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    materia = models.ManyToManyField(Materia)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
