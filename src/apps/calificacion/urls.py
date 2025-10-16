from django.urls import path

from apps.calificacion.views import CalificacionCreateView, CalificacionDeleteView, CalificacionListView, CalificacionUpdateView

app_name = 'calificacion'

urlpatterns = [
    path('leer/',CalificacionListView.as_view(),name='calificacion_leer'),
    path('crear/',CalificacionCreateView.as_view(),name='calificacion_crear'),
    path('actualizar/<int:pk>/',CalificacionUpdateView.as_view(),name='calificacion_actualizar'),
    path('eliminar/<int:pk>/',CalificacionDeleteView.as_view(),name='calificacion_eliminar')   

]