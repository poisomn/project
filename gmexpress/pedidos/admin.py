from django.contrib import admin
from .models import Vehiculo, Chofer, Pedido

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'modelo', 'capacidad', 'activo')
    search_fields = ('patente', 'modelo')

@admin.register(Chofer)
class ChoferAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'activo')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'chofer', 'vehiculo', 'fecha_creacion', 'fecha_entrega')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('cliente__username', 'descripcion', 'direccion_entrega')
