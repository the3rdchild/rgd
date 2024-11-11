## <div align="center">RIVER GARBAGE DETECTION</div>
<h1 align="center">
 <img src="https://github.com/the3rdchild/rgd/blob/main/doc/banner2.png" />
</h1>
<div align="center">
 <a href="https://github.com/the3rdchild/rgd/">RGD</a> is a simple code that can detect river floating garbage and take note of the time stamp from the video taken and save the representative images of each minute in the folder <a href="https://github.com/the3rdchild/rgd/tree/main/Result/Capture">Result</a> as the clear image without box (detected image) also the folder containe box in <a href="https://github.com/the3rdchild/rgd/tree/main/Result/Capture/inference">Inference</a>.
</div>




## <div align="center">Documentation</div>

This code is using pyhton with minimum requarement is [**Python>=3.8**](https://www.python.org/). Download [RGD](https://github.com/the3rdchild/rgd/) using
```Git
git clone https://github.com/the3rdchild/rgd/
```

install [requirements.txt](https://github.com/the3rdchild/rgd/blob/main/requirements.txt) using:
```git
pip install requirements.txt
```

## Windows
Use [run.bat](https://github.com/the3rdchild/rgd/blob/main/run.bat) to run the program. this batch file contain simpel program to run all the python file sequently:
```
@echo off
python -u main.py
python -u frame.py
python -u boxing.py
```

## Linux
Use [run.sh](https://github.com/the3rdchild/rgd/blob/main/run.sh) to run the program. this bash file contain simpel program to run all the python file sequently:
```
#!/bin/bash
python3 main.py
python3 frame.py
python3 boxing.py
```

## <div align="center">YoloV8 Model</div>

the defaul model of yolo is yolov8 located in the [model](https://github.com/the3rdchild/rgd/blob/main/Model/) folder with default name:
```
model.pt
```

you can also train your own model and change the class to your data class(es) in [main.py](https://github.com/the3rdchild/rgd/main.py) line 27:
```
total_counts = {"your": 0, "own": 0, "class": 0}
```
