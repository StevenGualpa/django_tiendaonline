from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from gestionPedidos.models import Articulos
from TiendaOnline.settings import EMAIL_HOST_USER

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
    
    if request.method=="POST":
        
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" " +request.POST["email"]
        email_from=EMAIL_HOST_USER
        recipient_list=["stevengualpa@hotmail.com","rino.arias2018@uteq.edu.ec","jorge.gualpa2015@uteq.edu.ec"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"gracias.html")

    return render(request,"contacto.html")