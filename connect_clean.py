import shutil
shutil.copy("dashboard.html", "dashboard.html.before_clean")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
if "abdi-clean" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
CSS = r'''/*abdi-clean*/
html,body{background:#08090D!important;background-image:none!important}
.ab-blob{display:none!important}
#ab-snd,#ab-lt{display:none!important}
.card,.an-s,.ab-rel{background:#171A23!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;border:1px solid rgba(255,255,255,.06)!important;box-shadow:none!important;border-radius:20px!important;animation:none!important}
.ab-ic{box-shadow:none!important;border-radius:9px!important}
.an-s b{background:none!important;color:#fff!important;-webkit-text-fill-color:#fff!important}
.an-b i{background:#0a84ff!important;box-shadow:none!important}
#ab-qa .q1{background:#0a84ff!important;box-shadow:none!important;border-radius:16px!important}
#ab-qa .q2{background:#171A23!important;border:1px solid rgba(255,255,255,.1)!important;box-shadow:none!important;border-radius:16px!important}
.st-b{background:#0a84ff!important;box-shadow:none!important}
.st-d,.dg{background:#ff453a!important;box-shadow:none!important}
input,select,textarea{background:#171A23!important;border:1px solid rgba(255,255,255,.08)!important}
#tab{background:rgba(23,26,35,.94)!important;backdrop-filter:blur(20px)!important;-webkit-backdrop-filter:blur(20px)!important;box-shadow:0 -1px 0 rgba(255,255,255,.05)!important;border:1px solid rgba(255,255,255,.07)!important;border-radius:26px!important}
#tab>.ab-on{background:rgba(10,132,255,.18)!important;color:#0a84ff!important;box-shadow:none!important}
h1{font-size:30px!important}
'''
i = d.rfind("</style>")
d = d[:i] + CSS + d[i:]
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Clean theme waa la dhisay")
