import shutil
import re

# 1. Kaydi faylka
shutil.copy('dashboard.html', 'dashboard_viewport_backup.html')

# 2. Akhri faylka
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Beddel Meta Viewport-ka
# Waxaan u sheegaynaa browser-ka inuu isticmaalo ballaca caadiga ah ee Desktop-ka (1024px)
# waxaana ka saaraynaa "initial-scale=1.0" oo aan ku beddelaynaa "initial-scale=0.4" si uu si cad ugu soo bandhigo Desktop-ka
new_viewport = '<meta name="viewport" content="width=1024, initial-scale=0.4">'

# Waxaan raadinaynaa meta viewport-kii hore oo aan ku beddelaynaa kan cusub
c = re.sub(r'<meta name="viewport".*?>', new_viewport, c)

# 4. Qor faylka
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Meta Viewport-ka si sax ah ayaa loo beddelay. Hadda Desktop-ku wuu cad yahay.")
