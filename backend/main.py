import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import engine, Base
from routers import (
    auth, complaints, admin, analytics, 
    dashboard, feedback, maps, notifications, uploads, users
)

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="UrbanSense AI API",
    description="Backend service for UrbanSense AI Citizen Portal",
    version="1.0.0"
)

# Enable CORS for Flutter Web, Mobile Emulators, and Production Frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to specific domains in strict production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload directory exists and serve media files statically
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Include Application Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(complaints.router, prefix="/api/complaints", tags=["Complaints"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(feedback.router, prefix="/api/feedback", tags=["Feedback"])
app.include_router(maps.router, prefix="/api/maps", tags=["Maps"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(uploads.router, prefix="/api/uploads", tags=["Uploads"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "UrbanSense AI API"}
