import shutil
import os

# 1. Soo celi faylkii backup-ka ahaa ee ugu dambeeyay (kii quruxda badnaa)
if os.path.exists('dashboard_worker_link_backup.html'):
    shutil.copy('dashboard_worker_link_backup.html', 'dashboard.html')
    print("✅ Faylkii quruxda badnaa waa la soo celiyay.")
else:
    print("❌ Backup-kii lama helin. Waxaan isku dayayaa inaan hagaajiyo faylka hadda jira.")

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Hubi haddii uu leeyahay CSS (style)
if "<style>" not in c:
    print("⚠️ Digniin: Faylkaagu ma lahan CSS! Waxaa laga yaabaa inuu si buuxda u burburay.")
else:
    print("✅ CSS-ku wuu ku jiraa faylka.")

# 4. Si taxaddar leh u beddel link-ga Worker-ka
c = c.replace("https://YOUR_WORKER_URL.workers.dev/generate", "https://abdi-keys.dirxx.workers.dev/generate")
c = c.replace("https://YOUR_WORKER_URL.workers.dev/verify", "https://abdi-keys.dirxx.workers.dev/verify")

# 5. Qor faylka
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Faylka waa la hagaajiyay, link-gana waa lagu xidhay Worker-ka cusub!")
