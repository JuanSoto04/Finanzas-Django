# 💰 Mis Finanzas - Dashboard de Inversiones

Sistema web para la gestión y seguimiento de inversiones personales, desarrollado con Django. Permite registrar compras/ventas de activos, visualizar la distribución de la cartera y analizar la evolución del patrimonio.

## 🎥 Video Demostración
Puedes ver un recorrido completo por las funcionalidades del sistema (Login, CRUD, Buscador y Perfil) en el siguiente enlace:

👉 **[Ver Demo en Loom (5 min)](https://www.loom.com/share/b8fab5b33c7747a6863b8c01fcc6d305)**

## 🚀 Funcionalidades Principales

### 👤 Gestión de Usuarios (NUEVO)
- **Sistema de Registro y Login:** Autenticación segura de usuarios.
- **Perfiles Personalizados:** Cada usuario puede subir y editar su **foto de perfil (Avatar)**.
- **Privacidad:** La información (cuentas y transacciones) es privada y exclusiva de cada usuario.

### 📊 Gestión de Inversiones
- **Dashboard Interactivo:** Gráficos de distribución (Dona) y evolución histórica (Línea) usando Chart.js.
- **CRUD Completo:** Alta, Baja y Modificación de transacciones financieras.
- **Buscador Inteligente:** Filtro de transacciones por símbolo (ej: AAPL) o tipo (Compra/Venta).

### ⚙️ Administración
- Tablas Maestras para Categorías, Activos y Cuentas.
- Página "Sobre Mí" con información del desarrollador.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python, Django.
- **Frontend:** HTML5, CSS3, Bootstrap (Plantilla SB Admin 2).
- **Base de Datos:** SQLite.
- **Librerías Extra:** - `django-humanize` (Formato de moneda).
  - `Chart.js` (Gráficos).
  - `Pillow` (Gestión de imágenes).

## ⚙️ Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/JuanSoto04/Finanzas-Django.git](https://github.com/JuanSoto04/Finanzas-Django.git)
   cd Finanzas-Django

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
(Si el comando `pip` falla, prueba usar: `python -m pip install -r requirements.txt`)

3. **Aplicar Migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
4. **Iniciar El servidor:**
   ```bash
   python manage.py runserver
5.  **Acceso al Sistema:**
    Ingresa a `localhost:8000/`. El sistema solicitará iniciar sesión.

    **Credenciales de prueba (Superusuario):**

      * **Usuario:** soto
      * **Contraseña:** 123456


## Desarrollado por Soto Juan Pablo - 2025




   
