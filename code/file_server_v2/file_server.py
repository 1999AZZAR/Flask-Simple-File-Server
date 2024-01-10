from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import shutil
import sqlite3
import magic

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/databased/other_files'
XML_FOLDER = '/databased/xml_files'
IMG_FOLDER = '/databased/img_files'
NO_EXTENSION_FOLDER = '/databased/no_extension_files'
DATABASE = '/databased/files.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['XML_FOLDER'] = XML_FOLDER
app.config['IMG_FOLDER'] = IMG_FOLDER
app.config['NO_EXTENSION_FOLDER'] = NO_EXTENSION_FOLDER
app.config['DATABASE'] = DATABASE

def initialize_database():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            file_type TEXT,
            upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_file_record(filename, file_type):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO files (filename, file_type) VALUES (?, ?)
    ''', (filename, file_type))
    conn.commit()
    conn.close()

def generate_filename(file_extension):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    if file_extension:
        return f"{timestamp}.{file_extension.lower()}"
    else:
        return f"{timestamp}"

def debug_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def detect_file_type(file):
    mime = magic.Magic()

    # Read the first 1024 bytes to detect the file type
    file_type = mime.from_buffer(file.read(1024))

    if '/' in file_type:
        main_type, sub_type = file_type.split('/')

        # Categorize based on the main type
        if main_type == 'text':
            return 'text'
        elif main_type == 'image':
            return 'image'
        elif main_type == 'application':
            # Further categorize based on the sub type
            if sub_type == 'xml' or sub_type == 'json':
                return 'xml'
            elif sub_type == 'zip' or sub_type == 'rar':
                return 'zip'

    return None

def save_file(file, folder, filename):
    file.save(os.path.join(folder, filename))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        debug_message("No 'file' in the request.")
        return 'File is required', 400

    user_file = request.files['file']

    if user_file.filename == '':
        debug_message("Invalid file name: empty filename.")
        return 'Invalid file name', 400

    file_type = detect_file_type(user_file)
    filename = generate_filename(file_type)

    if not file_type:
        no_extension_filename = os.path.join(app.config['NO_EXTENSION_FOLDER'], filename)
        save_file(user_file, app.config['NO_EXTENSION_FOLDER'], filename)
        insert_file_record(filename, 'unknown')
        debug_message(f'File without extension saved successfully with filename: {filename}')
    else:
        file_folder = app.config['UPLOAD_FOLDER']
        if file_type == 'xml':
            file_folder = app.config['XML_FOLDER']
        elif file_type == 'image':
            file_folder = app.config['IMG_FOLDER']

        file_path = os.path.join(file_folder, filename)
        save_file(user_file, file_folder, filename)
        insert_file_record(filename, file_type)
        debug_message(f'File uploaded successfully with filename: {filename}')

    return f'File uploaded successfully with filename: {filename}'

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if filename == 'all':
        zip_filename = 'all_files.zip'
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)
        shutil.make_archive(zip_path[:-4], 'zip', app.config['UPLOAD_FOLDER'])
        return send_from_directory(app.config['UPLOAD_FOLDER'], zip_filename, as_attachment=True)
    else:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/download/format/<file_format>', methods=['GET'])
def download_files_by_format(file_format):
    zip_filename = f'all_files_{file_format}.zip'
    zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)
    files_to_zip = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith(f'.{file_format}')]
    with shutil.ZipFile(zip_path, 'w') as zip_file:
        for file in files_to_zip:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
            zip_file.write(file_path, os.path.basename(file_path))
    return send_from_directory(app.config['UPLOAD_FOLDER'], zip_filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if not os.path.exists(NO_EXTENSION_FOLDER):
        os.makedirs(NO_EXTENSION_FOLDER)

    initialize_database()
    app.run(port=2500, debug=True)
