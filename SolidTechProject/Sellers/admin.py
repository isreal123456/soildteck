from django.contrib import admin

from Sellers.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

# Register your models here.
