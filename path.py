import os

rgd = os.path.dirname(os.path.abspath(__file__))

main
model_path = os.path.join(rgd, 'Model', 'rgd.pt')
video_path = os.path.join(rgd, 'Source', 'video2.mp4')
result_path = os.path.join(rgd, 'Result', 'Result.txt')
final_result_path = os.path.join(rgd, 'Result', 'Tresult.txt')
class_path = os.path.join(rgd, 'class_names.py')

frame
r_path = os.path.join(rgd, "Result", "Representative.txt")
video_path = os.path.join(rgd, 'Source', 'video2.mp4')
output_dir = os.path.join(rgd, 'Result', 'Capture')

box
image_path = os.path.join(rgd,"Result", "Capture")
image_out = os.path.join(rgd,"Result", "Capture")
model_path = os.path.join(rgd, 'Model', 'rgd.pt')
