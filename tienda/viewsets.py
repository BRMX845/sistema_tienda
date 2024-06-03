from django.contrib.auth.models import User
from rest_framework import viewsets,response,status
from .models import *
from .serializers import *
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer