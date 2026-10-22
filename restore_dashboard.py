import shutil
import os

# 1. Soo celi backup-kii ugu dambeeyay ee quruxda badnaa
if os.path.exists('dashboard_worker_link_backup.html'):
    shutil.copy('dashboard_worker_link_backup.html', 'dashboard.html')
    print("✅ Faylkii hore ee quruxda badnaa waa la soo celiyay.")
else:
    print("⚠️ Backup-kii lama helin. Waxaan isku dayayaa inaan hagaajiyo kan hadda jira.")

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Si taxaddar leh u beddel link-ga Worker-ka
# Waxaan hubinayaa in aanan wax kale ku xumeyn
c = c.replace("https://YOUR_WORKER_URL.workers.dev/generate", "https://abdi-keys.dirxx.workers.dev/generate")
c = c.replace("https://YOUR_WORKER_URL.workers.dev/verify", "https://abdi-keys.dirxx.workers.dev/verify")

# 4. Hubi in CSS-ku si fiican ugu jiro (haddii uu ka baxay)
if "<style>" not in c:
    print("⚠️ Digniin: CSS-ka ayaa ka maqan faylka!")

# 5. Qor faylka
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Faylka si fiican ayaa loo hagaajiyay, link-gana waa lagu xidhay Worker-ka!")
