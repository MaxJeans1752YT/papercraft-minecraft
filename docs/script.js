document.addEventListener('DOMContentLoaded', () => {
  const loader = document.getElementById('loader');
  const container = document.getElementById('container');
  setTimeout(() => {
    loader.style.display = 'none';
    container.style.display = 'block';
  }, 2000);

  const form = document.getElementById('uploadForm');
  const foldLines = document.getElementById('foldLines');
  const canvas = document.getElementById('canvas2D');
  const ctx = canvas.getContext('2d');
  const downloadPNG = document.getElementById('downloadPNG');
  const downloadPDF = document.getElementById('downloadPDF');
  const render3D = document.getElementById('render3D');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const file = document.getElementById('skinInput').files[0];
    const formData = new FormData();
    formData.append('skin', file);
    formData.append('fold_lines', foldLines.checked);

    const res = await fetch('https://your-api-url.onrender.com/generar_plantilla/', {
      method: 'POST',
      body: formData
    });
    const blob = await res.blob();
    const img = await createImageBitmap(blob);
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);

    // Renderizado 3D
    const viewer = new skinview3d.SkinViewer({
      canvas: document.createElement('canvas'),
      width: 300,
      height: 400,
      skin: URL.createObjectURL(file)
    });
    viewer.controls.enableZoom = true;
    render3D.innerHTML = '';
    render3D.appendChild(viewer.canvas);
  });

  downloadPNG.addEventListener('click', () => {
    const a = document.createElement('a');
    a.href = canvas.toDataURL();
    a.download = 'papercraft.png';
    a.click();
  });

  downloadPDF.addEventListener('click', () => {
    const a = document.createElement('a');
    a.href = canvas.toDataURL('image/jpeg');
    a.download = 'papercraft.pdf';
    a.click();
  });
});
