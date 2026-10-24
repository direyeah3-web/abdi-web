import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'IOS18 THEME' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</head>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_ios18')
css=r'''
/* ===== IOS18 THEME ===== */
html,body{background:#000!important;background-image:none!important;color:#fff;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text",Inter,system-ui,sans-serif!important;-webkit-font-smoothing:antialiased;-webkit-tap-highlight-color:transparent;overscroll-behavior:none}
body::before,body::after{background:none!important}
::-webkit-scrollbar{display:none}
h1{font-size:34px!important;font-weight:700!important;letter-spacing:-.02em}
h2,h3{font-weight:700!important;letter-spacing:-.01em}
[class*="card"],[class*="glass"],[class*="tile"]{background:linear-gradient(160deg,rgba(255,255,255,.085),rgba(255,255,255,.035))!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:28px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 8px 30px rgba(0,0,0,.5)!important;-webkit-backdrop-filter:blur(24px) saturate(160%);backdrop-filter:blur(24px) saturate(160%)}
button,.btn{border-radius:999px!important;transition:transform .18s cubic-bezier(.2,.8,.2,1),opacity .18s}
button:active,.btn:active{transform:scale(.95);opacity:.85}
[class*="primary"]{background:#fff!important;color:#000!important;font-weight:600!important;border:none!important}
input,select,textarea{background:rgba(255,255,255,.07)!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:16px!important;color:#fff!important;font-size:16px!important}
#tab{position:fixed!important;left:14px!important;right:14px!important;width:auto!important;bottom:calc(env(safe-area-inset-bottom,0px) + 12px)!important;border-radius:999px!important;background:rgba(28,28,30,.70)!important;-webkit-backdrop-filter:blur(30px) saturate(180%)!important;backdrop-filter:blur(30px) saturate(180%)!important;border:1px solid rgba(255,255,255,.12)!important;box-shadow:0 12px 40px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.08)!important;padding:6px!important}
#tab>*{color:rgba(235,235,245,.45)!important;border-radius:999px!important}
#tab>.on,#tab>.active,#tab>[aria-selected="true"]{color:#fff!important;background:rgba(255,255,255,.13)!important}
[id^="v-"]{padding-bottom:120px!important;animation:abIn .38s cubic-bezier(.2,.8,.2,1)}
@keyframes abIn{from{opacity:0;transform:translateY(12px) scale(.99)}to{opacity:1;transform:none}}
/* ===== /IOS18 THEME ===== */
'''
i=s.rfind('</style>')
s=s[:i]+css+s[i:]
meta='<meta name="theme-color" content="#000000"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
j=s.find('</head>')
s=s[:j]+meta+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
