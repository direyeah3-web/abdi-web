import shutil

# 1. Kaydi
shutil.copy('dashboard.html', 'dashboard_backup_alert.html')

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Beddel alert-ka koodhka Copy-ga
c = c.replace(
    "navigator.clipboard.writeText(key); alert('Copied: ' + key);",
    "navigator.clipboard.writeText(key); showToast('Key copied: ' + key, 'success');"
)

# 4. Beddel alert-ka koodhka Delete-ka
c = c.replace(
    "alert('Key deleted.');",
    "showToast('Key deleted.', 'error');"
)

# 5. Beddel alert-ka Generate-ka
c = c.replace(
    "alert(`${qty} Key(s) generated successfully!`);",
    "showToast(`${qty} Key(s) generated successfully!`, 'success');"
)

# 6. Qor
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Alert() waa la tirtiray, Toast-ka ayaa lagu beddelay.")
