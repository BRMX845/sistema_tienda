from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

class UserconSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['Nombre']

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ['Nombre']

class ProductosSerializer(serializers.ModelSerializer):
    FK_Categoria=serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), many=False)
    class Meta:
        model = Productos
        fields = ['Nombre','Descripcion','precio','stock','FK_Categoria','Imagen']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['fecha','Total']

class ProveedoresSerializer(serializers.ModelSerializer):
    Empresa=EmpresasSerializer()
    class Meta:
        model = Proveedores
        fields = ['Nombre','Telefono','Empresa']

class InventarioSerializer(serializers.ModelSerializer):
    FK_product=serializers.PrimaryKeyRelatedField(queryset=Productos.objects.all(), many=False)
    FK_proveedor=serializers.PrimaryKeyRelatedField(queryset=Proveedores.objects.all(), many=False)
    class Meta:
        model = Inventario
        fields = ['FK_product','FK_proveedor','Cantidad','Fecha']

class DetalleSerializer(serializers.ModelSerializer):
    FK_venta = serializers.PrimaryKeyRelatedField(queryset=Venta.objects.all())
    FK_product=serializers.PrimaryKeyRelatedField(queryset=Productos.objects.all(), many=False)
    Vendedor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    class Meta:
        model = Detalle
        fields = ['FK_venta','FK_product','Cantidad','PrecioUnitario','Subtotal','cambio','Vendedor']