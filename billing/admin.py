from django.contrib import admin

from billing.models import DiscountCode, Invoice, Item

# Register your models here.


@admin.register(DiscountCode)
class AdminDiscountCode(admin.ModelAdmin):
    fields = ('code',)
    list_display = ['id', 'code', 'used']
    list_display_links = ['id']
    list_editable = []
    search_fields = ['id', 'code']
    ordering = ["id"]


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'product', 'quantity']
    list_display_links = ['id']
    list_editable = []
    ordering = ["id"]


@admin.register(Invoice)
class AdminInvoice(admin.ModelAdmin):
    fields = ('client_name', 'client_email')
    list_display = ['id', 'client_name',
                    'client_email', 'discount_code', 'created_at']
    list_display_links = ['id']
    list_editable = []
    ordering = ["id"]
    list_filter = ['client_email', ]
