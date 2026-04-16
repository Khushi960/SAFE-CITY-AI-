# app.py — Flask Backend for SafeCity AI
# Run: python app.py
# Open browser: http://localhost:5000

from flask import Flask, render_template, request, jsonify
from astar import astar, PUNE_GRAPH, NODE_COORDS
from safety_data import get_route_risk, AREA_SAFETY, TRAFFIC_DATA
from expert import assess_risk
from chatbot import get_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/areas")
def get_areas():
    """Return list of all Pune areas."""
    areas = sorted(PUNE_GRAPH.keys())
    return jsonify(areas)

@app.route("/api/route", methods=["POST"])
def find_route():
    """Find safest A* route between two Pune locations."""
    data = request.json
    start = data.get("start")
    goal = data.get("goal")

    if not start or not goal:
        return jsonify({"error": "Please select start and destination."}), 400
    if start == goal:
        return jsonify({"error": "Start and destination cannot be the same."}), 400
    if start not in PUNE_GRAPH or goal not in PUNE_GRAPH:
        return jsonify({"error": "Unknown location selected."}), 400

    path, cost = astar(PUNE_GRAPH, start, goal)
    if not path:
        return jsonify({"error": f"No route found between {start} and {goal}."}), 404

    safety = get_route_risk(path)

    # Get coordinates for map display
    coords = [{"name": n, "lat": NODE_COORDS[n][0], "lng": NODE_COORDS[n][1]} for n in path if n in NODE_COORDS]

    return jsonify({
        "path": path,
        "cost_km": cost,
        "stops": len(path),
        "safety": safety,
        "coords": coords,
    })

@app.route("/api/area_info/<area>")
def area_info(area):
    """Get safety info for a specific area."""
    info = AREA_SAFETY.get(area)
    if not info:
        return jsonify({"error": "Area not found"}), 404
    return jsonify({"area": area, **info})

@app.route("/api/expert", methods=["POST"])
def expert_advice():
    """Expert system risk assessment."""
    data = request.json
    result = assess_risk(
        time=data.get("time", "day"),
        area=data.get("area", "safe"),
        crowd=data.get("crowd", "medium"),
        weather=data.get("weather", "clear"),
        road_type=data.get("road_type", "city"),
        near_forest=data.get("near_forest", "no"),
        terrain=data.get("terrain", "flat"),
        traffic=data.get("traffic", "medium"),
    )
    return jsonify(result)

@app.route("/api/chat", methods=["POST"])
def chat():
    """Chatbot endpoint."""
    data = request.json
    user_msg = data.get("message", "")
    response = get_response(user_msg)
    return jsonify({"response": response})

@app.route("/api/dashboard")
def dashboard():
    """Dashboard stats."""
    hour = datetime.datetime.now().hour
    if 8 <= hour <= 10:
        traffic_zones = TRAFFIC_DATA["morning_peak"]
        traffic_label = "Morning Peak"
    elif 18 <= hour <= 20:
        traffic_zones = TRAFFIC_DATA["evening_peak"]
        traffic_label = "Evening Peak"
    else:
        traffic_zones = []
        traffic_label = "Normal"

    night_mode = hour >= 21 or hour <= 5
    unsafe_now = TRAFFIC_DATA["night_unsafe"] if night_mode else []

    safe_areas = [a for a, d in AREA_SAFETY.items() if d["risk"] <= 3]
    risky_areas = [a for a, d in AREA_SAFETY.items() if d["risk"] >= 6]

    return jsonify({
        "time": datetime.datetime.now().strftime("%I:%M %p"),
        "traffic_label": traffic_label,
        "traffic_zones": traffic_zones,
        "night_mode": night_mode,
        "unsafe_now": unsafe_now,
        "safe_areas": safe_areas,
        "risky_areas": risky_areas,
        "total_areas": len(AREA_SAFETY),
    })

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  SafeCity AI — Smart Urban Safety System")
    print("  Pune City Edition")
    print("="*50)
    print("\n  Open your browser and go to:")
    print("  http://localhost:5000\n")
    app.run(debug=True, port=5000)
