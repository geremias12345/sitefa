from django.urls import path
from apps.profesorado.views import ProfesoradoActualizarVista, ProfesoradoCrearVista, ProfesoradoEliminarVista, ProfesoradoLeerVista


app_name = 'profesorado'

urlpatterns = [
    path("leer/",ProfesoradoLeerVista.as_view(),name="profesorado_leer"),
    path("crear/",ProfesoradoCrearVista.as_view(),name="profesorado_crear"),
    path("<int:pk>/actualizar/",ProfesoradoActualizarVista.as_view(),name="profesorado_actualizar"),
    path("<int:pk>/eliminar/",ProfesoradoEliminarVista.as_view(),name="profesorado_eliminar")
]