from transformers import DetrForObjectDetection, DetrImageProcessor
import torch
from PIL import Image
model_name = "facebook/detr-resnet-50"
detr_model = DetrForObjectDetection.from_pretrained(model_name)
weights_path = "last.pt"
state_dict = torch.load(weights_path, map_location="cpu", weights_only=False)
detr_model.load_state_dict(state_dict)
detr_model.eval()

processor = DetrImageProcessor.from_pretrained(model_name)
image_path = "1.jpg"
image = Image.open(image_path).convert("RGB")
inputs = processor(images=image, return_tensors="pt")


with torch.no_grad():
    outputs = detr_model(**inputs)

logits = outputs.logits
bboxes = outputs.pred_boxes
probs = logits.softmax(-1)
scores, labels = probs.max(-1)


threshold = 0.5
filtered_defects = []
for score, label, bbox in zip(scores[0], labels[0], bboxes[0]):
    if score > threshold:
        defect = {
            "class": int(label),  # ID класса
            "confidence": float(score),  # Уверенность
        }
        filtered_defects.append(defect)

print("DETR Defects:", filtered_defects)