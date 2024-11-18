from ultralytics import YOLO
from path import image_out, image_path, model_path

model = YOLO(model_path)
detect = model(image_path, 
               save=True, 
               save_crop=False, 
               project=image_out, 
               name="inference", 
               exist_ok=True)
