import shutil
shutil.copy("dashboard.html", "dashboard.html.before_fix")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
if ":not(.ab-blob)" in d:
    print("⚠️ Hore ayaa loo hagaajiyay")
    raise SystemExit
a = "#side~*:not(#tab){"
if a not in d:
    print("❌ Xeerka lama helin")
    raise SystemExit
d = d.replace(a, "#side~*:not(#tab):not(.ab-blob):not(#ab-snd):not(#ab-lt){")
d = d.replace("opacity:.55;animation:abFloat", "opacity:.3;animation:abFloat")
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ La hagaajiyay")
