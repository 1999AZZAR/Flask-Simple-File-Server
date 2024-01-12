from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import sqlite3
import logging

app = Flask(__name__)
CORS(app)

BASE_FOLDER = '/media/azzar/betha/Downloads/project/quick_count/databased/'
OTHER_FOLDER = 'other_files'
XML_FOLDER = 'xml_files'
IMG_FOLDER = 'img_files'
VIDEO_FOLDER = 'video_files'
AUDIO_FOLDER = 'audio_files'
DOCUMENT_FOLDER = "document_files"
COMPRESSED_FOLDER = 'compressed_files'
NULL_FOLDER = 'null_files'
GENERAL_FOLDER = 'general_files'
DATABASE = 'files.db'

# Configure logging
log_format = "%(asctime)s - %(levelname)s - %(message)s"
log_file_path = os.path.join(BASE_FOLDER, 'app.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format=log_format)

app.config['OTHER_FOLDER'] = os.path.join(BASE_FOLDER, OTHER_FOLDER)
app.config['XML_FOLDER'] = os.path.join(BASE_FOLDER, XML_FOLDER)
app.config['IMG_FOLDER'] = os.path.join(BASE_FOLDER, IMG_FOLDER)
app.config['VIDEO_FOLDER'] = os.path.join(BASE_FOLDER, VIDEO_FOLDER)
app.config['AUDIO_FOLDER'] = os.path.join(BASE_FOLDER, AUDIO_FOLDER)
app.config['DOCUMENT_FOLDER'] = os.path.join(BASE_FOLDER, DOCUMENT_FOLDER)
app.config['COMPRESSED_FOLDER'] = os.path.join(BASE_FOLDER, COMPRESSED_FOLDER)
app.config['NULL_FOLDER'] = os.path.join(BASE_FOLDER, NULL_FOLDER)
app.config['GENERAL_FOLDER'] = os.path.join(BASE_FOLDER, GENERAL_FOLDER)
app.config['DATABASE'] = os.path.join(BASE_FOLDER, DATABASE)

def initialize_database():
    try:
        conn = sqlite3.connect(app.config['DATABASE'], check_same_thread=False)
        with conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS files (
                    id TEXT PRIMARY KEY,
                    filename TEXT,
                    extension TEXT,
                    category TEXT,
                    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

def generate_file_id():
    current_time = datetime.now().strftime("%y%m%d%H%M%S%f")
    return current_time

def insert_file_record(filename, extension, category):
    file_id = generate_file_id()
    try:
        with sqlite3.connect(app.config['DATABASE'], check_same_thread=False) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO files (id, filename, extension, category) VALUES (?, ?, ?, ?)
            ''', (file_id, filename, extension, category))
    except sqlite3.Error as e:
        logging.error(f"Error inserting file record: {e}")
    finally:
        if conn:
            conn.close()

def debug_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.debug(f"[{timestamp}] {message}")

def save_file(file, folder, filename):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.exists(file_path):
            debug_message(f'File "{filename}" already exists. Updating...')
        else:
            debug_message(f'Saving new file "{filename}"...')
        file.save(file_path)
    except Exception as e:
        logging.error(f"Error saving file: {e}")

def create_folders():
    folders = [
        app.config['OTHER_FOLDER'],
        app.config['XML_FOLDER'],
        app.config['IMG_FOLDER'],
        app.config['VIDEO_FOLDER'],
        app.config['AUDIO_FOLDER'],
        app.config['DOCUMENT_FOLDER'],
        app.config['COMPRESSED_FOLDER'],
        app.config['NULL_FOLDER'],
        app.config['GENERAL_FOLDER'],
    ]
    try:
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
    except Exception as e:
        logging.error(f"Error creating folders: {e}")

def get_category_folder(category):
    folder_mapping = {
        'Null': app.config['NULL_FOLDER'],
        'XML': app.config['XML_FOLDER'],
        'Image': app.config['IMG_FOLDER'],
        'Compressed': app.config['COMPRESSED_FOLDER'],
        'Video': app.config['VIDEO_FOLDER'],
        'Audio': app.config['AUDIO_FOLDER'],
        'Document': app.config['DOCUMENT_FOLDER'],
        'General': app.config['GENERAL_FOLDER'],
    }

    return folder_mapping.get(category, app.config['OTHER_FOLDER'])

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            debug_message("No 'file' in the request.")
            return 'File is required', 400

        user_file = request.files['file']

        if user_file.filename == '':
            debug_message("Invalid file name: empty filename.")
            return 'Invalid file name', 400

        create_folders()

        original_filename, file_extension = os.path.splitext(user_file.filename)

        if file_extension == '':
            file_folder = app.config['NULL_FOLDER']
            category = 'Null'

        if file_extension in ('', '.'):
            file_folder = app.config['NULL_FOLDER']
            category = 'Null'
        elif file_extension.endswith(('.xml', '.json', '.xsd', '.xsl', '.rss', '.atom')):
            file_folder = app.config['XML_FOLDER']
            category = 'XML'
        elif file_extension.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.raw', '.heif', '.heic', '.ico')):
            file_folder = app.config['IMG_FOLDER']
            category = 'Image'
        elif file_extension.lower().endswith(('.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tgz', '.lzh', '.cab')):
            file_folder = app.config['COMPRESSED_FOLDER']
            category = 'Compressed'
        elif file_extension.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.mpeg', '.mpg', '.3gp', '.webm')):
            file_folder = app.config['VIDEO_FOLDER']
            category = 'Video'
        elif file_extension.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a', '.opus', '.alac')):
            file_folder = app.config['AUDIO_FOLDER']
            category = 'Audio'
        elif file_extension.lower().endswith(('.docx', '.pdf', '.txt', '.rtf', '.odt', '.html', '.pptx', '.xlsx', '.csv', '.pages', '.key', '.numbers', '.tex', '.md')):
            file_folder = app.config['DOCUMENT_FOLDER']
            category = 'Document'
        else:
            file_folder = app.config['GENERAL_FOLDER']
            category = 'General'

        filename = original_filename + file_extension
        file_path = os.path.join(file_folder, filename)

        conn = sqlite3.connect(app.config['DATABASE'], check_same_thread=False)
        with conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM files WHERE filename = ?', (filename,))
        conn.commit()
        conn.close()

        save_file(user_file, file_folder, filename)
        insert_file_record(filename, file_extension, category)
        debug_message(f'File uploaded successfully with filename: {filename}, extension: {file_extension}, and '
                      f'category: {category}')

        return f'File uploaded successfully with filename: {filename}, extension: {file_extension}, and ' \
               f'category: {category}'

    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return 'Internal Server Error', 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        file_path = get_file_path(filename)

        if file_path is None:
            return 'File not found', 404

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        logging.error(f"Error downloading file: {e}")
        return 'Internal Server Error', 500

@app.route('/list', methods=['GET'])
def list_files():
    try:
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('SELECT id, filename, extension, category, upload_time FROM files ORDER BY upload_time DESC')
        files = cursor.fetchall()
        conn.close()

        file_list = [{'id': file[0], 'filename': file[1], 'extension': file[2], 'category': file[3], 'upload_time': file[4]} for file in files]

        return jsonify(file_list)

    except Exception as e:
        logging.error(f"Error listing files: {e}")
        return 'Internal Server Error', 500

def get_file_path(filename):
    try:
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('SELECT category FROM files WHERE filename = ?', (filename,))
        category = cursor.fetchone()
        conn.close()

        if category is None:
            return None

        category_folder = get_category_folder(category[0])
        file_path = os.path.join(category_folder, filename)

        return file_path

    except Exception as e:
        logging.error(f"Error getting file path: {e}")
        return None

if __name__ == '__main__':
    create_folders()
    initialize_database()
    app.run(port=2500, debug=True)
