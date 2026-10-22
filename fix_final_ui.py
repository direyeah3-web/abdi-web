import requests
import shutil
import os

# 1. Kaydi faylka hadda jira
if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_backup_final.html')

print("Fadlan sug, faylka quruxda badan ayaa la soo dejinayaa...")

# 2. Soo dejiso faylka quruxda badan (oo ku jira GitHub-kaaga hore)
url = "https://raw.githubusercontent.com/direyeah3-web/abdi-web/main/dashboard.html"
response = requests.get(url)

if response.status_code == 200:
    c = response.text
    
    # 3. Ku beddel link-ga Worker-ka cusub
    c = c.replace("https://YOUR_WORKER_URL.workers.dev/generate", "https://abdi-keys.dirxx.workers.dev/generate")
    c = c.replace("https://YOUR_WORKER_URL.workers.dev/verify", "https://abdi-keys.dirxx.workers.dev/verify")
    
    # 4. Qor faylka
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("✅ Faylka waa la soo celiyay oo link-ga Worker-ka waa lagu xidhay!")
else:
    print("❌ Khalad ayaa dhacay markii faylka la soo dejinayay.")
