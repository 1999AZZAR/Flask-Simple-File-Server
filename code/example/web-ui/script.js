const serverUrl = 'http://localhost:2500';

function updateFileName() {
    const fileInput = document.getElementById('file');
    const selectedFileName = document.getElementById('selectedFileName');

    if (fileInput.files.length > 0) {
        selectedFileName.textContent = fileInput.files[0].name;
    } else {
        selectedFileName.textContent = 'No file selected';
    }
}

function uploadFile() {
    const fileInput = document.getElementById('file');
    const selectedFileName = document.getElementById('selectedFileName');

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append('file', file);

        fetch(`${serverUrl}/upload`, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log('File uploaded successfully:', data);
            selectedFileName.textContent = 'No file selected'; // Reset the file name display
            fileInput.value = null; // Reset the file input
            fetchFileList(); // Refresh the file list after upload
        })
        .catch(error => console.error('Error uploading file:', error));
    } else {
        console.error('No file selected for upload.');
    }
}

function fetchFileList() {
    fetch(`${serverUrl}/list`)
        .then(response => response.json())
        .then(data => {
            const imageBoxContainer = document.getElementById('imageBoxContainer');
            imageBoxContainer.innerHTML = ''; // Clear existing file names
            data.forEach(file => {
                const imageBox = document.createElement('div');
                imageBox.className = 'image-box';

                const fileName = document.createElement('p');
                fileName.className = 'file-name';
                fileName.textContent = file.filename;

                imageBox.appendChild(fileName);
                imageBoxContainer.appendChild(imageBox);

                // Add click event to download the file
                imageBox.addEventListener('click', () => {
                    window.location.href = `${serverUrl}/download/${file.filename}`;
                });
            });
        })
        .catch(error => console.error('Error fetching file list:', error));
}

// Fetch file list initially
fetchFileList();

// Fetch file list every 5 seconds
setInterval(fetchFileList, 5000);
