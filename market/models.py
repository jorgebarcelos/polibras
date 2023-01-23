from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name}'


class Stock(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self) -> str:
        return f'{self.quantity}'


class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_qtd = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='sale_products')

    def __str__(self) -> str:
        return f'{self.date}'
