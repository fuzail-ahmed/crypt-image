# import sys
import os
import uuid
from flask import Flask, request, send_file, jsonify
from image_processing import process_image
from utils import cleanup_temp_files


app = Flask(__name__)
UPLOAD_FOLDER = 'temp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure temp folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return "CryptImage Backend is running!"


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ['.jpg', '.jpeg', '.png']:
        return jsonify({"error": "Invalid file format"}), 400

    unique_filename = f"{uuid.uuid4()}{file_ext}"
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(temp_path)

    processed_path = process_image(temp_path)
    return jsonify({"message": "File processed successfully", "file_id": unique_filename})


@app.route('/download/<file_id>', methods=['GET'])
def download_image(file_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found or already deleted"}), 404

    return send_file(file_path, as_attachment=True)


@app.route('/cleanup/<file_id>', methods=['POST'])
def cleanup_image(file_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id)
    cleanup_temp_files(file_path)
    return jsonify({"message": "File deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
