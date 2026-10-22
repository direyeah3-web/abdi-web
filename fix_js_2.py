import shutil

# 1. Kaydi faylka hadda jira
shutil.copy('index.html', 'index_backup.html')

# 2. Akhri faylka
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Qoraalka cusub ee JS-ka (oo leh qoraal taxaddar leh)
js_code = """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const form = document.getElementById('loginForm');
            if (form) {
                form.addEventListener('submit', async function(e) {
                    e.preventDefault(); 
                    const username = document.getElementById('username').value;
                    const password = document.getElementById('password').value;
                    const btn = document.querySelector('.btn');
                    const workerUrl = 'https://a.dirxx.workers.dev/verify'; 

                    btn.innerText = "Checking...";
                    btn.disabled = true; // Jooji inuu laba jeer riixo

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
                        } else {
                            btn.innerText = "Invalid Key";
                            btn.style.background = "#da3633"; 
                            setTimeout(() => {
                                btn.innerText = "Sign In";
                                btn.style.background = "linear-gradient(90deg, #1f6feb, #388bfd)";
                                btn.disabled = false;
                            }, 2000);
                        }
                    } catch (error) {
                        btn.innerText = "Network Error";
                        btn.style.background = "#da3633";
                        setTimeout(() => {
                            btn.innerText = "Sign In";
                            btn.style.background = "linear-gradient(90deg, #1f6feb, #388bfd)";
                            btn.disabled = false;
                        }, 2000);
                    }
                });
            } else {
                console.error("Form-ka loginForm lama helin!");
            }
        });
    </script>
</body>
"""

# 4. Tirtir JS-kii hore haddii uu jiro, kadibna ku dar kan cusub
if "<script>" in c:
    # Haddii uu jiro script hore, ka tirtir inta u dhaxaysa <script> iyo </script>
    import re
    c = re.sub(r'<script>.*?</script>', '', c, flags=re.DOTALL)

# Ku dar kan cusub
c = c.replace('</body>', js_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ JavaScript-ka cusub waa lagu beddelay kii hore.")
