from django.contrib import admin

from .models import *
# Register your models here.
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Descripcion', 'FK_Categoria')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre')
    
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha','Total')

@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'FK_venta','FK_product','Cantidad','Vendedor')
@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre','Empresa')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'FK_product','FK_proveedor','Cantidad','Fecha')
    
@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre')
