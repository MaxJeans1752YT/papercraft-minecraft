
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
from utils.papercraft_generator import create_template_with_tabs

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/generate', methods=['POST'])
def generate():
    skin1 = request.files['skin1']
    skin2 = request.files['skin2']
    show_guides = request.form.get('guides') == 'on'

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    skin1_path = os.path.join(UPLOAD_FOLDER, f'skin1_{timestamp}.png')
    skin2_path = os.path.join(UPLOAD_FOLDER, f'skin2_{timestamp}.png')
    skin1.save(skin1_path)
    skin2.save(skin2_path)

    png_out = os.path.join(OUTPUT_FOLDER, f'plantilla_{timestamp}.png')
    pdf_out = os.path.join(OUTPUT_FOLDER, f'plantilla_{timestamp}.pdf')

    create_template_with_tabs(skin1_path, skin2_path, png_out, pdf_out, show_guides)

    return jsonify({
        'png_url': f'/output/plantilla_{timestamp}.png',
        'pdf_url': f'/output/plantilla_{timestamp}.pdf',
        'skin1_url': f'/{skin1_path}'
    })

@app.route('/output/<path:filename>')
def output_files(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@app.route('/uploads/<path:filename>')
def skin_files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
