import cv2
import matplotlib.pyplot as plt
from ultralytics import RTDETR, YOLO
import os
from app import app


detr_model = RTDETR("last.pt")
yolo_model = YOLO("best.pt")

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
    processed_path = os.path.join(os.getcwd(),'app', 'static', filename)
    plt.savefig(processed_path, bbox_inches='tight', pad_inches=0.1)
    return filename
