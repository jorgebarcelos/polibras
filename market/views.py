from decimal import Decimal

from .models import Product, Stock, Sale
from .serializers import ProductSerializer, StockSerializer, SaleSerializer, SalePayloadSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
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

    @action(detail=False, methods=['post'], url_path='create_sales')
    def create_sale(self, request):
        product_id = request.data['product']
        total_sold = int(request.data['total_qtd'])
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            # Tratar exceção caso o produto não exista
            return Response('Produto não encontrado', status=status.HTTP_400_BAD_REQUEST)

        stock = Stock.objects.filter(product=product_id)

        if stock.get().quantity >= total_sold:
            # Cria nova venda
            new_sale = Sale.objects.create(product=product, total_qtd=Decimal(total_sold))

            # Atualiza o estoque
            quantity_updated = (stock.get().quantity - int(total_sold))
            stock.update(quantity=quantity_updated)

            serializer = self.get_serializer(new_sale)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response('Produto não tem quantidade suficiente em estoque para esta venda.',
                        status=status.HTTP_400_BAD_REQUEST)


class SalePayloadViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalePayloadSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SalePayloadSerializer
        if self.request.method == "GET":
            return SaleSerializer
        return SaleSerializer
