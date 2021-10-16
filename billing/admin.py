from django.contrib import admin

from billing.models import DiscountCode, Invoice, Item

# Register your models here.


@admin.register(DiscountCode)
class AdminDiscountCode(admin.ModelAdmin):
    fields = ('code',)


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    pass


@admin.register(Invoice)
class AdminInvoice(admin.ModelAdmin):
    fields = ('client_name', 'client_email')
