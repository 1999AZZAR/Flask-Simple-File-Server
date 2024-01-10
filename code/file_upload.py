import os
import requests

# Specify the server URL
server_url = 'http://localhost:2500//upload'

# Function to upload a file
def upload_file(file_path):
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        files = {'file': (file_name, file)}
        response = requests.post(server_url, files=files)
        print(response.text)

# Upload a JSON file
json_file_path = 'path/to/file.json'
upload_file(json_file_path)

# Upload an image file
image_file_path = 'path/to/file.jpg'
upload_file(image_file_path)

# Upload a zip file
zip_file_path = 'file.zip'
upload_file(zip_file_path)

# Upload a null file
null_file_path = 'path/to/Empty File'
upload_file(null_file_path)

# Upload a doc file
doc_file_path = 'path/to/file.docx'
upload_file(doc_file_path)
