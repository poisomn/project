from django.urls import path
from . import views

urlpatterns = [
    # Cliente
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('mis/', views.mis_pedidos, name='mis_pedidos'),

    # Admin
    path('admin/lista/', views.lista_pedidos, name='lista_pedidos'),
    path('admin/asignar/<int:pk>/', views.asignar_pedido, name='asignar_pedido'),

    # Chofer
    path('chofer/', views.pedidos_chofer, name='pedidos_chofer'),
    path('chofer/actualizar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),
]
