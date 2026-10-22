# 1. Akhri faylka
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 2. Beddel qoraalka
c = c.replace('Horay u soco', 'Horay u soco')
c = c.replace('Continue', 'Key cusub') # Halkan ayaad ku beddeli kartaa qoraalka aad rabto

# 3. Tirtir calaamadda Apple (SVG-ga)
import re
# Waxaan raadinaynaa SVG-ga Apple-ka oo aan ka tirtirnaa
c = re.sub(r'<svg[^>]*>.*?</svg>', '', c, flags=re.DOTALL)

# 4. Dib u qor faylka
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Calaamadda Apple-ka waa la tirtiray, qoraalkana waa la beddelay!")
