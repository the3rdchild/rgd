from ultralytics import YOLO
import os

home_directory = os.path.expanduser("D:\Download\perkuliahan\yolo\Floater ocean and river garbage")
image_path = os.path.join(home_directory,"Result", "Capture")
image_out = os.path.join(home_directory,"Result", "Capture")
model_path = os.path.join(home_directory, 'Model', 'best.pt')

model = YOLO(model_path)
detect = model(image_path, 
               save=True, 
               save_crop=False, 
               project=image_out, 
               name="inference", 
               exist_ok=True)
