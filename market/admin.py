from django.contrib import admin
from .models import Sale, Product, Stock


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['date', 'total_qtd']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
