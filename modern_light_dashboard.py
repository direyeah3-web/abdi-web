import shutil
import os

if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_dark_backup.html')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdi VIP | Modern Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #e0e5ec 0%, #cbd5e1 100%);
            --glass-bg: rgba(255, 255, 255, 0.45);
            --glass-border: rgba(255, 255, 255, 0.6);
            --text-main: #1e293b;
            --text-muted: #64748b;
            --blue: #3b82f6;
            --green: #10b981;
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
            --radius: 24px;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

        body {
            background: var(--bg-gradient);
            color: var(--text-main);
            display: flex;
            height: 100vh;
            overflow: hidden;
        }

        /* ===== SIDEBAR (Qaabka Sawirka 3aad) ===== */
        .sidebar {
            width: 90px;
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-right: 1px solid var(--glass-border);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px 0;
            border-radius: 0 30px 30px 0;
            box-shadow: var(--shadow);
            z-index: 100;
            transition: width 0.3s ease;
        }
        
        .sidebar:hover { width: 240px; align-items: flex-start; padding-left: 20px; }

        .logo {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 40px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .nav-item {
            width: 60px;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 15px;
            border-radius: 20px;
            cursor: pointer;
            color: var(--text-muted);
            transition: all 0.3s;
            overflow: hidden;
            white-space: nowrap;
        }

        .sidebar:hover .nav-item { width: 200px; justify-content: flex-start; padding-left: 20px; gap: 15px;}
        
        .nav-item:hover, .nav-item.active { background: rgba(255, 255, 255, 0.8); color: var(--text-main); box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .nav-item svg { min-width: 24px; height: 24px; fill: currentColor; }

        /* ===== MAIN CONTENT ===== */
        .main-content {
            flex: 1;
            padding: 40px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        /* Header */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header h1 { font-size: 32px; font-weight: 600; letter-spacing: -1px; color: #0f172a;}
        .header p { color: var(--text-muted); font-size: 14px; margin-top: 5px; }
        
        .logout-btn {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            padding: 12px 24px;
            border-radius: 50px;
            color: var(--text-main);
            font-weight: 600;
            cursor: pointer;
            backdrop-filter: blur(10px);
            transition: 0.3s;
            box-shadow: var(--shadow);
        }
        .logout-btn:hover { background: #fff; }

        /* ===== GRID SYSTEM (Sida Sawirka 2aad) ===== */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius);
            padding: 25px;
            backdrop-filter: blur(20px);
            box-shadow: var(--shadow);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.3s ease;
        }
        .card:hover { transform: translateY(-5px); }

        .card-title { font-size: 16px; font-weight: 600; color: var(--text-main); margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
        .card-subtitle { font-size: 12px; color: var(--text-muted); margin-bottom: 20px; }

        .big-number { font-size: 48px; font-weight: 700; color: #0f172a; letter-spacing: -2px; }

        /* Custom Controls (Sida Slider-ka Sawirka 2aad) */
        .slider-container {
            height: 40px;
            background: linear-gradient(90deg, #fcd34d 0%, #fbbf24 50%, #f59e0b 100%);
            border-radius: 20px;
            margin: 15px 0;
            display: flex;
            align-items: center;
            padding: 0 10px;
        }
        .slider-knob { width: 30px; height: 30px; background: #fff; border-radius: 50%; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }

        /* Special Card (Blue like the Door Lock) */
        .card.blue-card {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            border: none;
        }
        .card.blue-card .card-title, .card.blue-card .card-subtitle { color: rgba(255,255,255,0.8); }
        .card.blue-card .big-number { color: #fff; }

        /* ===== TABLES (License Table) ===== */
        .table-container { background: var(--glass-bg); border-radius: var(--radius); padding: 25px; backdrop-filter: blur(20px); border: 1px solid var(--glass-border); box-shadow: var(--shadow); }
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th { padding: 15px; color: var(--text-muted); font-size: 13px; font-weight: 600; border-bottom: 1px solid rgba(0,0,0,0.05); }
        td { padding: 15px; font-size: 14px; font-weight: 500; border-bottom: 1px solid rgba(0,0,0,0.05); }
        .badge { padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; background: rgba(16, 185, 129, 0.1); color: var(--green); }
        
        .gen-btn { background: var(--text-main); color: #fff; border: none; padding: 12px 24px; border-radius: 50px; font-weight: 600; cursor: pointer; transition: 0.3s; }
        .gen-btn:hover { background: #000; transform: scale(1.05); }
        
        /* Tab Visibility */
        .tab-content { display: none; animation: fadeIn 0.4s ease; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Modal */
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(255,255,255,0.3); display: none; justify-content: center; align-items: center; z-index: 1000; backdrop-filter: blur(10px); }
        .modal-overlay.active { display: flex; }
        .modal { background: #fff; padding: 35px; border-radius: 30px; width: 90%; max-width: 400px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.1); }
        .modal h3 { margin-bottom: 25px; font-size: 24px; color: var(--text-main); }
        .duration-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 25px; }
        .dur-btn { background: #f1f5f9; border: none; padding: 12px; border-radius: 15px; cursor: pointer; color: var(--text-muted); font-weight: 600; transition: 0.2s; }
        .dur-btn.active { background: var(--text-main); color: #fff; }
        .input-group { margin-bottom: 25px; text-align: left; }
        .input-group label { display: block; font-size: 13px; color: var(--text-muted); margin-bottom: 8px; font-weight: 600; }
        .input-group input { width: 100%; padding: 15px; border-radius: 15px; border: 1px solid #e2e8f0; font-size: 16px; outline: none; }
        .modal-gen-btn { width: 100%; padding: 18px; border-radius: 15px; border: none; background: var(--blue); color: #fff; font-weight: 700; cursor: pointer; font-size: 16px; transition: 0.3s; }
        .modal-gen-btn:hover { background: #2563eb; }

        /* Toast */
        .toast-container { position: fixed; top: 30px; right: 30px; z-index: 2000; display: flex; flex-direction: column; gap: 10px; }
        .toast { background: #fff; color: var(--text-main); padding: 16px 24px; border-radius: 15px; display: flex; align-items: center; gap: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); font-weight: 600; animation: slideIn 0.3s ease forwards; }
        .toast.success { border-left: 4px solid var(--green); }
        .toast.error { border-left: 4px solid #ef4444; }
        @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }
    </style>
</head>
<body>

    <div class="toast-container" id="toast-container"></div>

    <!-- Sidebar -->
    <div class="sidebar">
        <div class="logo">
            <svg style="width:30px; height:30px; fill:var(--blue);" viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
            <span class="nav-text" style="display:none;">ABDI VIP</span>
        </div>
        <div class="nav-item active" onclick="switchTab('dashboard', this)">
            <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
            <span style="display:none;">Dashboard</span>
        </div>
        <div class="nav-item" onclick="switchTab('users', this)">
            <svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
            <span style="display:none;">Users</span>
        </div>
        <div class="nav-item" onclick="switchTab('licenses', this)">
            <svg viewBox="0 0 24 24"><path d="M12.65 10C11.83 7.67 9.61 6 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6c2.61 0 4.83-1.67 5.65-4H17v4h4v-4h2v-4H12.65zM7 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/></svg>
            <span style="display:none;">Licenses</span>
        </div>
        <div class="nav-item" onclick="window.location.href='index.html'">
            <svg viewBox="0 0 24 24"><path d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"/></svg>
            <span style="display:none;">Logout</span>
        </div>
    </div>

    <div class="main-content">
        <!-- HEADER -->
        <div class="header">
            <div>
                <h1 id="page-title">Hi Abdi,</h1>
                <p id="page-subtitle">Have a great day.</p>
            </div>
            <button class="logout-btn" onclick="window.location.href='index.html'">Logout</button>
        </div>

        <!-- TAB 1: DASHBOARD (Sida Sawirka 2aad) -->
        <div id="tab-dashboard" class="tab-content active">
            <div class="dashboard-grid">
                
                <!-- Card 1: Total Users -->
                <div class="card">
                    <div>
                        <div class="card-title">Total Users <span style="color:var(--blue);">👥</span></div>
                        <div class="card-subtitle">+12% this month</div>
                    </div>
                    <div class="big-number">1,248</div>
                </div>

                <!-- Card 2: Active Licenses -->
                <div class="card">
                    <div>
                        <div class="card-title">Active Licenses <span style="color:var(--green);">🔑</span></div>
                        <div class="card-subtitle">Live status</div>
                    </div>
                    <div class="big-number">856</div>
                </div>

                <!-- Card 3: API Status -->
                <div class="card blue-card">
                    <div>
                        <div class="card-title">API Uptime <span>⚡</span></div>
                        <div class="card-subtitle">System Status: Secure</div>
                    </div>
                    <div class="big-number">98.9%</div>
                </div>

                <!-- Card 4: Analytics / Graph (Waxaan u isticmaalaynaa sanduuq Slider ah sida sawirkaaga) -->
                <div class="card" style="grid-column: span 2;">
                    <div class="card-title">Server Load / Usage</div>
                    <div class="card-subtitle">Real-time analytics overview</div>
                    <div class="slider-container">
                        <div class="slider-knob" style="margin-left: 60%;"></div>
                    </div>
                </div>

                <!-- Card 5: Banned Users -->
                <div class="card">
                    <div>
                        <div class="card-title">Banned Users <span style="color:#ef4444;">🚫</span></div>
                        <div class="card-subtitle">Action required</div>
                    </div>
                    <div class="big-number">42</div>
                </div>

            </div>
        </div>

        <!-- TAB 2: USERS -->
        <div id="tab-users" class="tab-content">
            <div class="table-container">
                <h2 style="margin-bottom: 20px;">Users Management</h2>
                <p style="color: var(--text-muted);">List of users will appear here.</p>
            </div>
        </div>

        <!-- TAB 3: LICENSES -->
        <div id="tab-licenses" class="tab-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h2 style="font-size: 24px; font-weight: 600;">License Management</h2>
                <button class="gen-btn" onclick="openModal()">+ Generate License</button>
            </div>
            
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>License Key</th>
                            <th>Duration</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="license-list">
                        <!-- Key-yada halkan ayaa lagu soo bandhigi doonaa -->
                    </tbody>
                </table>
            </div>
        </div>

    </div>

    <!-- MODAL -->
    <div class="modal-overlay" id="licenseModal">
        <div class="modal">
            <h3>Generate New License</h3>
            <div class="input-group" style="text-align: left;">
                <label>DURATION</label>
                <div class="duration-grid">
                    <button class="dur-btn active" onclick="selectDuration(this, '1 Day')">1 Day</button>
                    <button class="dur-btn" onclick="selectDuration(this, '7 Days')">7 Days</button>
                    <button class="dur-btn" onclick="selectDuration(this, '30 Days')">30 Days</button>
                </div>
            </div>
            <div class="input-group">
                <label>QUANTITY</label>
                <input type="number" id="key-quantity" value="1" min="1" max="10">
            </div>
            <button class="modal-gen-btn" onclick="generateKeys()">GENERATE NOW</button>
            <button style="background: transparent; border: none; color: var(--text-muted); margin-top: 15px; cursor: pointer;" onclick="closeModal()">Cancel</button>
        </div>
    </div>

    <script>
        // ===== NAVIGATION =====
        function switchTab(tabName, element) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            element.classList.add('active');
            
            const titles = { 'dashboard': 'Hi Abdi,', 'users': 'Users', 'licenses': 'Licenses' };
            const subs = { 'dashboard': 'Have a great day.', 'users': 'Manage system users', 'licenses': 'Manage your keys' };
            document.getElementById('page-title').innerText = titles[tabName];
            document.getElementById('page-subtitle').innerText = subs[tabName];
            
            if (tabName === 'licenses') loadLicenses();
        }

        // ===== MODAL =====
        let selectedDuration = '1 Day';
        function openModal() { document.getElementById('licenseModal').classList.add('active'); }
        function closeModal() { document.getElementById('licenseModal').classList.remove('active'); }
        function selectDuration(btn, duration) {
            document.querySelectorAll('.dur-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedDuration = duration;
        }

        // ===== TOAST =====
        function showToast(message, type = 'success') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            const icon = type === 'success' ? '✅' : '❌';
            toast.innerHTML = `<span>${icon}</span> ${message}`;
            container.appendChild(toast);
            setTimeout(() => {
                toast.style.animation = 'slideOut 0.3s ease forwards';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        // ===== KEY MANAGEMENT =====
        async function generateKeys() {
            const qty = parseInt(document.getElementById('key-quantity').value);
            const btn = document.querySelector('.modal-gen-btn');
            btn.innerText = "Generating..."; btn.disabled = true;

            try {
                for (let i = 0; i < qty; i++) {
                    const response = await fetch('https://abdi-keys.dirxx.workers.dev/generate', {
                        method: 'POST', headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ duration: selectedDuration })
                    });
                    const data = await response.json();
                    if (data.status) {
                        let keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
                        keys.push({ id: Date.now() + i, key: data.key, duration: selectedDuration, status: 'unused' });
                        localStorage.setItem('abdi_keys', JSON.stringify(keys));
                    }
                }
                closeModal(); loadLicenses(); showToast(`${qty} Key generated!`, 'success');
            } catch (error) { showToast('Connection Failed!', 'error'); }
            finally { btn.innerText = "GENERATE NOW"; btn.disabled = false; }
        }

        function loadLicenses() {
            const keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
            const tbody = document.getElementById('license-list');
            tbody.innerHTML = keys.length === 0 ? '<tr><td colspan="4" style="text-align:center; padding:20px; color:var(--text-muted);">No keys yet.</td></tr>' : '';
            
            keys.reverse().forEach(k => {
                tbody.innerHTML += `
                    <tr>
                        <td style="font-family: monospace; font-weight: 600;">${k.key}</td>
                        <td>${k.duration}</td>
                        <td><span class="badge">${k.status}</span></td>
                        <td><button class="icon-btn" onclick="copyKey('${k.key}')" style="background:none; border:none; font-size:18px; cursor:pointer;">📋</button></td>
                    </tr>`;
            });
        }
        function copyKey(key) { navigator.clipboard.writeText(key); showToast('Key copied!', 'success'); }
        
        window.onload = () => { if (document.getElementById('tab-licenses').classList.contains('active')) loadLicenses(); }
    </script>
</body>
</html>
"""

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Dashboard-ka Casriga ah (Light Mode + Glassmorphism) waa la dhisay!")
