import shutil
shutil.copy("dashboard.html", "dashboard.html.before_ios")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-ios" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if END not in d or 'id="tab"' not in d or 'id="side"' not in d or 'if($("v-settings")){' not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = r'''/*abdi-ios*/
:root{--ac:#30d158;--cd:#1c1c1e;--ln:rgba(255,255,255,.07);--mu:#8e8e93}
html,body{background:#000!important;font-family:-apple-system,"SF Pro Text",system-ui,Roboto,sans-serif!important;-webkit-font-smoothing:antialiased;-webkit-tap-highlight-color:transparent}
#side{display:none!important}
.ab-wrap{display:block!important;grid-template-columns:none!important}
#side~*:not(#tab){margin-left:0!important;width:100%!important;max-width:100%!important;box-sizing:border-box!important;padding-bottom:110px!important}
h1{font-size:30px!important;font-weight:700!important;letter-spacing:-.02em!important}
.card{background:var(--cd)!important;border:0!important;border-radius:20px!important;box-shadow:none!important}
#tab{display:flex!important;flex-direction:row!important;position:fixed!important;left:0!important;right:0!important;bottom:0!important;top:auto!important;width:auto!important;height:auto!important;margin:0!important;padding:8px 6px calc(8px + env(safe-area-inset-bottom,0px))!important;gap:0!important;border-radius:0!important;z-index:9000!important;background:rgba(10,10,10,.94)!important;backdrop-filter:blur(24px)!important;-webkit-backdrop-filter:blur(24px)!important;border:0!important;border-top:1px solid var(--ln)!important;box-shadow:none!important}
#tab>*{flex:1 1 0!important;min-width:0!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:4px!important;padding:6px 2px!important;margin:0!important;border:0!important;border-radius:0!important;background:transparent!important;box-shadow:none!important;color:var(--mu)!important;font-size:10px!important;font-weight:500!important;text-align:center;overflow:hidden}
#tab svg{width:24px!important;height:24px!important;margin:0!important}
#tab>.ab-on{color:var(--ac)!important;background:transparent!important}
.io-wrap{padding:4px 0 20px}
.io-h{font-size:13px;color:var(--mu);margin:22px 16px 8px}
.io-g{background:var(--cd);border-radius:20px;overflow:hidden}
.io-r{display:flex;align-items:center;gap:12px;padding:15px 16px;font-size:16px;color:#fff;cursor:pointer;border-top:1px solid var(--ln)}
.io-g>.io-r:first-child{border-top:0}
.io-r:active{background:rgba(255,255,255,.06)}
.io-r.red{color:#ff453a}
.io-i{width:22px;height:22px;display:flex;color:var(--mu)}
.io-r.red .io-i{color:#ff453a}
.io-i svg{width:22px;height:22px}
.io-l{flex:1}
.io-v{color:var(--mu);font-size:15px}
.io-c{color:#636366;font-size:22px;line-height:1}
.io-sw{width:51px;height:31px;border-radius:999px;background:#39393d;position:relative;transition:.25s;flex:none}
.io-sw:after{content:"";position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:50%;background:#fff;transition:.25s}
.io-sw.on{background:var(--ac)}
.io-sw.on:after{transform:translateX(20px)}
.io-f{padding:6px 16px 16px;border-top:1px solid var(--ln)}
.io-f input{width:100%;box-sizing:border-box;margin-top:10px;padding:13px 14px;border-radius:12px;border:0;background:#2c2c2e;color:#fff;font-size:16px}
.io-b{width:100%;margin-top:12px;padding:13px;border:0;border-radius:12px;background:var(--ac);color:#000;font-weight:700;font-size:16px}
'''

JS = r'''
(function(){
const TR={"Overview":"Guud","Keys":"Furayaal","Users":"Dadka","Referrals":"Casuumo","Analytics":"Falanqeyn","Settings":"Dejinta","Total Users":"Isticmaalayaasha","Active Keys":"Furayaal shaqeynaya","Expired Keys":"Furayaal dhacay","Activity Today":"Hawlaha maanta","Recent Activity":"Hawlihii dhowaa","Generate keys":"Samee furayaal","Generate":"Samee","Copy":"Koobi","Deactivate":"Jooji","Delete":"Tirtir","Logout":"Ka bax","Assign key":"Sii furaha","Ban":"Xidh","Unban":"Fur","Create code":"Samee code","Create referral code":"Samee referral code","Active":"Shaqeynaya","Full":"Buuxa","Live":"Toos"};
function tr(root){
const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null);const L=[];let n;
while(n=w.nextNode())L.push(n);
L.forEach(n=>{const p=n.parentNode;if(!p||/^(SCRIPT|STYLE|TEXTAREA)$/.test(p.nodeName))return;const t=n.nodeValue.trim();if(TR[t]!==undefined)n.nodeValue=n.nodeValue.replace(t,TR[t])});
}
let busy=false;
new MutationObserver(()=>{if(busy)return;busy=true;setTimeout(()=>{tr(document.body);busy=false},60)}).observe(document.body,{childList:true,subtree:true,characterData:true});
tr(document.body);

const t=document.getElementById("tab"),s=document.getElementById("side");
if(t&&s){
s.parentElement.classList.add("ab-wrap");
const mark=el=>{Array.prototype.forEach.call(t.children,c=>c.classList.remove("ab-on"));if(el)el.classList.add("ab-on")};
t.addEventListener("click",e=>{let n=e.target;while(n&&n.parentElement!==t)n=n.parentElement;if(n)mark(n)});
setTimeout(()=>mark(Array.prototype.find.call(t.children,c=>/(^|\s)(on|active|act|sel|cur)(\s|$)/.test(c.className))||t.children[0]),300);
}

const AC=window.AudioContext||window.webkitAudioContext;let cx=null;
const snd=()=>{try{return localStorage.getItem("abdi_snd")!=="0"}catch(e){return true}};
function tick(){
if(!snd()||!AC)return;
try{
if(!cx)cx=new AC();
if(cx.state==="suspended")cx.resume();
const tt=cx.currentTime,o=cx.createOscillator(),g=cx.createGain();
o.frequency.setValueAtTime(1400,tt);o.frequency.exponentialRampToValueAtTime(800,tt+.05);
g.gain.setValueAtTime(.0001,tt);g.gain.exponentialRampToValueAtTime(.06,tt+.006);g.gain.exponentialRampToValueAtTime(.0001,tt+.06);
o.connect(g);g.connect(cx.destination);o.start(tt);o.stop(tt+.08);
if(navigator.vibrate)navigator.vibrate(6);
}catch(e){}}
document.addEventListener("pointerdown",e=>{if(e.target.closest&&e.target.closest("button,.io-r,#tab>*"))tick()},true);

const S=document.getElementById("v-settings");
if(S){
const E=x=>String(x==null?"":x).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const hd=()=>({apikey:KEY,Authorization:"Bearer "+localStorage.getItem("abdi_tok"),"Content-Type":"application/json"});
const putPw=pw=>fetch(SB+"/auth/v1/user",{method:"PUT",headers:hd(),body:JSON.stringify({password:pw})});
const P={
user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
lock:'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
down:'<path d="M12 3v12m0 0l-4-4m4 4l4-4M4 21h16"/>',
trash:'<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
vol:'<path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16 9a4 4 0 0 1 0 6"/>',
info:'<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
out:'<path d="M9 4H5v16h4M16 8l4 4-4 4M20 12H9"/>'};
const I=k=>'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+P[k]+'</svg>';
const chev='<span class="io-c">›</span>';
const row=(id,ic,label,right,red)=>'<div class="io-r'+(red?' red':'')+'" id="'+id+'"><span class="io-i">'+I(ic)+'</span><span class="io-l">'+label+'</span>'+(right||'')+'</div>';
const grp=(title,rows)=>'<div class="io-h">'+title+'</div><div class="io-g">'+rows+'</div>';
function renderSettings(){
S.innerHTML='<div class="io-wrap">'
+grp("Akoonka",row("io-u","user","Magaca isticmaalaha",'<span class="io-v">'+E(u)+'</span>')+row("io-pw","lock","Beddel password",chev)
+'<div class="io-f" id="io-pwf" style="display:none"><input id="io-p1" type="password" placeholder="Password cusub"><input id="io-p2" type="password" placeholder="Ku celi password-ka"><button id="io-ps" class="io-b">Cusboonaysii</button></div>')
+grp("Xogta",row("io-ex","down","Soo deji backup (JSON)",chev)+row("io-cl","trash","Tirtir hawlaha",chev,1))
+grp("Dareenka",row("io-sn","vol","Dhawaaqa taabashada",'<span class="io-sw'+(snd()?' on':'')+'" id="io-swv"></span>'))
+grp("Nidaamka",row("io-vr","info","Nooca",'<span class="io-v">Abdi Panel 1.0</span>')+row("io-lo","out","Ka bax",chev,1))
+'</div>';
const q=id=>document.getElementById(id);
q("io-pw").onclick=()=>{const f=q("io-pwf");f.style.display=f.style.display==="none"?"block":"none"};
q("io-ps").onclick=async()=>{
const a=q("io-p1").value,b=q("io-p2").value;
if(a.length<6)return toast("Password-ku waa inuu ahaadaa 6+ xaraf");
if(a!==b)return toast("Labada password isma waafaqaan");
try{
let r=await putPw(a);
if(r.status===401&&await refresh())r=await putPw(a);
if(r.ok){toast("Password waa la beddelay");q("io-p1").value="";q("io-p2").value=""}
else{const j=await r.json().catch(()=>({}));toast(j.msg||j.message||"Ma suurtagalin")}
}catch(e){toast("Error")}};
q("io-ex").onclick=async()=>{
try{
const o={};
for(const tb of ["license_keys","profiles","referral_codes","activity"]){o[tb]=await(await api("/"+tb+"?select=*&limit=10000")).json()}
const bl=new Blob([JSON.stringify(o,null,2)],{type:"application/json"});
const a=document.createElement("a");
a.href=URL.createObjectURL(bl);
a.download="abdi-backup-"+new Date().toISOString().slice(0,10)+".json";
document.body.appendChild(a);a.click();a.remove();
toast("Backup waa la soo dejiyay");
}catch(e){toast("Error")}};
q("io-cl").onclick=async()=>{
if(!confirm("Dhammaan hawlaha ma tirtiraa?"))return;
try{
const r=await api("/activity?created_at=not.is.null",{method:"DELETE",headers:{Prefer:"return=minimal"}});
toast(r.ok?"Hawlaha waa la tirtiray":"Ma suurtagalin (ogolaansho la'aan)");
}catch(e){toast("Error")}};
q("io-sn").onclick=()=>{try{localStorage.setItem("abdi_snd",snd()?"0":"1")}catch(e){}q("io-swv").classList.toggle("on",snd());if(snd())tick()};
q("io-lo").onclick=()=>{if(confirm("Ma ka baxaysaa?"))logout()};
}
let was=false;
const chk=()=>{const v=getComputedStyle(S).display!=="none"&&S.offsetParent!==null;if(v&&!was)renderSettings();was=v};
new MutationObserver(chk).observe(S,{attributes:true,attributeFilter:["class","style","hidden"]});
document.addEventListener("click",()=>setTimeout(chk,80));
chk();
}
})();
'''

d = d.replace('if($("v-settings")){', 'if(false&&$("v-settings")){', 1)
i = d.rfind("</style>")
d = d[:i] + CSS + d[i:]
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ iOS theme waa la dhisay")
