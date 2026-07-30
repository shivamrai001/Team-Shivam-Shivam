from fastapi import FastAPI
# importing from database
from .database import Base, engine
# importing models
from . import models
# importing Routers
from .routers import users
from .routers import complaints
from .routers import dashboard
from .routers import analytics
from .routers import maps
# Creating Database Tables
Base.metadata.create_all(bind=engine)
# FastAPI Application
app = FastAPI(
    title="UrbanSense AI Backend",
    description="AI Powered Smart Complaint Management System",
    version="1.0.0"
)
# ******************************************
# Registering Routers
# ==========================================
app.include_router(users.router)
app.include_router(complaints.router)
app.include_router(dashboard.router)
app.include_router(analytics.router)
app.include_router(maps.router)
# ==========================================
# Home API
# ******************************************
@app.get("/")
def home():
    return {
        "message": "UrbanSense AI Backend Running Successfully",
        "version": "1.0.0",
        "status": "Running"
    }
# ==========================================
# Health Check API
# ******************************************
@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "database": "Connected",
        "server": "Running"
    }
# ==========================================
# API Information
#*******************************************
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
