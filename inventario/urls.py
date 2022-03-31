from django.urls import path, include
from . import views
from .views import ItemCreateView, ConsultaListView, ItemDetailView, ItemUpdateView, ItemDeleteView, ingreso_pedido
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('consulta_item/', ConsultaListView.as_view(), name='consulta_item'),
    path('nuevoitem/', ItemCreateView.as_view(), name="item-create"),
    path('item/<int:pk>/', ItemDetailView.as_view(), name="item-detail"),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name="item-update"),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name="item-delete"),
    path('login/', auth_views.LoginView.as_view(template_name='inventario/login.html'), name='login'),
    path('orden_venta/', views.orden_venta, name='ordenes-venta'),
    path('ingreso_pedido/', views.ingreso_pedido, name='ingreso-pedido')
    # path('accounts/login/', auth_views.LoginView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
