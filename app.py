import os
import pytesseract
from pdf2image import convert_from_path
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit for uploads
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def perform_ocr(pdf_path):
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path)
        
        # Perform OCR on each page
        text_results = []
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image, lang='eng')
            text_results.append(f"--- Page {i+1} ---\n{text}\n")
        
        # Combine results
        full_text = '\n'.join(text_results)
        return full_text, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Save uploaded file to temporary location
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Perform OCR
        text, error = perform_ocr(file_path)
        
        # Clean up
        try:
            os.remove(file_path)
        except:
            pass
        
        if error:
            return jsonify({'error': f'OCR failed: {error}'}), 500
        
        return jsonify({'success': True, 'text': text})
    
    return jsonify({'error': 'File type not allowed, please upload a PDF'}), 400

if __name__ == '__main__':
    app.run(debug=True)
