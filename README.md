<div align="center">

# 🌆 Welcome to UrbanSense AI

### 🚀 Intelligent Smart City Complaint Management System

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=Welcome+to+UrbanSense+AI;Making+Cities+Smarter+with+AI;AI-Powered+Complaint+Management;Built+using+Flutter+%7C+FastAPI+%7C+Python"/>

<p>

<img src="https://img.shields.io/github/license/shivamrai001/Team-Shivam-Shivam?style=for-the-badge">
<img src="https://img.shields.io/github/stars/shivamrai001/Team-Shivam-Shivam?style=for-the-badge">
<img src="https://img.shields.io/github/forks/shivamrai001/Team-Shivam-Shivam?style=for-the-badge">
<img src="https://img.shields.io/github/issues/shivamrai001/Team-Shivam-Shivam?style=for-the-badge">

</p>

<p>

<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black">
<img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white">

</p>

---

### 🌍 Building Smarter Cities Through Artificial Intelligence

UrbanSense AI empowers citizens to report civic issues effortlessly while enabling government authorities to respond faster using AI-driven complaint analysis, intelligent routing, and real-time monitoring.

</div>

---

# 📑 Table of Contents

- [📌 Overview](#-overview)
- [✨ Why UrbanSense AI?](#-why-urbansense-ai)
- [🚀 Features](#-features)
- [🤖 AI Capabilities](#-ai-capabilities)
- [💻 Technology Stack](#-technology-stack)
- [🏗️ Architecture](#-architecture)
- [⚙️ System Workflow](#-system-workflow)
- [📂 Project Structure](#-project-structure)
- [📸 Screenshots](#-screenshots)
- [📦 Installation](#-installation)
- [📡 API Highlights](#-api-highlights)
- [🛣️ Roadmap](#-roadmap)
- [👥 Team](#-team)
- [📄 License](#-license)

---

# 📌 Overview

UrbanSense AI is an intelligent complaint management platform designed to modernize the interaction between citizens and municipal authorities.

Instead of manually forwarding complaints between departments, UrbanSense AI uses Artificial Intelligence to automatically analyze incoming complaints, determine their urgency, validate supporting images, detect duplicate reports, and route them to the appropriate government department.

Citizens receive transparent status updates throughout the complaint lifecycle, while administrators gain access to a centralized dashboard with maps, analytics, and actionable insights.

---

# ✨ Why UrbanSense AI?

Urban civic issues often suffer from delayed responses due to manual complaint handling and fragmented workflows.

UrbanSense AI addresses these challenges by providing:

- 🤖 AI-powered complaint analysis
- 📍 GPS-enabled issue reporting
- 📸 Image verification
- 🚦 Automatic priority assignment
- 🏛 Smart department routing
- 📊 Real-time analytics
- 🗺 Interactive GIS visualization
- 📱 Seamless mobile experience

---

# 🚀 Features

## 👤 Citizen Module

| Feature | Description |
|----------|-------------|
| 🔐 Secure Authentication | Safe login and registration |
| 📸 Image Upload | Attach images as evidence |
| 📍 GPS Location | Automatic location capture |
| 📝 Complaint Submission | Easy issue reporting |
| 📊 Live Tracking | Monitor complaint status |
| 📜 Complaint History | Access previous reports |

---

## 🤖 AI Processing Engine

| AI Service | Purpose |
|------------|----------|
| 🧠 Complaint Classification | Identifies complaint category |
| 🚨 Priority Prediction | Determines urgency level |
| 🔍 Duplicate Detection | Prevents repeated complaints |
| 🚫 Spam Detection | Filters invalid submissions |
| 🖼 Image Validation | Verifies uploaded images |
| ⭐ Trust Score | Evaluates complaint credibility |
| 🏢 Department Recommendation | Routes to responsible authority |

---

## 🏛 Government Dashboard

- Centralized complaint management
- Complaint filtering
- Department-wise statistics
- Interactive GIS Maps
- Performance analytics
- Resolution tracking
- Complaint insights
- Priority monitoring

---

## 📊 Analytics Dashboard

- Total Complaints
- Pending Complaints
- Resolved Complaints
- Department Performance
- Category Distribution
- Priority Statistics
- Resolution Trends
- Daily Activity Reports

---

# 🤖 AI Capabilities

UrbanSense AI combines multiple AI modules to automate complaint management.

✔ Complaint Classification

✔ Priority Prediction

✔ Duplicate Complaint Detection

✔ Spam Detection

✔ Image Validation

✔ Trust Score Generation

✔ Department Recommendation

The AI pipeline significantly reduces manual intervention while improving response time and operational efficiency.

---

# 💻 Technology Stack

<div align="center">

## Languages & Frameworks

<img src="https://skillicons.dev/icons?i=flutter,dart,python,fastapi"/>

## Database & Cloud

<img src="https://skillicons.dev/icons?i=firebase,postgresql"/>

## Development Tools

<img src="https://skillicons.dev/icons?i=git,github,vscode"/>

</div>

| Category | Technology |
|-----------|------------|
| Mobile App | Flutter |
| Backend | FastAPI |
| Programming Language | Python |
| AI Engine | Python |
| Database | SQLite / PostgreSQL |
| Authentication | Firebase Authentication |
| Cloud Storage | Firebase Storage |
| Maps | Google Maps API |
| Version Control | Git & GitHub |
| Deployment | Render |

---
# 🏗️ Architecture

```text
                         ┌────────────────────────────┐
                         │        Citizen App         │
                         │ (Flutter Mobile Client)    │
                         └─────────────┬──────────────┘
                                       │
                          Complaint + Image + GPS
                                       │
                                       ▼
                         ┌────────────────────────────┐
                         │      FastAPI Backend       │
                         └─────────────┬──────────────┘
                                       │
                     ┌─────────────────┼─────────────────┐
                     │                 │                 │
                     ▼                 ▼                 ▼
         Complaint Analysis     Authentication     Database Layer
                     │                 │                 │
                     ▼                 ▼                 ▼
             AI Processing      Firebase Auth     PostgreSQL
                     │
                     ▼
      ┌─────────────────────────────────────────┐
      │ • Complaint Classification              │
      │ • Priority Prediction                   │
      │ • Spam Detection                        │
      │ • Duplicate Detection                   │
      │ • Image Validation                      │
      │ • Trust Score Generation                │
      │ • Department Recommendation             │
      └─────────────────────────────────────────┘
                     │
                     ▼
          Government Dashboard & Analytics
```

---

# ⚙️ System Workflow

```text
Citizen
    │
    ▼
Registers / Logs In
    │
    ▼
Submits Complaint
(Text + Image + GPS)
    │
    ▼
FastAPI Backend
    │
    ▼
AI Engine
    │
    ├── Complaint Classification
    ├── Priority Prediction
    ├── Spam Detection
    ├── Duplicate Detection
    ├── Image Validation
    ├── Trust Score Calculation
    └── Department Assignment
    │
    ▼
Database
    │
    ├────────────► Government Dashboard
    │                  │
    │                  ├── Complaint Monitoring
    │                  ├── Analytics
    │                  ├── Maps
    │                  └── Status Management
    │
    ▼
Citizen Receives Live Status Updates
```

---

# 📂 Project Structure

```text
UrbanSense-AI
│
├── backend/
│   ├── app/
│   ├── api/
│   ├── models/
│   ├── database/
│   ├── ai/
│   ├── utils/
│   ├── config/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/
│   ├── lib/
│   │   ├── screens/
│   │   ├── widgets/
│   │   ├── services/
│   │   ├── models/
│   │   └── main.dart
│   │
│   ├── assets/
│   └── pubspec.yaml
│
├── screenshots/
│
├── docs/
│
├── README.md
│
└── LICENSE
```

---

# 📸 Screenshots

> Replace these images with actual screenshots of your application.

<div align="center">

| Home Screen | Complaint Form |
|--------------|----------------|
| ![](screenshots/home.png) | ![](screenshots/complaint.png) |

| Dashboard | Analytics |
|------------|-----------|
| ![](screenshots/dashboard.png) | ![](screenshots/analytics.png) |

</div>

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/shivamrai001/Team-Shivam-Shivam.git
```

```bash
cd Team-Shivam-Shivam
```

---

## Backend Setup

```bash
cd backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn main:app --reload
```

Backend Documentation

```
http://127.0.0.1:8000/docs
```

---

## Flutter Setup

```bash
cd frontend
```

Install packages

```bash
flutter pub get
```

Run application

```bash
flutter run
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

```env
SECRET_KEY=your_secret_key

DATABASE_URL=your_database_url

FIREBASE_API_KEY=your_api_key

GOOGLE_MAPS_API_KEY=your_maps_key
```

---

# 📡 API Highlights

| Endpoint | Description |
|-----------|-------------|
| POST /register | User Registration |
| POST /login | User Authentication |
| POST /complaints | Submit Complaint |
| GET /complaints | Fetch Complaints |
| GET /complaints/{id} | Complaint Details |
| PUT /complaints/{id} | Update Complaint Status |
| GET /dashboard | Dashboard Statistics |
| GET /analytics | Complaint Analytics |

---

# 🌟 Project Highlights

- 🤖 AI-powered complaint classification
- 🚨 Intelligent priority prediction
- 🔍 Duplicate complaint detection
- 🚫 Spam filtering
- 🖼️ Image validation
- 📍 GPS-based complaint mapping
- 🏛️ Smart department routing
- 📊 Interactive analytics dashboard
- 📱 Real-time complaint tracking
- 🔐 Secure authentication
- ☁️ Cloud storage integration
- ⚡ Scalable backend architecture

---

# 📈 Future Scope

```text
✔ Multilingual Support

✔ Push Notifications

✔ Offline Complaint Submission

✔ Voice-based Complaint Registration

✔ Predictive Analytics

✔ IoT Sensor Integration

✔ AI Model Improvements

✔ Web Portal for Citizens

✔ Automated Report Generation

✔ Smart City Heatmaps
```

---
---

# 🤝 Contributing

Contributions are always welcome! If you'd like to improve **UrbanSense AI**, we'd love to have your support.

### Getting Started

1. **Fork** this repository.
2. **Create** a new feature branch.

```bash
git checkout -b feature/your-feature
```

3. **Commit** your changes.

```bash
git commit -m "Add: Your Feature"
```

4. **Push** the branch.

```bash
git push origin feature/your-feature
```

5. Open a **Pull Request** 🚀

---

# 📊 Project Status

| Module | Status |
|---------|:------:|
| 📱 Flutter Mobile Application | ✅ Completed |
| ⚙️ FastAPI Backend | ✅ Completed |
| 🔐 Authentication System | ✅ Completed |
| 📝 Complaint Management | ✅ Completed |
| 🤖 AI Complaint Classification | ✅ Completed |
| 🚨 Priority Prediction | ✅ Completed |
| 🔍 Duplicate Detection | ✅ Completed |
| 🚫 Spam Detection | ✅ Completed |
| 📍 Maps Integration | ✅ Completed |
| 📊 Dashboard & Analytics | ✅ Completed |

---

# 🛣️ Roadmap

### ✅ Phase 1

- Citizen Authentication
- Complaint Registration
- GPS Integration
- AI Complaint Classification
- Dashboard
- Complaint Tracking

### 🚧 Phase 2

- Push Notifications
- Complaint Heatmaps
- Multilingual Support
- Enhanced Analytics
- Performance Optimization

### 🔮 Phase 3

- IoT Sensor Integration
- Voice-based Complaint Registration
- Predictive Analytics
- Smart City Insights
- Web Portal
- Automated Reports

---

# 📚 Resources

Useful references used during development:

- Flutter Documentation
- FastAPI Documentation
- Firebase Documentation
- PostgreSQL Documentation
- Google Maps Platform
- GitHub Documentation

---

# 🌟 Why UrbanSense AI?

✔ AI-assisted complaint analysis

✔ Automatic complaint categorization

✔ Smart department assignment

✔ Faster grievance resolution

✔ Transparent complaint tracking

✔ Interactive GIS visualization

✔ Secure Authentication

✔ Modern Flutter Interface

✔ Scalable FastAPI Backend

✔ Real-time Analytics Dashboard

---

# 👥 Team

<div align="center">

## Team Shivam

**Building Smarter Cities Through AI & Innovation**

</div>

| 👤 Member | 🎓 Registration No. | 💼 Role |
|-----------|---------------------|----------|
| **Shivam Rai** | **25BAI11241** | **Team Lead & Project Coordinator** |
| **Mayank Kumar** | **25BCE10023** | **AI & Backend Development** |
| **Sagar Patel** | **25BCE11092** | **Testing & Documentation** |
| **Yash Kumar** | **25BCE11106** | **Flutter Development** |

---

<div align="center">

### 🚀 Meet Our Team

<table>
<tr>

<td align="center" width="25%">

### 👨‍💼 Shivam Rai

**Team Lead**

📌 Project Coordination

</td>

<td align="center" width="25%">

### 🤖 Mayank Kumar

**AI & Backend Development**

🎓 25BCE10023

</td>

<td align="center" width="25%">

### 🧪 Sagar Patel

**Testing & Documentation**

🎓 25BCE11092

</td>

<td align="center" width="25%">

### 📱 Yash Kumar

**Flutter Development**

🎓 25BCE11106

</td>

</tr>
</table>

---

### 💙 *Together, we're building smarter cities with Artificial Intelligence.*

</div>

---

# 💻 Built With

<div align="center">

<img src="https://skillicons.dev/icons?i=flutter,dart,python,fastapi,firebase,postgres,git,github,vscode"/>

</div>

---

# ⭐ Support the Project

If you found **UrbanSense AI** useful, consider giving this repository a ⭐ on GitHub.

Your support helps us improve the project and motivates us to build even better solutions.

---

# 📄 License

This project was developed for **educational purposes** and **hackathon participation**.

Feel free to explore, learn from, and contribute to the project.

---

# 🙏 Acknowledgements

Special thanks to the amazing open-source community and technologies that made this project possible.

- 💙 Flutter
- ⚡ FastAPI
- 🔥 Firebase
- 🐘 PostgreSQL
- 🗺️ Google Maps Platform
- 🐍 Python Community
- 🌍 Open Source Contributors

---

<div align="center">

# 🌆 UrbanSense AI

### *Making Cities Smarter with Artificial Intelligence*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C9FF,100:0052D4&height=140&section=footer"/>

### ⭐ Star this repository if you found it useful!

Made with ❤️ by **Team Shivam**

</div>
