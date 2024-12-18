import cv2
import time
from ultralytics import YOLO

from path import model_path, video_path, result_path, final_result_path, class_path 

######################### DETECT #########################
model = YOLO(model_path)
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

######################### RECORD DETECTED OBJECT ###########################
frame_count = 0
deteksi_interval = 3  # Interval detection in seconds
fps = int(cap.get(cv2.CAP_PROP_FPS))
deteksi_txt = open(result_path, "w")
deteksi_txt.write("Interval {} seconds:\n".format(deteksi_interval))

class_path = total_counts

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
            deteksi_txt.write("{}: {} ".format(cls_name, count))
            if cls_name in total_counts:
                total_counts[cls_name] += count
        deteksi_txt.write("\n")

cap.release()
deteksi_txt.close()

with open(final_result_path, "w") as final_result_txt:
    for cls_name, total in total_counts.items():
        final_result_txt.write("{}: {}\n".format(cls_name, total))

print("Detections finished. Results are in result.txt and Tresult.txt")

######################### DETAIL OF THE VIDEO #########################
video = cv2.VideoCapture(video_path)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
FPS = video.get(cv2.CAP_PROP_FPS)
MS = total_frames * 1000 / FPS
ALL = f"Total Video Frame: {total_frames}", f"Video FPS: {FPS}", f"Video Duration: {MS} ms"
video.release()

f = open(final_result_path, "a")
f.write(str(ALL))
