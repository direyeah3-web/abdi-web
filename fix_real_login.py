import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Waxaan tirtiraynaa koodhkii hore ee JavaScript-ka (si aan u beddelno mid cusub)
# Waxaan raadinaynaa bilowga <script> ilaa dhammaadka </script>
c = re.sub(r'<script>.*?</script>', '<script>\n// JS-ga cusub ayaa hoos ku yaal\n</script>', c, flags=re.DOTALL)

# 2. Ku darista JavaScript-ka cusub ee Login & Register
js_logic = """
        // Nidaamka Register-ka (Wuxuu xogta ku kaydiyaa localStorage)
        document.getElementById('registerForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('reg-username').value;
            const password = document.getElementById('reg-password').value;
            const referral = document.getElementById('reg-referral').value;
            const btn = document.getElementById('regBtn');

            const MY_REFERRAL_CODE = "ABDI-VIP-2024"; 

            // 1. Hubi Referral Code-ka
            if (referral !== MY_REFERRAL_CODE) {
                btn.innerText = "Invalid Referral Code!";
                btn.style.background = "#da3633";
                btn.style.color = "#fff";
                setTimeout(() => {
                    btn.innerText = "Sign Up";
                    btn.style.background = "#fff";
                    btn.style.color = "#000";
                }, 2000);
                return;
            }

            // 2. Hubi haddii User-ku horey u jiray
            if (localStorage.getItem('user_' + username)) {
                btn.innerText = "Username already exists!";
                btn.style.background = "#da3633";
                btn.style.color = "#fff";
                setTimeout(() => {
                    btn.innerText = "Sign Up";
                    btn.style.background = "#fff";
                    btn.style.color = "#000";
                }, 2000);
                return;
            }

            btn.innerText = "Creating...";
            
            // 3. Kaydi xogta isticmaalaha cusub
            setTimeout(() => {
                localStorage.setItem('user_' + username, password);
                btn.innerText = "Account Created!";
                btn.style.background = "#238636";
                btn.style.color = "#fff";
                
                setTimeout(() => {
                    // Ku celi Login-ka oo ku buuxi username-ka
                    hideRegister();
                    document.getElementById('username').value = username;
                    btn.innerText = "Sign Up";
                    btn.style.background = "#fff";
                    btn.style.color = "#000";
                }, 1500);
            }, 1000);
        });

        // Nidaamka Login-ka (Wuxuu hubinayaa localStorage)
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const btn = document.getElementById('submitBtn');

            btn.innerText = "Checking...";
            btn.style.opacity = '0.7';

            // Hubi xogta isticmaalaha
            const storedPassword = localStorage.getItem('user_' + username);

            setTimeout(() => {
                if (storedPassword && storedPassword === password) {
                    // Waa sax!
                    btn.innerText = "Success!";
                    btn.style.background = "#238636"; 
                    btn.style.color = "#fff";
                    btn.style.opacity = '1';
                    
                    setTimeout(() => {
                        window.location.href = 'dashboard.html';
                    }, 800);
                } else {
                    // Waa khalad!
                    btn.innerText = "Invalid Credentials!";
                    btn.style.background = "#da3633"; 
                    btn.style.color = "#fff";
                    btn.style.opacity = '1';
                    setTimeout(() => {
                        btn.innerText = "Sign In";
                        btn.style.background = "#fff";
                        btn.style.color = "#000";
                    }, 2000);
                }
            }, 1000);
        });
"""

# Ku dar JS-ga cusub ka hor </script>
c = c.replace('// JS-ga cusub ayaa hoos ku yaal', js_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Nidaamka Login & Register-ka dhabta ah waa lagu daray!")
