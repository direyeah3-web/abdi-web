import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Waxaan hubinaynaa haddii window.location.href uu horey ugu jiro
if "window.location.href = 'dashboard.html';" in c:
    print("✅ Isku xirka Dashboard-ka horey ayaa loo sameeyay.")
else:
    print("⚠️ Isku xirku ma jiro. Waan ku dareynaa hadda...")
    
    # Waxaan raadinaynaa badhanka 'Success!'
    # Haddii uu jiro, waxaan ka dib ku dareynaa amarka beddelka bogga
    pattern = r'(btn\.innerText = "Success!";.*?)(})'
    
    def add_redirect(match):
        # Waxaan ku dareynaa setTimeout ka dib marka Success la gaaro
        redirect_code = """
        setTimeout(() => {
            window.location.href = 'dashboard.html';
        }, 800);
        """
        return match.group(1) + redirect_code + match.group(2)

    # Beddel koodhka annagoo isticmaalayna Regex
    new_c, count = re.subn(pattern, add_redirect, c, flags=re.DOTALL)
    
    if count > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_c)
        print("✅ Amarka beddelka bogga si guul leh ayaa loogu daray faylka.")
    else:
        print("❌ Weli lama helin qoraalka. Waxaan isku dayayaa hab kale...")
        # Qaab kale oo fudud
        c = c.replace('btn.innerText = "Success!";', "btn.innerText = \"Success!\"; setTimeout(() => { window.location.href = 'dashboard.html'; }, 800);")
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("✅ Isku day kale ayaa lagu guulaystay.")
