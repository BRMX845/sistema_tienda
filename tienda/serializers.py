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
    FK_Categoria=CategoriaSerializer()
    class Meta:
        model = Productos
        fields = ['Nombre','Descripcion','precio','stock','FK_Categoria','Imagen']
    
    def create(self, validated_data):
        categoria_data = validated_data.pop('FK_Categoria')
        categoria_nombre = categoria_data['Nombre']
        try:
            categoria = Categoria.objects.get(Nombre=categoria_nombre)
        except Categoria.DoesNotExist:
            raise serializers.ValidationError(f"No existe la categoría {categoria_nombre}")
        producto = Productos.objects.create(FK_Categoria=categoria, **validated_data)
        return producto
    

    def update(self, instance, validated_data):
        categoria_data = validated_data.pop('FK_Categoria')
        categoria_nombre = categoria_data['Nombre']
        try:
            categoria = Categoria.objects.get(Nombre=categoria_nombre)
        except Categoria.DoesNotExist:
            raise serializers.ValidationError(f"No existe la categoría {categoria_nombre}")
        instance.Nombre = validated_data.get('Nombre', instance.Nombre)
        instance.Descripcion = validated_data.get('Descripcion', instance.Descripcion)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.FK_Categoria = categoria_nombre
        instance.Imagen = validated_data.get('Imagen', instance.Imagen)
        instance.save()
        return instance

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
    FK_product = serializers.SlugRelatedField(
        slug_field='Nombre', queryset=Productos.objects.all()
    )
    FK_proveedor = serializers.SlugRelatedField(
        slug_field='Nombre', queryset=Proveedores.objects.all()
    )
    class Meta:
        model = Inventario
        fields = ['FK_product','FK_proveedor','Cantidad','Fecha']
    def create(self, validated_data):
        producto_nombre = validated_data.pop('FK_product')
        proveedor_nombre = validated_data.pop('FK_proveedor')
        
        producto = Productos.objects.get(Nombre=producto_nombre)
        proveedor = Proveedores.objects.get(Nombre=proveedor_nombre)
        
        inventario = Inventario.objects.create(
            FK_product=producto, FK_proveedor=proveedor, **validated_data
        )
        return inventario

class DetalleSerializer(serializers.ModelSerializer):
    FK_venta = serializers.PrimaryKeyRelatedField(queryset=Venta.objects.all())
    FK_product = serializers.SlugRelatedField(slug_field='Nombre', queryset=Productos.objects.all())
    Vendedor = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # FK_product=serializers.PrimaryKeyRelatedField(queryset=Productos.objects.all(), many=False)
    # FK_venta=VentaSerializer()
    class Meta:
        model = Detalle
        fields = ['FK_venta','FK_product','Cantidad','PrecioUnitario','Subtotal','cambio','Vendedor']
    
    def create(self, validated_data):
        venta = validated_data.pop('FK_venta')
        product = validated_data.pop('FK_product')
        vendedor = validated_data.pop('Vendedor')

        detalle = Detalle.objects.create(FK_venta=venta, FK_product=product, Vendedor=vendedor, **validated_data)
        return detalle