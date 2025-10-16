from django.urls import path
from apps.docente.views import DocenteActualizarVista, DocenteCrearVista, DocenteEliminarVista, DocenteLeerVista

app_name = 'docente'
urlpatterns = [
    path ('crear/', DocenteCrearVista.as_view(), name = 'docente_crear'),
    path ('leer/', DocenteLeerVista.as_view(), name = 'docente_leer'),
    path ('<int:pk>/editar/', DocenteActualizarVista.as_view(), name = 'docente_actualizar'),
    path ('<int:pk>/eliminar/', DocenteEliminarVista.as_view(), name = 'docente_eliminar'),
]