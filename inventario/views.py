from aiohttp import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib import messages
from .models import Item, OrdenDeVenta, IngresoPedido, Lista, Venta
from .forms import OrdenDeVentaForm, IngresoPedidoForm
from .filters import ItemFilter
# Create your views here.


@login_required()
def home(request):
    lista = []
    totalvent = 0
    valor = 0
    ventas = Venta.objects.all()
    items = Item.objects.all()
    for item in items:
        lista.append(item.nombre_producto)
    for items in ventas:
        totalvent += items.total
    stock = Item.objects.all()
    for items in stock:
        valor += items.valor_en_stock
    print(lista)
    return render(request, 'inventario/home.html', {"total": totalvent, "stock": valor, "items": lista})


@login_required()
def orden_venta(request):
    form = OrdenDeVentaForm()
    subtotalventa = 0
    totalvent = 0
    if 'agregar' in request.POST:
        producto = request.POST['productos']
        querry2 = Item.objects.get(id=producto)
        cantidadvendida = request.POST['cantidadvendida']
        # print(f"el producto es {querry2.nombre_producto}")
        subtotalventa += int(cantidadvendida) * int(querry2.precio_venta)
        list = Lista(item=querry2.nombre_producto,
                     cantidad=cantidadvendida, subtotal=subtotalventa)
        list.save()
        for items in Lista.objects.all():
            querry = Lista.objects.get(item=items)
            print(querry)
            totalvent += querry.subtotal
            print(totalvent)
    if 'aceptar' in request.POST:
        itemslista = []
        form = OrdenDeVentaForm(request.POST)
        print(totalvent)
        for items in Lista.objects.all():
            querry = Lista.objects.get(item=items)
            totalvent += querry.subtotal
            itemslista.append((querry.item, querry.cantidad))
            print(itemslista)
        vent = Venta(total=totalvent, productos=itemslista)
        if form.is_valid():
            # form.save()
            vent.save()
            for items in Lista.objects.all():
                item = Item.objects.get(nombre_producto=items)
                item.cantidad_en_stock -= items.cantidad

                # print(item.cantidad_en_stock)
                # print(items.cantidad)
                item.save()
        totalvent = 0
        Lista.objects.all().delete()

    if 'cancelar' in request.POST:
        Lista.objects.all().delete()
    lista = Lista.objects.all()
    return render(request, 'inventario/ordenes_venta.html', {"form": form, "lista": lista, "total": totalvent})


@login_required()
def ingreso_pedido(request):
    form = IngresoPedidoForm()
    if 'agregar' in request.POST:
        producto = request.POST['productos']
        querry2 = Item.objects.get(id=producto)
        cantidadvendida = request.POST['cantidad']
        list = Lista(item=querry2.nombre_producto,
                     cantidad=cantidadvendida)
        list.save()
        print(f"el producto es {querry2.nombre_producto}")
    if 'aceptar' in request.POST:
        form = IngresoPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            lista = Lista.objects.all()
            for items in lista:
                item = Item.objects.get(nombre_producto=items)
                item.cantidad_en_stock += items.cantidad

                print(item.cantidad_en_stock)
                print(items.cantidad)
                item.save()
        Lista.objects.all().delete()

    if 'cancelar' in request.POST:
        Lista.objects.all().delete()
    lista = Lista.objects.all()

    return render(request, 'inventario/ingreso_pedido.html', {"form": form, "lista": lista})


class ConsultaListView(LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 100
    template_name = 'inventario/consulta_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['nombre_producto', 'descripcion_producto',
              'linea', 'cantidad_en_stock', 'precio_compra', 'precio_venta']

    def form_valid(self, form):
        form.save()
        nombre_producto = form.cleaned_data.get('nombre_producto')
        messages.success(
            self.request, f'¡Item {nombre_producto} ingresado correctamente!')
        return redirect('consulta_item')


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['nombre_producto', 'descripcion_producto',
              'linea', 'cantidad_en_stock', 'precio_compra', 'precio_venta']
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("/consulta_item/")

    pass


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/consulta_item'
    pass


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

    # if 'aceptar' in request.POST:
    #     print(request.POST)
    #     form = OrdenDeVentaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         producto = request.POST['productos']
    #         cantidadvendida2 = int(request.POST['cantidadvendida'])
    #         print(
    #             f'El producto es {producto} y se vendieron {cantidadvendida2}')
    #         querry1 = Item.objects.get(id=producto)
    #         print(querry1)
    #         print(querry1.cantidad_en_stock)
    #         querry1.cantidad_en_stock = querry1.cantidad_en_stock - cantidadvendida2
    #         querry1.save()
    #         print(querry1.cantidad_en_stock)
    #         Lista.objects.all().delete()
    #         return redirect('ordenes-venta')
