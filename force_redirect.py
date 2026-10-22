with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Waxaan hubinaynaa haddii isbeddelkii hore uu ku jiro
if "window.location.href = 'dashboard.html';" in c:
    print("✅ Isku xirka Dashboard-ka horey ayaa loo sameeyay.")
else:
    print("⚠️ Isku xirku ma jiro. Waan ku dareynaa hadda...")
    
    # Waxaan raadinaynaa qaybta "Success!" ee Login-ka oo aan ku dareynaa amarka beddelka bogga
    old_code = """btn.innerText = "Success!";
                            btn.style.background = "#238636"; 
                            btn.style.color = "#fff";"""
    
    new_code = """btn.innerText = "Success!";
                            btn.style.background = "#238636"; 
                            btn.style.color = "#fff";
                            setTimeout(() => {
                                window.location.href = 'dashboard.html';
                            }, 800);"""
    
    # Haddii qoraalka la helo, beddel
    if old_code in c:
        c = c.replace(old_code, new_code)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("✅ Amarka beddelka bogga si guul leh ayaa loogu daray faylka.")
    else:
        print("❌ Qoraalkii la raadinayay lama helin. Waxaa laga yaabaa in qaabka JS-ga uu yara duwan yahay.")
