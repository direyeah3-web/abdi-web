import shutil
shutil.copy("dashboard.html", "dashboard.html.before_glass")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-glass" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit
if "--cr" not in d:
    print("⚠️ Midabka live (connect_live.py) lama helin, glass wuxuu isticmaali doonaa midab go'an")

CSS = r'''/*abdi-glass*/
:root{--ar2:var(--cb),var(--cr),var(--cg);--ar3:var(--cg),var(--cb),var(--cr)}
html,body{background:#000!important}
body{background:transparent!important}
.ab-blob.ab-blob{position:fixed!important;z-index:-1;pointer-events:none;border-radius:50%;margin:0!important;padding:0!important;max-width:none!important;box-sizing:content-box!important;animation:abFl 18s ease-in-out infinite alternate}
.ab-blob.b1{width:420px!important;height:420px!important;top:-140px!important;right:-120px!important;left:auto!important;bottom:auto!important;background:radial-gradient(circle,rgba(var(--ar),.55),transparent 68%)}
.ab-blob.b2{width:380px!important;height:380px!important;bottom:70px!important;left:-150px!important;top:auto!important;right:auto!important;background:radial-gradient(circle,rgba(var(--ar2),.38),transparent 68%);animation-delay:-6s}
.ab-blob.b3{width:320px!important;height:320px!important;top:42%!important;right:-150px!important;left:auto!important;bottom:auto!important;background:radial-gradient(circle,rgba(var(--ar3),.30),transparent 68%);animation-delay:-11s}
@keyframes abFl{from{transform:translate(0,0) scale(1)}to{transform:translate(-30px,40px) scale(1.15)}}
.card,#ab-act{background:linear-gradient(150deg,rgba(var(--ar),.17),rgba(255,255,255,.035) 45%,rgba(16,16,18,.55))!important;backdrop-filter:blur(22px) saturate(165%)!important;-webkit-backdrop-filter:blur(22px) saturate(165%)!important;border:1px solid rgba(255,255,255,.09)!important;border-top-color:rgba(var(--ar),.55)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 10px 30px rgba(0,0,0,.35)!important}
.io-g{backdrop-filter:blur(22px) saturate(165%)!important;-webkit-backdrop-filter:blur(22px) saturate(165%)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.1)!important}
#tab{background:rgba(12,12,14,.72)!important;backdrop-filter:blur(30px) saturate(180%)!important;-webkit-backdrop-filter:blur(30px) saturate(180%)!important;border-top:1px solid rgba(255,255,255,.1)!important}
.ab-rel{position:relative!important}
.ab-ic{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:11px;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),0 6px 16px rgba(var(--ar),.35)}
.ab-ic svg{width:18px;height:18px}
.ab-ic.c1{background:linear-gradient(135deg,rgb(var(--ar)),rgba(var(--ar),.6))}
.ab-ic.c2{background:linear-gradient(135deg,rgb(var(--ar2)),rgba(var(--ar2),.6))}
.ab-ic.c3{background:linear-gradient(135deg,rgb(var(--ar3)),rgba(var(--ar3),.6))}
#ab-qa{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
#ab-qa button{display:flex;align-items:center;justify-content:center;gap:8px;padding:16px 10px;border:0;border-radius:999px;color:#fff;font-weight:700;font-size:15px;cursor:pointer}
#ab-qa svg{width:18px;height:18px}
#ab-qa .q1{background:linear-gradient(135deg,rgba(var(--ar),1),rgba(var(--ar),.72));box-shadow:0 10px 26px rgba(var(--ar),.4),inset 0 1px 0 rgba(255,255,255,.3)}
#ab-qa .q2{background:linear-gradient(135deg,rgba(var(--ar2),1),rgba(var(--ar2),.72));box-shadow:0 10px 26px rgba(var(--ar2),.4),inset 0 1px 0 rgba(255,255,255,.3)}
.ab-live{background:#000!important;color:#30d158!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:999px!important;padding:5px 12px 5px 22px!important;position:relative;font-weight:700}
.ab-live:before{content:"";position:absolute;left:9px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:#30d158;box-shadow:0 0 8px #30d158;animation:abPu 1.6s infinite}
@keyframes abPu{50%{opacity:.25}}
.card{animation:abUp .5s cubic-bezier(.2,.9,.2,1) both}
@keyframes abUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;
cat > connect_glass.py << 'EOF'
import shutil
shutil.copy("dashboard.html", "dashboard.html.before_glass")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-glass" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit
if "--cr" not in d:
    print("⚠️ Midabka live (connect_live.py) lama helin, glass wuxuu isticmaali doonaa midab go'an")

CSS = r'''/*abdi-glass*/
:root{--ar2:var(--cb),var(--cr),var(--cg);--ar3:var(--cg),var(--cb),var(--cr)}
html,body{background:#000!important}
body{background:transparent!important}
.ab-blob.ab-blob{position:fixed!important;z-index:-1;pointer-events:none;border-radius:50%;margin:0!important;padding:0!important;max-width:none!important;box-sizing:content-box!important;animation:abFl 18s ease-in-out infinite alternate}
.ab-blob.b1{width:420px!important;height:420px!important;top:-140px!important;right:-120px!important;left:auto!important;bottom:auto!important;background:radial-gradient(circle,rgba(var(--ar),.55),transparent 68%)}
.ab-blob.b2{width:380px!important;height:380px!important;bottom:70px!important;left:-150px!important;top:auto!important;right:auto!important;background:radial-gradient(circle,rgba(var(--ar2),.38),transparent 68%);animation-delay:-6s}
.ab-blob.b3{width:320px!important;height:320px!important;top:42%!important;right:-150px!important;left:auto!important;bottom:auto!important;background:radial-gradient(circle,rgba(var(--ar3),.30),transparent 68%);animation-delay:-11s}
@keyframes abFl{from{transform:translate(0,0) scale(1)}to{transform:translate(-30px,40px) scale(1.15)}}
.card,#ab-act{background:linear-gradient(150deg,rgba(var(--ar),.17),rgba(255,255,255,.035) 45%,rgba(16,16,18,.55))!important;backdrop-filter:blur(22px) saturate(165%)!important;-webkit-backdrop-filter:blur(22px) saturate(165%)!important;border:1px solid rgba(255,255,255,.09)!important;border-top-color:rgba(var(--ar),.55)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 10px 30px rgba(0,0,0,.35)!important}
.io-g{backdrop-filter:blur(22px) saturate(165%)!important;-webkit-backdrop-filter:blur(22px) saturate(165%)!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.1)!important}
#tab{background:rgba(12,12,14,.72)!important;backdrop-filter:blur(30px) saturate(180%)!important;-webkit-backdrop-filter:blur(30px) saturate(180%)!important;border-top:1px solid rgba(255,255,255,.1)!important}
.ab-rel{position:relative!important}
.ab-ic{position:absolute;top:14px;right:14px;width:32px;height:32px;border-radius:11px;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),0 6px 16px rgba(var(--ar),.35)}
.ab-ic svg{width:18px;height:18px}
.ab-ic.c1{background:linear-gradient(135deg,rgb(var(--ar)),rgba(var(--ar),.6))}
.ab-ic.c2{background:linear-gradient(135deg,rgb(var(--ar2)),rgba(var(--ar2),.6))}
.ab-ic.c3{background:linear-gradient(135deg,rgb(var(--ar3)),rgba(var(--ar3),.6))}
#ab-qa{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
#ab-qa button{display:flex;align-items:center;justify-content:center;gap:8px;padding:16px 10px;border:0;border-radius:999px;color:#fff;font-weight:700;font-size:15px;cursor:pointer}
#ab-qa svg{width:18px;height:18px}
#ab-qa .q1{background:linear-gradient(135deg,rgba(var(--ar),1),rgba(var(--ar),.72));box-shadow:0 10px 26px rgba(var(--ar),.4),inset 0 1px 0 rgba(255,255,255,.3)}
#ab-qa .q2{background:linear-gradient(135deg,rgba(var(--ar2),1),rgba(var(--ar2),.72));box-shadow:0 10px 26px rgba(var(--ar2),.4),inset 0 1px 0 rgba(255,255,255,.3)}
.ab-live{background:#000!important;color:#30d158!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:999px!important;padding:5px 12px 5px 22px!important;position:relative;font-weight:700}
.ab-live:before{content:"";position:absolute;left:9px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:#30d158;box-shadow:0 0 8px #30d158;animation:abPu 1.6s infinite}
@keyframes abPu{50%{opacity:.25}}
.card{animation:abUp .5s cubic-bezier(.2,.9,.2,1) both}
@keyframes abUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
'''

JS = r'''
(function(){
["b1","b2","b3"].forEach(function(c){var x=document.createElement("div");x.className="ab-blob "+c;document.body.appendChild(x)});
var S=function(p){return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+p+'</svg>'};
var IC={
users:S('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.5 3-6 6.5-6s6.5 2.5 6.5 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14c2.2.6 3.5 2.5 3.5 6"/>'),
key:S('<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>'),
hour:S('<path d="M6 3h12M6 21h12M7 3c0 5 5 5 5 9s-5 4-5 9M17 3c0 5-5 5-5 9s5 4 5 9"/>'),
bolt:S('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
link:S('<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>')};
var DEF={"Total Users":["users","c1"],"Active Keys":["key","c2"],"Expired Keys":["hour","c3"],"Activity Today":["bolt","c1"]};
function lf(t){var a=document.querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
function countTo(el,to){
 var from=parseInt(el.dataset.last||"0",10)||0;
 if(from===to){el.textContent=to;el.dataset.last=String(to);return}
 var t0=performance.now(),dur=800;
 function st(t){var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3),v=Math.round(from+(to-from)*e);el.textContent=v;el.dataset.last=String(v);if(p<1)requestAnimationFrame(st)}
 requestAnimationFrame(st);
}
function goTab(n){
 var t=document.getElementById("tab");if(!t)return;
 var k=t.children;
 for(var i=0;i<k.length;i++){if(k[i].textContent.trim()===n){k[i].click();break}}
 window.scrollTo({top:0,behavior:"smooth"});
}
function run(){
 var first=null;
 Object.keys(DEF).forEach(function(k){
  var el=lf(k);if(!el)return;
  var card=el.parentElement;if(!first)first=card;
  if(!card.dataset.abg){
   card.dataset.abg="1";card.classList.add("ab-rel");
   var b=document.createElement("span");b.className="ab-ic "+DEF[k][1];b.innerHTML=IC[DEF[k][0]];card.appendChild(b);
  }
  var kids=card.querySelectorAll("*"),num=null;
  for(var j=0;j<kids.length;j++){var q=kids[j];if(!q.children.length&&/^\d+$/.test(q.textContent.trim())){num=q;break}}
  if(num){var to=parseInt(num.textContent.trim(),10);if(String(to)!==num.dataset.last&&!num.dataset.run){num.dataset.run="1";countTo(num,to);setTimeout(function(){delete num.dataset.run},900)}}
 });
 if(first&&!document.getElementById("ab-qa")){
  var g=first.parentElement;
  g.insertAdjacentHTML("afterend",'<div id="ab-qa"><button class="q1" data-g="Keys">'+IC.key+'Generate key</button><button class="q2" data-g="Referrals">'+IC.link+'Create code</button></div>');
  var bs=document.querySelectorAll("#ab-qa button");
  for(var i=0;i<bs.length;i++)(function(b){b.onclick=function(){goTab(b.dataset.g)}})(bs[i]);
 }
 var lv=lf("Live");if(lv)lv.classList.add("ab-live");
}
setInterval(function(){try{run()}catch(e){}},1200);
})();
'''

i = d.rfind("</style>")
d = d[:i] + CSS + d[i:]
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Glass waa la dhisay")
