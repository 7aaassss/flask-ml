from ultralytics import YOLO
from PIL import Image

image_path = "1.jpg"
image = Image.open(image_path).convert("RGB")
yolo_model = YOLO("best.pt", task="detect")
results = yolo_model.predict(source=image, verbose=True)

defects = []
for result in results:
    classes = result.boxes.cls  # Метки классов
    confidences = result.boxes.conf  # Уверенность

    for cls, conf in zip( classes, confidences):
        defect = {
            "class": int(cls),
            "confidence": float(conf),
        }
        defects.append(defect)

print("YOLO Defects:", defects)