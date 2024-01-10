from flask import Flask, request, send_from_directory
import os
from datetime import datetime
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def generate_filename(file_extension):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{timestamp}.{file_extension}"

@app.route('/upload/xml', methods=['POST'])
def upload_xml_file():
    if 'xml' not in request.files:
        return 'XML file is required', 400

    xml_file = request.files['xml']

    if xml_file.filename == '':
        return 'Invalid file name', 400

    filename = generate_filename('xml')
    xml_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    xml_file.save(xml_filename)

    return f'XML file uploaded successfully with filename: {filename}'

@app.route('/upload/json', methods=['POST'])
def upload_json_file():
    if 'json' not in request.files:
        return 'JSON file is required', 400

    json_file = request.files['json']

    if json_file.filename == '':
        return 'Invalid file name', 400

    filename = generate_filename('json')
    json_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    json_file.save(json_filename)

    return f'JSON file uploaded successfully with filename: {filename}'

@app.route('/upload/txt', methods=['POST'])
def upload_txt_file():
    if 'txt' not in request.files:
        return 'TXT file is required', 400

    txt_file = request.files['txt']

    if txt_file.filename == '':
        return 'Invalid file name', 400

    filename = generate_filename('txt')
    txt_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    txt_file.save(txt_filename)

    return f'TXT file uploaded successfully with filename: {filename}'

@app.route('/upload/image', methods=['POST'])
def upload_image_file():
    if 'image' not in request.files:
        return 'Image file is required', 400

    image_file = request.files['image']

    if image_file.filename == '':
        return 'Invalid file name', 400

    original_extension = image_file.filename.rsplit('.', 1)[1].lower() if '.' in image_file.filename else 'jpg'

    filename = generate_filename(original_extension)
    image_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image_file.save(image_filename)

    return f'Image file uploaded successfully with filename: {filename}'

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
    app.run(port=2500, debug=True)
