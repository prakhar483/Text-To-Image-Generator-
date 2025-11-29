# utils.py

import os
from datetime import datetime
from pathlib import Path
from io import BytesIO

outputs_dir = Path("outputs")
outputs_dir.mkdir(exist_ok=True)

def save_image(image, directory=outputs_dir):
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    path = directory / filename
    image.save(path)
    return path

def list_saved_images(directory=outputs_dir):
    return sorted(directory.glob("*.png"), reverse=True)

def get_image_bytes(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()
