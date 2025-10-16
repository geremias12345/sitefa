"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from apps.seguridad.views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calificacion/', include('apps.calificacion.urls')),
    path('horario/', include('apps.horario.urls')),
    path('asistencia/', include('apps.asistencia.urls')),
    path('estudiante/', include('apps.estudiante.urls')),
    path("materia/" , include ("apps.materia.urls")),
    path('docente/', include('apps.docente.urls')),
    path('seguridad/', include('apps.seguridad.urls')),
    path('inicio/', include('apps.inicio.urls')),
    
    #Seguridad
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

