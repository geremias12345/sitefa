from django.urls import path
from .views import MateriaCrearVista,MateriaActualizarVista, MateriaDetalleVista,MateriaEliminarVista,MateriaLeerVista

app_name = 'materia'

urlpatterns = [
    path("leer/",MateriaLeerVista.as_view(),name="materia_leer"),
    path("crear/",MateriaCrearVista.as_view(),name="materia_crear"),
    path("<int:pk>/actualizar/",MateriaActualizarVista.as_view(),name="materia_actualizar"),
    path("<int:pk>/eliminar/",MateriaEliminarVista.as_view(),name="materia_eliminar"),
    path("<int:pk>/detalles/",MateriaDetalleVista.as_view(),name="materia_detalle"),
]