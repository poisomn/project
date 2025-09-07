from django.test import TestCase
from django.contrib.auth.models import User
from .models import Pedido

class PedidoTest(TestCase):
    def test_crear_pedido(self):
        u = User.objects.create_user(username='test', password='123')
        self.client.login(username='test', password='123')
        resp = self.client.post('/pedidos/crear/', {'descripcion': 'Caja', 'direccion_entrega': 'Av. Siempreviva 123'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Pedido.objects.count(), 1)
