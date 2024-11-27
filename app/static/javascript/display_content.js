document.addEventListener('DOMContentLoaded', function() {
  const fileInput = document.getElementById('file-input');
  const imageDisplay = document.getElementById('content-display');

  document.querySelectorAll('input[name="content"]').forEach((radio) => {
    radio.addEventListener('change', function() {
      if (this.checked) {
        updateDisplay(this.id);
      }
    });
  });

  function updateDisplay(selectedId) {
    fileInput.value = '';
    imageDisplay.src = imageDisplay.dataset.placeholder;
    switch (selectedId) {
      case 'radio-photo':
        fileInput.setAttribute('accept', '.jpg, .jpeg');
        fileInput.classList.remove('hidden');
        break;
      case 'radio-video':
        fileInput.setAttribute('accept', 'video/*');
        fileInput.classList.remove('hidden');
        break;
      case 'radio-camera':
        fileInput.classList.add('hidden');
        break;
    }
  }

  fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        imageDisplay.src = imageDisplay.dataset.placeholder;
      };
      reader.readAsDataURL(file);
    }
  });
});