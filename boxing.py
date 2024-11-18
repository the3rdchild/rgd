from ultralytics import YOLO
import os


model = YOLO(model_path)
detect = model(image_path, 
               save=True, 
               save_crop=False, 
               project=image_out, 
               name="inference", 
               exist_ok=True)
