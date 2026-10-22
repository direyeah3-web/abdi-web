import shutil, os

if not os.path.exists("v3.html"):
    print("❌ v3.html lama helin")
    raise SystemExit

if not os.path.exists("dashboard_gold.html"):
    shutil.copy("index.html", "dashboard_gold.html")
    print("✅ Gold dashboard -> dashboard_gold.html")

shutil.copy("v3.html", "index.html")
print("✅ index.html = v3 (Welcome + Login hore)")
print("ℹ️ dashboard.html lama taaban")
