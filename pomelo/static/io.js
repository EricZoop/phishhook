// Fetch the prediction output from the Flask app after form submission
document.getElementById('predictionForm').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission
    const formData = new FormData(event.target);
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('outputContainer').innerHTML = data.result;
    })
    .catch(error => console.error('Error:', error));
});