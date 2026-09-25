import cv2
from pathlib import Path
from ultralytics import YOLO


# =========================================================
# PATHS
# =========================================================

VIDEO_PATH = Path(__file__).parent / "videos" / "test.mp4"

MODEL_PATH = Path(__file__).parent.parent / "yolo11n.pt"


# =========================================================
# LOAD YOLO MODEL
# =========================================================

model = YOLO(str(MODEL_PATH))


# =========================================================
# CCTV PROCESSING
# =========================================================

def process_cctv_video():

    cap = cv2.VideoCapture(str(VIDEO_PATH))

    if not cap.isOpened():
        return {
            "status": "error",
            "message": "Could not open CCTV video",
            "video_path": str(VIDEO_PATH)
        }

    frame_count = 0
    frames_with_people = 0
    max_people_detected = 0

    # Process every 10th frame
    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 10 != 0:
            continue

        # YOLO detection
        results = model(
            frame,
            verbose=False
        )

        people_count = 0

        for result in results:

            if result.boxes is None:
                continue

            for box in result.boxes:

                # COCO class 0 = person
                class_id = int(box.cls[0])

                if class_id == 0:
                    people_count += 1

        # Track frames containing people
        if people_count > 0:

            frames_with_people += 1

            max_people_detected = max(
                max_people_detected,
                people_count
            )

    cap.release()


    # =====================================================
    # DETERMINE CCTV EVENT
    # =====================================================

    if max_people_detected > 0:

        event_type = "person_detected"

        signal = "Person detected by CCTV"

    else:

        event_type = "normal_activity"

        signal = None


    # =====================================================
    # RETURN CCTV INTELLIGENCE
    # =====================================================

    return {

        "status": "success",

        "message": "CCTV video analyzed successfully",

        "video": "test.mp4",

        "frames_processed": frame_count,

        "frames_with_people": frames_with_people,

        "max_people_detected": max_people_detected,

        "event_type": event_type,

        "signal": signal
    }