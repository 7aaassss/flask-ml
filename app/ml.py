import cv2
import matplotlib.pyplot as plt
from ultralytics import RTDETR, YOLO
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

detr_model_path = os.path.join(root_dir, "last.pt")
yolo_model_path = os.path.join(root_dir, "best.pt")

detr_model = RTDETR(detr_model_path)
yolo_model = YOLO(yolo_model_path)

def show_detected_image(img_path, method):
    img = cv2.imread(img_path)
    if method == 'd':
        results = detr_model(img)
    elif method == 'y':
        results = yolo_model(img)
    detect_img = results[0].plot()
    detect_img = cv2.cvtColor(detect_img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 10))
    plt.imshow(detect_img)
    plt.axis('off')
    filename = "processed_" + os.path.basename(img_path)
    processed_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', filename)
    plt.savefig(processed_path, bbox_inches='tight', pad_inches=0.1)
    
    return filename
