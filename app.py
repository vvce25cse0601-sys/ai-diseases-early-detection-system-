from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Mock Data
ALERTS = [
    {"id": 1, "type": "Stem Borer Worm", "severity": "High", "time": "10 Mins Ago", "status": "Infected"},
    {"id": 2, "type": "Leaf Folder", "severity": "Medium", "time": "2 Hours Ago", "status": "Risk"},
]

@app.route('/')
def home():
    health_status = "Infected" if any(a['status'] == 'Infected' for a in ALERTS) else "Healthy"
    return render_template('index.html', health_status=health_status, recent_alerts=ALERTS[:3])

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

@app.route('/alerts')
def alerts():
    return render_template('alerts.html', alerts=ALERTS)

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/helpline')
def helpline():
    # Mock Farmers
    farmers = [
        {"name": "Ravi Kumar", "paddy_type": "Basmati", "phone": "+91 9876543210"},
        {"name": "Suresh Singh", "paddy_type": "Sona Masuri", "phone": "+91 8765432109"}
    ]
    return render_template('helpline.html', farmers=farmers)

@app.route('/history')
def history():
    return render_template('history.html', history=ALERTS)

@app.route('/settings')
def settings():
    return render_template('settings.html')

# API for real-time polling
@app.route('/api/status')
def api_status():
    return jsonify({
        "alerts": ALERTS,
        "latest_detection": random.choice(["No pests detected.", "Warning: Stem borer activity possible.", "All clear."])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
