from django.contrib import admin
from gestionPedidos.models import Clientes,Pedidos,Articulos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tlfno")
    search_fields=("nombre","tlfno")

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    list_filter=("seccion",)

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Pedidos,PedidosAdmin)
admin.site.register(Articulos,ArticulosAdmin)


