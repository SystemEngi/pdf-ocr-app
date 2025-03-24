# PDF OCR Application

A web application that performs Optical Character Recognition (OCR) on uploaded PDF files using drag and drop functionality.

## Features

- Drag and drop PDF file upload
- OCR processing using Tesseract and PyPDF2
- Display and download extracted text
- Simple and intuitive user interface

## Requirements

- Python 3.8+
- Tesseract OCR engine
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/SystemEngi/pdf-ocr-app.git
   cd pdf-ocr-app
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - For Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
   - For macOS: `brew install tesseract`
   - For Ubuntu/Debian: `sudo apt install tesseract-ocr`

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000`

## Usage

1. Open the application in your browser
2. Drag and drop a PDF file onto the designated area
3. Wait for the OCR processing to complete
4. View the extracted text and download if needed

## License

MIT
