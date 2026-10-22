import shutil
import os

# 1. Kaydi
if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_toast_backup.html')

# 2. Qoraalka cusub
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>Abdi VIP | Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background-color: #000000; color: #ffffff; display: flex; height: 100vh; overflow: hidden; }

        .sidebar {
            width: 260px; background-color: #0a0a0a; border-right: 1px solid #1c1c1e;
            padding: 30px 20px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0;
        }
        .logo-area { display: flex; align-items: center; gap: 10px; font-size: 20px; font-weight: 700; margin-bottom: 40px; color: #fff; }
        .nav-menu { list-style: none; display: flex; flex-direction: column; gap: 8px; }
        .nav-item {
            padding: 12px 15px; border-radius: 12px; cursor: pointer;
            display: flex; align-items: center; gap: 12px; color: #888; font-weight: 500; transition: all 0.2s ease;
        }
        .nav-item:hover, .nav-item.active { background-color: #1c1c1e; color: #fff; }
        .nav-item svg { width: 20px; height: 20px; fill: currentColor; }
        .user-profile-bottom { display: flex; align-items: center; gap: 12px; padding: 15px; background-color: #1c1c1e; border-radius: 15px; margin-top: 20px; }
        .avatar { width: 40px; height: 40px; border-radius: 50%; background: #fff; color: #000; display: flex; justify-content: center; align-items: center; font-weight: bold; }
        .user-info p { font-size: 14px; font-weight: 600; color: #fff; }
        .user-info span { font-size: 12px; color: #888; }

        .main-content { flex: 1; padding: 40px; overflow-y: auto; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; }
        .header h1 { font-size: 32px; font-weight: 700; letter-spacing: -1px; }
        .logout-btn { background: #1c1c1e; border: none; color: #fff; padding: 10px 20px; border-radius: 20px; cursor: pointer; font-weight: 600; }

        .tab-content { display: none; animation: fadeIn 0.4s ease; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .stat-card { background: linear-gradient(145deg, #111, #0a0a0a); border: 1px solid #1c1c1e; padding: 25px; border-radius: 20px; }
        .stat-card h3 { font-size: 36px; margin-bottom: 5px; color: #fff; }
        .stat-card p { font-size: 14px; color: #888; }

        /* License Table */
        .table-container { background: #0a0a0a; border: 1px solid #1c1c1e; border-radius: 15px; overflow: hidden; margin-top: 20px;}
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th { padding: 15px 20px; color: #888; font-size: 13px; border-bottom: 1px solid #1c1c1e; background: #111; }
        td { padding: 15px 20px; font-size: 14px; border-bottom: 1px solid #1c1c1e; }
        tr:last-child td { border-bottom: none; }
        .badge { padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-unused { background: rgba(74, 222, 128, 0.1); color: #4ade80; }
        .icon-btn { background: #1c1c1e; border: none; color: #fff; width: 30px; height: 30px; border-radius: 8px; cursor: pointer; margin-right: 5px; }
        .icon-btn:hover { background: #333; }

        .gen-btn {
            background: linear-gradient(90deg, #1f6feb, #388bfd); color: #fff;
            border: none; padding: 12px 24px; border-radius: 12px; font-weight: 600; cursor: pointer; transition: 0.3s;
        }
        .gen-btn:hover { opacity: 0.9; }

        /* Modal */
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8);
            display: none; justify-content: center; align-items: center; z-index: 1000; backdrop-filter: blur(5px);
        }
        .modal-overlay.active { display: flex; }
        .modal {
            background: linear-gradient(145deg, #111, #0a0a0a); border: 1px solid #2c2c2e;
            padding: 30px; border-radius: 20px; width: 90%; max-width: 400px; text-align: center;
        }
        .modal h3 { margin-bottom: 20px; color: #fff; }
        .duration-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 20px; }
        .dur-btn {
            background: #1c1c1e; border: 1px solid #333; color: #aaa; padding: 10px; border-radius: 10px;
            cursor: pointer; font-weight: 500; transition: 0.2s; font-size: 12px;
        }
        .dur-btn.active { background: #fff; color: #000; }
        .input-group { margin-bottom: 20px; text-align: left; }
        .input-group label { display: block; color: #888; font-size: 12px; margin-bottom: 5px; }
        .input-group input { width: 100%; background: #000; border: 1px solid #333; color: #fff; padding: 12px; border-radius: 10px; }
        .modal-gen-btn {
            width: 100%; padding: 15px; border-radius: 12px; border: none;
            background: linear-gradient(90deg, #1f6feb, #388bfd); color: #fff; font-weight: bold; cursor: pointer; font-size: 16px;
        }

        /* TOAST NOTIFICATION (Qaabka Sawirkaaga 3aad) */
        .toast-container {
            position: fixed; top: 20px; right: 20px; z-index: 2000;
            display: flex; flex-direction: column; gap: 10px;
        }
        .toast {
            background: #111; border: 1px solid #2c2c2e; color: #fff;
            padding: 15px 20px; border-radius: 12px; display: flex; align-items: center; gap: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5); animation: slideIn 0.3s ease forwards;
            font-size: 14px;
        }
        .toast.success { border-left: 4px solid #238636; }
        .toast.error { border-left: 4px solid #da3633; }
        @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }
    </style>
</head>
<body>

    <!-- Toast Container -->
    <div class="toast-container" id="toast-container"></div>

    <div class="sidebar">
        <div>
            <div class="logo-area">
                <svg style="width:24px; height:24px; fill:#ffd700;" viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
                Abdi VIP
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

    <div class="main-content">
        <div class="header">
            <h1 id="page-title">Dashboard</h1>
            <button class="logout-btn" onclick="window.location.href='index.html'">Logout</button>
        </div>

        <div id="tab-dashboard" class="tab-content active">
            <div class="stats-grid">
                <div class="stat-card"><h3>1</h3><p>Total Users</p></div>
                <div class="stat-card"><h3>2</h3><p>Total Licenses</p></div>
                <div class="stat-card"><h3>1</h3><p>Available Keys</p></div>
                <div class="stat-card"><h3>0</h3><p>Referrals</p></div>
            </div>
        </div>

        <div id="tab-licenses" class="tab-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h2 style="font-size: 20px;">Licenses Management</h2>
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

        <div id="tab-users" class="tab-content"><h2>Users</h2><p style="color:#888;">Coming soon...</p></div>
        <div id="tab-settings" class="tab-content"><h2>Settings</h2><p style="color:#888;">Coming soon...</p></div>
    </div>

    <!-- MODAL -->
    <div class="modal-overlay" id="licenseModal">
        <div class="modal">
            <h3>🔑 Generate License</h3>
            <div class="input-group" style="text-align: left;">
                <label>DURATION</label>
                <div class="duration-grid">
                    <button class="dur-btn active" onclick="selectDuration(this, '1 Day')">1 Day</button>
                    <button class="dur-btn" onclick="selectDuration(this, '7 Days')">7 Days</button>
                    <button class="dur-btn" onclick="selectDuration(this, '30 Days')">30 Days</button>
                    <button class="dur-btn" onclick="selectDuration(this, '90 Days')">90 Days</button>
                    <button class="dur-btn" onclick="selectDuration(this, '1 Year')">1 Year</button>
                    <button class="dur-btn" onclick="selectDuration(this, 'Custom')">Custom</button>
                </div>
            </div>
            <div class="input-group">
                <label>QUANTITY</label>
                <input type="number" id="key-quantity" value="1" min="1" max="10">
            </div>
            <button class="modal-gen-btn" onclick="generateKeys()">⚡ GENERATE NOW</button>
            <button style="background: transparent; border: none; color: #888; margin-top: 15px; cursor: pointer;" onclick="closeModal()">Cancel</button>
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
            const titles = { 'dashboard': 'Dashboard', 'users': 'Users', 'licenses': 'Licenses', 'settings': 'Settings' };
            document.getElementById('page-title').innerText = titles[tabName];
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
                    status: 'unused'
                });
            }
            localStorage.setItem('abdi_keys', JSON.stringify(keys));
            closeModal();
            loadLicenses();
            showToast(`${qty} Key(s) generated successfully!`, 'success'); // Toast halkan
        }

        function loadLicenses() {
            const keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
            const tbody = document.getElementById('license-list');
            tbody.innerHTML = '';
            if (keys.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: #888; padding: 30px;">No licenses generated yet.</td></tr>';
                return;
            }
            keys.reverse().forEach(k => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td style="font-family: monospace; font-size: 13px;">${k.key}</td>
                    <td>${k.duration}</td>
                    <td><span class="badge badge-${k.status}">${k.status}</span></td>
                    <td>
                        <button class="icon-btn" onclick="copyKey('${k.key}')">📋</button>
                        <button class="icon-btn" onclick="deleteKey(${k.id})" style="color: #ff4d4d;">🗑️</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function copyKey(key) { 
            navigator.clipboard.writeText(key); 
            showToast('Key copied: ' + key, 'success'); // Toast halkan
        }

        function deleteKey(id) {
            if (confirm('Delete this key?')) {
                let keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
                keys = keys.filter(k => k.id !== id);
                localStorage.setItem('abdi_keys', JSON.stringify(keys));
                loadLicenses();
                showToast('Key deleted.', 'error'); // Toast halkan
            }
        }
        window.onload = function() { if (document.getElementById('tab-licenses').classList.contains('active')) loadLicenses(); }
    </script>
</body>
</html>
"""

# 3. Qor faylka
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Toast Notification iyo Key Management waa lagu daray! (Cache Control)")
