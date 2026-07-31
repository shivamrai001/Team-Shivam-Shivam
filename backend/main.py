from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import auth
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
# Routers
from .routers import (
    users,
    complaints,
    dashboard,
    analytics,
    maps,
    admin,
    feedback,
    notifications,
    uploads

)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="UrbanSense AI Backend",
    version="3.0.0",
    description="AI Powered Smart Complaint Management System"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Serve Uploaded Images
# ==========================

import os

UPLOAD_DIR = "backend/upload"
os.makedirs(UPLOAD_DIR, exist_ok=True)

if os.path.isdir(UPLOAD_DIR):
    app.mount("/upload", StaticFiles(directory=UPLOAD_DIR), name="upload")
)

# ==========================
# Home Route
# ==========================

@app.get("/")
def home():
    return {
        "message": "UrbanSense AI Backend Running",
        "version": "3.0.0"
    }

# ==========================
# Include Routers
# ==========================

app.include_router(users.router)
app.include_router(complaints.router)
app.include_router(dashboard.router)
app.include_router(analytics.router)
app.include_router(maps.router)
app.include_router(admin.router)
app.include_router(feedback.router)
app.include_router(notifications.router)
app.include_router(uploads.router)
app.include_router(auth.router)

# ==========================================
# Home API
# ==========================================

# ==========================================
# Health Check API
# ==========================================

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "database": "Connected",
        "server": "Running"
    }

# ==========================================
# API Information
# ==========================================

@app.get("/info")
def info():
    return {
        "project": "UrbanSense AI",
        "backend": "FastAPI",
        "database": "SQLite",
        "ai_features": [
            "Complaint Classification",
            "Severity Prediction",
            "Priority Detection",
            "Duplicate Detection",
            "Department Assignment"
        ],
        "available_modules": [
            "Users",
            "Complaints",
            "Dashboard",
            "Analytics",
            "Interactive Maps"
        ]
    }
