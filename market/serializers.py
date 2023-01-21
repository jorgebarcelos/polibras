from rest_framework import serializers
from .models import Product, Stock, Sale


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('quantity', 'product')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('date', 'total_value')
