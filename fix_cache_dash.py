import shutil

# 1. Kaydi faylka hadda jira
shutil.copy('dashboard.html', 'dashboard_backup2.html')

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Ku dar Meta Tags cusub oo joojinaya Cache-ka (si browser-ku u arko isbeddelka)
meta_tags = """
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
"""

if "Cache-Control" not in c:
    # Waxaan ku dareynaa meta tags-ka ka dib <head>
    c = c.replace('<head>', '<head>\n' + meta_tags)
    print("✅ Meta tags-ka Cache-ka waa lagu daray dashboard.html")
else:
    print("⚠️ Meta tags-ka horey ayaa loo daray.")

# 4. Hubi in faylku leeyahay 'mobile-nav' (si aan u hubinno inuu yahay kii cusub)
if "mobile-nav" not in c:
    print("❌ Faylkaagu waa kii hore! Waxaan u baahanahay inaan mar kale dhigno koodhka cusub.")
else:
    print("✅ Faylkaagu waa kii cusub (wuxuu leeyahay Liquid Navigation).")

# 5. Dib u qor
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)
