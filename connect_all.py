import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'IOS ALL' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_all')
css=r'''
/* ===== IOS ALL ===== */
.card{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.035))!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:28px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 30px rgba(0,0,0,.5)!important;padding:18px!important}
.card.sec{padding:20px!important}
.card h2,.card h3{font-size:20px!important;font-weight:700!important;letter-spacing:-.01em}
.kc{padding:18px!important;border-radius:28px!important}
.kc [class*="key"],.kc code,.kc .k{font-family:ui-monospace,"SF Mono",Menlo,monospace!important;letter-spacing:.04em;color:#fff!important}
.kc button,.card button:not(.pbtn){background:rgba(255,255,255,.09)!important;border:1px solid rgba(255,255,255,.12)!important;color:#fff!important;border-radius:999px!important;padding:11px 18px!important;font-size:15px!important;font-weight:600!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.10)!important;-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}
.kc button:active,.card button:active{background:rgba(255,255,255,.18)!important}
.kc button[class*="del"],.card button[class*="del"],.card button.dg,.card button.out{color:#ff453a!important}
.st-b{background:rgba(255,255,255,.12)!important;color:#fff!important;border:1px solid rgba(255,255,255,.14)!important;border-radius:999px!important;padding:5px 13px!important;font-size:13px!important;font-weight:600!important;box-shadow:none!important}
.st-b.st-d{background:rgba(255,255,255,.05)!important;color:rgba(235,235,245,.45)!important}
.st-i{background:rgba(255,255,255,.10)!important;color:#fff!important;border-radius:14px!important}
select,input,textarea{height:auto!important;padding:14px 18px!important;-webkit-appearance:none;appearance:none}
label,.lb{font-size:13px!important;font-weight:600!important;color:rgba(235,235,245,.5)!important;letter-spacing:.02em}
.me,.sub{color:rgba(235,235,245,.5)!important}
.row{padding:14px 0!important}
table{border-collapse:collapse;width:100%}
th{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:rgba(235,235,245,.45)!important;text-align:left;padding:10px 6px;border-bottom:.5px solid rgba(255,255,255,.1)!important}
td{padding:14px 6px;border-bottom:.5px solid rgba(255,255,255,.07)!important;color:#fff}
.view>*{animation:abIn .4s cubic-bezier(.2,.8,.2,1) both}
.view>*:nth-child(2){animation-delay:.04s}.view>*:nth-child(3){animation-delay:.08s}.view>*:nth-child(4){animation-delay:.12s}.view>*:nth-child(5){animation-delay:.16s}
*{-webkit-touch-callout:none}
input,textarea{-webkit-user-select:text;user-select:text}
/* ===== /IOS ALL ===== */
'''
js=r'''
/* ===== IOS ALL JS ===== */
try{document.addEventListener("click",function(e){
 if(e.target.closest&&e.target.closest("button,#tab>*,.kc,.pbtn")&&navigator.vibrate)navigator.vibrate(8)
},true)}catch(e){}
/* ===== /IOS ALL JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
