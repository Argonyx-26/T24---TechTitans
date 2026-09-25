def prioritize_alert(risk_score, correlated_incidents):
    """
    Determine how urgently a security event should be handled.
    """

    correlation_count = len(correlated_incidents)

    # Critical:
    # Multiple independent security sources
    # indicate a coordinated incident.
    if correlation_count >= 4:
        priority = "CRITICAL"
        response_time = "Immediate"
        reason = (
            "Multiple security sources indicate a highly correlated "
            "security incident."
        )

    # High:
    # More than one cross-source relationship exists.
    elif correlation_count >= 2:
        priority = "HIGH"
        response_time = "Urgent"
        reason = (
            "Suspicious activity is correlated across multiple "
            "security sources."
        )

    # Medium:
    # Either moderate risk or one correlation.
    elif correlation_count >= 1 or risk_score >= 50:
        priority = "MEDIUM"
        response_time = "Investigate Soon"
        reason = (
            "Suspicious activity requires investigation "
            "but does not currently indicate a critical incident."
        )

    # Low:
    else:
        priority = "LOW"
        response_time = "Monitor"
        reason = (
            "Limited suspicious activity detected with "
            "no significant cross-source correlation."
        )

    return {
        "priority": priority,
        "response_time": response_time,
        "reason": reason,
        "correlation_count": correlation_count
    }