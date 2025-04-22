from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image, ImageDraw

app = FastAPI()

@app.post("/generar_plantilla/")
async def generar_plantilla(skin: UploadFile = File(...), fold_lines: bool = Form(False)):
    image = Image.open(BytesIO(await skin.read())).convert("RGBA")
    plantilla = Image.new("RGBA", (496, 350), (255, 255, 255, 255))  # Espacio para 2 skins

    plantilla.paste(image.resize((248, 350)), (0, 0))
    plantilla.paste(image.resize((248, 350)), (248, 0))

    draw = ImageDraw.Draw(plantilla)
    if fold_lines:
        for i in range(0, 496, 10):
            draw.line((i, 0, i, 350), fill="gray", width=1)
        for j in range(0, 350, 10):
            draw.line((0, j, 496, j), fill="gray", width=1)

    buf = BytesIO()
    plantilla.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
