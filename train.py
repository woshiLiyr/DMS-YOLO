import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 训练参数官方详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

if __name__ == '__main__':
    model = YOLO('xxx/xxx/ultralytics/ultralytics/cfg/models/v8/yolov8.yaml')
    model.train(data='/xxx/xxx/ultralytics/ultralytics/cfg/datasets/RDD2022.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=0,
                workers=8,
                # device='0',
                optimizer='SGD', # using SGD
                # patience=0, # close earlystop
                resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp
                # fraction=0.2,
                project='/xxx/xxx/ultralytics/runs/train',
                name='xxx',
                )
