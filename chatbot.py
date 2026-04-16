# chatbot.py — Smart Safety Chatbot (Pune-specific)

RESPONSES = {
    "greet": [
        "Hello! 😊 I'm SafeCity AI — your Pune safety assistant. Ask me about safe routes, emergency numbers, or area safety.",
        "Hi there! I can help you with safe routes in Pune, emergency help, and travel tips. What do you need?",
    ],
    "route": "Use the Route Finder tab to get the safest A* path between Pune locations with real crime and traffic data.",
    "emergency": "🚨 Emergency Numbers in Pune:\n• Police: 100\n• Ambulance: 108\n• Fire: 101\n• All emergencies: 112\n• Women helpline: 1091",
    "police": "Dial 100 for Pune Police. Nearest police stations: Shivajinagar, Deccan, Kothrud, Hadapsar, Viman Nagar.",
    "ambulance": "Dial 108 for ambulance. Nearest hospitals: Ruby Hall Clinic, KEM Hospital, Jehangir Hospital, Sahyadri Hospital.",
    "safe_areas": "Safest areas in Pune: Koregaon Park, Viman Nagar, Aundh, Baner, FC Road, Magarpatta, Kalyani Nagar.",
    "unsafe_areas": "High-risk areas in Pune (especially at night): Swargate, Katraj, Wagholi, Market Yard. Avoid traveling alone.",
    "night": "🌙 Night Safety Tips:\n• Avoid Swargate, Katraj, Wagholi at night\n• Prefer well-lit areas like Koregaon Park, Baner\n• Share live location with family\n• Keep 100 (Police) on speed dial",
    "traffic": "Peak traffic in Pune:\n• Morning (8–10 AM): Swargate, FC Road, Hinjewadi\n• Evening (6–8 PM): Deccan, Koregaon Park, Viman Nagar\nUse alternate routes during these hours.",
    "safe_tips": "🛡️ Safety Tips:\n• Stay in crowded, well-lit areas\n• Share your location\n• Keep emergency contacts saved\n• Use SafeCity Route Finder for safe paths\n• Avoid isolated areas at night",
    "hospital": "🏥 Major Hospitals in Pune:\n• Ruby Hall Clinic — Sassoon Road\n• KEM Hospital — Rasta Peth\n• Jehangir Hospital — Sassoon Road\n• Sahyadri Hospital — Deccan\nDial 108 for ambulance.",
    "ai": "This system uses AI techniques:\n• A* Search Algorithm — for shortest safe path\n• Rule-Based Expert System — for risk assessment\n• Pattern Matching NLP — this chatbot\n• Computer Vision (OpenCV) — face detection",
    "algorithm": "A* algorithm finds the optimal path by combining actual distance (g-cost) with estimated remaining distance (heuristic). It's faster and smarter than Dijkstra's algorithm.",
    "swargate": "⚠️ Swargate has a high crime rate, especially at night. Avoid isolated lanes. Prefer main roads and travel with company.",
    "koregaon": "✅ Koregaon Park is one of the safest areas in Pune — well-lit, high crowd, police presence.",
    "hinjewadi": "🏢 Hinjewadi IT park area is moderately safe during office hours. Late night travel is not recommended.",
    "katraj": "🚨 Katraj has poor lighting and high crime. Avoid at night. If needed, travel on NH-48 main road only.",
    "thanks": "You're welcome! Stay safe in Pune! 😊",
    "bye": "Goodbye! Stay safe and take care 👋",
    "project": "This is the Smart Urban Safety & Assistance System — an AI project using A* search, expert systems, NLP chatbot, and face detection for Pune city safety.",
}

def get_response(query):
    """Return chatbot response for a user query."""
    q = query.lower().strip()

    if not q:
        return "Please type your question!"

    if any(w in q for w in ["hi", "hello", "hey", "namaste"]):
        import random
        return random.choice(RESPONSES["greet"])
    if any(w in q for w in ["bye", "goodbye", "tata"]):
        return RESPONSES["bye"]
    if any(w in q for w in ["thank", "thanks", "shukriya"]):
        return RESPONSES["thanks"]
    if any(w in q for w in ["emergency", "sos", "help me", "danger"]):
        return RESPONSES["emergency"]
    if "police" in q or "100" in q:
        return RESPONSES["police"]
    if "ambulance" in q or "108" in q or "hospital" in q:
        return RESPONSES["hospital"]
    if any(w in q for w in ["route", "path", "navigate", "way", "direction"]):
        return RESPONSES["route"]
    if any(w in q for w in ["safe area", "safest", "safe place"]):
        return RESPONSES["safe_areas"]
    if any(w in q for w in ["unsafe", "dangerous", "avoid", "crime"]):
        return RESPONSES["unsafe_areas"]
    if "night" in q or "midnight" in q or "late" in q:
        return RESPONSES["night"]
    if "traffic" in q or "congestion" in q or "jam" in q:
        return RESPONSES["traffic"]
    if any(w in q for w in ["tip", "advice", "suggestion", "precaution"]):
        return RESPONSES["safe_tips"]
    if "ai" in q or "artificial" in q or "how does" in q:
        return RESPONSES["ai"]
    if "algorithm" in q or "a*" in q or "astar" in q:
        return RESPONSES["algorithm"]
    if "swargate" in q:
        return RESPONSES["swargate"]
    if "koregaon" in q:
        return RESPONSES["koregaon"]
    if "hinjewadi" in q:
        return RESPONSES["hinjewadi"]
    if "katraj" in q:
        return RESPONSES["katraj"]
    if "project" in q or "system" in q:
        return RESPONSES["project"]

    return "I'm not sure about that. Try asking about:\n• Safe routes in Pune\n• Emergency numbers\n• Safe/unsafe areas\n• Night travel tips\n• Traffic information"
