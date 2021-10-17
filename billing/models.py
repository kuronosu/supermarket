import random
import string
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from products.models import Product


class DiscountCode(models.Model):
    code = models.CharField(_('Code'), max_length=255, unique=True)
    used = models.BooleanField(_('Used'), default=False)

    @classmethod
    def create_codes(cls):
        return ''.join(random.sample(string.ascii_uppercase, 10))


class Invoice(models.Model):
    client_name = models.CharField(_('Client name'), max_length=255)
    client_email = models.EmailField(_('Client email'), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    discount_code = models.OneToOneField(
        DiscountCode, on_delete=models.CASCADE, blank=True, null=True)


class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items',
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.FloatField(_('Sale price'))
    quantity = models.IntegerField(_('Quantity'), default=1,
                                   validators=[MinValueValidator(1)])
