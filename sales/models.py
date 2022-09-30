from django.db import models

# Create your models here.
from djmoney.models.fields import MoneyField


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=255, unique=True)
    price = MoneyField(max_digits=13, decimal_places=2, default_currency='USD')
    quantity = models.IntegerField(blank=True)


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    productName = models.ForeignKey('Products', to_field="product", db_column='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)