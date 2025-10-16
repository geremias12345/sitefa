from django.urls import path
from .views import EstudianteCrearVista, EstudianteActualizarVista, EstudianteEliminarVista, EstudianteLeerVista
app_name = 'estudiante'

urlpatterns = [ 
    path('crear/', EstudianteCrearVista.as_view(), name='estudiante_crear'),
    path('eliminar/', EstudianteEliminarVista.as_view(), name='estudiante_eliminar'),
    path('leer/', EstudianteLeerVista.as_view(), name='estudiante_leer'),
    path('actualizar/', EstudianteActualizarVista.as_view(), name='estudiante_actualizar'),
]