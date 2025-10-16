from django.db import models
from apps.materia.models import Materia

class Estudiante(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	dni = models.IntegerField()
	email = models.CharField(max_length=70)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField(null=True)
	ciclo_ingreso = models.CharField(max_length=40)
	estados = {
		"REGULAR": "Regular",
		"IRREGULAR": "Irregular",
		"OTRO": "Otro"
	}
	estado = models.CharField(max_length=50, choices=estados)
	materia = models.ManyToManyField(Materia)

	
	def __str__ (self):
		return f"{self.nombre},{self.apellido}"