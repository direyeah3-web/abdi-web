import shutil

# 1. Kaydi faylka hore
shutil.copy('index.html', 'index.html.bak')

# 2. Akhri faylka
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Hubi haddii JavaScript-ku uu ku jiro
if "document.getElementById('loginForm')" in c:
    print("✅ JavaScript-ku wuu ku jiraa faylka.")
else:
    print("⚠️ JavaScript-ku kuma jirin faylka. Waan ku dareynaa hadda...")
    js_code = """
    <script>
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault(); 
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const btn = document.querySelector('.btn');
            const workerUrl = 'https://a.dirxx.workers.dev/verify'; 

            btn.innerText = "Checking...";

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
                    }, 2000);
                }
            } catch (error) {
                btn.innerText = "Network Error";
                btn.style.background = "#da3633";
            }
        });
    </script>
</body>
"""
    c = c.replace('</body>', js_code)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("✅ JavaScript-ka waa lagu daray.")
