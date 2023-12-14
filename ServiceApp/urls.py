from django.urls import path
from ServiceApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('servicios', views.servicios, name="Servicios"),
    path('cotizaciones', views.cotizaciones, name="Cotizaciones"),
    path('proyectos', views.proyectos, name="Proyectos"),
]