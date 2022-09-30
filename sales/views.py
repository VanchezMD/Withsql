from django.shortcuts import render

# Create your views here.
from sales.models import Sales, Products
from rest_framework import generics
from sales.serializers import SaleSerializer, ProductSerializer


class SalesList(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer


class Wisher(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer


class ProdcuctList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class productcrud(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView,):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer