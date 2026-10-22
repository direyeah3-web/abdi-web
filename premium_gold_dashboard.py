import shutil

# Backup
try:
    shutil.copy('index.html', 'index.html.twitch_backup')
    print("✅ Backup: index.html.twitch_backup")
except:
    pass

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ABDI VIP | Premium Panel</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-main: #050505;
            --bg-card: #111111;
            --bg-sidebar: #0a0a0a;
            --gold-primary: #f5a623;
            --gold-gradient: linear-gradient(135deg, #f5a623 0%, #e08e1d 100%);
            --text-main: #ffffff;
            --text-muted: #888888;
            --border: #222222;
            --green: #10b981;
            --red: #ef4444;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background: var(--bg-main); color: var(--text-main); display: flex; min-height: 100vh; overflow-x: hidden; }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 10px; }

        /* ================= SIDEBAR ================= */
        .sidebar { width: 260px; background: var(--bg-sidebar); border-right: 1px solid var(--border); display: flex; flex-direction: column; position: fixed; height: 100vh; left: 0; top: 0; z-index: 100; }
        .logo-area { padding: 25px 20px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid var(--border); }
        .logo-icon { width: 36px; height: 36px; background: var(--gold-gradient); border-radius: 8px; display: flex; justify-content: center; align-items: center; color: #000; font-size: 18px; }
        .logo-text h2 { font-size: 18px; font-weight: 700; }
        .logo-text p { font-size: 11px; color: var(--text-muted); }

        .nav-menu { flex: 1; padding: 20px 10px; overflow-y: auto; }
        .nav-item { display: flex; align-items: center; gap: 15px; padding: 14px 15px; border-radius: 10px; color: var(--text-muted); text-decoration: none; font-size: 14px; font-weight: 500; margin-bottom: 5px; transition: 0.3s; }
        .nav-item:hover { color: var(--text-main); background: rgba(255,255,255,0.05); }
        .nav-item.active { background: rgba(245, 166, 35, 0.1); color: var(--gold-primary); border-left: 3px solid var(--gold-primary); border-radius: 0 10px 10px 0; padding-left: 12px; }
        .nav-item i { width: 20px; text-align: center; }

        .premium-box { margin: 20px; padding: 20px; border: 1px solid var(--gold-primary); border-radius: 15px; text-align: center; background: rgba(245, 166, 35, 0.05); box-shadow: 0 0 20px rgba(245, 166, 35, 0.1); }
        .premium-box i { color: var(--gold-primary); font-size: 24px; margin-bottom: 10px; }
        .premium-box h4 { font-size: 16px; color: var(--gold-primary); margin-bottom: 5px; }
        .premium-box p { font-size: 11px; color: var(--text-muted); }

        /* ================= MAIN CONTENT ================= */
        .main-content { flex: 1; margin-left: 260px; padding: 0; display: flex; flex-direction: column; }
        
        /* Top Nav */
        .top-nav { height: 70px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; padding: 0 30px; background: var(--bg-main); position: sticky; top: 0; z-index: 90; }
        .menu-toggle { display: none; font-size: 20px; cursor: pointer; color: var(--text-muted); }
        .nav-right { display: flex; align-items: center; gap: 20px; }
        .status-badge { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--green); background: rgba(16, 185, 129, 0.1); padding: 6px 12px; border-radius: 20px; }
        .status-badge .dot { width: 8px; height: 8px; background: var(--green); border-radius: 50%; }
        .icon-btn { color: var(--text-muted); font-size: 18px; cursor: pointer; position: relative; }
        .icon-btn .badge { position: absolute; top: -5px; right: -5px; background: var(--red); color: #fff; font-size: 9px; width: 14px; height: 14px; display: flex; justify-content: center; align-items: center; border-radius: 50%; }
        .admin-profile { display: flex; align-items: center; gap: 10px; cursor: pointer; }
        .admin-profile img { width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--gold-primary); }

        /* Dashboard Content */
        .dashboard-body { padding: 30px; }
        .page-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 25px; }
        .page-header h1 { font-size: 24px; font-weight: 600; }
        .page-header p { font-size: 13px; color: var(--text-muted); margin-top: 4px; }
        .date-picker { background: var(--bg-card); border: 1px solid var(--border); padding: 8px 15px; border-radius: 8px; font-size: 13px; color: var(--text-main); display: flex; align-items: center; gap: 10px; }

        /* Stats Grid */
        .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 25px; }
        .stat-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 20px; position: relative; overflow: hidden; }
        .stat-card::before { content: ''; position: absolute; top: 0; right: 0; width: 100px; height: 100px; background: radial-gradient(circle, rgba(245,166,35,0.1) 0%, transparent 70%); }
        .stat-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px; }
        .stat-icon { width: 45px; height: 45px; background: rgba(245, 166, 35, 0.1); border-radius: 12px; display: flex; justify-content: center; align-items: center; color: var(--gold-primary); font-size: 20px; }
        .stat-icon.bg-red { background: rgba(239, 68, 68, 0.1); color: var(--red); }
        .stat-value { font-size: 26px; font-weight: 700; margin-bottom: 4px; }
        .stat-title { font-size: 13px; color: var(--text-muted); font-weight: 500; }
        .stat-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 15px; font-size: 12px; }
        .trend-up { color: var(--green); display: flex; align-items: center; gap: 4px; }
        .trend-down { color: var(--red); display: flex; align-items: center; gap: 4px; }
        
        /* Main Chart */
        .main-chart-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 25px; margin-bottom: 25px; }
        .chart-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .chart-header h3 { font-size: 16px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
        .chart-box { height: 200px; width: 100%; position: relative; }
        
        /* Bottom Grid */
        .bottom-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 20px; margin-bottom: 25px; }
        .panel-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 25px; }
        
        /* Table */
        .table-responsive { width: 100%; overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th { text-align: left; padding: 12px; color: var(--text-muted); font-weight: 500; border-bottom: 1px solid var(--border); }
        td { padding: 12px; border-bottom: 1px solid var(--border); }
        .user-cell { display: flex; align-items: center; gap: 10px; }
        .user-avatar { width: 28px; height: 28px; border-radius: 50%; background: #333; display: flex; justify-content: center; align-items: center; font-size: 12px; }
        .status-dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 6px; }
        .status-dot.active { background: var(--green); }
        .status-dot.banned { background: var(--red); }

        /* Donut Chart Area */
        .donut-container { display: flex; align-items: center; justify-content: center; flex-direction: column; }
        .donut-chart { width: 160px; height: 160px; border-radius: 50%; background: conic-gradient(var(--gold-primary) 0% 71%, #333 71% 100%); display: flex; justify-content: center; align-items: center; position: relative; margin-bottom: 20px; }
        .donut-inner { width: 120px; height: 120px; background: var(--bg-card); border-radius: 50%; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        .donut-inner h4 { font-size: 20px; font-weight: 700; }
        .donut-inner p { font-size: 11px; color: var(--text-muted); }
        .legend { display: flex; justify-content: space-between; width: 100%; font-size: 12px; }
        .legend-item { display: flex; align-items: center; gap: 6px; }
        .legend-color { width: 10px; height: 10px; border-radius: 50%; }

        /* Activity List */
        .activity-list { list-style: none; }
        .activity-item { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid var(--border); font-size: 13px; }
        .activity-item:last-child { border-bottom: none; }
        .activity-left { display: flex; align-items: center; gap: 12px; }
        .activity-icon { width: 28px; height: 28px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 12px; }
        .activity-icon.success { background: rgba(16, 185, 129, 0.1); color: var(--green); }
        .activity-icon.warning { background: rgba(239, 68, 68, 0.1); color: var(--red); }
        .activity-icon.info { background: rgba(245, 166, 35, 0.1); color: var(--gold-primary); }
        .activity-time { color: var(--text-muted); font-size: 12px; }

        /* Mobile Bottom Nav */
        .mobile-nav { display: none; }

        /* ================= RESPONSIVE ================= */
        @media (max-width: 1024px) {
            .stats-grid { grid-template-columns: repeat(2, 1fr); }
            .bottom-grid { grid-template-columns: 1fr; }
        }

        @media (max-width: 768px) {
            .sidebar { transform: translateX(-100%); }
            .sidebar.active { transform: translateX(0); }
            .main-content { margin-left: 0; padding-bottom: 70px; }
            .menu-toggle { display: block; }
            .top-nav { padding: 0 15px; }
            .dashboard-body { padding: 15px; }
            .page-header { flex-direction: column; align-items: flex-start; gap: 10px; }
            .stats-grid { grid-template-columns: 1fr; gap: 15px; }
            
            .mobile-nav { display: flex; position: fixed; bottom: 0; left: 0; width: 100%; background: var(--bg-sidebar); border-top: 1px solid var(--border); justify-content: space-around; padding: 10px 0; z-index: 100; }
            .mobile-nav-item { display: flex; flex-direction: column; align-items: center; gap: 4px; font-size: 10px; color: var(--text-muted); text-decoration: none; }
            .mobile-nav-item.active { color: var(--gold-primary); }
            .mobile-nav-item i { font-size: 18px; }
        }
    </style>
</head>
<body>

    <!-- SIDEBAR -->
    <aside class="sidebar" id="sidebar">
        <div class="logo-area">
            <div class="logo-icon"><i class="fa-solid fa-shield-halved"></i></div>
            <div class="logo-text">
                <h2>Abdi VIP</h2>
                <p>Premium Panel</p>
            </div>
        </div>

        <nav class="nav-menu">
            <a href="#" class="nav-item active"><i class="fa-solid fa-house"></i> Dashboard</a>
            <a href="#" class="nav-item"><i class="fa-solid fa-users"></i> Users</a>
            <a href="#" class="nav-item"><i class="fa-solid fa-key"></i> Licenses</a>
            <a href="#" class="nav-item"><i class="fa-solid fa-wallet"></i> Keys</a>
            <a href="#" class="nav-item"><i class="fa-solid fa-clock-rotate-left"></i> Activity Logs</a>
            <a href="#" class="nav-item"><i class="fa-solid fa-gear"></i> Settings</a>
            <a href="#" class="nav-item"><i class="fa-solid fa-cloud"></i> API Status</a>
            <a href="#" class="nav-item" style="margin-top: auto;"><i class="fa-solid fa-arrow-right-from-bracket"></i> Logout</a>
        </nav>

        <div class="premium-box">
            <i class="fa-solid fa-crown"></i>
            <h4>Abdi VIP</h4>
            <p>Your Success<br>Our Priority</p>
        </div>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="main-content">
        
        <!-- TOP NAVIGATION -->
        <header class="top-nav">
            <div class="menu-toggle" onclick="document.getElementById('sidebar').classList.toggle('active')">
                <i class="fa-solid fa-bars"></i>
            </div>
            
            <div class="nav-right">
                <div class="status-badge">
                    <div class="dot"></div> Online
                </div>
                <div class="icon-btn">
                    <i class="fa-regular fa-bell"></i>
                    <span class="badge">3</span>
                </div>
                <div class="admin-profile">
                    <img src="https://ui-avatars.com/api/?name=Admin&background=f5a623&color=000&rounded=true" alt="Admin">
                    <span style="font-size: 13px; font-weight: 500;">Admin <i class="fa-solid fa-chevron-down" style="font-size: 10px; margin-left: 5px;"></i></span>
                </div>
            </div>
        </header>

        <!-- DASHBOARD BODY -->
        <div class="dashboard-body">
            
            <!-- Page Header -->
            <div class="page-header">
                <div>
                    <h1>Dashboard</h1>
                    <p>Welcome back, Admin!</p>
                </div>
                <div class="date-picker">
                    <i class="fa-regular fa-calendar"></i> Oct 22, 2026 <i class="fa-solid fa-chevron-down" style="font-size: 10px;"></i>
                </div>
            </div>

            <!-- STATS GRID -->
            <div class="stats-grid">
                <!-- Card 1 -->
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon"><i class="fa-solid fa-users"></i></div>
                        <i class="fa-solid fa-user" style="color: #333; font-size: 20px;"></i>
                    </div>
                    <div class="stat-value">1,248</div>
                    <div class="stat-title">Total Users</div>
                    <div class="stat-footer">
                        <div class="trend-up"><i class="fa-solid fa-arrow-up"></i> +12% this month</div>
                        <svg width="60" height="20" viewBox="0 0 60 20">
                            <path d="M0 15 Q 10 20, 20 10 T 40 5 T 60 0" fill="none" stroke="var(--gold-primary)" stroke-width="2"/>
                        </svg>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon"><i class="fa-solid fa-key"></i></div>
                        <i class="fa-solid fa-key" style="color: #333; font-size: 20px;"></i>
                    </div>
                    <div class="stat-value">856</div>
                    <div class="stat-title">Active Licenses</div>
                    <div class="stat-footer">
                        <div class="trend-up"><i class="fa-solid fa-arrow-up"></i> +8% this month</div>
                        <svg width="60" height="20" viewBox="0 0 60 20">
                            <path d="M0 18 Q 15 10, 30 15 T 60 0" fill="none" stroke="var(--gold-primary)" stroke-width="2"/>
                        </svg>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon"><i class="fa-solid fa-wallet"></i></div>
                        <i class="fa-solid fa-screwdriver-wrench" style="color: #333; font-size: 20px;"></i>
                    </div>
                    <div class="stat-value">342</div>
                    <div class="stat-title">Available Keys</div>
                    <div class="stat-footer">
                        <div class="trend-up"><i class="fa-solid fa-arrow-up"></i> +15% this month</div>
                        <svg width="60" height="20" viewBox="0 0 60 20">
                            <path d="M0 20 Q 20 0, 40 15 T 60 5" fill="none" stroke="var(--gold-primary)" stroke-width="2"/>
                        </svg>
                    </div>
                </div>

                <!-- Card 4 -->
                <div class="stat-card">
                    <div class="stat-header">
                        <div class="stat-icon bg-red"><i class="fa-regular fa-clock"></i></div>
                        <i class="fa-regular fa-clock" style="color: #333; font-size: 20px;"></i>
                    </div>
                    <div class="stat-value">48</div>
                    <div class="stat-title">Expired Licenses</div>
                    <div class="stat-footer">
                        <div class="trend-down"><i class="fa-solid fa-arrow-down"></i> -6% this month</div>
                        <svg width="60" height="20" viewBox="0 0 60 20">
                            <path d="M0 5 Q 15 15, 30 10 T 60 0" fill="none" stroke="var(--red)" stroke-width="2"/>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- MAIN CHART -->
            <div class="main-chart-card">
                <div class="chart-header">
                    <h3><i class="fa-solid fa-chart-simple" style="color: var(--gold-primary);"></i> User Activity <span style="color: var(--text-muted); font-weight: 400; font-size: 13px;">(Last 7 Days)</span></h3>
                    <div class="date-picker" style="padding: 4px 10px; font-size: 12px;">7 Days <i class="fa-solid fa-chevron-down" style="font-size: 10px;"></i></div>
                </div>
                <!-- SVG Line Chart -->
                <div class="chart-box">
                    <svg width="100%" height="100%" viewBox="0 0 800 200" preserveAspectRatio="none">
                        <defs>
                            <linearGradient id="goldGradient" x1="0" x2="0" y1="0" y2="1">
                                <stop offset="0%" stop-color="rgba(245, 166, 35, 0.3)"/>
                                <stop offset="100%" stop-color="rgba(245, 166, 35, 0)"/>
                            </linearGradient>
                        </defs>
                        <!-- Grid Lines -->
                        <line x1="0" y1="50" x2="800" y2="50" stroke="#222" stroke-width="1"/>
                        <line x1="0" y1="100" x2="800" y2="100" stroke="#222" stroke-width="1"/>
                        <line x1="0" y1="150" x2="800" y2="150" stroke="#222" stroke-width="1"/>
                        
                        <!-- Area under line -->
                        <path d="M0 150 Q 100 100, 200 120 T 400 80 T 600 40 T 800 60 L 800 200 L 0 200 Z" fill="url(#goldGradient)"/>
                        
                        <!-- Line -->
                        <path d="M0 150 Q 100 100, 200 120 T 400 80 T 600 40 T 800 60" fill="none" stroke="var(--gold-primary)" stroke-width="3"/>
                        
                        <!-- Data Points -->
                        <circle cx="0" cy="150" r="5" fill="var(--gold-primary)"/>
                        <circle cx="200" cy="120" r="5" fill="var(--gold-primary)"/>
                        <circle cx="400" cy="80" r="5" fill="var(--gold-primary)"/>
                        <circle cx="600" cy="40" r="5" fill="var(--gold-primary)"/>
                        <circle cx="800" cy="60" r="5" fill="var(--gold-primary)"/>
                    </svg>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 12px; color: var(--text-muted);">
                    <span>Oct 16</span><span>Oct 17</span><span>Oct 18</span><span>Oct 19</span><span>Oct 20</span><span>Oct 21</span><span>Oct 22</span>
                </div>
            </div>

            <!-- BOTTOM GRID -->
            <div class="bottom-grid">
                
                <!-- Recent Users -->
                <div class="panel-card">
                    <div class="chart-header">
                        <h3><i class="fa-solid fa-users" style="color: var(--gold-primary);"></i> Recent Users</h3>
                        <a href="#" style="color: var(--gold-primary); font-size: 12px; text-decoration: none;">View All <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>Username</th>
                                    <th>Status</th>
                                    <th>Joined</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        <div class="user-cell"><div class="user-avatar"><i class="fa-solid fa-user"></i></div> user_789</div>
                                    </td>
                                    <td><span class="status-dot active"></span> Active</td>
                                    <td style="color: var(--text-muted);">2026-10-22 10:24</td>
                                </tr>
                                <tr>
                                    <td>
                                        <div class="user-cell"><div class="user-avatar"><i class="fa-solid fa-user"></i></div> ahmed123</div>
                                    </td>
                                    <td><span class="status-dot active"></span> Active</td>
                                    <td style="color: var(--text-muted);">2026-10-22 09:12</td>
                                </tr>
                                <tr>
                                    <td>
                                        <div class="user-cell"><div class="user-avatar"><i class="fa-solid fa-user"></i></div> mohamed_21</div>
                                    </td>
                                    <td><span class="status-dot banned"></span> Banned</td>
                                    <td style="color: var(--text-muted);">2026-10-21 22:45</td>
                                </tr>
                                <tr>
                                    <td>
                                        <div class="user-cell"><div class="user-avatar"><i class="fa-solid fa-user"></i></div> fatima77</div>
                                    </td>
                                    <td><span class="status-dot active"></span> Active</td>
                                    <td style="color: var(--text-muted);">2026-10-21 18:32</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- License Distribution -->
                <div class="panel-card">
                    <div class="chart-header">
                        <h3><i class="fa-solid fa-key" style="color: var(--gold-primary);"></i> License Distribution</h3>
                    </div>
                    <div class="donut-container">
                        <!-- SVG Donut Chart -->
                        <div style="position: relative; width: 150px; height: 150px; margin-bottom: 20px;">
                            <svg width="100%" height="100%" viewBox="0 0 100 100">
                                <circle cx="50" cy="50" r="40" fill="none" stroke="#222" stroke-width="15"/>
                                <circle cx="50" cy="50" r="40" fill="none" stroke="var(--gold-primary)" stroke-width="15" stroke-dasharray="251.2" stroke-dashoffset="62.8" transform="rotate(-90 50 50)"/>
                            </svg>
                            <div style="position: absolute; top:0; left:0; width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                                <h4 style="font-size: 20px; font-weight: 700; margin:0;">1,200</h4>
                                <p style="font-size: 11px; color: var(--text-muted); margin:0;">Total Licenses</p>
                            </div>
                        </div>
                        <div class="legend">
                            <div class="legend-item"><div class="legend-color" style="background: var(--gold-primary);"></div> Active</div>
                            <div class="legend-item"><div class="legend-color" style="background: #e08e1d;"></div> Used</div>
                            <div class="legend-item"><div class="legend-color" style="background: #333;"></div> Expired</div>
                        </div>
                        <div style="display:flex; justify-content:space-between; width:100%; font-size:11px; color:var(--text-muted); margin-top:5px;">
                            <span>856 (71%)</span>
                            <span>298 (25%)</span>
                            <span>48 (4%)</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- LATEST ACTIVITY -->
            <div class="panel-card">
                <div class="chart-header">
                    <h3><i class="fa-regular fa-clock" style="color: var(--gold-primary);"></i> Latest Activity</h3>
                    <a href="#" style="color: var(--gold-primary); font-size: 12px; text-decoration: none;">View All <i class="fa-solid fa-arrow-right"></i></a>
                </div>
                <ul class="activity-list">
                    <li class="activity-item">
                        <div class="activity-left">
                            <div class="activity-icon success"><i class="fa-solid fa-check"></i></div>
                            <span>New license generated for user_789</span>
                        </div>
                        <div class="activity-time">Oct 22, 2026 10:24</div>
                    </li>
                    <li class="activity-item">
                        <div class="activity-left">
                            <div class="activity-icon info"><i class="fa-solid fa-user"></i></div>
                            <span>User ahmed123 logged in</span>
                        </div>
                        <div class="activity-time">Oct 22, 2026 09:12</div>
                    </li>
                    <li class="activity-item">
                        <div class="activity-left">
                            <div class="activity-icon warning"><i class="fa-solid fa-triangle-exclamation"></i></div>
                            <span>License expired for user mohamed_21</span>
                        </div>
                        <div class="activity-time">Oct 21, 2026 22:45</div>
                    </li>
                    <li class="activity-item">
                        <div class="activity-left">
                            <div class="activity-icon success"><i class="fa-solid fa-key"></i></div>
                            <span>Key used by fatima77</span>
                        </div>
                        <div class="activity-time">Oct 21, 2026 18:32</div>
                    </li>
                </ul>
            </div>

        </div>
    </main>

    <!-- MOBILE BOTTOM NAV -->
    <nav class="mobile-nav">
        <a href="#" class="mobile-nav-item active"><i class="fa-solid fa-house"></i> Home</a>
        <a href="#" class="mobile-nav-item"><i class="fa-solid fa-users"></i> Users</a>
        <a href="#" class="mobile-nav-item"><i class="fa-solid fa-key"></i> Licenses</a>
        <a href="#" class="mobile-nav-item"><i class="fa-solid fa-wallet"></i> Keys</a>
        <a href="#" class="mobile-nav-item"><i class="fa-solid fa-ellipsis"></i> More</a>
    </nav>

</body>
</html>
"""

# Qor faylka
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Dashboard-ka Premium Gold waa la abuuray!")
