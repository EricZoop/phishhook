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
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  
// Word counter
const textarea = document.getElementById('input_text');
const wordCount = document.getElementById('wordCount');
const characterCount = document.getElementById('characterCount');

// Character counter
textarea.addEventListener('input', updateCounts);

function updateCounts() {
    const inputText = textarea.value.trim();
    const wordsCount = inputText === '' ? 0 : inputText.split(/\s+/).length;
    const charactersCount = inputText.length;

    const wordCountText = wordsCount === 1 ? '1 word' : `${wordsCount} words`;
    const characterCountText = charactersCount === 1 ? '1 character' : `${charactersCount} characters`;

    wordCount.textContent = wordCountText;
    characterCount.textContent = characterCountText;
}

function handleFocus(isFocused) {
    const textarea = document.getElementById('input_text');
    if (isFocused) {
        textarea.placeholder = '';
    } else {
        textarea.placeholder = 'Paste Suspicious Text Here...';
    }
}

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

    // Update the background color
    if (data.background_color) {
      document.body.style.background = data.background_color;
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}