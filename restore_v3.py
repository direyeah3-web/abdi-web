import shutil, os

if not os.path.exists("v3.html"):
    print("❌ v3.html lama helin")
    raise SystemExit
if os.path.exists("dashboard.html"):
    print("⚠️ dashboard.html hore ayuu u jiray. Waan joogsaday.")
    raise SystemExit

shutil.copy("index.html", "index.html.gold_backup")
shutil.copy("index.html", "dashboard.html")
shutil.copy("v3.html", "index.html")
print("✅ Backup: index.html.gold_backup")
print("✅ Dashboard Gold -> dashboard.html")
print("✅ index.html = v3 (login-kii hore)")
