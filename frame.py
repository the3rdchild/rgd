import cv2
import os

from path import rgd, r_path, video_path, output_dir

######################### SAVE THE DETECTED OBJECT RESULT AS REPRESENTATIVE #########################
with open(os.path.join(rgd, "Result", 'Result.txt'), 'r') as file:
    lines = file.readlines()
minute_dict = {}

for line in lines:
    if "Time:" in line:
        time_part = line.split("Time:")[1].split(": ")
        time = time_part[0].strip()
        minute = int(time.split('m')[0])
        class_info = time_part[1].strip()

        class_type = class_info.split(":")[0].strip().capitalize()

        if minute not in minute_dict:
            minute_dict[minute] = {}
        
        if class_type not in minute_dict[minute]:
            minute_dict[minute][class_type] = time

for minute in sorted(minute_dict.keys()):
    classes = minute_dict[minute]

with open(r_path, 'a') as f:
    for minute in sorted(minute_dict.keys()):
        classes = minute_dict[minute]
        out = f"Minute {minute}: " + ", ".join([f"{cls} ({classes[cls]})" for cls in classes])
        f.write(out + "\n")

######################### SAVE REPRESENTATIVE IMAGES #########################
def parse_representative_times(r_path):
    representative_times = []
    with open(r_path, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            for part in parts:
                if "(" in part and ")" in part:
                    time_str = part.split('(')[1].split(')')[0]
                    minutes, seconds = time_str.split('m')
                    seconds = seconds.replace(':', '').replace('s', '').strip()
                    minutes = int(minutes)
                    total_seconds = minutes * 60 + int(seconds)
                    representative_times.append(total_seconds)
    return representative_times

def parse_representative_times_with_classes(r_path):
    times_classes = []
    with open(r_path, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            minute_classes = []
            for part in parts:
                if "(" in part and ")" in part:
                    time_str = part.split('(')[1].split(')')[0]
                    class_name = part.split('(')[0].strip().capitalize()
                    
                    if not class_name:
                        class_name = 'No Object'
                    
                    minutes, seconds = time_str.split('m')
                    seconds = seconds.replace(':', '').replace('s', '').strip()
                    total_seconds = int(minutes) * 60 + int(seconds)
                    minute_classes.append((total_seconds, class_name))
                    
            if minute_classes:
                times_classes.append(minute_classes)
            else:
                times_classes.append([(0, 'No Object')])  # Handle empty minutes with no detection
    return times_classes

def capture_frames_at_times(video, times_classes, path_output_dir):
    vidcap = cv2.VideoCapture(video)

    for minute, time_class_list in enumerate(times_classes):
        for time_sec, class_name in time_class_list:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, time_sec * 1000)  # Move to the specific time
            success, image = vidcap.read()
            if success:
                class_name = class_name.split(":")[-1].split("(")[0].strip().capitalize()  # Extract the actual class name

                frame_name = os.path.join(path_output_dir, f'{minute} {class_name}.png')
                cv2.imwrite(frame_name, image)
                print(f"Captured frame at {time_sec} seconds, saved as {frame_name}")

    vidcap.release()
    cv2.destroyAllWindows()

os.makedirs(output_dir, exist_ok=True)

representative_times_classes = parse_representative_times_with_classes(r_path)
capture_frames_at_times(video_path, representative_times_classes, output_dir)

print("Images saved in ./Result/Capture folder")
