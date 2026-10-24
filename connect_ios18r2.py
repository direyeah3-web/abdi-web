import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'IOS18 R2' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_ios18r2')
css=r'''
/* ===== IOS18 R2 ===== */
.km{background:linear-gradient(160deg,#1f1f22,#121214)!important;border:1px solid rgba(255,255,255,.09)!important;border-radius:30px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 10px 30px rgba(0,0,0,.55)!important}
.num{font-size:46px!important;font-weight:700!important;letter-spacing:-.03em!important;line-height:1.05;font-variant-numeric:tabular-nums}
.lab{font-size:12px!important;font-weight:600!important;letter-spacing:.06em;text-transform:uppercase;color:rgba(235,235,245,.5)!important}
.card.empty,.empty{background:transparent!important;border:1px dashed rgba(255,255,255,.14)!important;box-shadow:none!important;color:rgba(235,235,245,.45)!important;border-radius:24px!important}
.kc{background:linear-gradient(160deg,#242427,#161618)!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:26px!important;padding:16px 18px!important;margin-bottom:12px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 8px 24px rgba(0,0,0,.5)!important}
.kc:active{transform:scale(.985);transition:transform .15s}
.pbtn{background:#fff!important;color:#000!important;font-weight:600!important;font-size:16px!important;border:none!important;border-radius:999px!important;padding:13px 22px!important;box-shadow:0 4px 18px rgba(255,255,255,.12)!important}
.srch{background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:999px!important;padding:12px 18px!important;color:#fff!important;font-size:16px!important}
.pill{border-radius:999px!important;background:rgba(255,255,255,.10)!important;border:1px solid rgba(255,255,255,.12)!important;padding:4px 12px!important;font-size:12px!important;font-weight:600!important}
.row{border-bottom:.5px solid rgba(255,255,255,.08)!important}
.row:last-child{border-bottom:none!important}
.sec{font-size:22px!important;font-weight:700!important;letter-spacing:-.01em}
.view{animation:abIn .38s cubic-bezier(.2,.8,.2,1)}
/* ===== /IOS18 R2 ===== */
'''
i=s.rfind('</style>')
s=s[:i]+css+s[i:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
