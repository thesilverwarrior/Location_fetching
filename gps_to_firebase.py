import geocoder
import requests
import time
import math
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase with your JSON key file
cred = credentials.Certificate("gps-location-by-aditya-firebase-adminsdk-fbsvc-d96717f2c1.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://gps-location-by-aditya-default-rtdb.asia-southeast1.firebasedatabase.app/"})

# Reference to the database node
ref = db.reference("gps")

# Store initial location
initial_lat = None
initial_lon = None

def get_location():
    """Fetches the current GPS location using IP-based geolocation."""
    g = geocoder.ip('me')
    return g.latlng if g.latlng else [0, 0]  # Default to [0, 0] if location fetch fails

def haversine(lat1, lon1, lat2, lon2):
    """Calculate distance between two GPS coordinates in meters (Haversine formula)."""
    R = 6371000  # Radius of Earth in meters
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def send_to_firebase(lat, lon, alert):
    """Sends GPS coordinates to Firebase."""
    data = {"latitude": lat, "longitude": lon, "timestamp": time.time(), "alert": alert}
    ref.push(data)  # Push new data entry
    print(f"📍 Location sent to Firebase: {lat}, {lon}, Alert: {alert}")

# Continuously update GPS location every 5 seconds
if __name__ == "__main__":
    while True:
        location = get_location()
        lat, lon = location[0], location[1]

        global initial_lat, initial_lon
        if initial_lat is None or initial_lon is None:
            initial_lat, initial_lon = lat, lon  # Store initial location

        distance = haversine(initial_lat, initial_lon, lat, lon)
        alert = distance > 500  # Trigger alert if moved > 500m

        send_to_firebase(lat, lon, alert)
        
        if alert:
            print("⚠️ ALERT: User moved more than 500 meters!")

        time.sleep(5)  # Send data every 5 seconds







