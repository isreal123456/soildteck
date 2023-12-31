from django.contrib import admin

from Warehouse.models import Category, Product, IncomingProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(IncomingProduct)


# Register your models here.
