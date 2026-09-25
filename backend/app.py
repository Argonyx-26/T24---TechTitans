from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime


# ============================================================
# ARGUS AI — BACKEND
# ============================================================

app = FastAPI(
    title="ARGUS AI",
    description="Autonomous Security Intelligence Platform",
    version="1.0.0"
)


# ============================================================
# CORS — FRONTEND CONNECTION
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "system": "ARGUS AI",
        "status": "online",
        "message": "ARGUS AI backend is running"
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():
    return {
        "system": "ARGUS AI",
        "status": "online",
        "backend": "FastAPI",
        "timestamp": datetime.now().isoformat()
    }


# ============================================================
# RISK CALCULATION ENGINE
# ============================================================

def calculate_risk(
    restricted_area=False,
    after_hours=False,
    suspicious_network=False,
    high_data_transfer=False,
    multiple_sources=False,
    repeated_activity=False,
    unknown_device=False
):

    score = 0

    # Physical security
    if restricted_area:
        score += 22

    # Access control
    if after_hours:
        score += 18

    # Network anomaly
    if suspicious_network:
        score += 21

    # Data exfiltration indicator
    if high_data_transfer:
        score += 14

    # Cross-source correlation
    if multiple_sources:
        score += 15

    # Behavioral repetition
    if repeated_activity:
        score += 7

    # Unknown device
    if unknown_device:
        score += 9

    score = min(score, 100)

    # Risk classification
    if score >= 80:
        level = "CRITICAL"
        priority = "CRITICAL"
        response = "Immediate"

    elif score >= 60:
        level = "HIGH"
        priority = "HIGH"
        response = "Within 5 minutes"

    elif score >= 40:
        level = "MEDIUM"
        priority = "MEDIUM"
        response = "Within 15 minutes"

    elif score >= 20:
        level = "LOW"
        priority = "LOW"
        response = "Within 30 minutes"

    else:
        level = "NORMAL"
        priority = "INFORMATIONAL"
        response = "Routine monitoring"

    return score, level, priority, response


# ============================================================
# SIGNAL GENERATION
# ============================================================

def generate_signals(config):

    signals = []

    if config["restricted_area"]:
        signals.append("Restricted-area entry detected")

    if config["after_hours"]:
        signals.append("After-hours access detected")

    if config["suspicious_network"]:
        signals.append("Suspicious network connection")

    if config["high_data_transfer"]:
        signals.append("High network data transfer detected")

    if config["multiple_sources"]:
        signals.append(
            "Suspicious activity observed across multiple security sources"
        )

    if config["repeated_activity"]:
        signals.append(
            "Repeated abnormal activity detected"
        )

    if config["unknown_device"]:
        signals.append(
            "Unknown device activity detected"
        )

    return signals


# ============================================================
# EVENT GENERATION
# ============================================================

def generate_events(config):

    events = []

    if config["restricted_area"]:
        events.append({
            "source": "CCTV",
            "camera_id": "CAM-01",
            "event_type": "restricted_area_entry",
            "location": "Server Room",
            "timestamp": datetime.now().isoformat()
        })

    if config["after_hours"]:
        events.append({
            "source": "ACCESS_LOG",
            "user_id": "EMP-101",
            "location": "Server Room",
            "access_type": "after_hours_access",
            "timestamp": datetime.now().isoformat()
        })

    if config["suspicious_network"]:
        events.append({
            "source": "NETWORK",
            "device_id": "PC-101",
            "event_type": "suspicious_connection",
            "timestamp": datetime.now().isoformat()
        })

    if config["high_data_transfer"]:
        events.append({
            "source": "NETWORK",
            "device_id": "PC-101",
            "event_type": "high_data_transfer",
            "data_volume_mb": 500,
            "timestamp": datetime.now().isoformat()
        })

    if config["repeated_activity"]:
        events.append({
            "source": "CCTV",
            "camera_id": "CAM-02",
            "event_type": "repeated_suspicious_activity",
            "location": "Restricted Corridor",
            "timestamp": datetime.now().isoformat()
        })

    if config["unknown_device"]:
        events.append({
            "source": "NETWORK",
            "device_id": "UNKNOWN-DEV-01",
            "event_type": "unknown_device",
            "timestamp": datetime.now().isoformat()
        })

    return events


# ============================================================
# CORRELATION ENGINE
# ============================================================

def generate_correlations(events):

    sources = list(set(
        event["source"] for event in events
    ))

    correlations = []

    if "CCTV" in sources and "ACCESS_LOG" in sources:
        correlations.append({
            "type": "possible_physical_intrusion",
            "sources": ["CCTV", "ACCESS_LOG"],
            "description":
                "Suspicious physical activity and unauthorized access detected together"
        })

    if "ACCESS_LOG" in sources and "NETWORK" in sources:
        correlations.append({
            "type": "possible_coordinated_intrusion",
            "sources": ["ACCESS_LOG", "NETWORK"],
            "description":
                "Unauthorized access occurred together with suspicious network activity"
        })

    if "CCTV" in sources and "NETWORK" in sources:
        correlations.append({
            "type": "possible_multi_stage_attack",
            "sources": ["CCTV", "NETWORK"],
            "description":
                "Suspicious physical activity occurred together with suspicious network activity"
        })

    if len(sources) >= 3:
        correlations.append({
            "type": "high_confidence_security_incident",
            "sources": sources,
            "description":
                "Suspicious activity detected across multiple independent security sources"
        })

    return correlations


# ============================================================
# SCENARIOS
# ============================================================

SCENARIOS = {

    "normal": {
        "restricted_area": False,
        "after_hours": False,
        "suspicious_network": False,
        "high_data_transfer": False,
        "multiple_sources": False,
        "repeated_activity": False,
        "unknown_device": False
    },

    "low": {
        "restricted_area": False,
        "after_hours": True,
        "suspicious_network": False,
        "high_data_transfer": False,
        "multiple_sources": False,
        "repeated_activity": False,
        "unknown_device": False
    },

    "medium": {
        "restricted_area": True,
        "after_hours": True,
        "suspicious_network": False,
        "high_data_transfer": False,
        "multiple_sources": False,
        "repeated_activity": False,
        "unknown_device": False
    },

    "medium_high": {
        "restricted_area": True,
        "after_hours": True,
        "suspicious_network": True,
        "high_data_transfer": False,
        "multiple_sources": False,
        "repeated_activity": False,
        "unknown_device": False
    },

    "high": {
        "restricted_area": True,
        "after_hours": True,
        "suspicious_network": True,
        "high_data_transfer": False,
        "multiple_sources": True,
        "repeated_activity": False,
        "unknown_device": False
    },

    "high_plus": {
        "restricted_area": True,
        "after_hours": True,
        "suspicious_network": True,
        "high_data_transfer": True,
        "multiple_sources": True,
        "repeated_activity": False,
        "unknown_device": False
    },

    "critical": {
        "restricted_area": True,
        "after_hours": True,
        "suspicious_network": True,
        "high_data_transfer": True,
        "multiple_sources": True,
        "repeated_activity": True,
        "unknown_device": True
    }
}


# ============================================================
# ANALYSIS ENGINE
# ============================================================

def generate_analysis(scenario_name):

    config = SCENARIOS[scenario_name]

    score, level, priority, response = calculate_risk(
        restricted_area=config["restricted_area"],
        after_hours=config["after_hours"],
        suspicious_network=config["suspicious_network"],
        high_data_transfer=config["high_data_transfer"],
        multiple_sources=config["multiple_sources"],
        repeated_activity=config["repeated_activity"],
        unknown_device=config["unknown_device"]
    )

    events = generate_events(config)

    signals = generate_signals(config)

    correlations = generate_correlations(events)

    why_it_matters = list(signals)

    if correlations:
        why_it_matters.append(
            f"{len(correlations)} cross-source correlation pattern(s) detected"
        )

    if score >= 80:
        recommendation = (
            "Immediate investigation recommended. "
            "Multiple correlated security indicators suggest "
            "a potentially serious security incident."
        )

    elif score >= 60:
        recommendation = (
            "Investigate the correlated events and verify "
            "whether coordinated suspicious activity is occurring."
        )

    elif score >= 40:
        recommendation = (
            "Review the detected events and verify the "
            "associated physical and digital activity."
        )

    elif score >= 20:
        recommendation = (
            "Continue monitoring the detected activity "
            "and verify the associated access event."
        )

    else:
        recommendation = (
            "No significant security threat detected. "
            "Continue routine monitoring."
        )

    return {

        "system": "ARGUS AI",

        "scenario": scenario_name,

        "timestamp": datetime.now().isoformat(),

        "risk_score": score,

        "risk_level": level,

        "alert_priority": {

            "priority": priority,

            "response_time": response,

            "reason":
                "ARGUS AI calculated the alert priority using "
                "fused CCTV, access-control and network intelligence.",

            "correlation_count": len(correlations)
        },

        "detected_signals": signals,

        "events": events,

        "correlated_incidents": correlations,

        "threat_assessment": {

            "summary":
                "ARGUS AI identified security activity by "
                "combining multiple independent security sources.",

            "why_it_matters": why_it_matters,

            "recommendation": recommendation,

            "correlation_summary": correlations
        },

        "source_status": {

            "CCTV": {
                "status": "ONLINE",
                "description": "Video surveillance"
            },

            "ACCESS_LOG": {
                "status": "ONLINE",
                "description": "Physical access monitoring"
            },

            "NETWORK": {
                "status": "ONLINE",
                "description": "Network activity monitoring"
            }
        },

        "system_status": {

            "backend": "ONLINE",

            "data_fusion": "ACTIVE",

            "threat_detection": "ACTIVE",

            "correlation_engine": "ACTIVE",

            "alert_prioritization": "ACTIVE"
        }
    }


# ============================================================
# MAIN DEMO
# ============================================================

@app.get("/analyze/demo")
def analyze_demo():

    return generate_analysis("critical")


# ============================================================
# INDIVIDUAL SCENARIOS
# ============================================================

@app.get("/analyze/{scenario}")
def analyze_scenario(scenario: str):

    scenario = scenario.lower()

    if scenario not in SCENARIOS:

        return {
            "system": "ARGUS AI",
            "error": "Unknown scenario",
            "available_scenarios": list(SCENARIOS.keys())
        }

    return generate_analysis(scenario)


# ============================================================
# SCENARIO LIST
# ============================================================

@app.get("/scenarios")
def scenarios():

    return {
        "system": "ARGUS AI",

        "scenarios": {

            "normal": "0-19",

            "low": "20-39",

            "medium": "40-59",

            "medium_high": "60-69",

            "high": "70-84",

            "high_plus": "85-95",

            "critical": "96-100"
        }
    }


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )