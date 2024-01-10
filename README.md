# Flask Simple File Server (FSFS)

## Introduction

FSFS is a simple Python Flask application that provides file upload and download services. Users can upload XML, JSON, TXT, and image files, and then download them individually or as a zip archive.

## Features

- Upload XML, JSON, TXT, and image files.
- Download files individually or as a zip archive.
- RESTful API for easy file handling.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/1999AZZAR/Flask-Simple-File-Server.git
   cd flask-simple-file-server
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Upload

Send a POST request to `/upload` with the file attached. The server automatically categorizes the file based on its type.

### Download

- To download a file, send a GET request to `/download/filename`.
- To download all files as a zip archive, use `/download/all`.
- To download files of a specific format as a zip archive, use `/download/format/file_format`.

## Examples

- [Upload Example](example/upload.py)
- [Download Example](example/download.py)

## Dependencies

- Flask
- Python (>= 3.6)
- datetime
- shutil
- python-magic

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
