from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
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
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.date}'
