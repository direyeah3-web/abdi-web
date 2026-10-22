# 1. Akhri faylka
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 2. Qoraalka HTML-ka ee Register-ka
register_html = """
        <!-- Qaybta Register-ka -->
        <div id="register-screen" class="login-form-container">
            <button class="back-btn" onclick="hideRegister()">&#8592;</button>
            
            <div class="text-content" style="text-align: left; margin-bottom: 30px;">
                <h1 style="font-size: 28px;">Register</h1>
                <p>Create an account with your referral code</p>
            </div>

            <form id="registerForm">
                <div class="form-group">
                    <label>Username</label>
                    <input type="text" id="reg-username" placeholder="Choose a username" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" id="reg-password" placeholder="Create a password" required>
                </div>
                <div class="form-group">
                    <label>Referral Code (Waajib)</label>
                    <input type="text" id="reg-referral" placeholder="Enter your special code" required>
                </div>
                <button type="submit" class="btn btn-white submit-btn" id="regBtn">Sign Up</button>
            </form>
        </div>
"""

# Ku dar HTML-ka register-ka
c = c.replace('</div>\n\n    <script>', register_html + '\n    </div>\n\n    <script>')

# 3. Ku dar JavaScript-ka Register-ka
register_js = """
        // 4. Isbeddelka Register-ka
        const registerScreen = document.getElementById('register-screen');

        function showRegister() {
            loginScreen.classList.remove('active');
            setTimeout(() => {
                registerScreen.classList.add('active');
            }, 300);
        }

        function hideRegister() {
            registerScreen.classList.remove('active');
            setTimeout(() => {
                loginScreen.classList.add('active');
            }, 300);
        }

        // 5. Xiriirka Register-ka
        document.getElementById('registerForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('reg-username').value;
            const password = document.getElementById('reg-password').value;
            const referral = document.getElementById('reg-referral').value;
            const btn = document.getElementById('regBtn');

            const MY_REFERRAL_CODE = "ABDI-VIP-2024"; 

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

            btn.innerText = "Creating...";
            
            setTimeout(() => {
                btn.innerText = "Account Created!";
                btn.style.background = "#238636";
                btn.style.color = "#fff";
            }, 1500);
        });
"""

# Ku dar JS-ga
c = c.replace('</script>\n</body>', register_js + '\n    </script>\n</body>')

# Ku dar badhan "Sign Up" oo ku yaal Login-ka (Halkan waxaan ka saaray Don't)
c = c.replace('<button type="submit" class="btn btn-white submit-btn" id="submitBtn">Sign In</button>', 
              '<button type="submit" class="btn btn-white submit-btn" id="submitBtn">Sign In</button>\n                <p style="text-align:center; margin-top:15px; font-size:14px; color:#888;">Do not have an account? <a href="#" onclick="showRegister()" style="color:#fff; text-decoration:underline;">Register</a></p>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Qaybta Register-ka si guul leh ayaa loogu daray!")
