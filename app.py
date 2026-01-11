from flask import Flask, render_template
import os

app = Flask(__name__)

# URLs de los proyectos (usar variables de entorno en producción)

DASHBOARD_URL = os.getenv('DASHBOARD_URL', 'http://localhost:8000')
PDF_TOOLS_URL = os.getenv('PDF_TOOLS_URL', 'http://localhost:5001')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    projects = [
        {
            'title': 'Dashboard de Analíticas', 
            'description': 'Sistema de dashboard con visualizaciones de datos, reportes de ventas y análisis en tiempo real. Construido con Django y Chart.js.', 
            'link': '/demo/dashboard',
            'external_link': DASHBOARD_URL,
            'image': '/static/images/dashboard-preview.png',
            'tech': ['Django', 'Chart.js', 'SQLite', 'Bootstrap']
        },
        {
            'title': 'PDF Tools SaaS', 
            'description': 'Herramientas en línea para procesar PDFs: comprimir, dividir, fusionar, convertir a imágenes y viceversa. Plataforma SaaS con sistema de pagos.', 
            'link': '/demo/pdf-tools',
            'external_link': PDF_TOOLS_URL,
            'image': '/static/images/pdf-tools-preview.png',
            'tech': ['Flask', 'PyPDF2', 'Pillow', 'Stripe API']
        }
    ]
    return render_template('portfolio.html', projects=projects)

@app.route('/demo/dashboard')
def demo_dashboard():
    return render_template('demos/dashboard_demo.html', external_link=DASHBOARD_URL)

@app.route('/demo/pdf-tools')
def demo_pdf_tools():
    return render_template('demos/pdf_tools_demo.html', external_link=PDF_TOOLS_URL)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/debug')
def debug():
    """Ruta de diagnóstico para verificar variables de entorno"""
    return f"""
    <h1>Variables de Entorno</h1>
    <p><strong>DASHBOARD_URL:</strong> {DASHBOARD_URL}</p>
    <p><strong>PDF_TOOLS_URL:</strong> {PDF_TOOLS_URL}</p>
    <hr>
    <p>Si ves 'localhost', las variables NO están configuradas en Render.</p>
    """

if __name__ == '__main__':
    # Desarrollo local con debug, producción sin debug
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)