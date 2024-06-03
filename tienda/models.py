from django.db import models
from django.contrib.auth.models import User

class Empresas(models.Model):
    Nombre = models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.Nombre
    
    class Meta:
        db_table ='empresa'
        verbose_name = 'Empresa'
        verbose_name_plural ='Empresas'
class Categoria(models.Model):
    Nombre = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.Nombre
    class Meta:
        db_table ='categoria'
        verbose_name = 'Categoria'
        verbose_name_plural ='Categorias'

class Productos(models.Model):
    Nombre = models.CharField(max_length=50,null=False)
    Descripcion = models.TextField(blank=True,null=True)
    precio=models.FloatField(null=False)
    stock=models.IntegerField(null=False)
    FK_Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Imagen=models.ImageField(upload_to='img/%Y/%m/%d',null=True,blank=True,verbose_name='Imagen del producto')

    def __str__(self):
        return self.Nombre
    class Meta:
        db_table ='producto'
        verbose_name = 'Producto'
        verbose_name_plural ='Productos'


class Venta(models.Model):

    fecha = models.DateTimeField(auto_now_add=True,null=False)
    Total = models.FloatField(null=False)
    class Meta:
        db_table ='venta'
        verbose_name = 'Venta'
        verbose_name_plural ='Ventas'

class Detalle(models.Model):
    FK_venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    FK_product = models.ForeignKey(Productos,on_delete=models.CASCADE)
    Cantidad = models.IntegerField(null=False)
    PrecioUnitario = models.FloatField(null=False)
    Subtotal = models.FloatField(null=False)
    cambio = models.FloatField(null=False)
    Vendedor= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return super().__str__()
    class Meta:
        db_table ='detalle'
        verbose_name = 'Detalle'
        verbose_name_plural ='Detalles'

class Proveedores(models.Model):
    Nombre= models.CharField(max_length=50,null=False)
    Telefono=models.BigIntegerField(null=False)
    Empresa=models.ForeignKey(Empresas, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre
    class Meta:
        db_table ='proveedores'
        verbose_name = 'Proveedor'
        verbose_name_plural ='Proveedores'

class Inventario(models.Model):
    FK_product=models.ForeignKey(Productos,on_delete=models.CASCADE)
    FK_proveedor=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    Cantidad=models.IntegerField(null=False)
    Fecha=models.DateField(auto_now_add=True,null=False)
    class Meta:
        db_table ='inventario'
        verbose_name = 'Inventario'
        verbose_name_plural ='Inventarios'
# Create your models here.
