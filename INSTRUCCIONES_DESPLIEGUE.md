# Instrucciones detalladas para desplegar en Render.com

## 📦 PASO 1: Dashboard Django

### 1.1 Crear repositorio en GitHub
1. Ve a GitHub y crea un nuevo repositorio llamado `dashboard-django`
2. En tu terminal local:
```bash
cd C:\Users\MS\Documents\portafolio\dashboard_django
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/dashboard-django.git
git push -u origin main
```

### 1.2 Crear Web Service en Render
1. Ve a https://dashboard.render.com
2. Click en "New +" → "Web Service"
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio `dashboard-django`
5. Configura:
   - **Name**: `dashboard-analytics` (o el nombre que prefieras)
   - **Region**: Oregon (US West) o el más cercano
   - **Branch**: `main`
   - **Root Directory**: (dejar vacío)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt && chmod +x build.sh && ./build.sh`
   - **Start Command**: `gunicorn dashboard_project.wsgi:application`

### 1.3 Variables de entorno
En la sección "Environment Variables", agrega:
```
SECRET_KEY=genera-una-clave-segura-aleatoria-de-50-caracteres
DEBUG=False
ALLOWED_HOSTS=dashboard-analytics.onrender.com
```

6. Click en "Create Web Service"
7. Espera 5-10 minutos mientras se despliega
8. **COPIA LA URL** que te da Render (ej: https://dashboard-analytics.onrender.com)

---

## 📄 PASO 2: PDF Tools SaaS

### 2.1 Crear repositorio en GitHub
1. Crea un nuevo repositorio llamado `pdf-tools-saas`
2. En tu terminal:
```bash
cd C:\Users\MS\Documents\portafolio\pdf_tools_saas
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/pdf-tools-saas.git
git push -u origin main
```

### 2.2 Crear Web Service en Render
1. En Render, click "New +" → "Web Service"
2. Selecciona el repositorio `pdf-tools-saas`
3. Configura:
   - **Name**: `pdf-tools-app`
   - **Region**: Oregon (US West)
   - **Branch**: `main`
   - **Root Directory**: (dejar vacío)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### 2.3 Variables de entorno
```
SECRET_KEY=otra-clave-segura-diferente-50-caracteres
STRIPE_SECRET_KEY=sk_test_tu_clave_de_stripe_aqui
```

4. Click en "Create Web Service"
5. **COPIA LA URL** (ej: https://pdf-tools-app.onrender.com)

---

## 🔗 PASO 3: Actualizar Portafolio

### 3.1 Actualizar variables de entorno en Render
1. Ve a tu servicio de portafolio en Render
2. Ve a "Environment" en el menú lateral
3. Agrega estas variables:
```
DASHBOARD_URL=https://tu-url-del-dashboard.onrender.com
PDF_TOOLS_URL=https://tu-url-de-pdf-tools.onrender.com
```
4. Click en "Save Changes"
5. El servicio se redesplegará automáticamente

---

## ⚠️ NOTAS IMPORTANTES:

### Plan gratuito de Render:
- Los servicios se duermen después de 15 minutos sin actividad
- La primera carga puede tardar 30-60 segundos
- Límite de 750 horas/mes (suficiente para demos)

### Si hay errores:
- Revisa los logs en Render (pestaña "Logs")
- Verifica que todas las dependencias estén en requirements.txt
- Asegúrate de que build.sh tenga permisos de ejecución

### Para mejorar el rendimiento:
- Considera el plan de pago ($7/mes por servicio)
- Los servicios de pago no se duermen
- Mejor para demos a reclutadores

---

## 🎯 RESULTADO FINAL:

Una vez completados los 3 pasos:
- ✅ Portafolio: https://portafolio-kjr0.onrender.com
- ✅ Dashboard: https://dashboard-analytics.onrender.com
- ✅ PDF Tools: https://pdf-tools-app.onrender.com

Los reclutadores podrán ver todos tus proyectos funcionando en línea.
