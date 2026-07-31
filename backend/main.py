from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .database import get_db
from . import crud
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

try:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
except OSError:
    pass

if os.path.isdir(UPLOAD_DIR):
    app.mount("/upload", StaticFiles(directory=UPLOAD_DIR), name="upload")
# ==========================
# Home Route
# ==========================

@app.get("/", response_class=HTMLResponse)
def home(db: Session = Depends(get_db)):

    total = crud.total_complaints(db)
    pending = crud.pending_complaints(db)
    resolved = crud.resolved_complaints(db)
    rejected = crud.rejected_complaints(db)
    in_progress = crud.inprogress_complaints(db)
    total_users = len(crud.get_all_users(db))

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UrbanSense AI Dashboard</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: #0f1115;
                color: #e6e6e6;
                padding: 40px 24px;
            }}
            .container {{ max-width: 1000px; margin: 0 auto; }}
            header {{ margin-bottom: 36px; }}
            h1 {{ font-size: 28px; font-weight: 700; margin-bottom: 6px; }}
            .subtitle {{ color: #9aa0a6; font-size: 14px; }}
            .status-badge {{
                display: inline-block;
                background: #1e3a2f;
                color: #4ade80;
                font-size: 12px;
                font-weight: 600;
                padding: 4px 10px;
                border-radius: 999px;
                margin-top: 10px;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 16px;
                margin-bottom: 32px;
            }}
            .card {{
                background: #171a21;
                border: 1px solid #262a33;
                border-radius: 12px;
                padding: 20px;
            }}
            .card .label {{
                font-size: 13px;
                color: #9aa0a6;
                margin-bottom: 8px;
            }}
            .card .value {{
                font-size: 32px;
                font-weight: 700;
            }}
            .card.total .value {{ color: #60a5fa; }}
            .card.pending .value {{ color: #fbbf24; }}
            .card.progress .value {{ color: #38bdf8; }}
            .card.resolved .value {{ color: #4ade80; }}
            .card.rejected .value {{ color: #f87171; }}
            .card.users .value {{ color: #c084fc; }}
            footer {{
                margin-top: 40px;
                font-size: 12px;
                color: #5f6570;
            }}
            a {{ color: #60a5fa; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>UrbanSense AI</h1>
                <div class="subtitle">Smart City Complaint Management &mdash; Live Dashboard</div>
                <div class="status-badge">&#9679; Backend Running &middot; v3.0.0</div>
            </header>

            <div class="grid">
                <div class="card total">
                    <div class="label">Total Complaints</div>
                    <div class="value">{total}</div>
                </div>
                <div class="card pending">
                    <div class="label">Pending</div>
                    <div class="value">{pending}</div>
                </div>
                <div class="card progress">
                    <div class="label">In Progress</div>
                    <div class="value">{in_progress}</div>
                </div>
                <div class="card resolved">
                    <div class="label">Resolved</div>
                    <div class="value">{resolved}</div>
                </div>
                <div class="card rejected">
                    <div class="label">Rejected</div>
                    <div class="value">{rejected}</div>
                </div>
                <div class="card users">
                    <div class="label">Total Users</div>
                    <div class="value">{total_users}</div>
                </div>
            </div>

            <footer>
                API docs: <a href="/docs">/docs</a> &nbsp;&bull;&nbsp;
                Health check: <a href="/health">/health</a> &nbsp;&bull;&nbsp;
                Analytics: <a href="/analytics/status">/analytics/status</a>
            </footer>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html)

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
