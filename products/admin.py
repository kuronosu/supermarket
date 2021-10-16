from django.contrib import admin

from products.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id']
    list_editable = []
    search_fields = ['name', 'price']
    ordering = ["id"]
