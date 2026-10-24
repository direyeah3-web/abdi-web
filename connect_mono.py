import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'MONO THEME' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_mono')
css=r'''
/* ===== MONO THEME ===== */
.ab-mono-bg{background:#fff!important;color:#000!important;border-color:transparent!important;box-shadow:0 4px 18px rgba(255,255,255,.12)!important;text-shadow:none!important}
.ab-mono-bg *{color:#000!important}
.ab-mono-soft{background:rgba(255,255,255,.10)!important;border-color:rgba(255,255,255,.16)!important;color:#fff!important}
.ab-mono-soft *{color:#fff!important}
.ab-mono-fg{color:#fff!important}
.ab-tile{background:linear-gradient(160deg,rgba(255,255,255,.20),rgba(255,255,255,.07))!important;border:1px solid rgba(255,255,255,.14)!important;border-radius:14px!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.14)!important;color:#fff!important}
.ab-tile *{color:#fff!important;stroke:#fff!important}
/* ===== /MONO THEME ===== */
'''
js=r'''
/* ===== MONO THEME JS ===== */
try{(function(){
var d=document.documentElement;
['--cr','--cg','--cb'].forEach(function(v){d.style.setProperty(v,'255')});
function q(c){var m=(c||'').match(/[\d.]+/g);return m?m.map(Number):[0,0,0,0]}
function run(){
document.querySelectorAll('body *').forEach(function(el){
if(el.closest('#ab-toast'))return;
var cs=getComputedStyle(el),b=q(cs.backgroundColor),r=b[0],g=b[1],bl=b[2],a=b.length>3?b[3]:1;
var w=el.offsetWidth,h=el.offsetHeight;
if(a>0.15){
if(r>180&&g<150&&bl<90&&r-g>70){el.classList.add('ab-mono-bg');return}
if(bl>r+35&&bl>g+15&&r<60){el.classList.add('ab-mono-soft');return}
var sq=w>=30&&w<=70&&h>=30&&h<=70;
if(sq&&g>140&&r<110&&bl<130&&g-r>60){el.classList.add('ab-tile');return}
if(sq&&Math.abs(r-g)<10&&Math.abs(g-bl)<12&&r>90&&r<190){el.classList.add('ab-tile');return}
}
var c=q(cs.color);
if(c[0]>180&&c[1]<150&&c[2]<90&&c[0]-c[1]>70)el.classList.add('ab-mono-fg');
else if(c[2]>150&&c[0]<80&&c[2]-c[0]>90)el.classList.add('ab-mono-fg');
});}
var t;function sch(){clearTimeout(t);t=setTimeout(run,250)}
new MutationObserver(sch).observe(document.body,{childList:true,subtree:true});
sch();setTimeout(run,1200);
})()}catch(e){console.log(e)}
/* ===== /MONO THEME JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
