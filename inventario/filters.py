from ast import Num
import django_filters
from django_filters import NumberFilter, RangeFilter
from .models import Item


class ItemFilter(django_filters.FilterSet):
    nombre_producto = django_filters.CharFilter(lookup_expr='icontains')
    descripcion_producto = django_filters.CharFilter(lookup_expr='icontains')
    linea = django_filters.CharFilter(lookup_expr='icontains')
    precio_compra = RangeFilter(field_name='precio_compra',
                                lookup_expr='está entre los valores')
    precio_venta = RangeFilter(field_name='precio_venta',
                               lookup_expr='está entre los valores')

    class Meta:
        model = Item
        fields = '__all__'
