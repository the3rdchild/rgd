import cv2
import time
from ultralytics import YOLO
import os

home_directory = os.path.expanduser('D:/Download/perkuliahan/yolo/Floater ocean and river garbage/')
model_path = os.path.join(home_directory, 'best.pt')
video_path = os.path.join(home_directory, 'video.mp4')
result_path = os.path.join(home_directory, 'Result', 'Result.txt')
final_result_path = os.path.join(home_directory, 'Result', 'Tresult.txt')

model = YOLO(model_path)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
deteksi_interval = 3  # Interval detection in seconds
fps = int(cap.get(cv2.CAP_PROP_FPS))
deteksi_txt = open(result_path, "w")
deteksi_txt.write("Interval {} seconds:\n".format(deteksi_interval))

total_counts = {"Glass": 0, "Metal": 0, "Plastic": 0}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1920, 1080))

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

        minutes = int(current_time // 60)
        seconds = int(current_time % 60)

        deteksi_txt.write("Time: {}m:{}s: ".format(minutes, seconds))
        for cls_name, count in class_counts.items():
            deteksi_txt.write("[{}: {}] ".format(cls_name, count))
            if cls_name in total_counts:
                total_counts[cls_name] += count
        deteksi_txt.write("\n")

cap.release()
deteksi_txt.close()

with open(final_result_path, "w") as final_result_txt:
    for cls_name, total in total_counts.items():
        final_result_txt.write("{}: {}\n".format(cls_name, total))

print("Detections finished. Results are in result.txt and Tresult.txt")
