from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    """
    Defined Category model
    """
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_categories", null=True, blank=True,
                               verbose_name="Parent Category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """
    Defined Product model
    """
    name = models.CharField(max_length=120)
    categories = models.ManyToManyField(Category, blank=True, related_name="products")
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-id",)
        verbose_name = "Product"
        verbose_name_plural = "Products"
