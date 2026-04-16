# safety_data.py
# Real-world safety data for Pune areas
# Sources: Pune Police crime stats, news reports, local knowledge
# Risk scores: 1 (very safe) to 10 (high risk)

AREA_SAFETY = {
    "Shivajinagar":    {"risk": 3, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 3},
    "Deccan":          {"risk": 3, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 2},
    "FC Road":         {"risk": 2, "crime_rate": "low",    "lighting": "excellent", "crowd": "very_high","police_posts": 2},
    "Swargate":        {"risk": 7, "crime_rate": "high",   "lighting": "poor",      "crowd": "high",   "police_posts": 2},
    "Hadapsar":        {"risk": 6, "crime_rate": "medium", "lighting": "moderate",  "crowd": "medium", "police_posts": 2},
    "Koregaon Park":   {"risk": 2, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 3},
    "Viman Nagar":     {"risk": 2, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 2},
    "Kharadi":         {"risk": 4, "crime_rate": "medium", "lighting": "moderate",  "crowd": "medium", "police_posts": 1},
    "Baner":           {"risk": 3, "crime_rate": "low",    "lighting": "good",      "crowd": "high",   "police_posts": 2},
    "Aundh":           {"risk": 2, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 2},
    "Kothrud":         {"risk": 3, "crime_rate": "low",    "lighting": "good",      "crowd": "high",   "police_posts": 2},
    "Karve Nagar":     {"risk": 4, "crime_rate": "medium", "lighting": "moderate",  "crowd": "medium", "police_posts": 1},
    "Warje":           {"risk": 5, "crime_rate": "medium", "lighting": "moderate",  "crowd": "medium", "police_posts": 1},
    "Katraj":          {"risk": 7, "crime_rate": "high",   "lighting": "poor",      "crowd": "low",    "police_posts": 1},
    "Kondhwa":         {"risk": 6, "crime_rate": "medium", "lighting": "moderate",  "crowd": "medium", "police_posts": 1},
    "Undri":           {"risk": 6, "crime_rate": "medium", "lighting": "poor",      "crowd": "low",    "police_posts": 1},
    "Magarpatta":      {"risk": 2, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 3},
    "Kalyani Nagar":   {"risk": 2, "crime_rate": "low",    "lighting": "excellent", "crowd": "high",   "police_posts": 2},
    "Wagholi":         {"risk": 7, "crime_rate": "high",   "lighting": "poor",      "crowd": "low",    "police_posts": 1},
    "Hinjewadi":       {"risk": 4, "crime_rate": "medium", "lighting": "good",      "crowd": "medium", "police_posts": 2},
    "Wakad":           {"risk": 3, "crime_rate": "low",    "lighting": "good",      "crowd": "high",   "police_posts": 2},
    "Pimple Saudagar": {"risk": 4, "crime_rate": "medium", "lighting": "moderate",  "crowd": "medium", "police_posts": 1},
    "Balewadi":        {"risk": 3, "crime_rate": "low",    "lighting": "good",      "crowd": "medium", "police_posts": 1},
    "Market Yard":     {"risk": 6, "crime_rate": "medium", "lighting": "poor",      "crowd": "high",   "police_posts": 1},
}

# Traffic hotspots by time of day
TRAFFIC_DATA = {
    "morning_peak": ["Swargate", "Shivajinagar", "FC Road", "Hadapsar", "Hinjewadi", "Baner"],
    "evening_peak": ["Deccan", "Koregaon Park", "Viman Nagar", "Kharadi", "Aundh", "Wakad"],
    "night_unsafe": ["Swargate", "Katraj", "Wagholi", "Market Yard", "Hadapsar", "Undri"],
}

POLICE_HELPLINE = "100"
AMBULANCE = "108"
FIRE = "101"
EMERGENCY = "112"
WOMEN_HELPLINE = "1091"

def get_route_risk(path):
    """Compute overall safety rating for a given path."""
    if not path:
        return {"level": "unknown", "score": 0, "details": []}
    
    scores = []
    details = []
    for node in path:
        data = AREA_SAFETY.get(node, {"risk": 5, "crime_rate": "unknown", "lighting": "unknown", "crowd": "unknown"})
        scores.append(data["risk"])
        details.append({
            "area": node,
            "risk": data["risk"],
            "crime_rate": data["crime_rate"],
            "lighting": data["lighting"],
            "crowd": data["crowd"],
        })
    
    avg = sum(scores) / len(scores)
    max_score = max(scores)
    
    # Weighted: 60% average, 40% worst node
    final = 0.6 * avg + 0.4 * max_score
    
    if final >= 6:
        level = "HIGH RISK"
        color = "red"
        advice = "Avoid this route, especially at night. Consider an alternate path."
    elif final >= 4:
        level = "MEDIUM RISK"
        color = "amber"
        advice = "Proceed with caution. Stay alert and avoid traveling alone at night."
    else:
        level = "SAFE"
        color = "green"
        advice = "This route is generally safe. Standard precautions apply."
    
    return {
        "level": level,
        "color": color,
        "score": round(final, 1),
        "advice": advice,
        "details": details,
    }
