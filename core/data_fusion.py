import random
import time
from datetime import datetime

from core.threat_detector import calculate_risk
from backend.cctv_processor import process_cctv_video


# =========================================================
# CCTV EVENT
# =========================================================

def generate_cctv_event():

    # Process the real CCTV video
    cctv_result = process_cctv_video()

    # If CCTV processing failed
    if cctv_result.get("status") != "success":

        return {
            "source": "CCTV",
            "camera_id": "CAM-01",
            "event_type": "cctv_processing_error",
            "timestamp": datetime.now().isoformat(),
            "cctv_status": "error"
        }

    # Get event detected by YOLO
    event_type = cctv_result.get(
        "event_type",
        "normal_activity"
    )

    return {
        "source": "CCTV",
        "camera_id": "CAM-01",
        "event_type": event_type,
        "timestamp": datetime.now().isoformat(),

        # CCTV intelligence
        "video": cctv_result.get("video"),
        "frames_processed": cctv_result.get(
            "frames_processed",
            0
        ),
        "frames_with_people": cctv_result.get(
            "frames_with_people",
            0
        ),
        "max_people_detected": cctv_result.get(
            "max_people_detected",
            0
        )
    }


# =========================================================
# ACCESS CONTROL EVENT
# =========================================================

def generate_access_event():

    events = [
        "normal_access",
        "normal_access",
        "unauthorized_access",
        "after_hours_access"
    ]

    return {
        "source": "ACCESS_LOG",

        "user_id": random.choice([
            "EMP-101",
            "EMP-102",
            "ADMIN-01",
            "GUEST-01"
        ]),

        "location": random.choice([
            "Main Gate",
            "Office Floor",
            "Server Room",
            "Control Room"
        ]),

        "access_type": random.choice(events),

        "timestamp": datetime.now().isoformat()
    }


# =========================================================
# NETWORK EVENT
# =========================================================

def generate_network_event():

    events = [
        "normal_traffic",
        "normal_traffic",
        "port_scan",
        "large_data_transfer",
        "suspicious_connection"
    ]

    return {
        "source": "NETWORK",

        "device_id": random.choice([
            "PC-101",
            "PC-102",
            "SERVER-01",
            "SERVER-02"
        ]),

        "event_type": random.choice(events),

        "data_volume_mb": random.randint(
            10,
            1000
        ),

        "timestamp": datetime.now().isoformat()
    }


# =========================================================
# COLLECT SECURITY EVENTS
# =========================================================

def collect_security_events():

    events = []

    # -----------------------------------------------------
    # REAL CCTV EVENT
    # -----------------------------------------------------

    events.append(
        generate_cctv_event()
    )

    # -----------------------------------------------------
    # ACCESS CONTROL EVENT
    # -----------------------------------------------------

    events.append(
        generate_access_event()
    )

    # -----------------------------------------------------
    # NETWORK EVENT
    # -----------------------------------------------------

    events.append(
        generate_network_event()
    )

    return events


# =========================================================
# SECURITY BATCH ANALYSIS
# =========================================================

def analyze_security_batch(events):

    score, risk_level, reasons = calculate_risk(
        events
    )

    print(
        "\n========== THREAT ANALYSIS =========="
    )

    print(
        f"Risk Score : {score}"
    )

    print(
        f"Risk Level : {risk_level}"
    )

    print(
        "\nDetected Signals:"
    )

    if reasons:

        for reason in reasons:

            print(
                f" - {reason}"
            )

    else:

        print(
            " - No suspicious activity detected"
        )

    print(
        "====================================="
    )


# =========================================================
# TEST MODE
# =========================================================

if __name__ == "__main__":

    print(
        "ARGUS AI - DATA FUSION ENGINE"
    )

    print(
        "=============================="
    )

    for _ in range(5):

        events = collect_security_events()

        print(
            "\n--- Unified Security Event Batch ---"
        )

        for event in events:

            print(event)

        # Send unified events
        # to Threat Detector

        analyze_security_batch(events)

        time.sleep(2)