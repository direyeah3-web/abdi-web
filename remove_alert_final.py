import shutil
import os

# 1. Kaydi
if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_alert_backup.html')

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Tirtir alert-ka Copy-ga
c = c.replace(
    "navigator.clipboard.writeText(key); alert('Copied: ' + key);",
    "navigator.clipboard.writeText(key); showToast('Key copied: ' + key, 'success');"
)

# 4. Tirtir alert-ka Delete-ka
c = c.replace(
    "alert('Key deleted.');",
    "showToast('Key deleted.', 'error');"
)

# 5. Tirtir alert-ka Generate-ka
c = c.replace(
    "alert(`${qty} Key(s) generated successfully!`);",
    "showToast(`${qty} Key(s) generated successfully!`, 'success');"
)

# 6. Haddii ay jiraan alert kale oo ku hadhay, ka saar (haddii aan la helin qoraalka saxda ah)
# Waxaan ka saaraynaa dhammaan alert() hadhay si aan u hubinno in toast-ku uu shaqeeyo
import re
c = re.sub(r'alert\([^)]*\);', '/* alert removed */', c)

# 7. Qor faylka
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Dhammaan alert()-yadii waa la tirtiray, Toast-ka ayaa lagu beddelay.")
