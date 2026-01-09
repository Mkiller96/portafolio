# Render.com - Guía de Despliegue

## 1. Portafolio Principal

### Crear nuevo Web Service en Render:
- **Name**: `mi-portafolio`
- **Root Directory**: `/`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

### Variables de entorno:
```
PYTHON_VERSION=3.11.0
DASHBOARD_URL=https://tu-dashboard.onrender.com
PDF_TOOLS_URL=https://tu-pdf-tools.onrender.com
```

---

## 2. Dashboard Django

### Crear nuevo Web Service en Render:
- **Name**: `dashboard-analytics`
- **Root Directory**: `/dashboard_django`
- **Build Command**: `pip install -r requirements.txt && chmod +x build.sh && ./build.sh`
- **Start Command**: `gunicorn dashboard_project.wsgi:application`

### Variables de entorno:
```
PYTHON_VERSION=3.11.0
SECRET_KEY=tu-clave-secreta-super-segura-aqui
DEBUG=False
ALLOWED_HOSTS=dashboard-analytics.onrender.com
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 3. PDF Tools SaaS

### Crear nuevo Web Service en Render:
- **Name**: `pdf-tools-saas`
- **Root Directory**: `/pdf_tools_saas`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

### Variables de entorno:
```
PYTHON_VERSION=3.11.0
SECRET_KEY=tu-clave-secreta-diferente
STRIPE_SECRET_KEY=tu-clave-de-stripe
DATABASE_URL=sqlite:///pdftools.db
```

---

## Orden de despliegue:

1. **Primero**: Despliega Dashboard y PDF Tools
2. **Copia las URLs** generadas por Render
3. **Actualiza** las variables de entorno del Portafolio con las URLs reales
4. **Despliega** el Portafolio

---

## Notas importantes:

- Render.com ofrece plan gratuito con algunas limitaciones
- Los servicios gratuitos se duermen después de 15 minutos de inactividad
- La primera carga puede tardar 30-60 segundos al despertar
- Para producción real, considera el plan de pago ($7/mes por servicio)

---

## Estructura de repositorios:

Puedes crear 3 repositorios separados en GitHub o usar monorepo con subdirectorios.
Render detectará automáticamente el Root Directory configurado.
