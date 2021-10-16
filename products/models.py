from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator as MinValidator

# Create your models here.


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=30, unique=True)
    price = models.FloatField(_('Price'), validators=[MinValidator(0.1)])
