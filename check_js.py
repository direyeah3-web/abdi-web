with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Waxaan hubineynaa haddii xariiqda muhiimka ah ee JS-ka ay ku jirto
if "e.preventDefault();" in c:
    print("✅ JavaScript-ku si fiican ayuu ugu jiraa faylka.")
else:
    print("❌ JavaScript-ku kuma jiro ama wuu qaldan yahay. Waan ku dareynaa hadda...")
    
    # Haddii uusan ku jirin, waxaan ku dareynaa qaybta ugu dambaysa </body>
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
