with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Ku dar CSS-ka loo baahan yahay (Password wrapper iyo Icon-ka)
css_addition = """
        .password-wrapper {
            position: relative;
            display: flex;
            align-items: center;
        }
        .password-wrapper input {
            width: 100%;
            padding-right: 45px; /* Meel bannaan oo icon-ka laga dhigo */
        }
        .eye-icon {
            position: absolute;
            right: 15px;
            cursor: pointer;
            color: #888;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: color 0.3s;
        }
        .eye-icon:hover {
            color: #fff;
        }
        .eye-icon svg {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
"""
c = c.replace('</style>', css_addition + '\n    </style>')

# 2. Beddel qaybta Password-ka ee Login-ka
login_pass_old = """<div class="form-group">
                    <label>Password</label>
                    <input type="password" id="password" placeholder="Enter password" required>
                </div>"""
login_pass_new = """<div class="form-group">
                    <label>Password</label>
                    <div class="password-wrapper">
                        <input type="password" id="password" placeholder="Enter password" required>
                        <div class="eye-icon" onclick="togglePassword('password', this)">
                            <svg viewBox="0 0 24 24"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
                        </div>
                    </div>
                </div>"""
c = c.replace(login_pass_old, login_pass_new)

# 3. Beddel qaybta Password-ka ee Register-ka
reg_pass_old = """<div class="form-group">
                    <label>Password</label>
                    <input type="password" id="reg-password" placeholder="Create a password" required>
                </div>"""
reg_pass_new = """<div class="form-group">
                    <label>Password</label>
                    <div class="password-wrapper">
                        <input type="password" id="reg-password" placeholder="Create a password" required>
                        <div class="eye-icon" onclick="togglePassword('reg-password', this)">
                            <svg viewBox="0 0 24 24"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
                        </div>
                    </div>
                </div>"""
c = c.replace(reg_pass_old, reg_pass_new)

# 4. Ku dar JavaScript-ka shaqeeya (Toggle Function)
js_addition = """
        // 6. Shaqada Indhaha (Password Toggle)
        function togglePassword(inputId, iconElement) {
            const input = document.getElementById(inputId);
            if (input.type === "password") {
                input.type = "text";
                iconElement.style.color = "#fff"; // Indhaha oo iftiimaya
            } else {
                input.type = "password";
                iconElement.style.color = "#888"; // Indhaha oo mugdi noqonaya
            }
        }
"""
c = c.replace('</script>\n</body>', js_addition + '\n    </script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Indhaha (Eye Icon) si guul leh ayaa loogu daray Login-ka iyo Register-ka!")
