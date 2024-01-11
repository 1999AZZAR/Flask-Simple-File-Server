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

## Installation

Setting up FSFS is a straightforward process. Follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/1999AZZAR/Flask-Simple-File-Server.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    python the_server.py
    ```

    Access the server at [http://localhost:2500](http://localhost:2500).

## Usage

FSFS offers a user-friendly experience for managing files. Users can utilize the provided API endpoints to interact with the file server. Refer to the [API Endpoints](#api-endpoints) section for detailed information.

## API Endpoints

### 1. Upload File

**Endpoint:** `/upload`  
**Method:** `POST`  
**Parameters:**

- `file`: The file to be uploaded
- [example](code/file_upload.py)

### 2. Download File

**Endpoint:** `/download/<filename>`  
**Method:** `GET`  
**Parameters:**

- `filename`: The name of the file to be downloaded
- [exapmle](code/file_download.py)

### 3. List Files

**Endpoint:** `/list`  
**Method:** `GET`  
**Returns:** JSON array containing details of all uploaded files

- [example](code/file_list.py)

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
  J -->|Null| Q[Null Folder]
  K -->|Save file| R[Insert file record]
  R --> S[Debug message]
  S -->|Success| T[Return success message]
  K -->|Return success| T[Return success message]
  L -->|Save file| U[Insert file record]
  U --> V[Debug message]
  V -->|Success| W[Return success message]
  L -->|Return success| W[Return success message]
  M -->|Save file| X[Insert file record]
  X --> Y[Debug message]
  Y -->|Success| Z[Return success message]
  M -->|Return success| Z[Return success message]
  N -->|Save file| AA[Insert file record]
  AA --> AB[Debug message]
  AB -->|Success| AC[Return success message]
  N -->|Return success| AC[Return success message]
  O -->|Save file| AD[Insert file record]
  AD --> AE[Debug message]
  AE -->|Success| AF[Return success message]
  O -->|Return success| AF[Return success message]
  P -->|Save file| AG[Insert file record]
  AG --> AH[Debug message]
  AH -->|Success| AI[Return success message]
  P -->|Return success| AI[Return success message]
  Q -->|Save file| AJ[Insert file record]
  AJ --> AK[Debug message]
  AK -->|Success| AL[Return success message]
  Q -->|Return success| AL[Return success message]
  T --> BM[Response]
  W --> BM[Response]
  Z --> BM[Response]
  AC --> BM[Response]
  AF --> BM[Response]
  AI --> BM[Response]
  AL --> BM[Response]
```

## Contributing

Contributions to FSFS are highly encouraged. Whether it's bug fixes, feature enhancements, or feedback, your input is valuable. Feel free to open issues or submit pull requests.

## License

FSFS is licensed under the [MIT License](LICENSE). Your usage and contributions are subject to the terms specified in the license.
