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
    - [4. Web-ui example](#4-web-ui-example)
    - [5. List Files with Specific File Format or Extension](#5-list-files-with-specific-file-format-or-extension)
  - [Database Structure](#database-structure)
  - [File Categories](#file-categories)
  - [Flowchart](#flowchart)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

Flask Simple File Server (FSFS) is a robust and user-friendly web application developed with Flask. Its primary purpose is to facilitate seamless file management, offering features like file upload, download, and categorization. Built on top of Flask, FSFS ensures a lightweight and efficient solution for organizing and accessing files.

## Features

1. **File Upload and Categorization:** Users can effortlessly upload files through the intuitive web interface. FSFS automatically categorizes files based on their extensions, making it easy to organize and locate them.

2. **File Download:** Downloading files is straightforward. Users can retrieve files by specifying the filename, and FSFS provides a direct download link for quick access.

3. **File Listing:** FSFS maintains a detailed list of all uploaded files, including essential information such as filename, extension, category, and upload timestamp. This feature enhances visibility and allows users to review their uploaded content easily.

4. **File Categorization:** Uploaded files are intelligently organized into distinct folders according to their file types. This systematic categorization includes folders for images, videos, audio files, documents, compressed files, XML-related files, and a miscellaneous folder for unrecognized file types.

5. **SQLite Database Integration:** FSFS utilizes an SQLite database (`files.db`) to store and manage file metadata. The database ensures data persistence and enables efficient retrieval of file information.

6. **General Folder:** FSFS now includes a "GENERAL_FOLDER" for files with extensions not covered by existing categories.

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

    Access the server at [http://localhost:2500](http://localhost:2500).
    and [here](instruction.md) the more detailed instruction

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

**Endpoint:** `/download/<filename>`  
**Method:** `GET`  
**Parameters:**

- `filename`: The name of the file to be downloaded
- [example](code/example/api-call/file_download.py)

### 3. List Files

**Endpoint:** `/list`  
**Method:** `GET`  
**Returns:** JSON array containing details of all uploaded files

- [example](code/example/api-call/file_list.py)

### 4. Web-ui example

- [example](code/example/web-ui/)

### 5. List Files with Specific File Format or Extension

- To list files of a specific file format, use `/list?fileformat=<your_file_format>`
- To list files with a specific extension, use `/list?extension=<your_extension>`

For example:

- `/list?fileformat=Image` will list all image files.
- `/list?extension=.pdf` will list all PDF files.

## Database Structure

FSFS employs an SQLite database (`files.db`) with a table named `files` to store file information. The table structure is as follows:

- `id`: Unique identifier for each file (Primary Key)
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

```mermaid
graph TD
  A[Request] -->|POST| B[Check 'file' in request]
  B -->|No| C[Return 'File is required', 400]
  B -->|Yes| D[Get user file]
  D -->|Check filename| E[Invalid filename?]
  E -->|Yes| F[Return 'Invalid file name', 400]
  E -->|No| G[Create folders]
  G --> H[Get file extension]
  H --> I[Handle no extension]
  I -->|No| J[Identify file category]
  J -->|XML| K[XML Folder]
  J -->|Image| L[Image Folder]
  J -->|Compressed| M[Compressed Folder]
  J -->|Video| N[Video Folder]
  J -->|Audio| O[Audio Folder]
  J -->|Document| P[Document Folder]
  J -->|General| Q[General Folder]
  J -->|Null| R[Null Folder]
  K -->|Save file| S[Insert file record]
  S --> T[Debug message]
  T -->|Success| U[Return success message]
  K -->|Return success| U[Return success message]
  L -->|Save file| V[Insert file record]
  V --> W[Debug message]
  W -->|Success| X[Return success message]
  L -->|Return success| X[Return success message]
  M -->|Save file| Y[Insert file record]
  Y --> Z[Debug message]
  Z -->|Success| AA[Return success message]
  M -->|Return

 success| AA[Return success message]
  N -->|Save file| AB[Insert file record]
  AB --> AC[Debug message]
  AC -->|Success| AD[Return success message]
  N -->|Return success| AD[Return success message]
  O -->|Save file| AE[Insert file record]
  AE --> AF[Debug message]
  AF -->|Success| AG[Return success message]
  O -->|Return success| AG[Return success message]
  P -->|Save file| AH[Insert file record]
  AH --> AI[Debug message]
  AI -->|Success| AJ[Return success message]
  P -->|Return success| AJ[Return success message]
  Q -->|Save file| AK[Insert file record]
  AK --> AL[Debug message]
  AL -->|Success| AM[Return success message]
  Q -->|Return success| AM[Return success message]
  R -->|Save file| AN[Insert file record]
  AN --> AO[Debug message]
  AO -->|Success| AP[Return success message]
  R -->|Return success| AP[Return success message]
  U --> BM[Response]
  X --> BM[Response]
  AA --> BM[Response]
  AD --> BM[Response]
  AG --> BM[Response]
  AJ --> BM[Response]
  AM --> BM[Response]
  AP --> BM[Response]
```

## Contributing

Contributions to FSFS are highly encouraged. Whether it's bug fixes, feature enhancements, or feedback, your input is valuable. Feel free to open issues or submit pull requests.

## License

FSFS is licensed under the [MIT License](LICENSE). Your usage and contributions are subject to the terms specified in the license.
