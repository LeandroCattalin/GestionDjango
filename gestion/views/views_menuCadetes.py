from django.shortcuts import render

def certificados(request):
    return render(request, 'menuPanelDeControl/menuCadetes/certificados.html')

def darDeBaja(request):
    return render(request, 'menuPanelDeControl/menuCadetes/darDeBaja.html')

def datosPersonales(request):
    return render(request, 'menuPanelDeControl/menuCadetes/datosPersonales.html')

def excluirOrdenDeMerito(request):
    return render(request, 'menuPanelDeControl/menuCadetes/excluirOrdenDeMerito.html')

def marcarNoRegulares(request):
    return render(request, 'menuPanelDeControl/menuCadetes/marcarNoRegulares.html')

def materiasCursadas(request):
    return render(request, 'menuPanelDeControl/menuCadetes/materiasCursadas.html')

def resumenDeCalificaciones(request):
    return render(request, 'menuPanelDeControl/menuCadetes/resumenDeCalificaciones.html')