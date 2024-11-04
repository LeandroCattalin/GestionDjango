from django.urls import path
from . import views

urlpatterns = [
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