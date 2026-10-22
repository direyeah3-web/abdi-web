import shutil
import os

# 1. Kaydi
if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_backup_definitive.html')

# 2. Qoraalka cusub ee Dashboard-ka
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

        .section-title { font-size: 18px; font-weight: 600; margin-bottom: 20px; color: #fff; }
        .actions-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
        .action-btn {
            background-color: #1c1c1e; border: 1px solid #2c2c2e; color: #fff; padding: 20px;
            border-radius: 15px; cursor: pointer; display: flex; align-items: center; gap: 15px; font-weight: 500; transition: all 0.3s ease;
        }
        .action-btn:hover { background-color: #2c2c2e; transform: translateY(-2px); }
        .action-btn svg { width: 20px; height: 20px; fill: #aaa; }
    </style>
</head>
<body>

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
            <div class="user-info">
                <p>Abdi</p>
                <span>Administrator</span>
            </div>
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
            <h2 class="section-title">Quick Actions</h2>
            <div class="actions-grid">
                <button class="action-btn" onclick="alert('Generate License Clicked!')">
                    <svg viewBox="0 0 24 24"><path d="M12.65 10C11.83 7.67 9.61 6 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6c2.61 0 4.83-1.67 5.65-4H17v4h4v-4h2v-4H12.65zM7 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/></svg> Generate License
                </button>
                <button class="action-btn" onclick="alert('Add New User Clicked!')">
                    <svg viewBox="0 0 24 24"><path d="M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm-9-2V7H4v3H1v2h3v3h2v-3h3v-2H6zm9 4c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg> Add New User
                </button>
            </div>
        </div>

        <div id="tab-licenses" class="tab-content">
            <h2 class="section-title">Manage Licenses</h2>
            <div style="background: #111; border: 1px solid #333; padding: 20px; border-radius: 15px;">
                <p style="color: #aaa; margin-bottom: 20px;">Here you can view and manage all generated license keys.</p>
                <table style="width: 100%; text-align: left; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid #333;">
                        <th style="padding: 10px 0; color: #888;">Key</th>
                        <th style="padding: 10px 0; color: #888;">Status</th>
                        <th style="padding: 10px 0; color: #888;">Action</th>
                    </tr>
                    <tr>
                        <td style="padding: 15px 0;">VIP-ABC123</td>
                        <td style="padding: 15px 0; color: #4ade80;">Active</td>
                        <td style="padding: 15px 0;"><button style="background: transparent; border: 1px solid #ff4d4d; color: #ff4d4d; padding: 5px 10px; border-radius: 5px; cursor:pointer;">Revoke</button></td>
                    </tr>
                </table>
            </div>
        </div>
        
        <div id="tab-users" class="tab-content">
             <h2 class="section-title">Manage Users</h2>
             <div style="background: #111; border: 1px solid #333; padding: 20px; border-radius: 15px;">
                 <p style="color: #aaa;">No users found.</p>
             </div>
        </div>

        <div id="tab-settings" class="tab-content">
             <h2 class="section-title">Settings</h2>
             <div style="background: #111; border: 1px solid #333; padding: 20px; border-radius: 15px;">
                 <p style="color: #aaa;">System settings go here.</p>
             </div>
        </div>

    </div>

    <script>
        function switchTab(tabName, element) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            element.classList.add('active');
            const titles = { 'dashboard': 'Dashboard', 'users': 'Users', 'licenses': 'Licenses', 'settings': 'Settings' };
            document.getElementById('page-title').innerText = titles[tabName];
        }
    </script>
</body>
</html>
"""

# 3. Qor
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Faylka dashboard.html waa la beddelay si buuxda. Tabs-ka wuu shaqeynayaa.")
