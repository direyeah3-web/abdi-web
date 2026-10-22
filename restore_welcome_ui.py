import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Ka saar "Cache-Control" Meta tags-ka aan ku darnay (sababtoo ah waxay sawirka xumeeyeen)
c = re.sub(r'<meta http-equiv="Cache-Control".*?>\n', '', c)
c = re.sub(r'<meta http-equiv="Pragma".*?>\n', '', c)
c = re.sub(r'<meta http-equiv="Expires".*?>\n', '', c)

# 2. Soo celi Qaabka Welcome-ka (Husky dots iyo badhannada)
welcome_html = """
        <!-- WELCOME SCREEN -->
        <div id="welcome-screen" class="fade-in-up">
            <div class="top-bar">
                <div class="profile-icon">
                    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
                </div>
            </div>

            <div class="animation-container">
                <div class="dots-animation" id="dots"></div>
            </div>

            <div class="text-content">
                <h1>Welcome</h1>
                <p>Your journey starts from here</p>
            </div>

            <div class="buttons-container">
                <button class="btn btn-white" onclick="showLogin()">Horay u soco</button>
                <button class="btn btn-dark">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701"/></svg>
                    Continue
                </button>
            </div>

            <div class="footer-text">
                By proceeding you agree <br> to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>
            </div>
        </div>
"""

# Beddel qaybta Welcome-ka ee hadda jirta
pattern = r'<!-- WELCOME SCREEN -->.*?</div>\s*<!-- LOGIN FORM -->'
c = re.sub(pattern, welcome_html + '\n        <!-- LOGIN FORM -->', c, flags=re.DOTALL)

# 3. Ku dar koodhka Animation-ka Dots-ka (maadaama aan tirtirnay JS-gii hore)
dots_js = """
        // Animation Dots (Sawirkaaga)
        const dotsContainer = document.getElementById('dots');
        if (dotsContainer) {
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
        }
"""
# Ku dar JS-ga dots-ka ka hor amarka kale
c = c.replace('// Navigation', dots_js + '\n        // Navigation')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Qaabkii hore ee Welcome-ka waa la soo celiyay, Login-kuna wuu shaqeynayaa!")
