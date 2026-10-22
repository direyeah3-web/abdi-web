import shutil

# 1. Kaydi
shutil.copy('dashboard.html', 'dashboard_pure_desktop_backup.html')

# 2. Akhri
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Beddel Meta Viewport-ka (Halkan ayaa xalku ku jiraa)
# Waxaan u sheegaynaa browser-ka inuu isticmaalo ballaca desktop-ka (1024px) mar walba
old_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
new_viewport = '<meta name="viewport" content="width=1024, initial-scale=0.4">'

if old_viewport in c:
    c = c.replace(old_viewport, new_viewport)
    print("✅ Meta Viewport-ka waa la beddelay si Desktop loo qasbo.")
else:
    # Haddii uu yara duwan yahay
    import re
    c = re.sub(r'<meta name="viewport" content=".*?">', new_viewport, c)
    print("✅ Regex ayaa lagu beddelay Meta Viewport-ka.")

# 4. Ka saar (disable) media queries-ka yaryar ee sidebar-ka yareynaya
# Waxaan ka dhigaynaa in aanay shaqeyn, si sidebar-ku u hadho mid weyn
old_media = """@media (max-width: 768px) {
            .sidebar { width: 70px; padding: 20px 10px; }
            .logo-area span, .nav-item span, .user-info { display: none; }
            .nav-item { justify-content: center; padding: 12px; }
            .user-profile-bottom { justify-content: center; padding: 10px; }
        }"""

new_media = """/* Media query-ga waa la joojiyay */
        @media (max-width: 0px) {
            /* Waxba ma qabanayo */
        }"""

if old_media in c:
    c = c.replace(old_media, new_media)
    print("✅ Media query-gii yareynayay sidebar-ka waa la joojiyay.")
else:
    # Haddii uu yara duwan yahay, isticmaal regex
    import re
    c = re.sub(r'@media \(max-width: 768px\).*?\}', '/* Media Query Disabled */', c, flags=re.DOTALL)
    print("✅ Regex ayaa lagu joojiyay media query-ga.")

# 5. Qor
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)
