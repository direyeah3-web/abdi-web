import shutil,sys,re
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'APPLE BLUE' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_apple')
s,n=re.subn(r'/\* ===== MONO THEME JS ===== \*/.*?/\* ===== /MONO THEME JS ===== \*/','',s,flags=re.S)
print('mono JS laga saaray:',n)
css=r'''
/* ===== APPLE BLUE ===== */
*{--cr:10!important;--cg:132!important;--cb:255!important;--ac:#0a84ff!important;-webkit-tap-highlight-color:transparent}
::selection{background:rgba(10,132,255,.35)}
a{color:#0a84ff}
.ab-prim.ab-prim,.pbtn.pbtn{background:#0a84ff!important;color:#fff!important;border:none!important;font-weight:600!important;box-shadow:0 8px 24px rgba(10,132,255,.35)!important}
.ab-prim.ab-prim *,.pbtn.pbtn *{color:#fff!important}
.ab-prim.ab-prim:active,.pbtn.pbtn:active{background:#0066d6!important;transform:scale(.97)}
input:focus,select:focus,textarea:focus{outline:none!important;border-color:#0a84ff!important;box-shadow:0 0 0 3px rgba(10,132,255,.25)!important}
#tab>.on,#tab>.active,#tab>[aria-selected="true"],#tab .on,#tab .active{color:#0a84ff!important}
/* ===== /APPLE BLUE ===== */
'''
js=r'''
/* ===== APPLE BLUE JS ===== */
try{
document.addEventListener("click",function(e){var t=e.target;if(t&&t.closest&&t.closest("h1")){e.stopPropagation();e.stopImmediatePropagation()}},true);
(function(){
function q(c){var m=(c||"").match(/[\d.]+/g);return m?m.map(Number):[0,0,0,0]}
function run(){
 document.querySelectorAll("button").forEach(function(b){
  if(b.classList.contains("ab-prim"))return;
  var w=b.offsetWidth,h=b.offsetHeight;if(w<160||h<44)return;
  var c=q(getComputedStyle(b).backgroundColor),a=c.length>3?c[3]:1;
  if(a>.5&&Math.max(c[0],c[1],c[2])>140)b.classList.add("ab-prim")
 })}
var t;function sch(){clearTimeout(t);t=setTimeout(run,250)}
new MutationObserver(sch).observe(document.body,{childList:true,subtree:true});
sch();setTimeout(run,1200)
})()}catch(e){console.log(e)}
/* ===== /APPLE BLUE JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
