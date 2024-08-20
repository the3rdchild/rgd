import cv2
import time
from ultralytics import YOLO

model = YOLO("best.pt")

video_path = "./video.mp4"  
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
deteksi_interval = 3  # interval detection
fps = int(cap.get(cv2.CAP_PROP_FPS))
deteksi_txt = open("result.txt", "w")  # file output
deteksi_txt.write("interval {} sec:\n".format(deteksi_interval))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    current_time = frame_count / fps

    if current_time % deteksi_interval < 1.0 / fps:
        results = model(frame)
        class_counts = {}

        for result in results:
            for cls in result.boxes.cls:
                cls_name = model.names[int(cls)]
                if cls_name in class_counts:
                    class_counts[cls_name] += 1
                else:
                    class_counts[cls_name] = 1

        deteksi_txt.write("Waktu {:.2f}s: ".format(current_time))
        for cls_name, count in class_counts.items():
            deteksi_txt.write("[{}: {}] ".format(cls_name, count))
        deteksi_txt.write("\n")

cap.release()
deteksi_txt.close()

print("Detections ends, result in result.txt")
