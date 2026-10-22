import shutil

# 1. Backup
try:
    shutil.copy('index.html', 'index.html.old_backup')
    print("✅ Backup: index.html.old_backup")
except:
    pass

# 2. HTML-ka Cusub (Exact Match to Image)
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | ABDI VIP</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            /* Background Colors */
            --bg-dark: #1c1c1e;
            --bg-panel: rgba(30, 30, 32, 0.6);
            --bg-rail: rgba(20, 20, 22, 0.8);
            --bg-hover: rgba(255, 255, 255, 0.08);
            --bg-active: rgba(255, 255, 255, 0.15);
            
            /* Text Colors */
            --text-main: #ffffff;
            --text-muted: #8e8e93;
            --text-dark: #1c1c1e;
            
            /* Accents */
            --green: #30d158;
            --border: rgba(255, 255, 255, 0.1);
            
            /* Glass */
            --blur: blur(30px);
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', -apple-system, sans-serif; }
        
        body { 
            background: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop') no-repeat center center fixed; 
            background-size: cover;
            color: var(--text-main); 
            display: flex; 
            height: 100vh; 
            overflow: hidden; 
            -webkit-font-smoothing: antialiased;
        }

        /* Background Overlay for dark effect */
        body::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.4); z-index: -1;
        }

        /* 1. FAR LEFT RAIL */
        .rail { 
            width: 70px; 
            background: var(--bg-rail); 
            backdrop-filter: var(--blur);
            border-right: 1px solid var(--border);
            display: flex; flex-direction: column; align-items: center; padding: 20px 0; gap: 20px; z-index: 10;
        }
        .rail-icon { 
            width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
            color: var(--text-muted); font-size: 18px; cursor: pointer; transition: 0.2s;
        }
        .rail-icon:hover, .rail-icon.active { background: var(--bg-hover); color: var(--text-main); }
        .rail-icon.active { background: #ffffff; color: #000; }
        .rail-spacer { flex: 1; }

        /* 2. MIDDLE SIDEBAR */
        .sidebar { 
            width: 320px; 
            background: var(--bg-panel); 
            backdrop-filter: var(--blur);
            border-right: 1px solid var(--border);
            display: flex; flex-direction: column; padding: 30px 20px; overflow-y: auto;
        }
        
        /* Profile Section */
        .profile { display: flex; align-items: center; gap: 15px; margin-bottom: 30px; cursor: pointer; }
        .profile img { width: 45px; height: 45px; border-radius: 50%; object-fit: cover; border: 2px solid rgba(255,255,255,0.2); }
        .profile-info h3 { font-size: 15px; font-weight: 600; margin-bottom: 2px; }
        .profile-info p { font-size: 12px; color: var(--text-muted); }

        /* Menu Groups */
        .menu-group { margin-bottom: 25px; }
        .menu-title { font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; padding-left: 10px; }
        .menu-item { 
            display: flex; align-items: center; justify-content: space-between; padding: 10px; border-radius: 10px; 
            font-size: 14px; font-weight: 500; color: var(--text-muted); cursor: pointer; transition: 0.2s; margin-bottom: 2px;
        }
        .menu-item:hover { background: var(--bg-hover); color: var(--text-main); }
        .menu-item.active { background: var(--bg-active); color: var(--text-main); box-shadow: inset 0 1px 0 rgba(255,255,255,0.1); }
        .menu-item-left { display: flex; align-items: center; gap: 12px; }
        .menu-item i { width: 16px; text-align: center; font-size: 16px; }
        .badge { background: var(--bg-hover); padding: 2px 8px; border-radius: 10px; font-size: 12px; }

        /* Folder Tree (Documents) */
        .folder-tree { padding-left: 10px; margin-top: 10px; }
        .folder-item { display: flex; align-items: center; gap: 10px; padding: 8px; font-size: 13px; color: var(--text-muted); cursor: pointer; border-radius: 8px; }
        .folder-item:hover { background: var(--bg-hover); color: var(--text-main); }
        .folder-item i { color: #ffcc00; }
        .folder-children { padding-left: 20px; border-left: 1px solid var(--border); margin-left: 15px; }

        /* 3. MAIN CONTENT (Right Side) */
        .main { 
            flex: 1; 
            padding: 40px; 
            overflow-y: auto; 
            display: flex; 
            flex-direction: column;
        }
        
        /* Top Header */
        .main-header { margin-bottom: 30px; }
        .main-header h1 { font-size: 28px; font-weight: 600; letter-spacing: -0.5px; margin-bottom: 5px; }
        .main-header p { font-size: 14px; color: var(--text-muted); }

        /* Grid Layout */
        .dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 25px; }
        
        /* Cards */
        .glass-card { 
            background: var(--bg-panel); 
            backdrop-filter: var(--blur);
            border: 1px solid var(--border); 
            border-radius: 24px; 
            padding: 25px; 
            box-shadow: var(--shadow);
            display: flex; flex-direction: column;
        }

        /* Execution Card */
        .execution-card { grid-column: 1 / -1; flex-direction: row; justify-content: space-between; align-items: center; }
        .execution-info h3 { font-size: 16px; font-weight: 500; color: var(--text-muted); margin-bottom: 10px; }
        .execution-info .number { font-size: 64px; font-weight: 600; letter-spacing: -2px; display: flex; align-items: flex-start; gap: 10px; }
        .execution-info .number span { font-size: 16px; color: var(--green); background: rgba(48, 209, 88, 0.15); padding: 4px 10px; border-radius: 20px; font-weight: 600; margin-top: 10px; display: flex; align-items: center; gap: 5px;}
        
        .btn-report { 
            background: var(--bg-hover); color: var(--text-main); border: 1px solid var(--border); 
            padding: 12px 20px; border-radius: 14px; font-size: 14px; font-weight: 500; cursor: pointer; 
            display: flex; align-items: center; gap: 8px; transition: 0.2s;
        }
        .btn-report:hover { background: var(--bg-active); }

        /* Tabs */
        .tabs { display: flex; gap: 20px; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 10px; }
        .tab { font-size: 14px; font-weight: 500; color: var(--text-muted); cursor: pointer; padding-bottom: 10px; margin-bottom: -11px; }
        .tab.active { color: var(--text-main); border-bottom: 2px solid var(--text-main); }

        /* Search */
        .search-box { 
            background: rgba(0,0,0,0.2); border: 1px solid var(--border); border-radius: 12px; 
            padding: 12px 15px; display: flex; align-items: center; gap: 10px; margin-bottom: 20px;
        }
        .search-box input { background: transparent; border: none; color: var(--text-main); outline: none; width: 100%; font-size: 14px; }
        .search-box i { color: var(--text-muted); }

        /* Empty State Box */
        .empty-box { flex: 1; background: rgba(0,0,0,0.1); border-radius: 16px; border: 1px dashed var(--border); min-height: 200px; display: flex; align-items: center; justify-content: center; color: var(--text-muted); font-size: 14px; }

        /* Responsive */
        @media (max-width: 900px) {
            .dashboard-grid { grid-template-columns: 1fr; }
            .sidebar { width: 250px; }
        }
        @media (max-width: 768px) {
            .rail { display: none; }
            .sidebar { display: none; } /* Mobile-ka sidebar-ka wuu qarsoonaanayaa sida app-ka oo kale */
            .main { padding: 20px; }
            .execution-card { flex-direction: column; align-items: flex-start; gap: 20px; }
        }
    </style>
</head>
<body>

    <!-- 1. RAIL NAVIGATION (Far Left) -->
    <nav class="rail">
        <div class="rail-icon"><i class="fa-solid fa-bolt"></i></div>
        <div class="rail-icon active"><i class="fa-solid fa-house"></i></div>
        <div class="rail-icon"><i class="fa-solid fa-chart-pie"></i></div>
        <div class="rail-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
        <div class="rail-icon"><i class="fa-solid fa-share-nodes"></i></div>
        <div class="rail-icon"><i class="fa-solid fa-folder"></i></div>
        <div class="rail-icon"><i class="fa-solid fa-box"></i></div>
        <div class="rail-spacer"></div>
        <div class="rail-icon"><i class="fa-solid fa-gear"></i></div>
    </nav>

    <!-- 2. SIDEBAR PANEL (Middle Left) -->
    <aside class="sidebar">
        <!-- Profile -->
        <div class="profile">
            <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?q=80&w=100&auto=format&fit=crop" alt="Profile">
            <div class="profile-info">
                <h3>John Doe</h3>
                <p>customerpop@gmail.com</p>
            </div>
        </div>

        <!-- Projects -->
        <div class="menu-group">
            <div class="menu-title">Projects</div>
            <div class="menu-item active">
                <div class="menu-item-left"><i class="fa-solid fa-diagram-project"></i> Dashboard</div>
                <span class="badge">0</span>
            </div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-layer-group"></i> Library</div>
            </div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-folder-open"></i> Shared Projects</div>
            </div>
        </div>

        <!-- Status -->
        <div class="menu-group">
            <div class="menu-title">Status</div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-circle-dot"></i> New</div>
                <span class="badge">3</span>
            </div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-bell"></i> Updates</div>
                <span class="badge">2</span>
            </div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-users"></i> Team Review</div>
            </div>
        </div>

        <!-- History -->
        <div class="menu-group">
            <div class="menu-title">History</div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-clock-rotate-left"></i> Recently Edited</div>
            </div>
            <div class="menu-item">
                <div class="menu-item-left"><i class="fa-solid fa-box-archive"></i> Archive</div>
            </div>
        </div>

        <!-- Documents (Tree) -->
        <div class="menu-group">
            <div class="menu-title" style="display:flex; justify-content:space-between; align-items:center;">
                Documents <i class="fa-solid fa-plus" style="cursor:pointer;"></i>
            </div>
            <div class="search-box" style="padding: 8px 12px; margin-bottom: 10px;">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" placeholder="Search">
            </div>
            
            <div class="folder-tree">
                <div class="folder-item" style="color: var(--text-main); font-weight: 500;">
                    <i class="fa-solid fa-folder" style="color: #ffcc00;"></i> System Management's
                    <span class="badge" style="margin-left:auto;">12</span>
                </div>
                <div class="folder-children">
                    <div class="folder-item"><i class="fa-solid fa-folder" style="color: #ffcc00;"></i> 2025 Update's <span class="badge" style="margin-left:auto;">2</span></div>
                    <div class="folder-children">
                        <div class="folder-item"><i class="fa-solid fa-file-lines"></i> Hiring Process <span class="badge" style="margin-left:auto;">4</span></div>
                        <div class="folder-item"><i class="fa-solid fa-file-lines"></i> Billing Process <span class="badge" style="margin-left:auto;">3</span></div>
                    </div>
                    <div class="folder-item active" style="background:var(--bg-hover); color:#fff;"><i class="fa-solid fa-folder-open" style="color: #ffcc00;"></i> Fundamentals <span class="badge" style="margin-left:auto;">4</span></div>
                    <div class="folder-item"><i class="fa-solid fa-folder" style="color: #ffcc00;"></i> Off Grid Servers <span class="badge" style="margin-left:auto;">5</span></div>
                </div>
            </div>
        </div>
    </aside>

    <!-- 3. MAIN DASHBOARD (Right) -->
    <main class="main">
        <header class="main-header">
            <h1>Dashboard</h1>
            <p>All Your Workflows And Permissions</p>
        </header>

        <div class="dashboard-grid">
            <!-- Executions Card -->
            <div class="glass-card execution-card">
                <div class="execution-info">
                    <h3>Executions</h3>
                    <div class="number">
                        340
                        <span><i class="fa-solid fa-arrow-up"></i> 2%</span>
                    </div>
                </div>
                <button class="btn-report">See Report <i class="fa-solid fa-arrow-right"></i></button>
            </div>

            <!-- Workflows Card (Bottom Left) -->
            <div class="glass-card">
                <h3 style="font-size: 20px; font-weight: 600; margin-bottom: 20px;">Executions</h3>
                <div class="tabs">
                    <div class="tab active">Workflows</div>
                    <div class="tab">Permissions</div>
                </div>
                <div class="search-box">
                    <i class="fa-solid fa-magnifying-glass"></i>
                    <input type="text" placeholder="Search">
                </div>
                <div class="empty-box">
                    <!-- Empty state area as seen in image -->
                </div>
            </div>

            <!-- Placeholder for Right Side (If needed, based on original image) -->
            <div class="glass-card" style="background: transparent; border: none; box-shadow: none; padding: 0;">
                <!-- This area is blank in the reference image, but we keep the grid structure -->
            </div>
        </div>
    </main>

</body>
</html>
"""

# 3. Qor faylka
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Dashboard-ka saxda ah (Glassmorphism) waa la abuuray!")
