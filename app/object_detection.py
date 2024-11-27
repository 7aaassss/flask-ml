import os
from ultralytics import RTDETR, YOLO
import matplotlib.pyplot as plt
import cv2
from datetime import datetime
from werkzeug.utils import secure_filename


class ObjectDetection:
    def __init__(self):
        detr_model = RTDETR(os.path.abspath("last.pt"))
        yolo_model = YOLO(os.path.abspath("best.pt"))

        self.models = {"RTDETR": detr_model, "YOLO": yolo_model}

        self.input_dir = os.path.join(os.path.dirname(__file__), "media", "input")
        self.output_dir = os.path.join(os.path.dirname(__file__), "media", "output")

    def save_file(self, file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        input_path = os.path.join(self.input_dir, secure_filename(filename))
        file.save(input_path)

        return input_path, filename

    def handle_video(self, model, file):
        input_path, filename = self.save_file(file)

        return self.process_video(input_path, model)

    def process_video(self, video, model, content_type):
        if content_type == "video":
            video = os.path.join(object_detection_handler.input_dir, video)
            cap = cv2.VideoCapture(video)
        else:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        selected_model = self.models[model]

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = selected_model(frame, stream=True)
            for result in results:
                processed_frame = result.plot()
                ret, buffer = cv2.imencode(".jpg", processed_frame)
                frame_bytes = buffer.tobytes()

                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
                )
                break

        cap.release()

    def handle_image(self, model, file):
        selected_model = self.models[model]
        input_path, filename = self.save_file(file)

        result = selected_model(input_path)
        handled_result = result[0].plot()
        cv2.imwrite(
            os.path.join(self.output_dir, f"processed_{filename}"), handled_result
        )

        return {f"image_path": f"/media/output/processed_{filename}"}


object_detection_handler = ObjectDetection()
