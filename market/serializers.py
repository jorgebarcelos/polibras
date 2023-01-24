from rest_framework import serializers

from .models import Product, Stock, Sale


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Stock
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Sale
        fields = '__all__'


class SalePayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['product', 'total_qtd']
