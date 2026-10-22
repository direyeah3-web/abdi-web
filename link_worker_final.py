import shutil

shutil.copy('dashboard.html', 'dashboard_worker_link_backup.html')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Waxaan ku beddelaynaa link-ga Worker-ka cusub
c = c.replace("https://YOUR_WORKER_URL.workers.dev/generate", "https://abdi-keys.dirxx.workers.dev/generate")
c = c.replace("https://YOUR_WORKER_URL.workers.dev/verify", "https://abdi-keys.dirxx.workers.dev/verify")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Dashboard-ka waa lagu xidhay Worker-ka cusub (abdi-keys)!")
