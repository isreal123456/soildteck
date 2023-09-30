from django.contrib import admin
from .models import Category,Item

admin.site.register(Item)

class CategoryItemInline(admin.TabularInline):
    model = Item
    classes = ('collapse',)
    show_change_link = True
    readonly_fields = ('id',)
    extra = 1

@admin.register(Category)
class ItemAdmin(admin.ModelAdmin):
    inlines = [CategoryItemInline]
# Register your models here.
