# instruction

## Initial Setup

1. **Clone the Repository:**
   - Open a terminal or command prompt.
   - Run the following commands:

     ```bash
     git clone git clone https://github.com/1999AZZAR/Flask-Simple-File-Server.git
     cd Flask-Simple-File-Server
     ```

2. **Create a Virtual Environment (Optional but recommended):**
   - If you don't have `virtualenv` installed, you can install it using:

     ```bash
     pip install virtualenv
     ```

   - Create a virtual environment in the project folder:

     ```bash
     virtualenv venv
     ```

   - Activate the virtual environment:
     - On Windows:

       ```bash
       .\venv\Scripts\activate
       ```

     - On Unix or MacOS:

       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   - Install the required dependencies using:

     ```bash
     pip install -r requirements.txt
     ```

4. **Database Initialization:**
   - Run the Flask application to initialize the database and create necessary folders:

     ```bash
     cd code
     python the_server.py
     ```

     This step creates the `files.db` database and the required folders for file storage.

5. **Run the Application:**
   - Start the Flask application:

     ```bash
     python the_server.py
     ```

     The application will run on port 2500.

## Subsequent Runs

1. **Activate Virtual Environment (if using venv):**
   - If the virtual environment is not already activated:
     - On Windows:

       ```bash
       .\venv\Scripts\activate
       ```

     - On Unix or MacOS:

       ```bash
       source venv/bin/activate
       ```

2. **Run the Application:**
   - Start the Flask application:

     ```bash
     python the_server.py
     ```

     The application will start, and you can access it through the specified port.

## Usage

- **Upload a File:**
  - Use a tool like `curl` or Postman to send a POST request to `http://127.0.0.1:2500/upload`.
  - Include the file in the request with the key `file`.

- **Download a File:**
  - Access a file using the endpoint `http://127.0.0.1:2500/download?filename=<filename>`.
  - Replace `<filename>` with the actual filename you want to download.

- **List Uploaded Files:**
  - Access the list of uploaded files through `http://127.0.0.1:2500/list`.

NB: Remember to deactivate the virtual environment when you're done:

```bash
# On Windows:
deactivate
# On Unix or MacOS:
deactivate
```
