dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdi Web | Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: #0d1117;
            color: #c9d1d9;
            display: flex;
            min-height: 100vh;
        }

        /* Sidebar-ka Bidix */
        .sidebar {
            width: 260px;
            background-color: #161b22;
            border-right: 1px solid #30363d;
            padding: 20px;
            display: flex;
            flex-direction: column;
        }

        .user-profile {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #30363d;
        }

        .user-avatar {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #58a6ff, #1f6feb);
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            color: white;
        }

        .nav-menu {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .nav-item {
            padding: 12px 15px;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            color: #8b949e;
            transition: 0.3s;
        }

        .nav-item:hover, .nav-item.active {
            background-color: #21262d;
            color: #ffffff;
        }

        /* Qaybta Midig (Content) */
        .main-content {
            flex: 1;
            padding: 30px;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }

        .welcome-banner {
            background: linear-gradient(90deg, #1f6feb22, #388bfd22);
            border: 1px solid #1f6feb55;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
        }

        .welcome-banner h2 {
            color: #ffffff;
            margin-bottom: 5px;
        }

        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 20px;
            border-radius: 12px;
        }

        .stat-card h3 {
            font-size: 24px;
            color: #ffffff;
            margin-bottom: 5px;
        }

        .stat-card p {
            font-size: 13px;
            color: #8b949e;
        }

        /* Quick Actions */
        .actions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .action-btn {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 20px;
            border-radius: 12px;
            cursor: pointer;
            text-align: left;
            color: #c9d1d9;
            font-size: 15px;
            font-weight: 500;
            transition: 0.3s;
        }

        .action-btn:hover {
            border-color: #58a6ff;
            background-color: #21262d;
        }
    </style>
</head>
<body>

    <!-- Sidebar-ka -->
    <div class="sidebar">
        <div class="user-profile">
            <div class="user-avatar">A</div>
            <div>
                <h4 style="color: white;">ABDI VIP</h4>
                <p style="font-size: 12px; color: #8b949e;">Administrator</p>
            </div>
        </div>

        <ul class="nav-menu">
            <li class="nav-item active">🏠 Dashboard</li>
            <li class="nav-item">👥 Users</li>
            <li class="nav-item">🔑 Licenses</li>
            <li class="nav-item">⚙️ Settings</li>
        </ul>
    </div>

    <!-- Qaybta Content-ka -->
    <div class="main-content">
        <div class="header">
            <h1 style="color: white;">Dashboard</h1>
            <button class="action-btn" style="padding: 10px 20px;" onclick="logout()">Logout</button>
        </div>

        <div class="welcome-banner">
            <h2>Welcome back, Abdi!</h2>
            <p>You are in control. Here is what is happening with your panel today.</p>
        </div>

        <!-- Stats -->
        <div class="stats-grid">
            <div class="stat-card">
                <h3>1</h3>
                <p>Total Users</p>
            </div>
            <div class="stat-card">
                <h3>2</h3>
                <p>Total Licenses</p>
            </div>
            <div class="stat-card">
                <h3>1</h3>
                <p>Available Keys</p>
            </div>
            <div class="stat-card">
                <h3>0</h3>
                <p>Referrals</p>
            </div>
        </div>

        <h3 style="color: white; margin-bottom: 15px;">Quick Actions</h3>
        <div class="actions-grid">
            <button class="action-btn">🔑 Generate New License</button>
            <button class="action-btn">👤 Add New User</button>
            <button class="action-btn">📊 View Analytics</button>
            <button class="action-btn">⚙️ System Settings</button>
        </div>
    </div>

    <script>
        function logout() {
            // Halkan waxaan ku celinaynaa bogga Login-ka
            window.location.href = 'index.html';
        }
    </script>
</body>
</html>
"""

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dashboard_html)

print("✅ Faylka Dashboard-ka cusub waa la abuuray!")
