from rest_framework import routers
from .viewsets import *

app_name = 'tienda'

router = routers.DefaultRouter()
router.register('user',UserViewSet)
router.register('categoria',CategoriaViewSet)
router.register('empresas',EmpresasViewSet)
router.register('productos',ProductosViewSet)
router.register('venta',VentaViewSet)
router.register('proveedores',ProveedoresViewSet)
router.register('inventario',InventarioViewSet)
router.register('detalles',DetalleViewSet)
