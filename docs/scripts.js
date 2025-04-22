const BACKEND_URL = "https://papercraft-backend.onrender.com"; // Cambiar si es necesario

const form = document.getElementById("uploadForm");
const input = document.getElementById("skinInput");
const toggle = document.getElementById("foldLinesToggle");
const loading = document.getElementById("loading");
const preview = document.getElementById("preview");
const canvas = document.getElementById("skin3d");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = input.files[0];
  if (!file) return;

  loading.style.display = "block";
  preview.style.display = "none";

  const formData = new FormData();
  formData.append("file", file);
  formData.append("fold_lines", toggle.checked);

  const response = await fetch(`${BACKEND_URL}/generate`, {
    method: "POST",
    body: formData
  });

  const blob = await response.blob();

  const pdfURL = URL.createObjectURL(blob);
  document.getElementById("downloadPdf").href = pdfURL;

  // Cargar vista 3D
  const skinViewer = new skinview3d.SkinViewer({
    canvas: canvas,
    width: 300,
    height: 300,
    skin: URL.createObjectURL(file),
  });
  skinViewer.controls.enableZoom = true;
  skinViewer.controls.enableRotate = true;
  skinViewer.animation = new skinview3d.WalkingAnimation();
  skinViewer.animation.speed = 1;

  // Mostrar vista previa
  loading.style.display = "none";
  preview.style.display = "block";
});