from django.contrib import admin

from Seller.models import OrderItem, Order

# Register your models here.
admin.site.register(OrderItem)


class CategoryItemInline(admin.TabularInline):
    model = OrderItem
    classes = ('collapse',)
    show_change_link = True
    readonly_fields = ('id',)
    extra = 1

@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    inlines = [CategoryItemInline]