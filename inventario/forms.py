from django import forms
from .models import OrdenDeVenta, IngresoPedido


class OrdenDeVentaForm(forms.ModelForm):
    class Meta:
        model = OrdenDeVenta
        fields = ['productos', 'cantidadvendida']


class IngresoPedidoForm(forms.ModelForm):
    class Meta:
        model = IngresoPedido
        fields = ['productos', 'cantidad']
