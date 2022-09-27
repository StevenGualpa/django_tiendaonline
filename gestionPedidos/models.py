import email
from pyexpat import model
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)
    tlfno=models.CharField(max_length=7)

    def __str__(self):
        return 'El nombre es %s , la direccion es %s , el email es %s y el telefono es %s' %(self.nombre, self.direccion, self.email, self.tlfno)


class Articulos(models.Model): 
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entreado=models.BooleanField()

