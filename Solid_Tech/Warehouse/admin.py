from django.contrib import admin

from Warehouse.models import Category, Product, IncomingProduct

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(IncomingProduct)