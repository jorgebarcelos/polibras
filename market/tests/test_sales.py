from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from decimal import Decimal

from market.models import Product, Stock


class TestSale(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="machado", email="machado_assis@art.br",
                                             password="some-very-strong-psw")

        self.product = Product.objects.create(name='Xbox', price=Decimal(100))

        self.stock = Stock.objects.create(product=self.product, quantity=Decimal(2))

    def test_create_sale(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'product': self.product.id,
            'total_qtd': Decimal(1)
        }
        response = self.client.post('/api/v1/sales/create_sales/', data=data)
        self.assertEqual(response.status_code, 201)
        stock = Stock.objects.filter(product=self.product).values('quantity')
        self.assertEqual(stock[0].get('quantity'), 1)
