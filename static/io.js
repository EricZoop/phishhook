function predictPercentage() {
  const inputText = document.getElementById('input_text').value;
  const formData = new FormData();
  formData.append('input_text', inputText);

  fetch('/predict', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    const outputContainer = document.getElementById('outputContainer');
    outputContainer.textContent = data.result;

    const body = document.body;
    const backgroundGradient = data.background_color;

    // Apply the background gradient to the body
    body.style.backgroundImage = backgroundGradient;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
