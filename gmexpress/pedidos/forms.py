from django import forms
from django.contrib.auth.models import User
from .models import Pedido

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['descripcion', 'direccion_entrega']

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['chofer', 'vehiculo', 'estado']

class EvidenciaForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['evidencia', 'estado']
        widgets = {
            'estado': forms.Select(choices=[('entregado', 'Entregado'), ('camino', 'En Camino')])
        }
