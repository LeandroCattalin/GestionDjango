from django.shortcuts import render

def paneldecontrol(request):
    cicloLectivo = "2024"
    return render(request, 'paneldecontrol.html', {'cicloLectivo' : cicloLectivo})

def cadetes_view(request):
    return render(request, 'menuPanelDeControl/cadetes.html')

def notas_view(request):
    return render(request, 'menuPanelDeControl/notas.html')

def araucano_view(request):
    return render(request, 'menuPanelDeControl/araucano.html')

def estadisticasypremios_view(request):
    return render(request, 'menuPanelDeControl/estadisticasypremios.html')

def aptitudesygut_view(request):
    return render(request, 'menuPanelDeControl/aptitudesygut.html')

def exportar_view(request):
    return render(request, 'menuPanelDeControl/exportar.html')

def nuevociclolectivo_view(request):
    return render(request, 'menuPanelDeControl/nuevociclolectivo.html')

def ordendemerito_view(request):
    return render(request, 'menuPanelDeControl/ordendemerito.html')

def materias_view(request):
    return render(request, 'menuPanelDeControl/materias.html')

def sistema_view(request):
    return render(request, 'menuPanelDeControl/sistema.html')