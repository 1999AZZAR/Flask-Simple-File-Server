import requests

# Replace 'your_server_url' with the actual URL where your Flask server is running
server_url = 'http://your_server_url:2500'

# Example: Downloading an individual file
filename = '20220101120000.xml'  # Replace with the actual filename you want to download
download_endpoint = f'{server_url}/download/{filename}'
response = requests.get(download_endpoint)
with open(f'downloaded_{filename}', 'wb') as file:
    file.write(response.content)

# Example: Downloading all files as a zip
all_files_zip_endpoint = f'{server_url}/download/all'
response = requests.get(all_files_zip_endpoint)
with open('downloaded_all_files.zip', 'wb') as file:
    file.write(response.content)

# Example: Downloading files of a specific format as a zip
file_format = 'json'  # Replace with the desired file format
format_zip_endpoint = f'{server_url}/download/format/{file_format}'
response = requests.get(format_zip_endpoint)
with open(f'downloaded_all_files_{file_format}.zip', 'wb') as file:
    file.write(response.content)