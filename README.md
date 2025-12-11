# 💰 Mis Finanzas - Dashboard de Inversiones

Sistema web para la gestión y seguimiento de inversiones personales, desarrollado con Django. Permite registrar compras/ventas de activos, visualizar la distribución de la cartera y analizar la evolución del patrimonio.

## 🚀 Funcionalidades

- **Dashboard Interactivo:** Gráficos de distribución (Dona) y evolución histórica (Línea) usando Chart.js.
- **Gestión Completa (CRUD):**
  - Alta, Baja y Modificación de Operaciones.
  - Tablas Maestras para Categorías, Activos y Cuentas.
- **Perfil:** Sección "Sobre Mí" del desarrollador.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python, Django.
- **Frontend:** HTML5, CSS3, Bootstrap (Plantilla SB Admin 2).
- **Base de Datos:** SQLite (por defecto).
- **Librerías Extra:** `django-humanize`, `Chart.js`.

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/JuanSoto04/Finanzas-Django.git](https://github.com/JuanSoto04/Finanzas-Django.git)

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
(Si el comando `pip` falla, prueba usar: `python -m pip install -r requirements.txt`)

3. Aplicar Migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
4. Iniciar El servidor:
   ```bash
   python manage.py runserver
5. Ingresa en el navegador a `localhost:8000`


## Desarrollado por Soto Juan Pablo - 2025

   
