import os
import requests
import tkinter as tk
from tkinter import filedialog

# Specify the server URL
server_url = 'http://localhost:2500/upload'

# Function to upload a file
def upload_files(file_paths):
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as file:
            files = {'file': (file_name, file)}
            response = requests.post(server_url, files=files)
            print(response.text)

# Create a Tkinter root window (it will be hidden)
root = tk.Tk()
root.withdraw()

# Ask the user to select multiple files
file_paths = filedialog.askopenfilenames(title="Select files", filetypes=[("All files", "*.*")])

# Check if files were selected before attempting to upload
if file_paths:
    # Upload the selected files
    upload_files(file_paths)
else:
    print("No files selected.")
