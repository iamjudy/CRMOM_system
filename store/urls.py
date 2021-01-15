from django.urls import path
from store import views
from . import views
from .views import (
    create_supplier,
    create_material,
    create_dealer,
    create_product,
    create_order,

    SupplierListView,
    MaterialListView,
    ProductListView,
    OrderListView,
    DealerListView,

)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-material/', create_material, name='create-material'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-dealer/', create_dealer, name='create-dealer'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('material-list/', MaterialListView.as_view(), name='material-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('dealer-list/', DealerListView.as_view(), name='dealer-list'),

    path('testt/', views.testt),
    path('material', views.Raw_EOQ),
    path('plot', views.raw_plot, name='plot'),
    path('order', views.EOQ_calculate, name='order'),
    path('rate', views.rate),
    path('cat', views.cat),
    path('time', views.time),
    path('new', views.new),

]