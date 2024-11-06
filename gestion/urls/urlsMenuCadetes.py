from django.urls import path
from ..views import views_menuCadetes

urlpatterns = [
    path('certificados/', views_menuCadetes.certificados, name='certificados'),
    path('dardebaja/', views_menuCadetes.darDeBaja, name='darDeBaja'),
    path('datospersonales/', views_menuCadetes.datosPersonales, name='datosPersonales'),
    path('excluirordendemerito/', views_menuCadetes.excluirOrdenDeMerito, name='excluirOrdenDeMerito'),
    path('marcarnoregulares/', views_menuCadetes.marcarNoRegulares, name='marcarNoRegulares'),
    path('materias cursadas/', views_menuCadetes.materiasCursadas, name='materiasCursadas'),
    path('resumendecalificaciones/', views_menuCadetes.resumenDeCalificaciones, name='resumenDeCalificaciones'),
]
