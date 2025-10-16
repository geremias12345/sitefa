from django.urls import path
from .views import AsistenciaCrearView, AsistenciaEliminarView, AsistenciaActualizarView, AsistenciaLeerView

app_name = "asistencia"

urlpatterns = [
    path('leer/', AsistenciaLeerView.as_view(), name='asistencia_leer'),
    path('crear/', AsistenciaCrearView.as_view(), name='asistencia_crear'),
    path('<int:pk>/editar/', AsistenciaActualizarView.as_view(), name='asistencia_actualizar'),
    path('<int:pk>/actualizar/', AsistenciaActualizarView.as_view(), name='asistencia_actualizar'),
    path('<int:pk>/eliminar/', AsistenciaEliminarView.as_view(), name='asistencia_eliminar'),
]