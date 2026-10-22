import shutil

shutil.copy('dashboard.html', 'dashboard_gold_backup.html')

# Waxaan beddelaynaa midabka background-ka oo kaliya si aan u tijaabino
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Beddel midabka madowga
c = c.replace('background-color: #000000;', 'background-color: #08090C;')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("✅ Faylka waa la beddelay (Midabka waa la tijaabiyay).")
