from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
from utils import process_skin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(file: UploadFile = File(...), fold_lines: bool = False):
    temp_id = str(uuid.uuid4())
    os.makedirs("temp", exist_ok=True)
    output_path = f"temp/{temp_id}.pdf"
    png_path = f"temp/{temp_id}.png"

    contents = await file.read()
    with open(f"temp/{temp_id}.png", "wb") as f:
        f.write(contents)

    process_skin(f"temp/{temp_id}.png", output_path, fold_lines=fold_lines)
    return FileResponse(output_path, media_type="application/pdf", filename="papercraft.pdf")