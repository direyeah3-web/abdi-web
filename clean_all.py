import os, shutil, subprocess

KEEP = {"clean_all.py"}

subprocess.run(["git", "tag", "-f", "old-backup"], check=True)
print("✅ Tag: old-backup (wax kasta waa la soo celin karaa)")

for name in os.listdir("."):
    if name in KEEP or name.startswith("."):
        continue
    if os.path.isdir(name):
        shutil.rmtree(name)
    else:
        os.remove(name)
    print("🗑️", name)

with open("index.html", "w", encoding="utf-8") as f:
    f.write('<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Abdi</title></head>'
            '<body style="background:#000;color:#fff;font-family:sans-serif;'
            'display:flex;align-items:center;justify-content:center;height:100vh;margin:0">'
            '<h2>Cusub: diyaar</h2></body></html>')
print("✅ index.html cusub oo madhan waa la sameeyay")
