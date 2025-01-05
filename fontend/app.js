async function uploadFile() {
	const fileInput = document.getElementById('fileInput');
	const statusDiv = document.getElementById('status');

	if (fileInput.files.length === 0) {
			statusDiv.innerText = 'Please select a file.';
			return;
	}

	const formData = new FormData();
	formData.append('file', fileInput.files[0]);

	statusDiv.innerText = 'Uploading...';

	try {
			const response = await fetch('http://localhost:5000/upload', {
					method: 'POST',
					body: formData,
			});

			const result = await response.json();
			if (response.ok) {
					statusDiv.innerHTML = `File processed. <a href="http://localhost:5000/download/${result.file_id}" download>Download Processed Image</a>`;
			} else {
					statusDiv.innerText = `Error: ${result.error}`;
			}
	} catch (error) {
			statusDiv.innerText = `Error: ${error.message}`;
	}
}
