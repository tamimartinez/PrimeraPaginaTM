from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "ServiceApp/inicio.html")

def servicios(request):
    return render(request, "ServiceApp/servicios.html")

def cotizaciones(request):
    return render(request, "ServiceApp/cotizaciones.html")

def proyectos(request):
    return render(request, "ServiceApp/proyectos.html")