from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np

app = FastAPI()

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    object_coordinates = process_image(image)
    return {"filename": file.filename, "object_coordinates": object_coordinates}


def process_image(image):
    
    #TODO: add image detection here
    
    detected_objects = []

    grid_size = 50
    object_coordinates = []
    for (x, y, w, h) in detected_objects:
        center_x, center_y = x + w // 2, y + h // 2
        grid_x, grid_y = center_x // grid_size, center_y // grid_size
        object_coordinates.append((grid_x, grid_y))

    return object_coordinates
