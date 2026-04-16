# SafeCity AI — Smart Urban Safety & Assistance System
# Pune City Edition | AI + Expert Systems Project

## PROJECT STRUCTURE
```
SafeCity/
├── app.py              ← Main Flask server (RUN THIS)
├── astar.py            ← A* pathfinding with Pune city graph
├── safety_data.py      ← Real Pune area crime/safety data
├── expert.py           ← Rule-based Expert System
├── chatbot.py          ← NLP Safety Chatbot
├── face.py             ← OpenCV Face Detection (run separately)
├── requirements.txt    ← Python dependencies
└── templates/
    └── index.html      ← Premium frontend (auto-served by Flask)
```

## SETUP — STEP BY STEP

### Step 1: Open VS Code
Open the SafeCity folder in VS Code:
  File → Open Folder → Select SafeCity folder

### Step 2: Open Terminal in VS Code
  Press: Ctrl + ` (backtick key)
  OR: Terminal → New Terminal

### Step 3: Install dependencies
  pip install flask opencv-python

### Step 4: Run the website
  python app.py

### Step 5: Open in browser
  Go to: http://localhost:5000

That's it! The website will be live.

---

## RUNNING FACE DETECTION (separately)
Open a NEW terminal tab and run:
  python face.py
Press ESC to close the camera window.

---

## AI TECHNIQUES USED (for your exam)

1. A* SEARCH ALGORITHM (astar.py)
   - Finds shortest + safest path between Pune locations
   - Uses Haversine distance as heuristic
   - Informed search — smarter than Dijkstra

2. RULE-BASED EXPERT SYSTEM (expert.py)
   - Mimics human expert decision making
   - Weighted risk scoring rules
   - Knowledge base + inference engine

3. NLP CHATBOT (chatbot.py)
   - Pattern matching for natural language queries
   - Pune-specific safety knowledge base
   - Keyword extraction and response mapping

4. COMPUTER VISION (face.py)
   - OpenCV Haar Cascade face detection
   - Real-time camera processing
   - Can be extended with DeepFace for recognition

---

## TROUBLESHOOTING

Problem: "ModuleNotFoundError: No module named 'flask'"
Fix: pip install flask

Problem: Website not opening
Fix: Make sure you ran "python app.py" first, then open http://localhost:5000

Problem: Camera not working in face.py
Fix: pip install opencv-python  (then run python face.py again)

Problem: Port already in use
Fix: Change port=5000 to port=5001 in app.py, then go to http://localhost:5001
