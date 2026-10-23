import shutil
shutil.copy("dashboard.html", "dashboard.html.before_final")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-final" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

# dami tarjumaaddii Somali ee hore
old = 'const TR={"Overview":"Guud",'
if old in d:
    d = d.replace(old, 'const TR={"__":"__"},TR_OLD={"Overview":"Guud",', 1)

CSS = r'''/*abdi-final*/
:root{--ac:#f25c05;--cd:#141414}
html,body{background:#000!important}
body{background:radial-gradient(520px 300px at 50% -70px,rgba(242,92,5,.22),transparent 70%),#000!important;background-attachment:fixed!important}
.card{background:linear-gradient(165deg,rgba(242,92,5,.20),rgba(20,20,20,.97) 58%)!important;border:1px solid rgba(255,255,255,.06)!important;border-top-color:rgba(242,92,5,.45)!important;border-radius:22px!important;box-shadow:none!important}
.io-g{background:linear-gradient(165deg,rgba(242,92,5,.12),#141414 55%)!important;border:1px solid rgba(255,255,255,.05);border-top-color:rgba(242,92,5,.35)}
.io-b{color:#fff!important;border-radius:999px!important}
.io-sw.on{background:var(--ac)!important}
button[class*=gen],button[class*=pri],button[class*=btn]:not(.dg):not(.io-b){background:var(--ac)!important;color:#fff!important;border:0!important;border-radius:999px!important;box-shadow:0 8px 22px rgba(242,92,5,.3)!important}
input,select,textarea{background:#171717!important;border:1px solid rgba(255,255,255,.08)!important;border-radius:14px!important;color:#fff}
input:focus,select:focus,textarea:focus{outline:0!important;border-color:var(--ac)!important;box-shadow:0 0 0 3px rgba(242,92,5,.25)!important}
#tab{background:rgba(12,12,12,.95)!important}
#tab>.ab-on{color:var(--ac)!important}
#tab>.ab-on svg{filter:drop-shadow(0 0 8px rgba(242,92,5,.65))}
#ab-toast{position:fixed;top:calc(env(safe-area-inset-top,0px) + 12px);left:50%;transform:translate(-50%,-160%);opacity:0;display:flex;align-items:center;gap:10px;max-width:90vw;padding:9px 20px 9px 9px;border-radius:999px;background:rgba(28,28,30,.92);backdrop-filter:blur(24px) saturate(180%);-webkit-backdrop-filter:blur(24px) saturate(180%);border:1px solid rgba(255,255,255,.1);box-shadow:0 12px 36px rgba(0,0,0,.6);color:#fff;font:600 15px -apple-system,"SF Pro Text",system-ui,sans-serif;z-index:99999;pointer-events:none;transition:transform .55s cubic-bezier(.2,1.35,.4,1),opacity .25s}
#ab-toast.show{transform:translate(-50%,0);opacity:1}
.ab-ti{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:800;color:#000;flex:none}
.ab-ti.ok{background:#30d158}
.ab-ti.bad{background:#ff453a;color:#fff}
.ab-tt{line-height:1.25}
'''

JS = r'''
(function(){
const EX={
"Maamul license keys":"Manage license keys","Liiska akoonnada":"Account list","Tirakoob isticmaal":"Usage stats","Profile iyo doorbidyo":"Profile and preferences",
"Muddo":"Duration","Aaladaha (devices)":"Devices","Tirada":"Quantity","Raadi key…":"Search keys…","Raadi key...":"Search keys…","Raadi user…":"Search users…","Raadi user...":"Search users…",
"Code (ikhtiyaari)":"Code (optional)","Isticmaal ugu badnaan":"Max uses","Auto: ABDI-XXXXXX":"Auto: ABDI-XXXXXX",
"Key la tirtiray":"Key deleted","Referral code la tirtiray":"Referral code deleted","Key lama siin":"No key assigned",
"Wali user ma jiro":"No users yet","Waxba lama helin":"Nothing found","Isku day raadin kale.":"Try a different search.",
"Qaybtan waa la dhisayaa tallaabada xigta.":"Coming soon.","Waa la soo rarayaa...":"Loading...","Data lama helin.":"Couldn't load data.",
"Midna ma dhacayo":"None expiring","Keys guud":"Total keys","Aan la siin":"Unassigned","Referral la isticmaalay":"Referrals used",
"Hawlaha 7 maalmood":"Activity, last 7 days","Keys dhacaya 7 maalmood gudahood":"Keys expiring within 7 days",
"hadda":"just now",
"Akoonka":"Account","Magaca isticmaalaha":"Username","Beddel password":"Change password","Password cusub":"New password","Ku celi password-ka":"Confirm password","Cusboonaysii":"Update",
"Xogta":"Data","Soo deji backup (JSON)":"Export backup (JSON)","Tirtir hawlaha":"Clear activity","Dareenka":"Feedback","Dhawaaqa taabashada":"Touch sounds",
"Nidaamka":"System","Nooca":"Version","Ka bax":"Log out",
"Password-ku waa inuu ahaadaa 6+ xaraf":"Password must be 6+ characters","Labada password isma waafaqaan":"Passwords don't match",
"Password waa la beddelay":"Password updated","Ma suurtagalin":"Couldn't complete","Backup waa la soo dejiyay":"Backup downloaded",
"Hawlaha waa la tirtiray":"Activity cleared","Ma suurtagalin (ogolaansho la'aan)":"Not permitted",
"Ma jiraan keys bannaan. Samee mid Keys-ka.":"No free keys. Create one in Keys.","Waa la koobiyeeyay":"Copied","La koobiyeeyay":"Copied",
"Dhammaan hawlaha ma tirtiraa?":"Clear all activity?","Ma ka baxaysaa?":"Log out?","Dhammaan activity log-ka ma tirtiraa?":"Clear all activity?"
};
const RX=[
[/^Soo dhawoow, (.+)$/,"Welcome, $1"],
[/^Key la siiyay (.+)$/,"Key assigned to $1"],
[/^(\d+) key cusub la sameeyay$/,(m,n)=>n+(n==="1"?" new key created":" new keys created")],
[/^Referral code cusub: (.+)$/,"New referral code: $1"],
[/^Akoon cusub: (.+)$/,"New account: $1"],
[/^(\d+) maalmood$/,"$1 days"],
[/^(\d+) aalad$/,(m,n)=>n+(n==="1"?" device":" devices")],
[/^(\d+) \/ (\d+) la isticmaalay$/,"$1 / $2 used"],
[/^(\d+) daqiiqo ka hor$/,"$1 min ago"],
[/^(\d+) saac ka hor$/,"$1 h ago"],
[/^(\d+) maalin ka hor$/,"$1 d ago"]
];
function T(s){
const t=s.trim();if(!t)return s;
if(EX[t]!==undefined)return s.replace(t,EX[t]);
for(const r of RX){if(r[0].test(t))return s.replace(t,t.replace(r[0],r[1]))}
return s}
function run(root){
const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null);const L=[];let n;
while(n=w.nextNode())L.push(n);
L.forEach(n=>{const p=n.parentNode;if(!p||/^(SCRIPT|STYLE|TEXTAREA)$/.test(p.nodeName))return;const v=T(n.nodeValue);if(v!==n.nodeValue)n.nodeValue=v});
Array.prototype.forEach.call(root.querySelectorAll("[placeholder]"),e=>{const v=T(e.getAttribute("placeholder"));if(v!==e.getAttribute("placeholder"))e.setAttribute("placeholder",v)});
}
let busy=false;
new MutationObserver(()=>{if(busy)return;busy=true;setTimeout(()=>{run(document.body);busy=false},60)}).observe(document.body,{childList:true,subtree:true,characterData:true});
run(document.body);

const _cf=window.confirm.bind(window);
window.confirm=m=>_cf(T(String(m)));

let tm;
function showToast(msg){
msg=T(String(msg==null?"":msg));
let el=document.getElementById("ab-toast");
if(!el){el=document.createElement("div");el.id="ab-toast";document.body.appendChild(el)}
const bad=/error|couldn|not permitted|don.t match|must be|failed|no free/i.test(msg);
el.innerHTML='<span class="ab-ti '+(bad?"bad":"ok")+'">'+(bad?"!":"✓")+'</span><span class="ab-tt"></span>';
el.querySelector(".ab-tt").textContent=msg;
el.classList.remove("show");void el.offsetWidth;el.classList.add("show");
clearTimeout(tm);tm=setTimeout(()=>el.classList.remove("show"),2600);
try{if(navigator.vibrate)navigator.vibrate(bad?[10,40,10]:8)}catch(e){}
}
try{toast=showToast}catch(e){}
window.toast=showToast;
})();
'''

i = d.rfind("</style>")
d = d[:i] + CSS + d[i:]
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Final waa la dhisay")
