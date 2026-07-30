from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import auth
from .database import Base, engine

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

# =====================
# Serve Uploaded Images
# =====================

app.mount(
    "/upload",
    StaticFiles(directory="backend/upload"),
    name="upload"
)

# ==========
# Home Route
# ==========

@app.get("/")
def home():
    return {
        "message": "UrbanSense AI Backend Running",
        "version": "3.0.0"
    }

# ===============
# Include Routers
# ===============

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

# ========
# Home API
# ========

# ================
# Health Check API
# ================

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "database": "Connected",
        "server": "Running"
    }

# ===============
# API Information
# ===============

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
