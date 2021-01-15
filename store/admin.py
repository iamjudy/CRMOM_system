from django.contrib import admin

from .models import (
    Dealer,
    Supplier,
    Material,
    Product,
    Order,
    Consume,
    Use,
    Retention,
)

admin.site.register(Supplier)
admin.site.register(Material)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Dealer)
admin.site.register(Consume)
admin.site.register(Use)
admin.site.register(Retention)

