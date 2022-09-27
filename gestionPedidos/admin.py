from django.contrib import admin
from gestionPedidos.models import Clientes,Pedidos,Articulos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tlfno")
    search_fields=("nombre","tlfno")



admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Pedidos)
admin.site.register(Articulos)


