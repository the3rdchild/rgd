from ultralytics import YOLO
import os

home_directory = os.path.expanduser("path/to/your/home")
image_path = os.path.join(home_directory,"Result", "Capture")
image_out = os.path.join(home_directory,"Result", "Capture")
model_path = os.path.join(home_directory, 'Model', 'model.pt')

model = YOLO(model_path)
detect = model(image_path, 
               save=True, 
               save_crop=False, 
               project=image_out, 
               name="inference", 
               exist_ok=True)
