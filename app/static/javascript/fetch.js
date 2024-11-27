const img = document.getElementById('content-display');
const startButton = document.getElementById('start-button');

let isPlaying = false;

async function makeRequest(url, method, formData) {
  const contentType = formData.get('content');
  
  let response = await fetch(url, {
    method: method,
    body: formData
  });

  const data = await response.json();

  if (contentType === 'video' || contentType === 'camera') {
    img.src = `/video_feed/${data.video_id}?model=${data.model}&content_type=${data.content_type}`;
    isPlaying = true;
    startButton.textContent = 'Остановить';
    
    img.onended = function() {
      isPlaying = false;
      startButton.textContent = 'Запустить';
      img.src = img.dataset.placeholder;
    };
  } else {
    img.src = data.image_path;
  }
}

startButton.addEventListener('click', async function(e) {
  e.preventDefault();
  const formData = new FormData(document.querySelector('form'));
  const contentType = formData.get('content');
  console.log(contentType);

  if (contentType === 'video' || contentType === 'camera') {
    if (isPlaying) {

      img.src = img.dataset.placeholder;
      isPlaying = false;
      startButton.textContent = 'Запустить';

      return;
    }
  }

  try {
    await makeRequest('/object-detection', 'POST', formData);
  } catch (error) {
    console.error('Error:', error);
  }
});