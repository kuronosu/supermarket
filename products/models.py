from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator as MinValidator

# Create your models here.


class LowerCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCaseCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Product(models.Model):
    name = LowerCaseCharField(_('Name'), max_length=30, unique=True)
    price = models.FloatField(_('Price'), validators=[MinValidator(0.1)])
