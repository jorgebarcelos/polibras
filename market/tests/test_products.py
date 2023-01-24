from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from decimal import Decimal

from market.models import Product


class TestProduct(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="machado", email="machado_assis@art.br",
                                             password="some-very-strong-psw")

        self.product = Product.objects.create(name='Xbox', price=Decimal(100))

    def test_list_products(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0].get('name'), 'Xbox')

    def test_add_product(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Atari',
            'price': Decimal(50)
        }
        response = self.client.post('/api/v1/products/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), 'Atari')

    def test_edit_product(self):
        self.client.force_authenticate(user=self.user)
        id = self.product.id
        response = self.client.patch(f'/api/v1/products/{id}/', {'price': Decimal(150)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('price'), '150.00')

    def test_delete_product(self):
        self.client.force_authenticate(user=self.user)
        product = Product.objects.create(name='Nintendo', price=Decimal(100))
        id = product.id
        response = self.client.delete(f'/api/v1/products/{id}/')
        self.assertEqual(response.status_code, 204)
