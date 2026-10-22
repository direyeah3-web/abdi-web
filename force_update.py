with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Waxaan hubinaynaa haddii qoraalkii hore uu ku jiro
if "Continue with Phone" in c:
    c = c.replace('Continue with Phone', 'Horay u soco')
    print("✅ 'Continue with Phone' waxaa loo beddelay 'Horay u soco'")
else:
    print("⚠️ 'Continue with Phone' lama helin faylka.")

if "Continue with Apple" in c:
    c = c.replace('Continue with Apple', 'Continue')
    print("✅ 'Continue with Apple' waxaa loo beddelay 'Continue'")
else:
    print("⚠️ 'Continue with Apple' lama helin faylka.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("✅ Faylka waa la cusboonaysiiyay.")
