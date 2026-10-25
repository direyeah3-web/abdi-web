import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'DYNAMIC ISLAND' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_island')
css=r'''
/* ===== DYNAMIC ISLAND ===== */
[id^="v-"]{padding-top:40px!important}
#ab-di{position:fixed;top:calc(env(safe-area-inset-top,0px) + 8px);left:50%;transform:translateX(-50%);z-index:99990;width:128px;height:34px;border-radius:20px;background:#000;border:1px solid rgba(255,255,255,.14);color:#fff;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.65);transition:width .45s cubic-bezier(.2,.9,.25,1.05),height .45s cubic-bezier(.2,.9,.25,1.05),border-radius .45s;cursor:pointer;-webkit-tap-highlight-color:transparent}
#ab-di.peek{width:min(340px,calc(100vw - 24px));height:64px;border-radius:32px}
#ab-di.full{width:min(340px,calc(100vw - 24px));height:182px;border-radius:34px}
#ab-di .di-idle{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:8px;font-size:13px;font-weight:600;transition:opacity .15s}
#ab-di.peek .di-idle,#ab-di.full .di-idle{opacity:0}
#ab-di .di-dot{width:8px;height:8px;border-radius:50%;background:#30d158;box-shadow:0 0 8px currentColor;color:#30d158}
#ab-di .di-dot.w{background:#ff9f0a;color:#ff9f0a}
#ab-di .di-dot.r{background:#ff453a;color:#ff453a}
#ab-di .di-top{position:absolute;top:0;left:0;right:0;height:64px;display:flex;align-items:center;gap:12px;padding:0 16px;opacity:0;transition:opacity .2s}
#ab-di.peek .di-top,#ab-di.full .di-top{opacity:1;transition-delay:.15s}
#ab-di .di-i{width:38px;height:38px;border-radius:13px;flex:none;display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,rgba(255,255,255,.24),rgba(255,255,255,.08));border:1px solid rgba(255,255,255,.14)}
#ab-di .di-i svg{width:19px;height:19px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
#ab-di .di-m{min-width:0}
#ab-di .di-m b{display:block;font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ab-di .di-m span{font-size:12px;color:rgba(235,235,245,.55)}
#ab-di .di-st{position:absolute;top:64px;left:0;right:0;padding:0 14px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;opacity:0;transition:opacity .2s}
#ab-di.full .di-st{opacity:1;transition-delay:.2s}
#ab-di .di-st div{background:rgba(255,255,255,.08);border-radius:16px;padding:9px 4px;text-align:center}
#ab-di .di-st b{display:block;font-size:22px;font-weight:700}
#ab-di .di-st span{font-size:11px;font-weight:600;color:rgba(235,235,245,.5)}
#ab-di .di-bt{position:absolute;left:14px;right:14px;bottom:14px;height:42px;border:none!important;border-radius:999px!important;background:#0a84ff!important;color:#fff!important;font-size:15px;font-weight:600;opacity:0;transition:opacity .2s}
#ab-di.full .di-bt{opacity:1;transition-delay:.25s}
/* ===== /DYNAMIC ISLAND ===== */
'''
js=r'''
/* ===== DYNAMIC ISLAND JS ===== */
(function(){
var P={
key:'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>',
trash:'<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
link:'<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
ban:'<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
unlock:'<rect x="5" y="11" width="14" height="10" rx="3"/><path d="M8 11V8a4 4 0 0 1 7.5-2"/>',
clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
info:'<circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v5h1"/>'};
var el,st="idle",tm,last=null,K=null,warned=false,exp3=0;
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function tr(s){
 var m,t=String(s||"").trim();
 if(t==="Key la tirtiray"||t==="Key waa la tirtiray")return ["trash","Key deleted"];
 if(t==="Referral code la tirtiray")return ["trash","Referral code deleted"];
 if(m=t.match(/^(\d+) key cusub la sameeyay$/))return ["key",m[1]+(m[1]==="1"?" new key created":" new keys created")];
 if(m=t.match(/^Referral code cusub: (.+)$/))return ["link","New referral code: "+m[1]];
 if(m=t.match(/^Key la siiyay (.+)$/))return ["key","Key assigned to "+m[1]];
 if(m=t.match(/^Akoon cusub: (.+)$/))return ["user","New account: "+m[1]];
 if(m=t.match(/^(.+?) la unban gareeyay$/i))return ["unlock",m[1]+" was unbanned"];
 if(m=t.match(/^(.+?) la ban gareeyay$/i))return ["ban",m[1]+" was banned"];
 return ["info",t]}
function set(s){st=s;el.className=s}
function vib(){try{if(navigator.vibrate)navigator.vibrate([10,40,10])}catch(e){}}
function idleTxt(){var d=el.querySelector(".di-dot"),t=el.querySelector(".di-it");
 if(exp3>0){d.className="di-dot w";t.textContent=exp3+" expiring"}else{d.className="di-dot";t.textContent="Live"}}
function online(ok){var d=el.querySelector(".di-dot"),t=el.querySelector(".di-it");if(!ok){d.className="di-dot r";t.textContent="Offline"}else idleTxt()}
function peek(ic,title,sub){
 if(st==="full")return;
 el.querySelector(".di-i").innerHTML='<svg viewBox="0 0 24 24">'+P[ic]+'</svg>';
 el.querySelector(".di-m").innerHTML='<b>'+esc(title)+'</b><span>'+esc(sub)+'</span>';
 set("peek");vib();clearTimeout(tm);tm=setTimeout(function(){if(st==="peek")set("idle")},4300)}
function EF(){if(!K||!K.length)return null;var k=Object.keys(K[0]);for(var i=0;i<k.length;i++){if(/expir|valid_until|ends/i.test(k[i]))return k[i]}return null}
function isOn(r){if("is_active" in r)return r.is_active!==false;if(typeof r.status==="string")return /^active$/i.test(r.status);if("active" in r)return r.active!==false;return true}
function stats(){
 var f=EF(),now=Date.now(),lv=0,ex=0;exp3=0;
 (K||[]).forEach(function(r){var e=f&&r[f]?new Date(r[f]).getTime():null;
  if(e&&e<now){ex++;return}
  if(!isOn(r))return;lv++;
  if(e&&e-now<=3*864e5)exp3++});
 var b=el.querySelectorAll(".di-st b");
 if(b.length===3){b[0].textContent=lv;b[1].textContent=exp3;b[2].textContent=ex}
 idleTxt()}
async function loadKeys(){
 try{var r=await api("/license_keys?select=*&limit=3000");var j=await r.json();
  if(Array.isArray(j)){K=j;stats();
   if(!warned&&exp3>0){warned=true;setTimeout(function(){peek("clock",exp3+(exp3===1?" key expiring soon":" keys expiring soon"),"Within 3 days")},1500)}}
 }catch(e){}}
async function poll(){
 if(document.hidden)return;
 try{
  var q=last?"&created_at=gt."+encodeURIComponent(last):"";
  var r=await api("/activity?select=message,created_at"+q+"&order=created_at.desc&limit="+(last?5:1));
  var j=await r.json();if(!Array.isArray(j))return;
  online(true);
  if(!last){last=j.length?j[0].created_at:new Date().toISOString();return}
  if(j.length){last=j[0].created_at;var t=tr(j[0].message);peek(t[0],t[1],j.length>1?("+"+(j.length-1)+" more"):"Just now")}
 }catch(e){online(false)}}
function build(){
 if(document.getElementById("ab-di")||!document.body)return;
 el=document.createElement("div");el.id="ab-di";el.className="idle";
 el.innerHTML='<div class="di-idle"><span class="di-dot"></span><span class="di-it">Live</span></div><div class="di-top"><div class="di-i"></div><div class="di-m"></div></div><div class="di-st"><div><b>-</b><span>Live</span></div><div><b>-</b><span>Expiring</span></div><div><b>-</b><span>Expired</span></div></div><button class="di-bt">Refresh</button>';
 document.body.appendChild(el);
 el.addEventListener("click",function(e){
  e.stopPropagation();
  if(e.target.closest&&e.target.closest(".di-bt")){vib();loadKeys();poll();try{refresh()}catch(x){}try{toast("Refreshed")}catch(x){}return}
  clearTimeout(tm);
  if(st==="full"){set("idle");return}
  el.querySelector(".di-i").innerHTML='<svg viewBox="0 0 24 24">'+P.info+'</svg>';
  el.querySelector(".di-m").innerHTML='<b>Overview</b><span>Tap Refresh to update</span>';
  set("full");loadKeys();tm=setTimeout(function(){if(st==="full")set("idle")},9000)});
 document.addEventListener("click",function(){if(st!=="idle"){clearTimeout(tm);set("idle")}});
 loadKeys();poll()}
setInterval(poll,6000);setInterval(loadKeys,60000);
setInterval(build,1000);build();
})();
/* ===== /DYNAMIC ISLAND JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
