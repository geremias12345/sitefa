from django.urls import path
from .views import HorarioCrearVista, HorarioLeerVista, HorarioActualizarVista, HorarioEliminarVista

app_name = 'horario'

urlpatterns = [
    path('crear/',HorarioCrearVista.as_view( ), name='horario_crear'),
    path('leer/',HorarioLeerVista.as_view( ), name='horario_leer'),
    path('<int:pk>/actualizar/',HorarioActualizarVista.as_view( ), name='horario_actualizar'),
    path('<int:pk>/eliminar/',HorarioEliminarVista.as_view( ), name='horario_eliminar')
]