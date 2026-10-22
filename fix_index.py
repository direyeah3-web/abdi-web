import shutil

# 1. Kaydi (Backup) faylka hore
shutil.copy('index.html', 'index.html.backup')

# 2. Akhri faylka
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Qoraalka cusub ee JavaScript-ka ah ee lagu dari doono </body>
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

# 4. Beddel </body> oo dhig koodhka cusub
c = c.replace('</body>', js_code)

# 5. Dib u qor faylka
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('✅ JavaScript-ka si guul leh ayaa loogu daray index.html')
