import shutil,sys,json,os
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'rel="manifest"' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</head>' not in s: sys.exit('Struktur khalad')
if not os.path.exists('xero.png'): sys.exit('xero.png lama helin')
shutil.copy(f,'dashboard.html.before_pwa')
m={"name":"Abdi Panel","short_name":"Abdi","start_url":"dashboard.html","scope":"./","display":"standalone","orientation":"portrait","background_color":"#000000","theme_color":"#000000","icons":[{"src":"xero.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"xero.png","sizes":"512x512","type":"image/png","purpose":"any"}]}
open('manifest.json','w').write(json.dumps(m,indent=1))
tags='<link rel="manifest" href="manifest.json"><link rel="apple-touch-icon" href="xero.png"><meta name="apple-mobile-web-app-title" content="Abdi">\n'
j=s.find('</head>')
s=s[:j]+tags+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
