import shutil
import re

# 1. Kaydi faylka
shutil.copy('dashboard.html', 'dashboard_true_desktop_backup.html')

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Hagaaji Meta Viewport-ka (Waxaan u sheegaynaa browser-ka inuu isticmaalo ballaca caadiga ah ee desktop-ka, ma aha mid yar)
# Waxaan ka saaraynaa "width=device-width" oo aan ku beddelaynaa "width=1024" si uu u noqdo desktop dhab ah
c = re.sub(r'<meta name="viewport".*?>', '<meta name="viewport" content="width=1024, initial-scale=1.0">', c)

# 4. Tirtir dhammaan Media Queries-ka (kuwaas oo shaashadda yareynaya)
# Waxaan raadinaynaa @media oo dhan oo aan ka dhigaynaa wax aan shaqeyn
c = re.sub(r'@media\s*\([^)]*\)\s*\{.*?\}', '/* Media query removed for True Desktop */', c, flags=re.DOTALL)

# 5. Hubi in sidebar-ku uu leeyahay qoraal (aan la qarin)
# Waxaan hubinaynaa in .text uu muuqdo
if '.logo-area span, .nav-item span, .user-info { display: none; }' in c:
    c = c.replace('.logo-area span, .nav-item span, .user-info { display: none; }', '/* Qoraalka waa la ilaaliyay */')

# 6. Qor faylka cusub
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Dashboard-ka hadda waa Desktop Dhab ah! Media queries-kii yaraa waa la tirtiray.")
