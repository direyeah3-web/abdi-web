import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'ACT MODERN' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_act')
css=r'''
/* ===== ACT MODERN ===== */
#ab-act{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.03))!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:30px!important;padding:18px 18px 8px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 10px 30px rgba(0,0,0,.5)!important;-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px)}
#ab-act .ac-h{font-size:12px!important;font-weight:600!important;letter-spacing:.08em!important;text-transform:uppercase!important;color:rgba(235,235,245,.45)!important;margin:6px 0 8px!important;padding:0!important}
#ab-act .ac-r{position:relative;display:flex!important;align-items:center!important;gap:14px!important;margin:0!important;padding:9px 0!important;border:none!important;background:none!important;box-shadow:none!important}
#ab-act .ac-r:not(:last-child)::after{content:"";position:absolute;left:20px;top:52px;bottom:-9px;width:1px;background:linear-gradient(rgba(255,255,255,.14),rgba(255,255,255,.03))}
#ab-act .ac-i{width:42px!important;height:42px!important;min-width:42px!important;border-radius:14px!important;display:flex!important;align-items:center!important;justify-content:center!important;background:linear-gradient(160deg,rgba(255,255,255,.22),rgba(255,255,255,.07))!important;border:1px solid rgba(255,255,255,.14)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 4px 12px rgba(0,0,0,.4)!important;color:#fff!important;margin:0!important}
#ab-act .ac-i svg{width:20px!important;height:20px!important;stroke:#fff!important;color:#fff!important}
#ab-act .ac-m{flex:1;min-width:0;margin:0!important;padding:0!important;border:none!important}
#ab-act .ac-t{font-size:16px!important;font-weight:600!important;letter-spacing:-.01em;color:#fff!important;line-height:1.25;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ab-act .ac-s{font-size:13px!important;color:rgba(235,235,245,.5)!important;margin-top:2px!important}
#ab-act .ac-e{color:rgba(235,235,245,.45)!important;text-align:center;padding:24px 0}
/* ===== /ACT MODERN ===== */
'''
i=s.rfind('</style>')
s=s[:i]+css+s[i:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
