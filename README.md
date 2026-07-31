# 🌆 UrbanSense AI – Intelligent Smart City Complaint Management System


## 📌 Overview

**UrbanSense AI** is an AI-powered Smart City Complaint Management System designed to simplify how citizens report civic issues and how government authorities resolve them. Citizens can report problems such as potholes, garbage accumulation, water leakage, broken streetlights, drainage issues, and more through a mobile application.

The platform automatically analyzes every complaint using Artificial Intelligence, categorizes it, assigns a priority level, detects duplicate or spam complaints, validates uploaded images, and routes the complaint to the appropriate department. Government officials can monitor complaints through a centralized dashboard with maps and analytics, enabling faster and more transparent grievance redressal.

---

# 🚀 Key Features

### 👤 Citizen Module

* Secure user registration and login
* Report complaints with description, image, and GPS location
* Track complaint status in real time
* View complaint history

### 🤖 AI-Powered Complaint Analysis

* Complaint Classification
* Priority Prediction
* Spam Detection
* Duplicate Complaint Detection
* Image Validation
* Trust Score Generation
* Automatic Department Assignment

### 🏛 Government Dashboard

* Complaint monitoring
* Status management
* Department-wise filtering
* Complaint analytics
* Performance insights

### 🗺 Interactive Maps

* GPS-based complaint locations
* Priority-colored map markers
* Location visualization for authorities

### 📊 Analytics

* Total complaints
* Pending vs Resolved complaints
* Category-wise statistics
* Priority distribution
* Department performance
* Real-time dashboard

---

# 🧠 AI Capabilities

The AI module performs:

* ✅ Complaint Classification
* ✅ Priority Detection
* ✅ Duplicate Detection
* ✅ Spam Detection
* ✅ Image Validation
* ✅ Trust Score Calculation
* ✅ Department Recommendation

---

# 🛠 Tech Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| Mobile App      | Flutter                 |
| Backend         | FastAPI (Python)        |
| AI Engine       | Python                  |
| Database        | SQLite / PostgreSQL     |
| Maps            | Google Maps API         |
| Authentication  | Firebase Authentication |
| Image Storage   | Firebase Storage        |
| Deployment      | Render                  |
| Version Control | Git & GitHub            |

---

# ⚙️ System Workflow

```text
Citizen
    │
    ▼
Submit Complaint
(Text + Image + GPS)
    │
    ▼
Flutter Mobile App
    │
    ▼
FastAPI Backend
    │
    ▼
AI Processing
• Category Classification
• Priority Prediction
• Spam Detection
• Duplicate Detection
• Image Validation
• Trust Score
• Department Assignment
    │
    ▼
Database
    │
    ├────────► Government Dashboard
    │              │
    │              ▼
    │      Maps & Analytics
    │
    ▼
Citizen Tracks Complaint Status
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/shivamrai001/Team-Shivam-Shivam.git
cd Team-Shivam-Shivam
```

---

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Flutter Setup

```bash
cd frontend
flutter pub get
flutter run
```

---

# 📡 API Highlights

* User Registration & Login
* Create Complaint
* Fetch Complaints
* Update Complaint Status
* Dashboard Statistics
* Analytics
* Maps Integration

---

# 🌟 Project Highlights

* AI-assisted complaint management
* Faster complaint resolution
* Transparent complaint tracking
* Smart department routing
* Interactive GIS visualization
* Real-time analytics dashboard
* Scalable and modular architecture

---

# 🎯 Future Enhancements

* Multilingual support
* Push notifications
* Predictive analytics
* IoT sensor integration
* Voice-based complaint registration
* Offline complaint submission
* Machine learning model improvements

---

# 👥 Team

**Team Shivam**

* AI & Backend Development
* Flutter Mobile Application
* Dashboard & Analytics
* Database Integration
* API Development

---

# 📜 License

This project is developed for educational purposes and hackathon participation.

---

<p align="center">
  <b>⭐ If you found this project useful, consider giving it a Star on GitHub! ⭐</b>
</p>
