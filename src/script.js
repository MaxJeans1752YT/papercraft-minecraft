
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const loadingScreen = document.getElementById('loading-screen');
  const preview = document.getElementById('preview');
  const renderContainer = document.getElementById('render-container');

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    loadingScreen.style.display = 'flex';

    fetch('/generate', {
      method: 'POST',
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      loadingScreen.style.display = 'none';
      preview.innerHTML = `
        <h2>Vista previa</h2>
        <img src="${data.png_url}" alt="Vista previa" width="500"><br><br>
        <a href="${data.png_url}" download><button>Descargar PNG</button></a>
        <a href="${data.pdf_url}" download><button>Descargar PDF</button></a>
      `;
      load3DViewer(data.skin1_url);
    });
  });

  function load3DViewer(skinURL) {
    if (renderContainer.children.length > 0) {
      renderContainer.innerHTML = '';
    }
    const viewer = new skinview3d.Player(renderContainer, {
      width: 300,
      height: 400,
      skin: skinURL
    });
    viewer.camera.rotation.y = Math.PI;
    viewer.controls.enableZoom = true;
    viewer.animation = new skinview3d.WalkingAnimation();
    viewer.animation.speed = 1;
    viewer.animation.play();
  }
});
