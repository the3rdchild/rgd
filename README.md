
<h1 align="center">
 <img src="https://github.com/the3rdchild/rgd/blob/main/doc/banner2.png" />
</h1>

[RGD](https://github.com/the3rdchild/rgd/) is a simple code that can detect river floating garbage and take note of the time stamp from the video taken and save the representative images of each minute in the folder [Result](https://github.com/the3rdchild/rgd/Result) as the clear image without box (detected image) also the folder containe box in [Inference](https://github.com/the3rdchild/rgd/Result/inference).

## <div align="center">Documentation</div>

This code is using pyhton with minimum requarement is [**Python>=3.8**](https://www.python.org/). Download [RGD](https://github.com/the3rdchild/rgd/) using
```Git
git clone https://github.com/the3rdchild/rgd/
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

the defaul model of yolo is yolov8 located in the [yolov8 model](https://github.com/the3rdchild/rgd/blob/main/Model/) folder with default name:
```
model.pt
```

you can also train your own model and change the class to your data class(es) in [main.py](https://github.com/the3rdchild/rgd/main.py) line 27:
```
total_counts = {"your": 0, "own": 0, "class": 0}
```