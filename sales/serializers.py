from rest_framework import serializers
from sales.models import Sales, Products


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = [
                  'id',
                  'firstName',
                  'lastName',
                  'productName',
                  'quantity'
                  ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
                  'id',
                  'product',
                  'price',
                  'quantity'
                  ]