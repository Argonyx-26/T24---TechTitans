# ============================================================
# ARGUS AI — THREAT DETECTION ENGINE
# ============================================================

def calculate_risk(events):

    score = 5
    signals = []

    sources = set()

    # --------------------------------------------------------
    # Analyze every security event
    # --------------------------------------------------------

    for event in events:

        source = event.get("source", "")
        sources.add(source)

        # ====================================================
        # CCTV EVENTS
        # ====================================================

        if source == "CCTV":

            event_type = event.get("event_type", "")

            if event_type == "restricted_area_entry":

                score += 25

                signals.append(
                    "Restricted-area entry detected"
                )

            elif event_type == "person_detected":

                score += 5

                signals.append(
                    "Person detected by CCTV"
                )

            elif event_type == "weapon_detected":

                score += 35

                signals.append(
                    "Potential weapon detected by CCTV"
                )

            elif event_type == "violent_activity":

                score += 30

                signals.append(
                    "Potential violent activity detected"
                )

            elif event_type == "unknown_person":

                score += 15

                signals.append(
                    "Unknown person detected"
                )

        # ====================================================
        # ACCESS LOG EVENTS
        # ====================================================

        elif source == "ACCESS_LOG":

            access_type = event.get("access_type", "")

            if access_type == "after_hours_access":

                score += 20

                signals.append(
                    "After-hours access detected"
                )

            elif access_type == "unauthorized_access":

                score += 30

                signals.append(
                    "Unauthorized access detected"
                )

            elif access_type == "failed_access":

                score += 10

                signals.append(
                    "Repeated failed access attempt detected"
                )

            elif access_type == "admin_access":

                score += 10

                signals.append(
                    "Administrative access detected"
                )

        # ====================================================
        # NETWORK EVENTS
        # ====================================================

        elif source == "NETWORK":

            event_type = event.get("event_type", "")

            if event_type == "suspicious_connection":

                score += 25

                signals.append(
                    "Suspicious network connection"
                )

            elif event_type == "port_scan":

                score += 20

                signals.append(
                    "Network port scanning detected"
                )

            elif event_type == "malware_detected":

                score += 35

                signals.append(
                    "Potential malware activity detected"
                )

            elif event_type == "data_exfiltration":

                score += 40

                signals.append(
                    "Possible data exfiltration detected"
                )

            # ------------------------------------------------
            # Data volume analysis
            # ------------------------------------------------

            data_volume = event.get("data_volume_mb", 0)

            if data_volume >= 1000:

                score += 20

                signals.append(
                    "Very high network data transfer detected"
                )

            elif data_volume >= 500:

                score += 10

                signals.append(
                    "High network data transfer detected"
                )

            elif data_volume >= 100:

                score += 5

                signals.append(
                    "Elevated network data transfer detected"
                )

    # ========================================================
    # MULTI-SOURCE DATA FUSION
    # ========================================================

    source_count = len(sources)

    if source_count >= 3:

        score += 10

        signals.append(
            "Suspicious activity observed across three security sources"
        )

    elif source_count == 2:

        score += 5

        signals.append(
            "Suspicious activity observed across multiple security sources"
        )

    # ========================================================
    # MULTIPLE SECURITY SIGNALS
    # ========================================================

    if len(signals) >= 4:

        score += 5

    # ========================================================
    # LIMIT SCORE TO 0–100
    # ========================================================

    score = min(score, 100)

    # ========================================================
    # DETERMINE RISK LEVEL
    # ========================================================

    if score >= 80:

        risk_level = "CRITICAL"

    elif score >= 60:

        risk_level = "HIGH"

    elif score >= 30:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    # ========================================================
    # REMOVE DUPLICATE SIGNALS
    # ========================================================

    signals = list(dict.fromkeys(signals))

    return score, risk_level, signals