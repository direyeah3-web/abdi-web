import shutil, re
shutil.copy("dashboard.html", "dashboard.html.before_theme3")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-theme3" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

# beddel toast-kii asalka ahaa
d, c1 = re.subn(r'function\s+toast\s*\(', 'function __oldToast(', d)
d, c2 = re.subn(r'\b(?:const|let|var)\s+toast\s*=', 'var __oldToast=', d)
print("toast asal la helay:", c1 + c2)
if c1 + c2 == 0:
    print("❌ toast lama helin, ii soo dir: grep -n 'toast' dashboard.html | cut -c1-160 | head")
    raise SystemExit
d = d.replace("try{toast=showToast}catch(e){}", "")
d = d.replace("window.toast=showToast;", "")

CSS = r'''/*abdi-theme3*/
:root{--ar:242,92,5;--ac:rgb(242,92,5)}
body{background:radial-gradient(560px 320px at 50% -80px,rgba(var(--ar),.24),transparent 70%),#000!important;background-attachment:fixed!important}
.card{background:linear-gradient(165deg,rgba(var(--ar),.18),rgba(20,20,20,.97) 58%)!important;border-top-color:rgba(var(--ar),.5)!important}
.io-g{background:linear-gradient(165deg,rgba(var(--ar),.12),#141414 55%)!important;border-top-color:rgba(var(--ar),.4)!important}
button[class*=gen],button[class*=pri],button[class*=btn]:not(.dg):not(.io-b){background:var(--ac)!important;box-shadow:0 8px 22px rgba(var(--ar),.3)!important}
.io-b,.io-sw.on{background:var(--ac)!important}
input:focus,select:focus,textarea:focus{border-color:var(--ac)!important;box-shadow:0 0 0 3px rgba(var(--ar),.25)!important}
#tab>.ab-on{color:var(--ac)!important}
#tab>.ab-on svg{filter:drop-shadow(0 0 8px rgba(var(--ar),.65))!important}
h1{cursor:pointer}
#ab-toast{position:fixed;top:calc(env(safe-area-inset-top,0px) + 12px);left:50%;transform:translate(-50%,-160%);opacity:0;display:flex;align-items:center;gap:10px;max-width:90vw;width:auto;height:auto;padding:9px 20px 9px 9px;border-radius:999px;background:rgba(28,28,30,.92);backdrop-filter:blur(24px) saturate(180%);-webkit-backdrop-filter:blur(24px) saturate(180%);border:1px solid rgba(255,255,255,.1);box-shadow:0 12px 36px rgba(0,0,0,.6);color:#fff;font:600 15px -apple-system,"SF Pro Text",system-ui,sans-serif;z-index:99999;pointer-events:none;transition:transform .55s cubic-bezier(.2,1.35,.4,1),opacity .25s}
#ab-toast.show{transform:translate(-50%,0);opacity:1}
.ab-ti{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:800;color:#000;flex:none}
.ab-ti.ok{background:#30d158}
.ab-ti.bad{background:#ff453a;color:#fff}
.ab-ti.th{background:var(--ac);color:#fff}
.ab-tt{line-height:1.25}
'''

JS = r'''
var __abTm;
function toast(msg,kind){
  var EX={"Key waa la tirtiray":"Key deleted","Key la tirtiray":"Key deleted","Key waa la joojiyay":"Key deactivated","Key waa la furay":"Key activated","Key waa la koobiyeeyay":"Key copied","Waa la koobiyeeyay":"Copied","La koobiyeeyay":"Copied","Referral code waa la sameeyay":"Referral code created","Referral code waa la tirtiray":"Referral code deleted","Referral code la tirtiray":"Referral code deleted","Password waa la beddelay":"Password updated","Backup waa la soo dejiyay":"Backup downloaded","Hawlaha waa la tirtiray":"Activity cleared","Ma suurtagalin":"Couldn't complete","Ma jiraan keys bannaan. Samee mid Keys-ka.":"No free keys. Create one in Keys."};
  var s=String(msg==null?"":msg).trim(),m;
  if(EX[s]!==undefined)s=EX[s];
  else if(m=s.match(/^(\d+) key waa la sameeyay$/))s=m[1]+(m[1]==="1"?" key created":" keys created");
  else if(m=s.match(/^(\d+) key cusub la sameeyay$/))s=m[1]+(m[1]==="1"?" key created":" keys created");
  else if(m=s.match(/^Key la siiyay (.+)$/))s="Key assigned to "+m[1];
  var bad=kind!=="th"&&/error|couldn|not permitted|don.t match|must be|failed|no free|ma suurtagalin|khalad/i.test(s);
  var el=document.getElementById("ab-toast");
  if(!el){el=document.createElement("div");el.id="ab-toast";document.body.appendChild(el)}
  el.innerHTML='<span class="ab-ti '+(kind==="th"?"th":bad?"bad":"ok")+'">'+(kind==="th"?"●":bad?"!":"✓")+'</span><span class="ab-tt"></span>';
  el.querySelector(".ab-tt").textContent=s;
  el.classList.remove("show");void el.offsetWidth;el.classList.add("show");
  clearTimeout(__abTm);__abTm=setTimeout(function(){el.classList.remove("show")},2600);
  try{if(navigator.vibrate)navigator.vibrate(bad?[10,40,10]:8)}catch(e){}
}
window.toast=toast;
(function(){
var TH=[["Obsidian Orange","242,92,5"],["Ocean Blue","10,132,255"],["Emerald","48,209,88"],["Violet","191,90,242"],["Rose","255,55,95"],["Gold","255,214,10"],["Ice","100,210,255"]];
var i=0;
try{i=parseInt(localStorage.getItem("abdi_th")||"-1",10);if(isNaN(i))i=-1}catch(e){i=-1}
function apply(n,say){
  i=((n%TH.length)+TH.length)%TH.length;
  try{localStorage.setItem("abdi_th",String(i))}catch(e){}
  var r=document.documentElement.style;
  r.setProperty("--ar",TH[i][1]);r.setProperty("--ac","rgb("+TH[i][1]+")");
  if(say)toast(TH[i][0],"th");
}
apply(i+1,false);
document.addEventListener("click",function(e){
  if(e.target.closest&&e.target.closest("h1"))apply(i+1,true);
});
})();
'''

k = d.rfind("</style>")
d = d[:k] + CSS + d[k:]
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Theme3 waa la dhisay")
