from django.db import models
from django.urls import reverse

# Create your models here.


class Item(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.CharField(max_length=200)
    linea = models.CharField(max_length=200)
    cantidad_en_stock = models.IntegerField(null=True)
    precio_compra = models.IntegerField(default=0, null=True)
    precio_venta = models.IntegerField(default=0, null=True)
    on_delete = models.CASCADE

    def get_absolute_url(self):
        return reverse("item-create")

    def __str__(self):
        return self.nombre_producto

    @property
    def valor_en_stock(self):
        return self.precio_compra * self.cantidad_en_stock


class OrdenDeVenta(models.Model):
    productos = models.ForeignKey(
        Item, default=1, verbose_name='Producto', on_delete=models.SET_DEFAULT)
    cantidadvendida = models.IntegerField(
        null=True, verbose_name='Cantidad Vendida', blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #fecha = models.DateTimeField(auto_now_add=True)


class IngresoPedido(models.Model):
    productos = models.ForeignKey(
        Item, default=1, verbose_name='Producto', on_delete=models.SET_DEFAULT)
    cantidad = models.IntegerField(
        null=True, verbose_name='Cantidad a Ingresar')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #fecha = models.DateTimeField(auto_now_add=True)
    on_delete = models.CASCADE


class Lista(models.Model):
    item = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0, null=True)
    subtotal = models.IntegerField(default=0, null=True)
    on_delete = models.CASCADE

    def __str__(self):
        return self.item


class Venta(models.Model):
    productos = models.CharField(max_length=500, null=True)
    total = models.IntegerField(default=0, null=True)
    creado = models.DateTimeField(auto_now_add=True, editable=True)
    actualizado = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return str(self.id)
