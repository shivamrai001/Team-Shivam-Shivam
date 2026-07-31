const API_BASE_URL = 'http://localhost:8000/api'; 
let token = localStorage.getItem('urbansense_token');
let mapInstance = null;

// ==========================================
// Initialization & Navigation
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    if (token) {
        unlockApp();
    }
});

const navItems = document.querySelectorAll('.nav-item[data-target]');
navItems.forEach(item => {
    item.addEventListener('click', (e) => {
        // Update active class
        navItems.forEach(n => n.classList.remove('active'));
        e.currentTarget.classList.add('active');
        
        // Switch view
        const targetId = e.currentTarget.getAttribute('data-target');
        document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
        document.getElementById(targetId).classList.add('active');

        // Trigger view-specific logic
        if (targetId === 'dashboard-view') loadDashboardData();
        if (targetId === 'map-view') loadMapData();
        if (targetId === 'notifications-view') loadNotifications();
    });
});

function unlockApp() {
    document.getElementById('app-sidebar').classList.remove('hidden');
    document.getElementById('auth-view').classList.remove('active');
    document.getElementById('dashboard-view').classList.add('active');
    loadDashboardData();
    loadNotifications();
}

document.getElementById('nav-logout').addEventListener('click', () => {
    localStorage.removeItem('urbansense_token');
    location.reload();
});

// ==========================================
// Authentication
// ==========================================
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    try {
        const res = await fetch(`${API_BASE_URL}/users/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        const data = await res.json();
        
        if (res.ok) {
            token = data.access_token;
            localStorage.setItem('urbansense_token', token);
            unlockApp();
        } else {
            document.getElementById('auth-error').innerText = `> ERR: ${data.detail || 'Auth failed'}`;
        }
    } catch (err) {
        document.getElementById('auth-error').innerText = '> ERR: Connection refused.';
    }
});

// ==========================================
// Form Submission & File Upload (/upload/image)
// ==========================================
document.getElementById('complaint-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const statusLog = document.getElementById('upload-status');
    statusLog.innerText = '> Initiating upload sequence...';

    let imagePath = null;
    const fileInput = document.getElementById('comp-image');

    // 1. Handle File Upload if present
    if (fileInput.files.length > 0) {
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        try {
            const uploadRes = await fetch(`${API_BASE_URL}/upload/image`, {
                method: 'POST',
                headers: { 'Authorization': `Bearer ${token}` }, // Add auth if your endpoint requires it
                body: formData
            });
            const uploadData = await uploadRes.json();
            if (uploadRes.ok) {
                imagePath = uploadData.image_path;
                statusLog.innerText = `> Image uploaded successfully: ${uploadData.filename}`;
            } else {
                statusLog.innerText = `> ERR: Image upload failed.`;
                return;
            }
        } catch (err) {
            statusLog.innerText = `> ERR: Upload service down.`;
            return;
        }
    }

    // 2. Submit Complaint Data
    const payload = {
        title: document.getElementById('comp-title').value,
        description: document.getElementById('comp-desc').value,
        latitude: parseFloat(document.getElementById('comp-lat').value),
        longitude: parseFloat(document.getElementById('comp-lng').value),
        image_path: imagePath 
    };

    const res = await fetch(`${API_BASE_URL}/complaints/`, {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(payload)
    });

    if (res.ok) {
        document.getElementById('complaint-form').reset();
        statusLog.innerText += '\n> Report deployed successfully.';
    }
});

// ==========================================
// Dashboard Analytics (/dashboard & /feedback)
// ==========================================
async function loadDashboardData() {
    // Summary
    const sumRes = await fetch(`${API_BASE_URL}/dashboard/summary`, { headers: { 'Authorization': `Bearer ${token}` } });
    if (sumRes.ok) {
        const stats = await sumRes.json();
        document.getElementById('stat-total').innerText = stats.total_complaints || 0;
        document.getElementById('stat-pending').innerText = stats.pending || 0;
        document.getElementById('stat-resolved').innerText = stats.resolved || 0;
    }

    // Critical Issues
    const critRes = await fetch(`${API_BASE_URL}/dashboard/critical`, { headers: { 'Authorization': `Bearer ${token}` } });
    if (critRes.ok) {
        const critical = await critRes.json();
        const list = document.getElementById('critical-list');
        list.innerHTML = critical.map(c => `<div class="data-item"><strong>[ID: ${c.id}]</strong> ${c.title} - ${c.status}</div>`).join('');
    }

    // Feedback
    const fbRes = await fetch(`${API_BASE_URL}/feedback/`, { headers: { 'Authorization': `Bearer ${token}` } });
    if (fbRes.ok) {
        const feedback = await fbRes.json();
        const list = document.getElementById('feedback-list');
        list.innerHTML = feedback.map(f => `<div class="data-item">User ${f.user_id}: "${f.comment}" (Rating: ${f.rating}/5)</div>`).join('');
    }
}

// ==========================================
// Interactive Map (/maps/markers)
// ==========================================
async function loadMapData() {
    if (!mapInstance) {
        mapInstance = L.map('urban-map').setView([20.5937, 78.9629], 5); // Default center
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '© OpenStreetMap contributors © CARTO'
        }).addTo(mapInstance);
    }

    const res = await fetch(`${API_BASE_URL}/maps/markers`, { headers: { 'Authorization': `Bearer ${token}` } });
    if (res.ok) {
        const markers = await res.json();
        markers.forEach(m => {
            if (m.latitude && m.longitude) {
                const color = m.priority === 'Emergency' ? 'red' : 'blue';
                L.circleMarker([m.latitude, m.longitude], {
                    radius: 8, fillColor: color, color: '#fff', weight: 1, opacity: 1, fillOpacity: 0.8
                }).addTo(mapInstance)
                  .bindPopup(`<strong>${m.title}</strong><br>Status: ${m.status}<br>Category: ${m.category}`);
            }
        });
    }
    
    // Fix Leaflet rendering bug when map is initialized in a hidden div
    setTimeout(() => { mapInstance.invalidateSize(); }, 100);
}

// ==========================================
// Notifications (/notifications)
// ==========================================
async function loadNotifications() {
    const res = await fetch(`${API_BASE_URL}/notifications/`, { headers: { 'Authorization': `Bearer ${token}` } });
    if (res.ok) {
        const notifs = await res.json();
        document.getElementById('notif-badge').innerText = notifs.length;
        
        const list = document.getElementById('notifications-list');
        list.innerHTML = notifs.map(n => `
            <div class="data-item">
                <div style="color: var(--accent-color); font-weight: bold;">${n.created_at.split('T')[0]}</div>
                ${n.message}
            </div>
        `).join('');
    }
}
