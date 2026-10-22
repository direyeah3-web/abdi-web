with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Marka Success la gaaro, u dir Dashboard-ka
old_success = """btn.innerText = "Success!";
                            btn.style.background = "#238636"; 
                            btn.style.color = "#fff";"""
new_success = """btn.innerText = "Success!";
                            btn.style.background = "#238636"; 
                            btn.style.color = "#fff";
                            setTimeout(() => {
                                window.location.href = 'dashboard.html';
                            }, 1000);"""

c = c.replace(old_success, new_success)

# Marka Account Created la gaaro, u dir Login-ka
old_created = """btn.innerText = "Account Created!";
                btn.style.background = "#238636";
                btn.style.color = "#fff";"""
new_created = """btn.innerText = "Account Created!";
                btn.style.background = "#238636";
                btn.style.color = "#fff";
                setTimeout(() => {
                    hideRegister();
                    document.getElementById('username').value = document.getElementById('reg-username').value;
                }, 1500);"""

c = c.replace(old_created, new_created)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Isku xirka Login-ka iyo Dashboard-ka waa la sameeyay!")
