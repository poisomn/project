# GMExpress – Sistema de distribución (Django)

Proyecto listo para correr con Django. Incluye:
- App `pedidos` con modelos: Vehiculo, Chofer, Pedido
- Roles por grupos: Admin (staff), Chofer, Cliente
- Flujo Cliente: crear pedido y ver "Mis pedidos"
- Flujo Admin: listar, asignar chofer/vehículo, actualizar estados, dashboard básico
- Flujo Chofer: ver pedidos asignados, marcar entregado y subir evidencia (foto/firma)
- Seed de datos para partir altiro

## 1) Requisitos
- Python 3.10+
- pip

## 2) Crear entorno y paquetes
### Windows (PowerShell)
```powershell
cd gmexpress
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Linux/Mac
```bash
cd gmexpress
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3) Migraciones y seed
```bash
python manage.py migrate
python manage.py seed_data     # crea grupos, usuarios demo y data base
python manage.py createsuperuser  # opcional si quieres otro admin
```

Usuarios demo (cámbialos en producción):
- Admin: **admin / admin1234**
- Chofer: **chofer1 / chofer1234**
- Cliente: **cliente1 / cliente1234**

## 4) Levantar servidor
```bash
python manage.py runserver
```

- Ir a: http://127.0.0.1:8000/
- Login / Signup en la barra superior.

## 5) Notas
- Archivos de evidencia se guardan en `media/evidencias/`
- Ajusta zona horaria, idioma y URL base en `settings.py`
- Este es un MVP, listo para iterar (por ejemplo, mapas, rutas, costos, etc.)
