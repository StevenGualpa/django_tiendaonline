from django.shortcuts import render
from django.http import HttpResponse

from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")


def buscarp(request):

    if request.GET["prd"]:
    
        mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"

        else:
            #art=Articulos.objects.filter(nombre=producto)   #busca un producto
            art=Articulos.objects.filter(nombre__icontains=producto)   #busca conicidencias
            return render(request,"resultados_busqueda.html",{"articulos":art,"query":producto})
    
    else:
        mensaje="No has introducido ningun valor"
    
    return HttpResponse(mensaje)

def contacto(request):
    
    return render(request,"contacto.html")