from .models import Product, Stock, Sale
from .serializers import ProductSerializer, StockSerializer, SaleSerializer, SalePayloadSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @action(detail=True, methods=['post'])
    def create_sale(self, request, pk=None):
        try:
            product = Product.objects.get(name=product_name)
        except Product.DoesNotExist:
            # Tratar exceção caso o produto não exista
            return 'Produto não encontrado'
        if product.stock.quantity < 1:
            # Tratar exceção caso o estoque esteja esgotado
            return 'Produto esgotado'
        else:
            new_sale = Sale()
            new_sale.save()
            new_sale.products.add(product)
            new_sale.total_value += product.price
            new_sale.save()
            product.stock.quantity -= 1
            product.stock.save()


class SalePayloadViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalePayloadSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SalePayloadSerializer
        if self.request.method == "GET":
            return SaleSerializer
        return SaleSerializer
