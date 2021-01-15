from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Supplier, Material, Product, Order, Dealer


@login_required(login_url='login')
def dashboard(request):
    total_supplier = Supplier.objects.count()
    total_material = Material.objects.count()
    total_product = Product.objects.count()
    total_order = Order.objects.count()
    total_dealer = Dealer.objects.count()
    #orders = Order.objects.all().order_by('-id')
    context = {
        'supplier': total_supplier,
        'material': total_material,
        'product': total_product,
        'order': total_order,
        'dealer': total_dealer
    }
    return render(request, 'dashboard.html', context)

