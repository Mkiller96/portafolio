from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    projects = [
        {'title': 'Proyecto 1', 'description': 'Descripción de tu primer proyecto', 'link': '#'},
        {'title': 'Proyecto 2', 'description': 'Descripción de tu segundo proyecto', 'link': '#'},
        {'title': 'Proyecto 3', 'description': 'Descripción de tu tercer proyecto', 'link': '#'}
    ]
    return render_template('portfolio.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)