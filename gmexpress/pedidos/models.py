from django.db import models
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patente} - {self.modelo}"

class Chofer(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        full = self.usuario.get_full_name()
        return full if full else self.usuario.username

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('camino', 'En Camino'),
        ('entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos_cliente")
    descripcion = models.TextField()
    direccion_entrega = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True, related_name="pedidos_asignados")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    evidencia = models.ImageField(upload_to="evidencias/", null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.pk} - {self.cliente.username}"
