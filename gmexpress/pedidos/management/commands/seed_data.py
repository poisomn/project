from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from pedidos.models import Vehiculo, Chofer, Pedido

class Command(BaseCommand):
    help = "Crea grupos, usuarios demo y datos base."

    def handle(self, *args, **kwargs):
        # Groups
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        chofer_group, _ = Group.objects.get_or_create(name='Chofer')

        # Admin user
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_user('admin', password='admin1234', is_staff=True, is_superuser=False)
            admin.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS('Usuario admin creado: admin / admin1234'))
        else:
            self.stdout.write('Usuario admin ya existe')

        # Chofer user
        if not User.objects.filter(username='chofer1').exists():
            chofer_user = User.objects.create_user('chofer1', password='chofer1234', first_name='Juan', last_name='Pérez')
            chofer_user.groups.add(chofer_group)
            ch = Chofer.objects.create(usuario=chofer_user, telefono='+56 9 1234 5678', activo=True)
            self.stdout.write(self.style.SUCCESS('Usuario chofer1 creado: chofer1 / chofer1234'))
        else:
            ch = Chofer.objects.get(usuario__username='chofer1')

        # Cliente user
        if not User.objects.filter(username='cliente1').exists():
            cliente = User.objects.create_user('cliente1', password='cliente1234', first_name='Cliente', last_name='Demo', email='cliente@demo.cl')
            self.stdout.write(self.style.SUCCESS('Usuario cliente1 creado: cliente1 / cliente1234'))
        else:
            cliente = User.objects.get(username='cliente1')

        # Vehiculos
        v1, _ = Vehiculo.objects.get_or_create(patente='AA-BB11', defaults={'modelo': 'Fiorino', 'capacidad': 800})
        v2, _ = Vehiculo.objects.get_or_create(patente='CC-DD22', defaults={'modelo': 'Sprinter', 'capacidad': 1500})

        # Pedidos demo
        Pedido.objects.get_or_create(cliente=cliente, descripcion='Cajas frágiles', direccion_entrega='Av. Francisco de Aguirre 123, La Serena')
        Pedido.objects.get_or_create(cliente=cliente, descripcion='Repuestos de auto', direccion_entrega='Ruta 5 Norte, Coquimbo', chofer=ch, vehiculo=v1, estado='camino')

        self.stdout.write(self.style.SUCCESS('Seed completado.'))
