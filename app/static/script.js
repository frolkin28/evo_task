let uploadForm = document.getElementsByClassName('upload-form')[0];

function handleSubmit(event) {
    event.preventDefault();
    let file = document.getElementById('file');
    let datetime = document.getElementById('datetime').value;
    let uploaded_file = file.files[0];
    if (uploaded_file != null && datetime != null) {
        ttl = new Date(datetime);
        current = new Date();
        current.setMinutes(current.getMinutes() + 1);
        if (ttl > current) {
            const formData = new FormData()
            formData.append('file', uploaded_file);
            formData.append('ttl', datetime);

            fetch('http://127.0.0.1:5000/upload', {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    file.value = "";
                    alert(`Url: ${data.url}`);
                })
        }
        else {
            alert('You need set date and time atleast 1 min from now');
        }
    }
    else {
        alert('You need to upload file');
    }

}

uploadForm.addEventListener('submit', handleSubmit)

