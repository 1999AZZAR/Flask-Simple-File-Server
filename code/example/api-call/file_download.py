import requests

# Replace the following URL with the appropriate endpoint
base_url = "http://localhost:2500"

# Test the /download endpoint with a specific filename
download_filename = "filename.extension"
download_url = f"{base_url}/download?filename={download_filename}"

response = requests.get(download_url)

if response.status_code == 200:
    with open(download_filename, "wb") as file:
        file.write(response.content)
    print(f"File '{download_filename}' downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
