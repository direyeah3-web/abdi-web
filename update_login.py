import shutil

# Kaydi faylka hore
shutil.copy('index.html', 'index_backup_v1.html')

# Qoraalka HTML, CSS iyo JS cusub (Qaabka sawirkaaga)
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Abdi Web | Welcome</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: #000000;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden; /* Jooji scroll-ka */
        }

        .app-container {
            width: 100%;
            max-width: 400px;
            height: 100vh;
            max-height: 800px;
            display: flex;
            flex-direction: column;
            padding: 30px 20px;
            position: relative;
        }

        /* Qaybta Sare (Logo-ga) */
        .top-bar {
            display: flex;
            justify-content: center;
            padding-top: 20px;
        }
        
        .profile-icon {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background-color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .profile-icon svg { width: 20px; height: 20px; fill: #000; }

        /* Qaybta Dhexe (Animation-ka) */
        .animation-container {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        /* Qoraalka Welcome */
        .text-content {
            text-align: center;
            margin-bottom: 40px;
            transition: all 0.5s ease;
        }

        .text-content h1 {
            font-size: 36px;
            font-weight: 600;
            letter-spacing: -1px;
            margin-bottom: 10px;
        }

        .text-content p {
            color: #888;
            font-size: 15px;
        }

        /* Badhannada (Buttons) */
        .buttons-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-bottom: 30px;
            transition: all 0.5s ease;
        }

        .btn {
            width: 100%;
            padding: 18px;
            border-radius: 30px;
            border: none;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, opacity 0.2s;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }

        .btn:active { transform: scale(0.98); }

        .btn-white {
            background-color: #ffffff;
            color: #000000;
        }

        .btn-dark {
            background-color: #1c1c1e;
            color: #ffffff;
        }

        /* Qaybta Hoose (Terms) */
        .footer-text {
            text-align: center;
            font-size: 11px;
            color: #666;
            line-height: 1.5;
            padding-bottom: 20px;
        }

        .footer-text a {
            color: #aaa;
            text-decoration: underline;
        }

        /* ====== QAABKA LOGIN FORM-KA (Wuxuu soo baxayaa marka la riixo) ====== */
        .login-form-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #000;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            pointer-events: none;
            transform: translateY(20px);
            transition: opacity 0.4s ease, transform 0.4s ease;
            z-index: 10;
        }

        .login-form-container.active {
            opacity: 1;
            pointer-events: auto;
            transform: translateY(0);
        }

        .back-btn {
            position: absolute;
            top: 40px;
            left: 20px;
            background: none;
            border: none;
            color: #fff;
            font-size: 24px;
            cursor: pointer;
        }

        .form-group {
            margin-bottom: 20px;
            position: relative;
        }

        .form-group label {
            display: block;
            font-size: 13px;
            color: #888;
            margin-bottom: 8px;
            margin-left: 10px;
        }

        .form-group input {
            width: 100%;
            padding: 18px;
            border-radius: 15px;
            background-color: #1c1c1e;
            border: 1px solid #333;
            color: #fff;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
        }

        .form-group input:focus {
            border-color: #fff;
        }

        .submit-btn {
            margin-top: 10px;
            background-color: #fff;
            color: #000;
        }

        /* Framer Motion Style Animations */
        .fade-in-up {
            animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Random animated dots (Qaabka sawirka) */
        .dots-animation {
            width: 150px;
            height: 150px;
            position: relative;
        }
        
        .dot {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: float 3s infinite ease-in-out alternate;
        }

        @keyframes float {
            0% { transform: translateY(0px) scale(1); opacity: 0.5; }
            100% { transform: translateY(-10px) scale(1.2); opacity: 1; }
        }

    </style>
</head>
<body>

    <div class="app-container">
        
        <!-- Qaybta Koowaad (Welcome Screen) -->
        <div id="welcome-screen" class="fade-in-up">
            <div class="top-bar">
                <div class="profile-icon">
                    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
                </div>
            </div>

            <div class="animation-container">
                <!-- Halkan waxaan ku daraynaa animation yar oo dots ah si ay u ekaato sawirkaaga -->
                <div class="dots-animation" id="dots"></div>
            </div>

            <div class="text-content">
                <h1>Welcome</h1>
                <p>Your journey starts from here</p>
            </div>

            <div class="buttons-container">
                <button class="btn btn-white" onclick="showLogin()">
                    Continue with Phone
                </button>
                <button class="btn btn-dark">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg>
                    Continue with Apple
                </button>
            </div>

            <div class="footer-text">
                By proceeding you agree <br> to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>
            </div>
        </div>

        <!-- Qaybta Labaad (Login Form-ka casriga ah) -->
        <div id="login-screen" class="login-form-container">
            <button class="back-btn" onclick="hideLogin()">&#8592;</button>
            
            <div class="text-content" style="text-align: left; margin-bottom: 30px;">
                <h1 style="font-size: 28px;">Sign In</h1>
                <p>Enter your credentials to continue</p>
            </div>

            <form id="loginForm">
                <div class="form-group">
                    <label>Username</label>
                    <input type="text" id="username" placeholder="Enter username" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" id="password" placeholder="Enter password" required>
                </div>
                <button type="submit" class="btn btn-white submit-btn" id="submitBtn">Sign In</button>
            </form>
        </div>

    </div>

    <script>
        // 1. Animation dots (Sawirkaaga)
        const dotsContainer = document.getElementById('dots');
        for (let i = 0; i < 40; i++) {
            let dot = document.createElement('div');
            dot.classList.add('dot');
            dot.style.width = Math.random() * 4 + 2 + 'px';
            dot.style.height = dot.style.width;
            dot.style.left = Math.random() * 100 + '%';
            dot.style.top = Math.random() * 100 + '%';
            dot.style.animationDelay = Math.random() * 2 + 's';
            dotsContainer.appendChild(dot);
        }

        // 2. Isbeddelka u dhexeeya Welcome & Login
        const welcomeScreen = document.getElementById('welcome-screen');
        const loginScreen = document.getElementById('login-screen');

        function showLogin() {
            welcomeScreen.style.opacity = '0';
            welcomeScreen.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                welcomeScreen.style.display = 'none';
                loginScreen.classList.add('active');
            }, 300);
        }

        function hideLogin() {
            loginScreen.classList.remove('active');
            setTimeout(() => {
                welcomeScreen.style.display = 'block';
                welcomeScreen.style.opacity = '1';
                welcomeScreen.style.transform = 'translateY(0)';
            }, 300);
        }

        // 3. Xiriirka Cloudflare Worker-ka
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const btn = document.getElementById('submitBtn');
            const workerUrl = 'https://a.dirxx.workers.dev/verify';

            btn.innerText = "Checking...";
            btn.style.opacity = '0.7';

            try {
                const response = await fetch(workerUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user: username, key: password })
                });
                
                const data = await response.json();
                
                if (data.status === true) {
                    btn.innerText = "Success!";
                    btn.style.background = "#238636"; 
                    btn.style.color = "#fff";
                    // Halkan ayaad ku dari kartaa koodhka aad u gudbeyso Dashboard-ka
                } else {
                    btn.innerText = "Invalid Key";
                    btn.style.background = "#da3633"; 
                    btn.style.color = "#fff";
                    setTimeout(() => {
                        btn.innerText = "Sign In";
                        btn.style.background = "#fff";
                        btn.style.color = "#000";
                        btn.style.opacity = '1';
                    }, 2000);
                }
            } catch (error) {
                btn.innerText = "Network Error";
                btn.style.background = "#da3633";
                btn.style.color = "#fff";
                setTimeout(() => {
                    btn.innerText = "Sign In";
                    btn.style.background = "#fff";
                    btn.style.color = "#000";
                    btn.style.opacity = '1';
                }, 2000);
            }
        });
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Login-ka cusub ee casriga ah waa lagu guulaystay!")
