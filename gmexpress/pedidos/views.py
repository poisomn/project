from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from django.contrib import messages

from .models import Pedido
from .forms import SignupForm, PedidoForm, AsignacionForm, EvidenciaForm
from .decorators import admin_required, chofer_required

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Cuenta creada. Inicia sesión para continuar.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    # Vista genérica: muestra info según rol
    context = {}
    if request.user.is_staff or request.user.groups.filter(name__iexact='Admin').exists():
        context['total_pedidos'] = Pedido.objects.count()
        context['entregados'] = Pedido.objects.filter(estado='entregado').count()
        context['pendientes'] = Pedido.objects.filter(estado='pendiente').count()
        context['en_camino'] = Pedido.objects.filter(estado='camino').count()
        return render(request, 'dashboard.html', context)
    elif request.user.groups.filter(name__iexact='Chofer').exists():
        pedidos = Pedido.objects.filter(chofer__usuario=request.user).order_by('-fecha_creacion')
        context['pedidos'] = pedidos
        return render(request, 'chofer/pedidos.html', context)
    else:
        pedidos = Pedido.objects.filter(cliente=request.user).order_by('-fecha_creacion')
        context['pedidos'] = pedidos
        return render(request, 'cliente/mis_pedidos.html', context)

# Cliente
@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.cliente = request.user
            p.save()
            messages.success(request, 'Pedido creado correctamente.')
            return redirect('mis_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'cliente/crear_pedido.html', {'form': form})

@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-fecha_creacion')
    return render(request, 'cliente/mis_pedidos.html', {'pedidos': pedidos})

# Admin
@admin_required
def lista_pedidos(request):
    estado = request.GET.get('estado')
    pedidos = Pedido.objects.all().order_by('-fecha_creacion')
    if estado in ('pendiente', 'camino', 'entregado'):
        pedidos = pedidos.filter(estado=estado)
    return render(request, 'admin/lista_pedidos.html', {'pedidos': pedidos, 'estado': estado})

@admin_required
def asignar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = AsignacionForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido asignado/actualizado.')
            return redirect('lista_pedidos')
    else:
        form = AsignacionForm(instance=pedido)
    return render(request, 'admin/asignar_pedido.html', {'form': form, 'pedido': pedido})

# Chofer
@chofer_required
def pedidos_chofer(request):
    pedidos = Pedido.objects.filter(chofer__usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'chofer/pedidos.html', {'pedidos': pedidos})

@chofer_required
def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, chofer__usuario=request.user)
    if request.method == 'POST':
        form = EvidenciaForm(request.POST, request.FILES, instance=pedido)
        if form.is_valid():
            p = form.save(commit=False)
            if p.estado == 'entregado' and p.fecha_entrega is None:
                p.fecha_entrega = timezone.now()
            p.save()
            messages.success(request, 'Pedido actualizado.')
            return redirect('pedidos_chofer')
    else:
        form = EvidenciaForm(instance=pedido)
    return render(request, 'chofer/actualizar_pedido.html', {'form': form, 'pedido': pedido})
