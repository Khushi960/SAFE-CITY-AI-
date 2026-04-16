# expert.py — Rule-Based Expert System for Urban Safety

def assess_risk(time, area, crowd, weather, road_type, near_forest, terrain, traffic):
    """
    Expert system that evaluates travel risk using weighted rules.
    Returns a dict with risk level, score, reasons, and advice.
    """
    risk_score = 0
    reasons = []

    # Time of day
    if time == "night":
        risk_score += 3
        reasons.append("Traveling at night significantly increases risk")
    elif time == "evening":
        risk_score += 1
        reasons.append("Evening travel — stay alert")
    else:
        risk_score += 0  # day is baseline safe

    # Area safety
    if area == "unsafe":
        risk_score += 4
        reasons.append("Area is flagged as unsafe by Pune Police data")
    elif area == "moderate":
        risk_score += 2
        reasons.append("Area has moderate crime history")
    else:
        risk_score -= 1  # safe area reduces overall risk

    # Crowd level
    if crowd == "low":
        risk_score += 2
        reasons.append("Low crowd — fewer witnesses, higher risk")
    elif crowd == "high":
        risk_score -= 1  # crowded areas are safer
    
    # Weather
    if weather == "rainy":
        risk_score += 2
        reasons.append("Rainy weather reduces visibility and road safety")
    elif weather == "foggy":
        risk_score += 2
        reasons.append("Foggy conditions reduce visibility")

    # Road type
    if road_type == "rural":
        risk_score += 2
        reasons.append("Rural roads lack lighting and police presence")
    elif road_type == "highway":
        risk_score += 1
        reasons.append("Highways have speed risks at night")
    elif road_type == "city":
        risk_score -= 1  # city roads are safer

    # Near forest
    if near_forest == "yes":
        risk_score += 2
        reasons.append("Isolated forest-adjacent area")

    # Terrain
    if terrain == "mountain":
        risk_score += 2
        reasons.append("Mountain terrain — road accident risk")
    elif terrain == "flood_prone":
        risk_score += 3
        reasons.append("Flood-prone area — dangerous during rain")

    # Traffic
    if traffic == "low":
        risk_score += 1
        reasons.append("Low traffic — isolated stretch")
    elif traffic == "high":
        risk_score += 1
        reasons.append("Heavy traffic — congestion and accident risk")

    # Determine risk level
    if risk_score >= 9:
        level = "HIGH RISK"
        color = "red"
        advice = "DO NOT travel this route. Call 112 if in emergency."
        emoji = "🚨"
    elif risk_score >= 5:
        level = "MEDIUM RISK"
        color = "amber"
        advice = "Be cautious. Share your location with someone you trust."
        emoji = "⚠️"
    elif risk_score >= 2:
        level = "LOW RISK"
        color = "yellow"
        advice = "Generally safe. Stay aware of your surroundings."
        emoji = "🟡"
    else:
        level = "SAFE"
        color = "green"
        advice = "Route is safe. Enjoy your journey!"
        emoji = "✅"

    return {
        "level": level,
        "color": color,
        "score": max(0, risk_score),
        "advice": advice,
        "emoji": emoji,
        "reasons": reasons if reasons else ["No significant risk factors detected"],
    }
