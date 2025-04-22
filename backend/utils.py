from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def process_skin(image_path, output_pdf_path, fold_lines=False):
    # Carga la imagen
    skin = Image.open(image_path).convert("RGBA")
    template = Image.new("RGBA", (595, 842), (255, 255, 255, 255))  # A4 in pixels at 72 PPI
    draw = ImageDraw.Draw(template)

    # Aquí iría el código para recortar y colocar las partes del cuerpo en posiciones específicas
    # Añade guías de doblado si fold_lines es True

    # Por simplicidad, solo pegamos la imagen original en la esquina
    template.paste(skin.resize((128, 128)), (50, 50))

    # Guarda la imagen temporal como PNG
    temp_png_path = output_pdf_path.replace(".pdf", ".png")
    template.save(temp_png_path)

    # Usa ReportLab para exportar a PDF
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    c.drawImage(temp_png_path, 0, 0, width=A4[0], height=A4[1])
    c.save()
    os.remove(temp_png_path)