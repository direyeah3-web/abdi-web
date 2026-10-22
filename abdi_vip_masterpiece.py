import shutil
import os

if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_masterpiece_backup.html')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdi VIP | Premium Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #08090C;
            --card-bg: #111318;
            --gold: #D4AF37;
            --gold-hover: #F3E5AB;
            --text-main: #FFFFFF;
            --text-muted: #8B8E98;
            --border: #1F2229;
            --danger: #E53935;
            --success: #43A047;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); display: flex; height: 100vh; overflow: hidden; }

        /* ===== SIDEBAR ===== */
        .sidebar {
            width: 260px; background-color: var(--card-bg); border-right: 1px solid var(--border);
            padding: 30px 20px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;
            transition: all 0.3s ease;
        }
        .logo-area { display: flex; align-items: center; gap: 12px; font-size: 22px; font-weight: 700; margin-bottom: 40px; color: var(--gold); letter-spacing: 1px;}
        .nav-menu { list-style: none; display: flex; flex-direction: column; gap: 8px; }
        .nav-item {
            padding: 14px 16px; border-radius: 12px; cursor: pointer; display: flex; align-items: center; gap: 14px; 
            color: var(--text-muted); font-weight: 500; transition: all 0.2s ease; border-left: 3px solid transparent;
        }
        .nav-item:hover { background-color: rgba(212, 175, 55, 0.05); color: var(--text-main); }
        .nav-item.active { background-color: rgba(212, 175, 55, 0.1); color: var(--gold); border-left-color: var(--gold); }
        .nav-item svg { width: 22px; height: 22px; fill: currentColor; }
        
        .user-profile-bottom { display: flex; align-items: center; gap: 12px; padding: 15px; background-color: rgba(255,255,255,0.03); border-radius: 15px; border: 1px solid var(--border); }
        .avatar { width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(135deg, var(--gold), #a88c2a); color: #000; display: flex; justify-content: center; align-items: center; font-weight: bold; font-size: 18px;}
        .user-info p { font-size: 14px; font-weight: 600; color: var(--text-main); }
        .user-info span { font-size: 12px; color: var(--text-muted); }

        /* ===== MAIN CONTENT ===== */
        .main-content { flex: 1; padding: 30px 40px; overflow-y: auto; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .header h1 { font-size: 28px; font-weight: 600; letter-spacing: -0.5px; }
        .logout-btn { background: transparent; border: 1px solid var(--border); color: var(--text-muted); padding: 10px 20px; border-radius: 10px; cursor: pointer; font-weight: 500; transition: 0.3s; }
        .logout-btn:hover { border-color: var(--danger); color: var(--danger); }

        .tab-content { display: none; animation: fadeIn 0.4s ease; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* ===== STATS & DASHBOARD ===== */
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .stat-card { 
            background-color: var(--card-bg); border: 1px solid var(--border); padding: 25px; border-radius: 16px; 
            position: relative; overflow: hidden; transition: 0.3s;
        }
        .stat-card:hover { transform: translateY(-5px); border-color: rgba(212, 175, 55, 0.4); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
        .stat-card h3 { font-size: 32px; margin-bottom: 5px; color: var(--text-main); }
        .stat-card p { font-size: 14px; color: var(--text-muted); font-weight: 500; }
        .stat-card .trend { font-size: 12px; color: var(--success); margin-top: 10px; display: block; }
        
        /* Graph Container */
        .graph-container { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 25px; margin-bottom: 30px; }
        .graph-header { display: flex; justify-content: space-between; margin-bottom: 20px; }
        .graph-header h2 { font-size: 18px; font-weight: 600; }
        .graph-bars { display: flex; align-items: flex-end; gap: 15px; height: 150px; padding-top: 20px; border-bottom: 1px solid var(--border); padding-bottom: 10px;}
        .bar { flex: 1; background: linear-gradient(to top, rgba(212, 175, 55, 0.1), var(--gold)); border-radius: 5px 5px 0 0; transition: 0.3s; position: relative;}
        .bar:hover { opacity: 0.8; }
        .bar::after { content: attr(data-day); position: absolute; bottom: -25px; left: 50%; transform: translateX(-50%); font-size: 12px; color: var(--text-muted); }

        /* ===== TABLES ===== */
        .table-container { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; }
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th { padding: 18px 20px; color: var(--text-muted); font-size: 13px; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.2); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;}
        td { padding: 18px 20px; font-size: 14px; border-bottom: 1px solid var(--border); }
        tr:last-child td { border-bottom: none; }
        tr:hover td { background-color: rgba(255,255,255,0.02); }
        
        .badge { padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-unused { background: rgba(67, 160, 71, 0.1); color: var(--success); border: 1px solid rgba(67, 160, 71, 0.2); }
        .badge-active { background: rgba(212, 175, 55, 0.1); color: var(--gold); border: 1px solid rgba(212, 175, 55, 0.2); }
        
        .icon-btn { background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: var(--text-main); width: 32px; height: 32px; border-radius: 8px; cursor: pointer; margin-right: 5px; transition: 0.2s; display: inline-flex; justify-content: center; align-items: center;}
        .icon-btn:hover { background: rgba(255,255,255,0.1); }

        /* Generate Button */
        .gen-btn {
            background: linear-gradient(135deg, var(--gold), #a88c2a); color: #000;
            border: none; padding: 12px 24px; border-radius: 10px; font-weight: 700; cursor: pointer; transition: 0.3s;
            display: flex; align-items: center; gap: 8px; font-size: 14px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
        }
        .gen-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4); }

        /* ===== MODAL ===== */
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: none; justify-content: center; align-items: center; z-index: 1000; backdrop-filter: blur(8px); }
        .modal-overlay.active { display: flex; }
        .modal { background: var(--card-bg); border: 1px solid var(--border); padding: 30px; border-radius: 20px; width: 90%; max-width: 400px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.5);}
        .modal h3 { margin-bottom: 25px; font-size: 20px; color: var(--gold); }
        .duration-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 20px; }
        .dur-btn { background: rgba(255,255,255,0.03); border: 1px solid var(--border); color: var(--text-muted); padding: 10px; border-radius: 10px; cursor: pointer; font-weight: 500; transition: 0.2s; font-size: 13px; }
        .dur-btn:hover { background: rgba(255,255,255,0.08); }
        .dur-btn.active { background: var(--gold); color: #000; border-color: var(--gold); font-weight: 700; }
        .input-group { margin-bottom: 25px; text-align: left; }
        .input-group label { display: block; color: var(--text-muted); font-size: 12px; margin-bottom: 8px; font-weight: 600; }
        .input-group input { width: 100%; background: var(--bg-color); border: 1px solid var(--border); color: var(--text-main); padding: 14px; border-radius: 10px; font-size: 16px; outline: none;}
        .input-group input:focus { border-color: var(--gold); }
        .modal-gen-btn { width: 100%; padding: 16px; border-radius: 12px; border: none; background: linear-gradient(135deg, var(--gold), #a88c2a); color: #000; font-weight: 700; cursor: pointer; font-size: 16px; transition: 0.3s; }
        .modal-gen-btn:hover { transform: translateY(-2px); }

        /* ===== TOAST NOTIFICATION ===== */
        .toast-container { position: fixed; top: 20px; right: 20px; z-index: 2000; display: flex; flex-direction: column; gap: 10px; }
        .toast { background: var(--card-bg); border: 1px solid var(--border); color: var(--text-main); padding: 16px 20px; border-radius: 12px; display: flex; align-items: center; gap: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); animation: slideIn 0.3s ease forwards; font-size: 14px; font-weight: 500;}
        .toast.success { border-left: 4px solid var(--gold); }
        .toast.error { border-left: 4px solid var(--danger); }
        @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }

        /* ===== RESPONSIVE (MOBILE) ===== */
        @media (max-width: 768px) {
            .sidebar { position: fixed; left: -260px; height: 100vh; z-index: 999; }
            .sidebar.active { left: 0; }
            .main-content { padding: 20px; }
            .header h1 { font-size: 22px; }
            .stats-grid { grid-template-columns: 1fr; }
            table { font-size: 12px; }
            th, td { padding: 12px 10px; }
            .menu-btn { display: block; background: transparent; border: none; color: white; font-size: 24px; cursor: pointer; }
        }
        @media (min-width: 769px) {
            .menu-btn { display: none; }
        }
    </style>
</head>
<body>

    <div class="toast-container" id="toast-container"></div>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <div>
            <div class="logo-area">
                <svg style="width:28px; height:28px;" viewBox="0 0 24 24" fill="var(--gold)"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
                ABDI VIP
            </div>
            <ul class="nav-menu">
                <li class="nav-item active" onclick="switchTab('dashboard', this)">
                    <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg> Dashboard
                </li>
                <li class="nav-item" onclick="switchTab('users', this)">
                    <svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg> Users
                </li>
                <li class="nav-item" onclick="switchTab('licenses', this)">
                    <svg viewBox="0 0 24 24"><path d="M12.65 10C11.83 7.67 9.61 6 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6c2.61 0 4.83-1.67 5.65-4H17v4h4v-4h2v-4H12.65zM7 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/></svg> Licenses
                </li>
                <li class="nav-item" onclick="switchTab('settings', this)">
                    <svg viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg> Settings
                </li>
            </ul>
        </div>
        <div class="user-profile-bottom">
            <div class="avatar">A</div>
            <div class="user-info"><p>Abdi</p><span>Administrator</span></div>
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <div class="header">
            <div style="display: flex; align-items: center; gap: 15px;">
                <button class="menu-btn" onclick="document.getElementById('sidebar').classList.toggle('active')">☰</button>
                <h1 id="page-title">Dashboard</h1>
            </div>
            <button class="logout-btn" onclick="window.location.href='index.html'">Logout</button>
        </div>

        <!-- TAB: DASHBOARD -->
        <div id="tab-dashboard" class="tab-content active">
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>1,248</h3>
                    <p>Total Users</p>
                    <span class="trend">+12% this month</span>
                </div>
                <div class="stat-card">
                    <h3>856</h3>
                    <p>Active Licenses</p>
                    <span class="trend" style="color: var(--gold);">Live status</span>
                </div>
                <div class="stat-card">
                    <h3>98.9%</h3>
                    <p>API Uptime</p>
                    <span class="trend" style="color: var(--success);">System Status: Secure</span>
                </div>
                <div class="stat-card">
                    <h3>42</h3>
                    <p>Banned Users</p>
                    <span class="trend" style="color: var(--danger);">Action required</span>
                </div>
            </div>

            <div class="graph-container">
                <div class="graph-header">
                    <h2>Analytics Overview (7 Days)</h2>
                </div>
                <div class="graph-bars">
                    <div class="bar" style="height: 40%;" data-day="Mon"></div>
                    <div class="bar" style="height: 60%;" data-day="Tue"></div>
                    <div class="bar" style="height: 35%;" data-day="Wed"></div>
                    <div class="bar" style="height: 80%;" data-day="Thu"></div>
                    <div class="bar" style="height: 55%;" data-day="Fri"></div>
                    <div class="bar" style="height: 90%;" data-day="Sat"></div>
                    <div class="bar" style="height: 70%;" data-day="Sun"></div>
                </div>
            </div>
        </div>

        <!-- TAB: USERS -->
        <div id="tab-users" class="tab-content">
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>User</th>
                            <th>Status</th>
                            <th>Joined Date</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="font-weight: 600;">Abdi (Admin)</td>
                            <td><span class="badge badge-active">Active</span></td>
                            <td>2023-10-22</td>
                            <td>
                                <button class="icon-btn" title="Edit">✏️</button>
                                <button class="icon-btn" style="color: var(--danger);" title="Ban">🚫</button>
                            </td>
                        </tr>
                        <tr>
                            <td style="font-weight: 600;">UserX</td>
                            <td><span class="badge" style="background: rgba(229, 57, 53, 0.1); color: var(--danger); border: 1px solid rgba(229, 57, 53, 0.2);">Banned</span></td>
                            <td>2023-11-05</td>
                            <td>
                                <button class="icon-btn" title="Edit">✏️</button>
                                <button class="icon-btn" style="color: var(--success);" title="Unban">✅</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- TAB: LICENSES -->
        <div id="tab-licenses" class="tab-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h2 style="font-size: 18px; font-weight: 600;">License Management</h2>
                <button class="gen-btn" onclick="openModal()">
                    <svg style="width:18px; height:18px; fill:#000;" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
                    Generate License
                </button>
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

        <!-- TAB: SETTINGS -->
        <div id="tab-settings" class="tab-content">
            <div class="table-container" style="padding: 25px;">
                <h2 style="font-size: 18px; margin-bottom: 15px;">Security & Settings</h2>
                <p style="color: var(--text-muted); margin-bottom: 20px;">Manage API keys, Admin roles, and system configurations.</p>
                <button class="logout-btn" style="border-color: var(--gold); color: var(--gold);">Update API Keys</button>
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
                    <button class="dur-btn" onclick="selectDuration(this, '90 Days')">90 Days</button>
                    <button class="dur-btn" onclick="selectDuration(this, '1 Year')">1 Year</button>
                    <button class="dur-btn" onclick="selectDuration(this, 'Lifetime')">Lifetime</button>
                </div>
            </div>
            <div class="input-group">
                <label>QUANTITY</label>
                <input type="number" id="key-quantity" value="1" min="1" max="50">
            </div>
            <button class="modal-gen-btn" onclick="generateKeys()">GENERATE NOW</button>
            <button style="background: transparent; border: none; color: var(--text-muted); margin-top: 15px; cursor: pointer;" onclick="closeModal()">Cancel</button>
        </div>
    </div>

    <script>
        // ===== 1. TOAST FUNCTION =====
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

        // ===== 2. NAVIGATION =====
        function switchTab(tabName, element) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            element.classList.add('active');
            
            const titles = { 'dashboard': 'Dashboard', 'users': 'Users Management', 'licenses': 'Licenses Management', 'settings': 'Settings' };
            document.getElementById('page-title').innerText = titles[tabName];
            
            // Close sidebar on mobile after clicking
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('active');
            }

            if (tabName === 'licenses') loadLicenses();
        }

        // ===== 3. MODAL =====
        let selectedDuration = '1 Day';
        function openModal() { document.getElementById('licenseModal').classList.add('active'); }
        function closeModal() { document.getElementById('licenseModal').classList.remove('active'); }
        function selectDuration(btn, duration) {
            document.querySelectorAll('.dur-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedDuration = duration;
        }

        // ===== 4. KEY MANAGEMENT =====
        function generateKeys() {
            const qty = parseInt(document.getElementById('key-quantity').value);
            let keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
            
            for (let i = 0; i < qty; i++) {
                const randomStr = Math.random().toString(36).substring(2, 8).toUpperCase();
                keys.push({
                    id: Date.now() + i,
                    key: `ABDI-VIP-${randomStr}`,
                    duration: selectedDuration,
                    status: 'unused',
                    date: new Date().toLocaleDateString()
                });
            }
            
            localStorage.setItem('abdi_keys', JSON.stringify(keys));
            closeModal();
            loadLicenses();
            showToast(`${qty} Key(s) generated successfully!`, 'success');
        }

        function loadLicenses() {
            const keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
            const tbody = document.getElementById('license-list');
            tbody.innerHTML = '';
            
            if (keys.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 30px;">No licenses generated yet.</td></tr>';
                return;
            }
            
            keys.reverse().forEach(k => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td style="font-family: monospace; font-size: 14px; color: var(--gold); font-weight: 600;">${k.key}</td>
                    <td>${k.duration}</td>
                    <td><span class="badge badge-${k.status}">${k.status}</span></td>
                    <td>
                        <button class="icon-btn" onclick="copyKey('${k.key}')" title="Copy Key">📋</button>
                        <button class="icon-btn" onclick="deleteKey(${k.id})" style="color: var(--danger);" title="Revoke">🗑️</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function copyKey(key) { 
            navigator.clipboard.writeText(key); 
            showToast('Key copied to clipboard!', 'success'); 
        }

        function deleteKey(id) {
            if (confirm('Are you sure you want to revoke/delete this key?')) {
                let keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
                keys = keys.filter(k => k.id !== id);
                localStorage.setItem('abdi_keys', JSON.stringify(keys));
                loadLicenses();
                showToast('Key revoked successfully.', 'error');
            }
        }

        // Load initial data
        window.onload = function() { 
            if (document.getElementById('tab-licenses').classList.contains('active')) loadLicenses(); 
        }
    </script>
</body>
</html>
"""

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Abdi VIP Masterpiece Dashboard waa la dhisay! (Black + Gold + Full Features)")
