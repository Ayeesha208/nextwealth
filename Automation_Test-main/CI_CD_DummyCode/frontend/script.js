function callBackend() {
  fetch('/api/message')
    .then(response => response.json())
    .then(data => {
      document.getElementById('response').innerText = data.message;
    })
    .catch(error => {
      console.error('Error:', error);
      document.getElementById('response').innerText = "Backend unreachable";
    });
}
