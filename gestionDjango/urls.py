"""
URL configuration for nombre_del_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion', include('gestion.urls')),
    path('', views.paneldecontrol, name='paneldecontrol'),
    path('cadetes/', views.cadetes_view, name='cadetes'),
    path('notas/', views.notas_view, name='notas'),
    path('araucano/', views.araucano_view, name='araucano'),
    path('estadisticas-premios/', views.estadisticasypremios_view, name='estadisticasypremios'),
    path('aptitudes-gut/', views.aptitudesygut_view, name='aptitudesygut'),
    path('exportar/', views.exportar_view, name='exportar'),
    path('nuevo-ciclo-lectivo/', views.nuevociclolectivo_view, name='nuevociclolectivo'),
    path('orden-merito/', views.ordendemerito_view, name='ordendemerito'),
    path('materias/', views.materias_view, name='materias'),
    path('sistema/', views.sistema_view, name='sistema'),
]
