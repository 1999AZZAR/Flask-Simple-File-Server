import requests

# Replace the following URL with the appropriate endpoint
base_url = "http://localhost:2500"

# Test the /list endpoint
list_url = f"{base_url}/list"

response = requests.get(list_url)

if response.status_code == 200:
    file_list = response.json()
    print("List of files:")
    for file in file_list:
        print(f"ID: {file['id']}, Filename: {file['filename']}, Category: {file['category']}, Upload Time: {file['upload_time']}")
else:
    print(f"Failed to retrieve the list of files. Status code: {response.status_code}")
