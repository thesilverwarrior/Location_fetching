# 📍 IoT GPS Tracker (Firebase + Flask + Web Dashboard)

## 📝 Project Overview
This **IoT-based GPS tracking system** retrieves **real-time GPS coordinates** from the user's laptop, sends them to **Firebase Realtime Database**, and displays the location on a **live web dashboard** with a map.  
🏰 It also **triggers an alert** if the user moves **more than 500 meters** from the starting point.

---

## 📌 Features
✅ **Fetch Live GPS Data** (IP-based geolocation)  
✅ **Send GPS Data to Firebase** (Every 5 seconds)  
✅ **Real-Time Map Dashboard** (Leaflet.js + Flask)  
✅ **500m Movement Alert** (Haversine formula)  
✅ **Secure API Keys & Firebase Credentials**  

---

## 🛠️ Tech Stack
💡 **Backend**: Python, Flask, Firebase Admin SDK  
💡 **Database**: Firebase Realtime Database  
💡 **Frontend**: HTML, Leaflet.js, Socket.IO  
💡 **Hosting**: GitHub (for project files)  

---

## 🚀 Project Setup (Run Locally)
### 👉 **1️⃣ Clone the Repository**
```sh
git clone https://github.com/thesilverwarrior/Location_fetching.git
cd Location_fetching
```

### 👉 **2️⃣ Install Dependencies**
```sh
pip install flask flask-socketio geocoder requests firebase-admin python-dotenv
```

### 👉 **3️⃣ Setup Firebase Credentials**
1. **Go to Firebase Console** → **Project Settings**  
2. **Generate a new private key** (Service Account JSON)  
3. **Save it as** `firebase_credentials.json`  
4. **Move it to your project folder**  

### 👉 **4️⃣ Create a `.env` File**
```sh
touch .env
```
Add the following:
```txt
FIREBASE_URL=https://your-firebase-project-default-rtdb.firebaseio.com/
FIREBASE_CREDENTIALS=firebase_credentials.json
```

### 👉 **5️⃣ Run the GPS Data Sender**
```sh
python gps_to_firebase.py
```
✅ **This sends GPS data to Firebase every 5 seconds.**  

### 👉 **6️⃣ Start the Flask Web Dashboard**
```sh
python app.py
```
✅ Open **`http://localhost:5000/`** in your browser to see the **real-time map**!  

---

## 🛡️ Security Measures
🔒 **Never Upload API Keys to GitHub**  
- `.env` file is **ignored using `.gitignore`**  
- Firebase keys are stored securely in **environment variables**  

🛡 **Protect Your Firebase Database**  
- **Set Firebase Rules** to prevent unauthorized access:
  ```json
  {
    "rules": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
  ```

---

## 🛠️ GitHub Workflow
### **Commit & Push Updates**
```sh
git add .
git commit -m "Updated project"
git push origin main
```

### **Remove Firebase Keys from Git History**
```sh
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch firebase_credentials.json" --prune-empty --tag-name-filter cat -- --all
git push --force origin main
```
✅ **Now, API keys are removed and secured!**

---

## 📌 Future Improvements
🚀 **Use Google Geolocation API for better accuracy**  
🚀 **Host Flask app on Heroku or Render**  
🚀 **Add GPS tracking history & analytics**  

---

## 🏆 Credits
Developed by **[@thesilverwarrior](https://github.com/thesilverwarrior)** 🚀  

---

## 📄 License
This project is **open-source** and available under the **MIT License**.  

