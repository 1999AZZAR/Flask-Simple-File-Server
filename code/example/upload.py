import requests

# Replace 'http://your-flask-server-url' with the actual URL where your Flask app is running
server_url = 'http://127.0.0.1:2500'

# Example XML data
xml_data = '<example><data>Hello 2, XML!</data></example>'
xml_upload_url = f'{server_url}/upload/xml'

# Example image data
image_path = 'path/to/your/image.jpg'
# here the endpoint just uncomment one of these 1st line for v1 and 2nd line for v2
# image_upload_url = f'{server_url}/upload/image' 
# image_upload_url = f'{server_url}/upload' 

# Send XML data to the server
xml_response = requests.post(xml_upload_url, files={'xml': ('example.xml', xml_data, 'application/xml')})

# Send image data to the server
image_response = requests.post(image_upload_url, files={'image': ('image.jpg', open(image_path, 'rb'), 'image/jpeg')})

# Check the responses from the server
if xml_response.status_code == 200:
    print('XML data uploaded successfully')
else:
    print(f'Error uploading XML data: {xml_response.text}')

if image_response.status_code == 200:
    print('Image data uploaded successfully')
else:
    print(f'Error uploading image data: {image_response.text}')