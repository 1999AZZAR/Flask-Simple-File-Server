# Flask Simple File Server (FSFS)

## Table of Contents

- [Flask Simple File Server (FSFS)](#flask-simple-file-server-fsfs)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
    - [1. Upload File](#1-upload-file)
    - [2. Download File](#2-download-file)
    - [3. List Files](#3-list-files)
    - [4. List Files with Specific File Format or Extension](#4-list-files-with-specific-file-format-or-extension)
    - [5. Delete File](#5-delete-file)
  - [Database Structure](#database-structure)
  - [File Categories](#file-categories)
  - [Flowchart](#flowchart)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

Flask Simple File Server (FSFS) is a robust and user(admin)-friendly data application developed with Flask. Its primary purpose is to facilitate seamless file management, offering features like file upload, download, and categorization. Built on top of Flask, FSFS ensures a lightweight and efficient solution for organizing and accessing files.

## Features

1. **File Upload and Categorization:** Users can effortlessly upload files through the intuitive web interface. FSFS automatically categorizes files based on their extensions, making it easy to organize and locate them.

2. **File Download:** Downloading files is straightforward. Users can retrieve files by specifying the filename, and FSFS provides a direct download link for quick access.

3. **File Listing:** FSFS maintains a detailed list of all uploaded files, including essential information such as filename, extension, category, and upload timestamp. This feature enhances visibility and allows users to review their uploaded content easily.

4. **File Categorization:** Uploaded files are intelligently organized into distinct folders according to their file types. This systematic categorization includes folders for images, videos, audio files, documents, compressed files, XML-related files, and a miscellaneous folder for unrecognized file types.

5. **SQLite Database Integration:** FSFS utilizes an SQLite database (`files.db`) to store and manage file metadata. The database ensures data persistence and enables efficient retrieval of file information.

6. **General Folder:** FSFS now includes a "GENERAL_FOLDER" for files with extensions not covered by existing categories.

7. **Enhanced Download Endpoints:** Added new download endpoints for better user experience, supporting specific files, file formats, extensions, and bulk downloads.

## Installation

Setting up FSFS is a straightforward process. Follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/1999AZZAR/Flask-Simple-File-Server.git
    cd Flask-Simple-File-Server
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    cd code
    python the_server.py
    ```

    Access the server at [http://localhost:2500](http://localhost:2500) and [here](instruction.md) for more detailed instructions.

## Usage

FSFS offers a user-friendly experience for managing files. Users can utilize the provided API endpoints to interact with the file server. Refer to the [API Endpoints](#api-endpoints) section for detailed information.

## API Endpoints

### 1. Upload File

**Endpoint:** `/upload`  
**Method:** `POST`  
**Parameters:**

- `file`: The file to be uploaded
- [example](code/example/api-call/file_upload.py)

### 2. Download File

**Endpoint:** `/download`  
**Method:** `GET`  
**Parameters:**

- `filename`: The name of the file to be downloaded
- `fileformat`: The file format for bulk download
- `extension`: The file extension for bulk download
- `all`: Download all files
- usage example `/download?fileformat=Image` will download all image files.
- [code example](code/example/api-call/file_download.py)

### 3. List Files

**Endpoint:** `/list`  
**Method:** `GET`  
**Returns:** JSON array containing details of all uploaded files

- [example](code/example/api-call/file_list.py)

### 4. List Files with Specific File Format or Extension

- To list files of a specific file format, use `/list?fileformat=<your_file_format>`
- To list files with a specific extension, use `/list?extension=<your_extension>`

For example:

- `/list?fileformat=Image` will list all image files.
- `/list?extension=.pdf` will list all PDF files.

### 5. Delete File

**Endpoint:** `/delete/<filename>`  
**Method:** `DELETE`  
**Parameters:**

- `filename`: The name of the file to be deleted

Usage example: `/delete/myfile.txt` will delete the file named "myfile.txt".

## Database Structure

FSFS employs an SQLite database (`files.db`) with a table named `files` to store file information. The table structure is as follows:

- `filename`: Name of the uploaded file
- `extension`: File extension
- `category`: File category (e.g., Image, Video)
- `upload_time`: Timestamp of when the file was uploaded

## File Categories

Files are intelligently categorized into the following folders based on their extensions:

- `other_files`: Miscellaneous files
- `xml_files`: XML-related files
- `img_files`: Image files
- `video_files`: Video files
- `audio_files`: Audio files
- `document_files`: Document files
- `compressed_files`: Compressed files
- `null_files`: Files with no recognizable extension
- `general_files`: Files with unknown extensions

## Flowchart

[![](https://mermaid.ink/img/pako:eNqFlllzokAUhf_KrX7xxaSIcUEeZgrFBfdEs7bzwEBrqBFwGkjFCfnv0zSJUZqlfKA559x7vwYKeUemZxGkoC019i-w0tYugIpvyd-Q-MEvuLj4ES3my1UEHdx9IeYfqGzsHamA7QL9DMUlHZ6ceRF0WXEQUhcqfRYE2-c5mxKrUoW6JJ3En4gfgYYHJIDQJxTiztzWuJ3Mi0XXcEgEPay7r8bOto7aT57ufTfrH4efRiHOnkzvHWEHuEuJERDYeDuLUJ_bg9iGIefi5eQtIK5vey63h9zW8dBwrbi3l_L1Y_cR1i3iBvbmkPQx2aStRw88NuKxx-kkgjFmB-hzhBNPd4wt2_YE84Xodz1nT4nvEyuCKf4-E5P3tkUYzwzzheiroWUzf475QvQ1zwwdtpMIFvhrLaYGxCXU2EVwgz-XYmYW7ljgFsfHU3fM3aXxSvilimDJbjZ7Jj7vACWmRy2eXPLLv8Ia-R1uwWE7ZheHO6ukR2iaTIzg7utZ8BPlLJvMOw-UlEzSiPd5iPcc8SED8eEc8bF8XhqxsGSaRnzKQ3ziiM8ZiM_niKpaPjAJrNnvm7O4bpYGVTt5pCp_V4DazWBVuylYrXxo-oIW18wF0F4uaC8B7WeB9lOgg_KhAmhhzUIAHeaCJm8wVc8C1VOgo_KhAmhhzY0AOs4FHSegkyzQSQp0Wj5UAC2suRVAZ7mgswR0ngU6T4EuyocKoIU1d3x4J96Mv_cYIVcfM1VVzZa1bHmQLY-y5Wm2vBBkVEUOoY5hW-zL4z0OrVHwQhyyRgpbWgb9s0Zr94PljDDwlgfXREpAQ1JF4d5i_6KabbAPFgcpG2PnM3VvuM-e53yF2ClS3tEbUmrtS6kmy3JdbsotudlqV9EBKY3aZfPqWmpKckNut6TaVeOjiv7xBtJlqy7XrqXGtVxrS_X2VevjPyFrDDo?type=png)](https://mermaid.live/edit#pako:eNqFlllzokAUhf_KrX7xxaSIcUEeZgrFBfdEs7bzwEBrqBFwGkjFCfnv0zSJUZqlfKA559x7vwYKeUemZxGkoC019i-w0tYugIpvyd-Q-MEvuLj4ES3my1UEHdx9IeYfqGzsHamA7QL9DMUlHZ6ceRF0WXEQUhcqfRYE2-c5mxKrUoW6JJ3En4gfgYYHJIDQJxTiztzWuJ3Mi0XXcEgEPay7r8bOto7aT57ufTfrH4efRiHOnkzvHWEHuEuJERDYeDuLUJ_bg9iGIefi5eQtIK5vey63h9zW8dBwrbi3l_L1Y_cR1i3iBvbmkPQx2aStRw88NuKxx-kkgjFmB-hzhBNPd4wt2_YE84Xodz1nT4nvEyuCKf4-E5P3tkUYzwzzheiroWUzf475QvQ1zwwdtpMIFvhrLaYGxCXU2EVwgz-XYmYW7ljgFsfHU3fM3aXxSvilimDJbjZ7Jj7vACWmRy2eXPLLv8Ia-R1uwWE7ZheHO6ukR2iaTIzg7utZ8BPlLJvMOw-UlEzSiPd5iPcc8SED8eEc8bF8XhqxsGSaRnzKQ3ziiM8ZiM_niKpaPjAJrNnvm7O4bpYGVTt5pCp_V4DazWBVuylYrXxo-oIW18wF0F4uaC8B7WeB9lOgg_KhAmhhzUIAHeaCJm8wVc8C1VOgo_KhAmhhzY0AOs4FHSegkyzQSQp0Wj5UAC2suRVAZ7mgswR0ngU6T4EuyocKoIU1d3x4J96Mv_cYIVcfM1VVzZa1bHmQLY-y5Wm2vBBkVEUOoY5hW-zL4z0OrVHwQhyyRgpbWgb9s0Zr94PljDDwlgfXREpAQ1JF4d5i_6KabbAPFgcpG2PnM3VvuM-e53yF2ClS3tEbUmrtS6kmy3JdbsotudlqV9EBKY3aZfPqWmpKckNut6TaVeOjiv7xBtJlqy7XrqXGtVxrS_X2VevjPyFrDDo)

## Contributing

Contributions to FSFS are highly encouraged. Whether it's bug fixes, feature enhancements, or feedback, your input is valuable. Feel free to open issues or submit pull requests.

## License

FSFS is licensed under the [MIT License](LICENSE). Your usage and contributions are subject to the terms specified in the license.
