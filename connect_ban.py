import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'was unbanned' in s: sys.exit('Hore ayaa loo dhejiyey')
a1='''dot:'<circle cx="12" cy="12" r="3"/>'};'''
a2='''var m,t=String(s||"").trim();'''
a3='''var x=s.toLowerCase();'''
for a in (a1,a2,a3):
    if s.count(a)!=1: sys.exit('Anchor lama helin: '+a)
shutil.copy(f,'dashboard.html.before_ban')
s=s.replace(a1,r'''dot:'<circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v5h1"/>',
ban:'<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
unlock:'<rect x="5" y="11" width="14" height="10" rx="3"/><path d="M8 11V8a4 4 0 0 1 7.5-2"/>'};''')
s=s.replace(a2,a2+r'''
 if(m=t.match(/^(.+?) la unban gareeyay$/i))return m[1]+" was unbanned";
 if(m=t.match(/^(.+?) la ban gareeyay$/i))return m[1]+" was banned";''')
s=s.replace(a3,a3+r'''
 if(/unban/.test(x))return ["unlock","#30d158"];
 if(/\bban(ned)?\b/.test(x))return ["ban","#ff453a"];''')
open(f,'w',encoding='utf-8').write(s)
print('OK')
