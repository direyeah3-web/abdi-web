import shutil
import re

# 1. Backup
shutil.copy('public/index.html', 'public/index.html.backup_apple_ui')

with open('public/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 2. Update Dashboard Data (Real Data)
# Waxaan beddelaynaa xogta static-ka ah ee Dashboard-ka xogta dhabta ah
old_dash = """<div class="stat-value" id="total-users">1,248</div>"""
new_dash = """<div class="stat-value" id="total-users">...</div>"""
if old_dash in c:
    c = c.replace(old_dash, new_dash)
    print("1. Dashboard Users: OK")

old_lic = """<div class="stat-value" id="active-licenses">856</div>"""
new_lic = """<div class="stat-value" id="active-licenses">...</div>"""
if old_lic in c:
    c = c.replace(old_lic, new_lic)
    print("2. Dashboard Licenses: OK")

# 3. Apple UI CSS (Glassmorphism + Smooth)
old_css = """<style>"""
new_css = """<style>
/* ===== APPLE UI THEME ===== */
:root {
    --apple-bg: #000000;
    --apple-card: rgba(28, 28, 30, 0.6);
    --apple-border: rgba(255, 255, 255, 0.1);
    --apple-text: #ffffff;
    --apple-muted: #8e8e93;
    --apple-blue: #0a84ff;
    --apple-green: #30d158;
    --apple-red: #ff453a;
    --apple-yellow: #ffd60a;
}

body {
    background: var(--apple-bg) !important;
    color: var(--apple-text) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    -webkit-font-smoothing: antialiased;
}

/* Glassmorphism Cards */
.card, .stat-card, .panel, .sidebar {
    background: var(--apple-card) !important;
    backdrop-filter: blur(20px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
    border: 1px solid var(--apple-border) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important;
}

/* Buttons */
.btn-primary {
    background: var(--apple-blue) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    transition: transform 0.2s, opacity 0.2s !important;
}
.btn-primary:active { transform: scale(0.95) !important; }

/* Sidebar */
.sidebar {
    background: rgba(20, 20, 22, 0.8) !important;
    border-right: 1px solid var(--apple-border) !important;
    border-radius: 0 !important;
}
.nav-item {
    border-radius: 10px !important;
    margin: 4px 8px !important;
    transition: background 0.2s !important;
}
.nav-item:hover, .nav-item.active {
    background: rgba(255, 255, 255, 0.1) !important;
}

/* Inputs */
input, select {
    background: rgba(0, 0, 0, 0.5) !important;
    border: 1px solid var(--apple-border) !important;
    border-radius: 12px !important;
    color: #fff !important;
}
input:focus { border-color: var(--apple-blue) !important; outline: none !important; }

/* Charts */
.chart-box { background: transparent !important; }
</style>"""

if old_css in c:
    c = c.replace(old_css, new_css, 1)
    print("3. Apple UI CSS: OK")

# 4. Fix Dashboard Real Data Script
old_script = """function loadDashboard() {"""
new_script = """async function loadDashboard() {
    try {
        var t = localStorage.getItem('token');
        var r = await fetch('/api/stats', { headers: { 'Authorization': 'Bearer ' + t } });
        var d = await r.json();
        
        // Update Cards
        var elUsers = document.getElementById('total-users');
        if(elUsers) elUsers.textContent = d.totalUsers || '0';
        
        var elLic = document.getElementById('active-licenses');
        if(elLic) elLic.textContent = d.activeLicenses || '0';
        
        // ... (update charts if necessary)
    } catch (e) {
        console.error('Dashboard error:', e);
    }
"""
if old_script in c:
    c = c.replace(old_script, new_script, 1)
    print("4. Real Data Script: OK")

# 5. Save
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Dhammaan isbeddellada la sameeyay!")
