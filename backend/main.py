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
# Home Route - Admin Dashboard
# ==========================

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UrbanSense AI Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0f1115;
            color: #e6e6e6;
            padding: 32px 24px 80px;
        }
        .container { max-width: 1100px; margin: 0 auto; }
        header { margin-bottom: 28px; }
        h1 { font-size: 26px; font-weight: 700; margin-bottom: 4px; }
        .subtitle { color: #9aa0a6; font-size: 14px; }
        .status-badge {
            display: inline-block;
            background: #1e3a2f;
            color: #4ade80;
            font-size: 12px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 999px;
            margin-top: 8px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 12px;
            margin-bottom: 28px;
        }
        .card {
            background: #171a21;
            border: 1px solid #262a33;
            border-radius: 12px;
            padding: 16px 18px;
        }
        .card .label { font-size: 12px; color: #9aa0a6; margin-bottom: 6px; }
        .card .value { font-size: 26px; font-weight: 700; }
        .card.total .value { color: #60a5fa; }
        .card.pending .value { color: #fbbf24; }
        .card.progress .value { color: #38bdf8; }
        .card.resolved .value { color: #4ade80; }
        .card.rejected .value { color: #f87171; }
        .card.users .value { color: #c084fc; }

        .tabs { display: flex; gap: 8px; margin-bottom: 16px; border-bottom: 1px solid #262a33; }
        .tab-btn {
            background: none;
            border: none;
            color: #9aa0a6;
            font-size: 14px;
            font-weight: 600;
            padding: 10px 16px;
            cursor: pointer;
            border-bottom: 2px solid transparent;
        }
        .tab-btn.active { color: #e6e6e6; border-bottom-color: #60a5fa; }

        .panel { display: none; }
        .panel.active { display: block; }

        .toolbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
        .refresh-btn {
            background: #1c2028;
            border: 1px solid #2a2f3a;
            color: #e6e6e6;
            font-size: 13px;
            padding: 7px 14px;
            border-radius: 8px;
            cursor: pointer;
        }
        .refresh-btn:hover { background: #232833; }

        table { width: 100%; border-collapse: collapse; background: #171a21; border: 1px solid #262a33; border-radius: 12px; overflow: hidden; }
        thead th {
            text-align: left;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.03em;
            color: #9aa0a6;
            padding: 12px 14px;
            border-bottom: 1px solid #262a33;
            background: #14161c;
        }
        tbody td {
            padding: 12px 14px;
            font-size: 13px;
            border-bottom: 1px solid #1f232c;
            vertical-align: middle;
        }
        tbody tr:last-child td { border-bottom: none; }
        tbody tr:hover { background: #1a1e26; }

        .badge {
            display: inline-block;
            padding: 3px 9px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 600;
        }
        .badge.Pending { background: #3a2f1e; color: #fbbf24; }
        .badge.In-Progress { background: #1e3038; color: #38bdf8; }
        .badge.Resolved { background: #1e3a2f; color: #4ade80; }
        .badge.Rejected { background: #3a1e1e; color: #f87171; }
        .badge.Unknown { background: #2a2a2a; color: #9aa0a6; }

        select.status-select {
            background: #14161c;
            color: #e6e6e6;
            border: 1px solid #2a2f3a;
            border-radius: 6px;
            padding: 5px 8px;
            font-size: 12px;
        }
        .row-actions { display: flex; gap: 8px; align-items: center; }
        .btn-update {
            background: #1e3a5f; color: #93c5fd; border: none; border-radius: 6px;
            padding: 5px 10px; font-size: 12px; cursor: pointer;
        }
        .btn-update:hover { background: #24466e; }
        .btn-delete {
            background: #3a1e1e; color: #f87171; border: none; border-radius: 6px;
            padding: 5px 10px; font-size: 12px; cursor: pointer;
        }
        .btn-delete:hover { background: #4a2424; }

        .empty-state { padding: 30px; text-align: center; color: #9aa0a6; font-size: 13px; }
        footer { margin-top: 36px; font-size: 12px; color: #5f6570; }
        a { color: #60a5fa; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>UrbanSense AI</h1>
            <div class="subtitle">Smart City Complaint Management &mdash; Admin Dashboard</div>
            <div class="status-badge">&#9679; Backend Running &middot; v3.0.0</div>
        </header>

        <div class="grid" id="statsGrid">
            <div class="card total"><div class="label">Total Complaints</div><div class="value" id="statTotal">&hellip;</div></div>
            <div class="card pending"><div class="label">Pending</div><div class="value" id="statPending">&hellip;</div></div>
            <div class="card progress"><div class="label">In Progress</div><div class="value" id="statProgress">&hellip;</div></div>
            <div class="card resolved"><div class="label">Resolved</div><div class="value" id="statResolved">&hellip;</div></div>
            <div class="card rejected"><div class="label">Rejected</div><div class="value" id="statRejected">&hellip;</div></div>
            <div class="card users"><div class="label">Total Users</div><div class="value" id="statUsers">&hellip;</div></div>
        </div>

        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('complaints')">Complaints</button>
            <button class="tab-btn" onclick="switchTab('users')">Users</button>
        </div>

        <div class="panel active" id="panel-complaints">
            <div class="toolbar">
                <div></div>
                <button class="refresh-btn" onclick="loadAll()">Refresh</button>
            </div>
            <div id="complaintsWrap">
                <div class="empty-state">Loading complaints&hellip;</div>
            </div>
        </div>

        <div class="panel" id="panel-users">
            <div class="toolbar">
                <div></div>
                <button class="refresh-btn" onclick="loadAll()">Refresh</button>
            </div>
            <div id="usersWrap">
                <div class="empty-state">Loading users&hellip;</div>
            </div>
        </div>

        <footer>
            API docs: <a href="/docs">/docs</a> &nbsp;&bull;&nbsp;
            Health check: <a href="/health">/health</a> &nbsp;&bull;&nbsp;
            Analytics: <a href="/analytics/status">/analytics/status</a>
        </footer>
    </div>

    <script>
        const STATUS_OPTIONS = ["Pending", "In Progress", "Resolved", "Rejected"];
        let usersById = {};

        function switchTab(tab) {
            document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
            document.querySelectorAll(".panel").forEach(p => p.classList.remove("active"));
            document.getElementById("panel-" + tab).classList.add("active");
            event.target.classList.add("active");
        }

        function badgeClass(status) {
            return (status || "Unknown").replace(" ", "-");
        }

        async function fetchJSON(url, options) {
            const res = await fetch(url, options);
            if (!res.ok) {
                const text = await res.text();
                throw new Error(res.status + ": " + text);
            }
            const contentType = res.headers.get("content-type") || "";
            if (contentType.includes("application/json")) {
                return res.json();
            }
            return null;
        }

        async function loadStats() {
            try {
                const summary = await fetchJSON("/dashboard/summary");
                document.getElementById("statTotal").textContent = summary.total_complaints ?? 0;
                document.getElementById("statPending").textContent = summary.pending ?? 0;
                document.getElementById("statProgress").textContent = summary.in_progress ?? 0;
                document.getElementById("statResolved").textContent = summary.resolved ?? 0;
                document.getElementById("statRejected").textContent = summary.rejected ?? 0;
            } catch (e) {
                console.error("stats error", e);
            }
        }

        async function loadUsers() {
            try {
                const usersData = await fetchJSON("/admin/users");
                usersById = {};
                (usersData || []).forEach(u => { usersById[u.id] = u; });

                document.getElementById("statUsers").textContent = (usersData || []).length;

                const wrap = document.getElementById("usersWrap");
                if (!usersData || usersData.length === 0) {
                    wrap.innerHTML = '<div class="empty-state">No users yet.</div>';
                    return;
                }

                let rows = usersData.map(u => `
                    <tr>
                        <td>${u.id}</td>
                        <td>${escapeHtml(u.name || "")}</td>
                        <td>${escapeHtml(u.email || "")}</td>
                        <td>${escapeHtml(u.role || "citizen")}</td>
                        <td>${formatDate(u.created_at)}</td>
                    </tr>
                `).join("");

                wrap.innerHTML = `
                    <table>
                        <thead>
                            <tr><th>ID</th><th>Name</th><th>Email</th><th>Role</th><th>Joined</th></tr>
                        </thead>
                        <tbody>${rows}</tbody>
                    </table>
                `;
            } catch (e) {
                document.getElementById("usersWrap").innerHTML =
                    '<div class="empty-state">Could not load users (' + escapeHtml(e.message) + ')</div>';
            }
        }

        async function loadComplaints() {
            try {
                const complaintsData = await fetchJSON("/admin/complaints");
                const wrap = document.getElementById("complaintsWrap");

                if (!complaintsData || complaintsData.length === 0) {
                    wrap.innerHTML = '<div class="empty-state">No complaints yet.</div>';
                    return;
                }

                let rows = complaintsData.map(c => {
                    const owner = usersById[c.user_id];
                    const ownerLabel = owner ? escapeHtml(owner.name) : ("User #" + c.user_id);
                    const options = STATUS_OPTIONS.map(s =>
                        `<option value="${s}" ${s === c.status ? "selected" : ""}>${s}</option>`
                    ).join("");

                    return `
                        <tr>
                            <td>${c.id}</td>
                            <td>${escapeHtml(c.title || "")}</td>
                            <td>${escapeHtml(c.category || "Unknown")}</td>
                            <td>${escapeHtml(c.priority || "Low")}</td>
                            <td><span class="badge ${badgeClass(c.status)}">${escapeHtml(c.status || "Unknown")}</span></td>
                            <td>${ownerLabel}</td>
                            <td>${formatDate(c.created_at)}</td>
                            <td>
                                <div class="row-actions">
                                    <select class="status-select" id="status-${c.id}">${options}</select>
                                    <button class="btn-update" onclick="updateStatus(${c.id})">Update</button>
                                    <button class="btn-delete" onclick="deleteComplaint(${c.id})">Delete</button>
                                </div>
                            </td>
                        </tr>
                    `;
                }).join("");

                wrap.innerHTML = `
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th><th>Title</th><th>Category</th><th>Priority</th>
                                <th>Status</th><th>Filed By</th><th>Created</th><th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>${rows}</tbody>
                    </table>
                `;
            } catch (e) {
                document.getElementById("complaintsWrap").innerHTML =
                    '<div class="empty-state">Could not load complaints (' + escapeHtml(e.message) + ')</div>';
            }
        }

        async function updateStatus(id) {
            const select = document.getElementById("status-" + id);
            const newStatus = select.value;
            try {
                await fetchJSON(`/admin/complaints/${id}?status=${encodeURIComponent(newStatus)}`, { method: "PUT" });
                await loadAll();
            } catch (e) {
                alert("Failed to update status: " + e.message);
            }
        }

        async function deleteComplaint(id) {
            if (!confirm("Delete complaint #" + id + "? This cannot be undone.")) return;
            try {
                await fetchJSON(`/admin/complaints/${id}`, { method: "DELETE" });
                await loadAll();
            } catch (e) {
                alert("Failed to delete: " + e.message);
            }
        }

        function formatDate(value) {
            if (!value) return "&mdash;";
            const d = new Date(value);
            if (isNaN(d.getTime())) return escapeHtml(String(value));
            return d.toLocaleDateString() + " " + d.toLocaleTimeString([], {hour: "2-digit", minute: "2-digit"});
        }

        function escapeHtml(str) {
            return String(str)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;");
        }

        async function loadAll() {
            await loadUsers();
            await loadStats();
            await loadComplaints();
        }

        loadAll();
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(content=DASHBOARD_HTML)

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
