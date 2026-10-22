import shutil

# 1. Kaydi faylka hadda jira
shutil.copy('dashboard.html', 'dashboard_force_backup.html')

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Waxaan beddelaynaa CSS-ka @media si aan u joojino in uu isbeddelo (Force Desktop)
# Qoraalkii hore:
old_media = """@media (max-width: 768px) {
            .sidebar { display: none; }
            .main-content { padding: 20px; padding-bottom: 100px; }
            .mobile-nav { display: flex; }
        }"""

# Qoraalka cusub (waxaan ka dhigaynaa mid aan shaqeyn, si Desktop-ku u hadho)
new_media = """/* Media query-ga waa la joojiyay si Desktop Site uu mar walba u shaqeeyo */
        @media (max-width: 0px) {
            .sidebar { display: none; }
            .main-content { padding: 20px; padding-bottom: 100px; }
            .mobile-nav { display: flex; }
        }"""

# 4. Beddel qoraalka
if old_media in c:
    c = c.replace(old_media, new_media)
    print("✅ CSS-ka waa la beddelay: Desktop Site-ku mar walba wuu shaqeynayaa.")
else:
    # Haddii qoraalku yara duwan yahay, waxaan isticmaalaynaa Regex
    import re
    c = re.sub(r'@media \(max-width: 768px\).*?\}', '/* Media Query Disabled */', c, flags=re.DOTALL)
    print("✅ Regex ayaa lagu beddelay: Desktop Site-ku mar walba wuu shaqeynayaa.")

# 5. Dib u qor
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)
