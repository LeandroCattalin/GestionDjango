from django.shortcuts import render

def paneldecontrol(request):
    cicloLectivo = "2024"
    return render(request, 'paneldecontrol.html', {'cicloLectivo' : cicloLectivo})

def cadetes_view(request):
    return render(request, 'cadetes.html')

def notas_view(request):
    return render(request, 'notas.html')

def araucano_view(request):
    return render(request, 'araucano.html')

def estadisticasypremios_view(request):
    return render(request, 'estadisticasypremios.html')

def aptitudesygut_view(request):
    return render(request, 'aptitudesygut.html')

def exportar_view(request):
    return render(request, 'exportar.html')

def nuevociclolectivo_view(request):
    return render(request, 'nuevociclolectivo.html')

def ordendemerito_view(request):
    return render(request, 'ordendemerito.html')

def materias_view(request):
    return render(request, 'materias.html')

def sistema_view(request):
    return render(request, 'sistema.html')