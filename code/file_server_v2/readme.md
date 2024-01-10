# Flask Simple File Server (FSFS)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Upload](#upload)
    - [Uploading XML, JSON, TXT, and Image Files](#uploading-files)
  - [Download](#download)
    - [Downloading Files](#downloading-files)
    - [Download All Files](#download-all-files)
    - [Download Files by Format](#download-files-by-format)
  - [Examples](#examples)
- [Dependencies](#dependencies)
- [Flowchart](#flowchart)
- [License](#license)

## Introduction

This Python Flask application provides a simple file upload and download service. It allows users to upload XML, JSON, TXT, and image files, and then download them individually or as a zip archive.

## Features

- Supports uploading XML, JSON, TXT, and image files.
- Allows downloading files individually or as a zip archive.
- Convenient RESTful API for file handling.

## Installation

1. Clone the repository:

   ```bash
   git clone [repository_url]
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-simple-file-server
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Upload

#### Uploading Files

To upload a file, send a POST request to `/upload` with the file attached. The server will automatically categorize the file based on its type.

### Download

#### Downloading Files

To download a file, send a GET request to `/download/filename`, where `filename` is the name of the file.

##### Download All Files

To download all uploaded files as a zip archive, send a GET request to `/download/all`.

##### Download Files by Format

To download all files of a specific format as a zip archive, send a GET request to `/download/format/file_format`, where `file_format` is the desired file format.

### Examples

- [upload](example/upload.py)
- [downloads](example/download.py)

## Dependencies

- Flask
- Python (>= 3.6)
- datetime
- shutil
- python-magic

Install the required dependencies using the provided `requirements.txt` file.

## Flowchart

```mermaid
flowchart TB

subgraph Init
  A[Start]
  B[Check 'file' in request]
end

subgraph File Upload
  B -- Yes --> C[Get user file]
  C -- Yes --> D[Check if file name is empty]
  D -- No --> E[Detect file type]
  E -- No --> F[Generate filename]
  F --> G[Save file to appropriate folder]
  G --> H[Insert file record to database]
  H --> I[Print success message]
  I --> J[End]

  D -- Yes --> K[Generate filename for file without extension]
  K --> L[Save file without extension to 'no_extension' folder]
  L --> M[Insert file record for file without extension to database]
  M --> N[Print success message for file without extension]
  N --> O[End]
end

subgraph File Download
  B -- No --> P[Print error message]
  P --> Q[End]
  Q --> R[Choose file to download or download all files]
  R -- Single --> S[Download selected file]
  R -- All --> T[Create zip archive for all files]
  S --> U[End]
  T --> U[End]
end

subgraph File Download by Format
  R -- Format --> V[Choose file format to download]
  V --> W[Create zip archive for files with selected format]
  W --> X[End]
end

subgraph Server Initialization
  A --> Y[Check if 'UPLOAD_FOLDER' exists]
  Y -- No --> Z[Create 'UPLOAD_FOLDER']
  Z --> AA[Check if 'NO_EXTENSION_FOLDER' exists]
  AA -- No --> AB[Create 'NO_EXTENSION_FOLDER']
  AB --> AC[Initialize database]
  AC --> AD[Run the server]
end
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
