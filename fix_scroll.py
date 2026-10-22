import shutil

# 1. Kaydi faylka
shutil.copy('dashboard.html', 'dashboard_scroll_backup.html')

# 2. Akhri
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Ka saar overflow: hidden ee body-ga (waxaan u beddelaynaa overflow-y: auto)
# Qoraalka hore ee body-ga:
old_body_css = "body { background-color: #000000; color: #ffffff; display: flex; height: 100vh; overflow: hidden; }"

# Qoraalka cusub (waxaan ka dhignay overflow-y: auto, height: 100%):
new_body_css = "body { background-color: #000000; color: #ffffff; display: flex; min-height: 100vh; overflow-y: auto; overflow-x: hidden; }"

if old_body_css in c:
    c = c.replace(old_body_css, new_body_css)
    print("✅ Body-ga waa la hagaajiyay (Scroll wuu shaqeynayaa).")
else:
    # Haddii qoraalku yara duwan yahay, isticmaal regex
    import re
    c = re.sub(r'body\s*\{[^}]*\}', 'body { background-color: #000000; color: #ffffff; display: flex; min-height: 100vh; overflow-y: auto; overflow-x: hidden; }', c)
    print("✅ Regex ayaa lagu hagaajiyay Body-ga.")

# 4. Hubi in .main-content uu leeyahay overflow-y: auto
if ".main-content {" in c:
    # Waxaan ku dareynaa ama ku beddelaynaa overflow-y: auto
    c = c.replace("overflow-y: auto;", "overflow-y: auto !important;")
    print("✅ Main-content scroll-ka waa la xoojiyay.")

# 5. Qor
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)
