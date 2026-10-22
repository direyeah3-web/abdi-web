import shutil

# 1. Kaydi faylka hadda jira
shutil.copy('index.html', 'index_backup_text.html')

# 2. Akhri faylka
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 3. Beddel qoraallada badhannada
c = c.replace('Continue with Phone', 'Horay u soco')
c = c.replace('Continue with Apple', 'Continue')

# 4. Dib u qor faylka
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Qoraallada badhannada si guul leh ayaa loo beddelay!")
