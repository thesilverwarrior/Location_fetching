from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Correct Firebase Realtime Database URL
FIREBASE_URL = "https://gps-location-by-aditya-default-rtdb.asia-southeast1.firebasedatabase.app/gps.json"

def fetch_gps_data():
    """Fetch the latest GPS data from Firebase and send it to the frontend."""
    while True:
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200 and response.json():
            data = response.json()
            latest_entry = list(data.values())[-1]  # Get latest location
            socketio.emit("update_location", latest_entry)  # Send data to frontend
        time.sleep(5)  # Fetch data every 5 seconds

# Start fetching GPS data in a background thread
threading.Thread(target=fetch_gps_data, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)


