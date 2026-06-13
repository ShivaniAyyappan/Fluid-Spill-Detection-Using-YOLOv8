from ultralytics import YOLO
import os

model_path = os.path.join("train", "weights", "best.pt")
model = YOLO("train/weights/best.pt")

model.predict(
    source=0,
    show=True,
    conf=0.4
)