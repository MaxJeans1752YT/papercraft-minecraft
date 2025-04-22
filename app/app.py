from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Aquí iría la lógica para procesar las skins y generar el archivo
    return send_file('output/example.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
