import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Waxaan tirtiraynaa dhammaan JavaScript-kii hore si aan u beddelno mid cusub oo nadiif ah
c = re.sub(r'<script>.*?</script>', '<script>\n// FINAL AUTH SCRIPT\n</script>', c, flags=re.DOTALL)

# 2. Ku darista JavaScript-ka rasmiga ah ee ammaan ah
final_js = """
        // Navigation
        const welcomeScreen = document.getElementById('welcome-screen');
        const loginScreen = document.getElementById('login-screen');
        const registerScreen = document.getElementById('register-screen');

        function showLogin() { welcomeScreen.style.display = 'none'; loginScreen.classList.add('active'); }
        function hideLogin() { loginScreen.classList.remove('active'); setTimeout(() => { welcomeScreen.style.display = 'block'; }, 300); }
        function showRegister() { loginScreen.classList.remove('active'); setTimeout(() => { registerScreen.classList.add('active'); }, 300); }
        function hideRegister() { registerScreen.classList.remove('active'); setTimeout(() => { loginScreen.classList.add('active'); }, 300); }

        function togglePassword(inputId, iconElement) {
            const input = document.getElementById(inputId);
            if (input.type === "password") { input.type = "text"; iconElement.style.color = "#fff"; } 
            else { input.type = "password"; iconElement.style.color = "#888"; }
        }

        // ==========================================
        // NIDAAMKA REGISTER-KA (Wuxuu xogta ku kaydiyaa localStorage)
        // ==========================================
        document.getElementById('registerForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('reg-username').value.trim();
            const password = document.getElementById('reg-password').value;
            const referral = document.getElementById('reg-referral').value.trim();
            const btn = document.getElementById('regBtn');

            // 1. Hubi Referral Code-ka
            if (referral !== "ABDI-VIP-2024") {
                btn.innerText = "Invalid Referral Code!";
                btn.style.background = "#da3633"; btn.style.color = "#fff";
                setTimeout(() => { btn.innerText = "Sign Up"; btn.style.background = "#fff"; btn.style.color = "#000"; }, 2000);
                return;
            }

            // 2. Hubi haddii User-ku horey u jiray
            if (localStorage.getItem('user_' + username)) {
                btn.innerText = "Username already exists!";
                btn.style.background = "#da3633"; btn.style.color = "#fff";
                setTimeout(() => { btn.innerText = "Sign Up"; btn.style.background = "#fff"; btn.style.color = "#000"; }, 2000);
                return;
            }

            btn.innerText = "Creating...";
            
            // 3. Kaydi xogta
            setTimeout(() => {
                localStorage.setItem('user_' + username, password);
                btn.innerText = "Account Created!";
                btn.style.background = "#238636"; btn.style.color = "#fff";
                
                setTimeout(() => {
                    hideRegister();
                    document.getElementById('login-username').value = username;
                    btn.innerText = "Sign Up"; btn.style.background = "#fff"; btn.style.color = "#000";
                }, 1500);
            }, 800);
        });

        // ==========================================
        // NIDAAMKA LOGIN-KA (Waa inuu ku xirmayaa xogta rasmiga ah)
        // ==========================================
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('login-username').value.trim();
            const password = document.getElementById('login-password').value;
            const btn = document.getElementById('loginBtn');

            btn.innerText = "Checking...";
            btn.style.opacity = '0.7';

            setTimeout(() => {
                const storedPassword = localStorage.getItem('user_' + username);
                
                // Haddii uu jiro user-ka oo password-ku sax yahay
                if (storedPassword && storedPassword === password) {
                    btn.innerText = "Success!";
                    btn.style.background = "#238636"; btn.style.color = "#fff"; btn.style.opacity = '1';
                    // Kaydi xogta qofka galay si Dashboard-ku u ogaado
                    localStorage.setItem('currentUser', username); 
                    setTimeout(() => { window.location.href = 'dashboard.html'; }, 800);
                } else {
                    // Haddii uusan jirin ama password-ku khaldan yahay
                    btn.innerText = "Invalid Credentials!";
                    btn.style.background = "#da3633"; btn.style.color = "#fff"; btn.style.opacity = '1';
                    setTimeout(() => { btn.innerText = "Sign In"; btn.style.background = "#fff"; btn.style.color = "#000"; }, 2000);
                }
            }, 800);
        });
"""
c = c.replace('// FINAL AUTH SCRIPT', final_js)

# 3. Ku dar Version cusub si browser-ku u arko isbeddelka (Cache Busting)
if '<meta charset="UTF-8">' in c:
    c = c.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n    <meta http-equiv="Pragma" content="no-cache">\n    <meta http-equiv="Expires" content="0">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Nidaamka ammaanka ah waa lagu daray! Fadlan nadiifi Cache-ka.")
