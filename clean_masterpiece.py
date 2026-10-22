import shutil
import os

if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_corrupted_backup.html')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdi VIP | Premium Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --bg-color: #050505; --card-bg: rgba(20, 20, 22, 0.6); --gold: #D4AF37;
            --gold-light: #F3E5AB; --text-main: #FFFFFF; --text-muted: #888;
            --border: rgba(255, 255, 255, 0.08); --danger: #ff4d4d; --success: #4ade80;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); display: flex; height: 100vh; overflow: hidden; background-image: radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.1) 0px, transparent 50%), radial-gradient(at 100% 100%, rgba(212, 175, 55, 0.05) 0px, transparent 50%); }
        
        .sidebar { width: 260px; background: rgba(10, 10, 12, 0.7); backdrop-filter: blur(20px); border-right: 1px solid var(--border); padding: 30px 20px; display: flex; flex-direction: column; justify-content: space-between; flex-shrink: 0; z-index: 100; }
        .logo-area { display: flex; align-items: center; gap: 12px; font-size: 22px; font-weight: 700; margin-bottom: 40px; color: var(--text-main); letter-spacing: 1px;}
        .logo-area svg { fill: var(--gold); filter: drop-shadow(0 0 8px rgba(212, 175, 55, 0.5)); }
        .nav-menu { list-style: none; display: flex; flex-direction: column; gap: 8px; }
        .nav-item { padding: 14px 16px; border-radius: 12px; cursor: pointer; display: flex; align-items: center; gap: 14px; color: var(--text-muted); font-weight: 500; transition: all 0.3s ease; border-left: 3px solid transparent; }
        .nav-item:hover { background: rgba(255, 255, 255, 0.03); color: var(--text-main); }
        .nav-item.active { background: linear-gradient(90deg, rgba(212, 175, 55, 0.15) 0%, transparent 100%); color: var(--gold); border-left-color: var(--gold); }
        .nav-item svg { width: 20px; height: 20px; fill: currentColor; }
        .user-profile-bottom { display: flex; align-items: center; gap: 12px; padding: 15px; background: rgba(255,255,255,0.02); border-radius: 15px; border: 1px solid var(--border); }
        .avatar { width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(135deg, var(--gold), var(--gold-light)); color: #000; display: flex; justify-content: center; align-items: center; font-weight: bold; font-size: 18px; box-shadow: 0 0 15px rgba(212, 175, 55, 0.3); }
        .user-info p { font-size: 14px; font-weight: 600; color: var(--text-main); }
        .user-info span { font-size: 12px; color: var(--text-muted); }

        .main-content { flex: 1; padding: 30px 40px; overflow-y: auto; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .header h1 { font-size: 28px; font-weight: 600; letter-spacing: -0.5px; }
        .logout-btn { background: transparent; border: 1px solid var(--border); color: var(--text-muted); padding: 10px 20px; border-radius: 10px; cursor: pointer; font-weight: 500; transition: 0.3s; }
        .logout-btn:hover { border-color: var(--danger); color: var(--danger); }

        .tab-content { display: none; animation: fadeIn 0.4s ease; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .stat-card { background: var(--card-bg); backdrop-filter: blur(10px); border: 1px solid var(--border); padding: 25px; border-radius: 16px; transition: 0.3s; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        .stat-card:hover { transform: translateY(-5px); border-color: rgba(212, 175, 55, 0.3); box-shadow: 0 10px 30px rgba(212, 175, 55, 0.1); }
        .stat-card h3 { font-size: 36px; margin-bottom: 5px; color: var(--text-main); font-weight: 700;}
        .stat-card p { font-size: 14px; color: var(--text-muted); font-weight: 500; }
        
        .chart-container { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 25px; margin-bottom: 30px; height: 350px; backdrop-filter: blur(10px); }

        .table-container { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; backdrop-filter: blur(10px);}
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th { padding: 18px 20px; color: var(--text-muted); font-size: 13px; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.3); font-weight: 600; text-transform: uppercase; }
        td { padding: 18px 20px; font-size: 14px; border-bottom: 1px solid var(--border); }
        tr:hover td { background-color: rgba(255,255,255,0.02); }
        .badge { padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-unused { background: rgba(74, 222, 128, 0.1); color: var(--success); border: 1px solid rgba(74, 222, 128, 0.2); }
        .icon-btn { background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: var(--text-main); width: 32px; height: 32px; border-radius: 8px; cursor: pointer; margin-right: 5px; }
        
        .gen-btn { background: linear-gradient(135deg, var(--gold), var(--gold-light)); color: #000; border: none; padding: 12px 24px; border-radius: 10px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; }
        
        .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: none; justify-content: center; align-items: center; z-index: 1000; backdrop-filter: blur(8px); }
        .modal-overlay.active { display: flex; }
        .modal { background: #111; border: 1px solid var(--border); padding: 30px; border-radius: 20px; width: 90%; max-width: 400px; text-align: center; }
        .modal h3 { margin-bottom: 25px; font-size: 20px; color: var(--gold); }
        .duration-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 20px; }
        .dur-btn { background: rgba(255,255,255,0.03); border: 1px solid var(--border); color: var(--text-muted); padding: 10px; border-radius: 10px; cursor: pointer; }
        .dur-btn.active { background: var(--gold); color: #000; font-weight: 700; }
        .input-group { margin-bottom: 25px; text-align: left; }
        .input-group label { display: block; color: var(--text-muted); font-size: 12px; margin-bottom: 8px; }
        .input-group input { width: 100%; background: var(--bg-color); border: 1px solid var(--border); color: var(--text-main); padding: 14px; border-radius: 10px; font-size: 16px; }
        .modal-gen-btn { width: 100%; padding: 16px; border-radius: 12px; border: none; background: linear-gradient(135deg, var(--gold), var(--gold-light)); color: #000; font-weight: 700; cursor: pointer; }
        
        .toast-container { position: fixed; top: 20px; right: 20px; z-index: 2000; display: flex; flex-direction: column; gap: 10px; }
        .toast { background: rgba(20,20,22,0.9); border: 1px solid var(--border); color: var(--text-main); padding: 16px 20px; border-radius: 12px; display: flex; align-items: center; gap: 12px; animation: slideIn 0.3s ease forwards; font-weight: 500; }
        .toast.success { border-left: 4px solid var(--gold); }
        .toast.error { border-left: 4px solid var(--danger); }
        @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }
    </style>
</head>
<body>
    <div class="toast-container" id="toast-container"></div>
    <div class="sidebar" id="sidebar">
        <div>
            <div class="logo-area">
                <svg style="width:28px; height:28px;" viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
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
                <div class="stat-card"><h3>1,248</h3><p>Total Users</p></div>
                <div class="stat-card"><h3>856</h3><p>Active Licenses</p></div>
                <div class="stat-card"><h3>98.9%</h3><p>API Uptime</p></div>
                <div class="stat-card"><h3>42</h3><p>Banned Users</p></div>
            </div>
            <div class="chart-container"><canvas id="myChart"></canvas></div>
        </div>

        <div id="tab-users" class="tab-content">
            <h2 style="margin-bottom: 20px;">Users Management</h2>
            <p style="color: #888;">User list will appear here.</p>
        </div>

        <div id="tab-licenses" class="tab-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h2 style="font-size: 18px;">License Management</h2>
                <button class="gen-btn" onclick="openModal()">+ Generate License</button>
            </div>
            <div class="table-container">
                <table>
                    <thead><tr><th>Key</th><th>Duration</th><th>Status</th><th>Actions</th></tr></thead>
                    <tbody id="license-list"></tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="modal-overlay" id="licenseModal">
        <div class="modal">
            <h3>Generate New License</h3>
            <div class="input-group">
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
            <button style="background: transparent; border: none; color: #888; margin-top: 15px; cursor: pointer;" onclick="closeModal()">Cancel</button>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: { labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], datasets: [{ label: 'Keys', data: [12, 19, 13, 25, 22, 30, 28], borderColor: '#D4AF37', tension: 0.4 }] },
            options: { responsive: true, maintainAspectRatio: false }
        });

        function showToast(message, type = 'success') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            toast.innerHTML = `<span>${type === 'success' ? '✅' : '❌'}</span> ${message}`;
            container.appendChild(toast);
            setTimeout(() => { toast.style.animation = 'slideOut 0.3s forwards'; setTimeout(() => toast.remove(), 300); }, 3000);
        }

        function switchTab(tabName, element) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            element.classList.add('active');
            const titles = { 'dashboard': 'Dashboard', 'users': 'Users', 'licenses': 'Licenses' };
            document.getElementById('page-title').innerText = titles[tabName];
            if (tabName === 'licenses') loadLicenses();
        }

        let selectedDuration = '1 Day';
        function openModal() { document.getElementById('licenseModal').classList.add('active'); }
        function closeModal() { document.getElementById('licenseModal').classList.remove('active'); }
        function selectDuration(btn, duration) {
            document.querySelectorAll('.dur-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active'); selectedDuration = duration;
        }

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
            tbody.innerHTML = keys.length === 0 ? '<tr><td colspan="4" style="text-align:center;">No keys yet.</td></tr>' : '';
            keys.reverse().forEach(k => {
                tbody.innerHTML += `<tr><td style="color:var(--gold);">${k.key}</td><td>${k.duration}</td><td><span class="badge badge-unused">${k.status}</span></td><td><button class="icon-btn" onclick="copyKey('${k.key}')">📋</button></td></tr>`;
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

print("✅ Faylka dashboard.html waa la dhisay si buuxda, qurux badanna waa u eg yahay!")
