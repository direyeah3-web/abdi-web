import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'SETTINGS HUB' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_settings')
css=r'''
/* ===== SETTINGS HUB ===== */
#v-settings>*:not(#ab-st){display:none!important}
#ab-st .st-h{display:flex;flex-direction:column;align-items:center;padding:6px 0 18px}
#ab-st .st-av{width:92px;height:92px;border-radius:50%;padding:3px;background:linear-gradient(160deg,rgba(255,255,255,.5),rgba(255,255,255,.08));box-shadow:0 12px 34px rgba(0,0,0,.6)}
#ab-st .st-av img{width:100%;height:100%;border-radius:50%;object-fit:cover;display:block;background:#111}
#ab-st .st-n{font-size:26px;font-weight:700;margin-top:12px;letter-spacing:-.02em;color:#fff}
#ab-st .st-pill{margin-top:6px;padding:4px 14px;border-radius:999px;font-size:13px;font-weight:600;background:rgba(10,132,255,.18);color:#0a84ff}
#ab-st .st-s{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:24px}
#ab-st .st-s div{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.035));border:1px solid rgba(255,255,255,.10);border-radius:22px;padding:14px 6px;text-align:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.07)}
#ab-st .st-s b{display:block;font-size:28px;font-weight:700;color:#fff;letter-spacing:-.02em}
#ab-st .st-s span{font-size:12px;font-weight:600;color:rgba(235,235,245,.5)}
#ab-st .st-t{font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:rgba(235,235,245,.45);margin:0 8px 8px}
#ab-st .st-g{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.035));border:1px solid rgba(255,255,255,.10);border-radius:26px;margin-bottom:24px;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 30px rgba(0,0,0,.5)}
#ab-st .st-r{display:flex;align-items:center;gap:14px;padding:13px 16px;border-bottom:.5px solid rgba(255,255,255,.08);color:#fff;font-size:17px;cursor:pointer}
#ab-st .st-r:last-child{border-bottom:none}
#ab-st .st-r:active{background:rgba(255,255,255,.06)}
#ab-st .st-i{width:34px;height:34px;border-radius:11px;flex:none;display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,rgba(255,255,255,.22),rgba(255,255,255,.07));border:1px solid rgba(255,255,255,.14)}
#ab-st .st-i svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
#ab-st .st-l{flex:1;min-width:0}
#ab-st .st-v{color:rgba(235,235,245,.5);font-size:15px;max-width:50%;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#ab-st .st-c{width:8px;height:14px;flex:none;stroke:rgba(235,235,245,.3);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
#ab-st .st-r.d{color:#ff453a}
#ab-st .st-r.d .st-i svg{stroke:#ff453a}
#ab-st .st-sw{width:51px;height:31px;border-radius:999px;background:rgba(120,120,128,.36);position:relative;flex:none;transition:background .2s}
#ab-st .st-sw::after{content:"";position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:50%;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.35);transition:transform .22s cubic-bezier(.2,.8,.2,1)}
#ab-st .st-sw.on{background:#0a84ff}
#ab-st .st-sw.on::after{transform:translateX(20px)}
#ab-st .st-seg{display:flex;background:rgba(255,255,255,.08);border-radius:999px;padding:3px}
#ab-st .st-seg button{padding:7px 14px;border:none!important;background:none!important;color:rgba(235,235,245,.6)!important;font-size:14px;font-weight:600;border-radius:999px!important}
#ab-st .st-seg button.on{background:rgba(255,255,255,.2)!important;color:#fff!important}
#ab-st .st-dot{width:9px;height:9px;border-radius:50%;flex:none}
#ab-st .st-f{text-align:center;color:rgba(235,235,245,.3);font-size:13px;padding:0 0 10px}
#st-o{position:fixed;inset:0;z-index:99997;background:rgba(0,0,0,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);display:flex;align-items:flex-end}
#st-o .ss{width:100%;max-height:90%;overflow:auto;background:#1c1c1e;border-radius:30px 30px 0 0;border:1px solid rgba(255,255,255,.10);border-bottom:none;padding:10px 20px calc(env(safe-area-inset-bottom,0px) + 22px);animation:kxUp .32s cubic-bezier(.2,.8,.2,1)}
#st-o .ss-g{width:40px;height:5px;border-radius:3px;background:rgba(255,255,255,.25);margin:4px auto 16px}
#st-o h3{font-size:22px;margin:0 0 6px;color:#fff}
#st-o p{color:rgba(235,235,245,.6);font-size:15px;margin:0 0 10px;line-height:1.4}
#st-o label{display:block;font-size:13px;font-weight:600;color:rgba(235,235,245,.5);margin:12px 0 6px}
#st-o input,#st-o select{width:100%;box-sizing:border-box}
#st-o .st-e{color:#ff453a;font-size:13px;margin-top:10px;word-break:break-word}
#st-o .st-b{width:100%;margin-top:12px;padding:16px;border:none;border-radius:999px;font-size:17px;font-weight:600;color:#fff;background:rgba(255,255,255,.12)}
#st-o .st-b.p{background:#0a84ff;box-shadow:0 8px 24px rgba(10,132,255,.35);margin-top:18px}
#st-o .st-b.r{background:#ff453a;margin-top:18px}
#pl-o{position:fixed;inset:0;z-index:100000;background:rgba(0,0,0,.86);-webkit-backdrop-filter:blur(30px);backdrop-filter:blur(30px);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;transition:opacity .18s}
#pl-o.out{opacity:0}
#pl-o .pl-t{font-size:22px;font-weight:600;color:#fff}
#pl-o .pl-d{display:flex;gap:18px}
#pl-o .pl-d i{width:14px;height:14px;border-radius:50%;border:1.5px solid #fff}
#pl-o .pl-d i.on{background:#fff}
#pl-o .pl-d.sh{animation:plSh .42s}
@keyframes plSh{0%,100%{transform:none}20%,60%{transform:translateX(-12px)}40%,80%{transform:translateX(12px)}}
#pl-o .pl-k{display:grid;grid-template-columns:repeat(3,76px);gap:18px 22px}
#pl-o .pl-k button{width:76px;height:76px;border-radius:50%!important;border:none!important;background:rgba(255,255,255,.13)!important;color:#fff!important;font-size:32px;font-weight:400;padding:0!important}
#pl-o .pl-k button:active{background:rgba(255,255,255,.34)!important}
#pl-o .pl-k button.pl-x{background:none!important;font-size:26px}
#pl-o .pl-c{background:none!important;border:none!important;color:#fff!important;font-size:17px;padding:8px 20px}
/* ===== /SETTINGS HUB ===== */
'''
js=r'''
/* ===== SETTINGS HUB JS ===== */
(function(){
var D=null,NU=null,ACT=0,PING=null,DEFOK=false,locked=false,hid=0;
var P={
lock:'<rect x="5" y="11" width="14" height="10" rx="3"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
shield:'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
timer:'<circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 2h6"/>',
snd:'<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/>',
sl:'<path d="M4 7h10M18 7h2M4 17h2M10 17h10"/><circle cx="16" cy="7" r="2"/><circle cx="8" cy="17" r="2"/>',
dl:'<path d="M12 3v12M7 10l5 5 5-5M5 21h14"/>',
box:'<rect x="3" y="4" width="18" height="5" rx="1.5"/><path d="M5 9v10h14V9M10 13h4"/>',
trash:'<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
wifi:'<path d="M2 9a15 15 0 0 1 20 0M5.5 12.5a10 10 0 0 1 13 0M9 16a5 5 0 0 1 6 0"/><circle cx="12" cy="19.5" r=".8"/>',
info:'<circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v5h1"/>',
out:'<path d="M10 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h4M15 8l4 4-4 4M19 12H9"/>'};
function g(k,d){try{var v=window.localStorage.getItem(k);return v==null?d:v}catch(e){return d}}
function sv(k,v){try{window.localStorage.setItem(k,v)}catch(e){}}
function rmv(k){try{window.localStorage.removeItem(k)}catch(e){}}
function T(m){try{toast(m)}catch(e){}}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
async function H(p){var b=new TextEncoder().encode("abdi:"+p),d=await crypto.subtle.digest("SHA-256",b);return Array.prototype.map.call(new Uint8Array(d),function(x){return ("0"+x.toString(16)).slice(-2)}).join("")}
function ask(title,cancel,val){
 return new Promise(function(res){
  var old=document.getElementById("pl-o");if(old)old.remove();
  var o=document.createElement("div");o.id="pl-o";
  var ks="";for(var i=1;i<=9;i++)ks+='<button data-n="'+i+'">'+i+'</button>';
  o.innerHTML='<div class="pl-t">'+title+'</div><div class="pl-d"><i></i><i></i><i></i><i></i></div><div class="pl-k">'+ks+'<span></span><button data-n="0">0</button><button class="pl-x" data-x="1">\u232b</button></div>'+(cancel?'<button class="pl-c">Cancel</button>':"<div></div>");
  var pin="",dd=o.querySelector(".pl-d");
  function dots(){o.querySelectorAll(".pl-d i").forEach(function(d,i){d.classList.toggle("on",i<pin.length)})}
  async function done(){
   var ok=true;if(val)ok=await val(pin);
   if(ok){o.classList.add("out");setTimeout(function(){o.remove()},180);res(pin)}
   else{dd.classList.add("sh");setTimeout(function(){pin="";dots();dd.classList.remove("sh")},420)}}
  o.addEventListener("click",function(e){
   var b=e.target.closest&&e.target.closest("button");if(!b)return;
   if(b.classList.contains("pl-c")){o.remove();res(null);return}
   if(b.getAttribute("data-x")){pin=pin.slice(0,-1);dots();return}
   var n=b.getAttribute("data-n");if(n==null||pin.length>=4)return;
   pin+=n;dots();try{if(navigator.vibrate)navigator.vibrate(6)}catch(x){}
   if(pin.length===4)setTimeout(done,120)});
  document.body.appendChild(o)})}
async function lock(){
 if(!g("ab_pin","")||locked)return;locked=true;
 await ask("Enter Passcode",false,async function(p){return (await H(p))===g("ab_pin","")});
 locked=false}
async function pinOn(title){
 var a=await ask(title,true);if(a==null)return;
 var b=await ask("Confirm Passcode",true,async function(x){return x===a});if(b==null)return;
 sv("ab_pin",await H(a));T("Passcode on");render()}
async function pinOff(){
 var cur=g("ab_pin","");
 var p=await ask("Enter Passcode",true,async function(x){return (await H(x))===cur});if(p==null)return;
 rmv("ab_pin");T("Passcode off");render()}
async function pinChange(){
 var cur=g("ab_pin","");
 var p=await ask("Current Passcode",true,async function(x){return (await H(x))===cur});if(p==null)return;
 pinOn("New Passcode")}
document.addEventListener("visibilitychange",function(){
 if(document.hidden){hid=Date.now();return}
 if(!g("ab_pin",""))return;
 if(hid&&Date.now()-hid>=(+g("ab_lt","1"))*60000)lock()});
if(g("ab_pin",""))lock();
function shut(){var o=document.getElementById("st-o");if(o)o.remove()}
function sheet(h){shut();var o=document.createElement("div");o.id="st-o";o.innerHTML='<div class="ss"><div class="ss-g"></div>'+h+'</div>';o.addEventListener("click",function(e){if(e.target===o)shut()});document.body.appendChild(o);return o.firstChild}
function dl(name,text,type){var url=URL.createObjectURL(new Blob([text],{type:type})),a=document.createElement("a");a.href=url;a.download=name;document.body.appendChild(a);a.click();a.remove()}
function EF(){if(!D||!D.length)return null;var k=Object.keys(D[0]);for(var i=0;i<k.length;i++){if(/expir|valid_until|ends/i.test(k[i]))return k[i]}return null}
function isOn(r){if("is_active" in r)return r.is_active!==false;if(typeof r.status==="string")return /^active$/i.test(r.status);if("active" in r)return r.active!==false;return true}
function live(){if(!D)return "-";var f=EF(),now=Date.now(),n=0;D.forEach(function(r){var e=f&&r[f]?new Date(r[f]).getTime():null;if(isOn(r)&&!(e&&e<now))n++});return n}
function sndOn(){var s=document.querySelector("#v-settings .io-sw");return !!(s&&s.classList.contains("on"))}
function oldRow(txt){var rs=document.querySelectorAll("#v-settings .io-r");for(var i=0;i<rs.length;i++){if(rs[i].textContent.indexOf(txt)>=0){rs[i].click();return true}}return false}
function R(ic,lab,right,a,cls){return '<div class="st-r'+(cls?" "+cls:"")+'" data-a="'+a+'"><span class="st-i"><svg viewBox="0 0 24 24">'+P[ic]+'</svg></span><span class="st-l">'+lab+'</span>'+(right||"")+'</div>'}
var CH='<svg class="st-c" viewBox="0 0 8 14"><path d="M1 1l6 6-6 6"/></svg>';
function SW(on){return '<span class="st-sw'+(on?" on":"")+'"></span>'}
function V(t){return '<span class="st-v">'+esc(t)+'</span>'}
function render(){
 var c=document.getElementById("ab-st");if(!c)return;
 var nm=(typeof u!=="undefined"&&u)?u:"admin";
 var pin=!!g("ab_pin",""),lt=g("ab_lt","1"),dd=g("ab_dd","30"),dv=g("ab_dv","1");
 var col=PING===null?"#8e8e93":(PING<0?"#ff453a":"#30d158");
 var ps=PING===null?"Testing...":(PING<0?"Offline":"Online \u00b7 "+PING+" ms");
 var seg='<div class="st-seg">'+[["0","Now"],["1","1m"],["5","5m"]].map(function(x){return '<button data-a="lt" data-v="'+x[0]+'" class="'+(lt===x[0]?"on":"")+'">'+x[1]+'</button>'}).join("")+'</div>';
 var h='<div class="st-h"><div class="st-av"><img src="xero.png" alt=""></div><div class="st-n">'+esc(nm)+'</div><span class="st-pill">Admin</span></div>'+
 '<div class="st-s"><div><b>'+live()+'</b><span>Live keys</span></div><div><b>'+(NU==null?"-":NU)+'</b><span>Users</span></div><div><b>'+ACT+'</b><span>Today</span></div></div>'+
 '<div class="st-t">Security</div><div class="st-g">'+
 R("shield","Passcode Lock",SW(pin),"pin")+
 (pin?R("lock","Change Passcode",CH,"pinc")+'<div class="st-r" style="cursor:default"><span class="st-i"><svg viewBox="0 0 24 24">'+P.timer+'</svg></span><span class="st-l">Auto-lock</span>'+seg+'</div>':"")+
 R("lock","Change password",CH,"pw")+'</div>'+
 '<div class="st-t">Preferences</div><div class="st-g">'+
 R("snd","Touch sounds",SW(sndOn()),"snd")+
 R("sl","Default key",V(dd+" days \u00b7 "+dv+" dev")+CH,"def")+'</div>'+
 '<div class="st-t">Data</div><div class="st-g">'+
 R("dl","Export keys (CSV)",CH,"csv")+
 R("box","Export backup (JSON)",CH,"bk")+
 R("clock","Delete expired keys",CH,"cl","d")+
 R("trash","Clear activity",CH,"ca","d")+'</div>'+
 '<div class="st-t">About</div><div class="st-g">'+
 R("wifi","Server",'<span class="st-dot" style="background:'+col+'"></span>'+V(ps),"ping")+
 R("info","Version",V("Abdi Panel 2.0"),"ver")+
 R("out","Log out","","lo","d")+'</div><div class="st-f">Abdi Panel</div>';
 c.innerHTML=h}
async function loadAll(){
 try{
  var a=await api("/license_keys?select=*&order=created_at.desc&limit=3000"),aj=await a.json();if(Array.isArray(aj))D=aj;
  var b=await api("/profiles?select=id&limit=1000"),bj=await b.json();if(Array.isArray(bj))NU=bj.length;
  var t0=new Date();t0.setHours(0,0,0,0);
  var c=await api("/activity?select=created_at&created_at=gte."+encodeURIComponent(t0.toISOString())+"&limit=1000"),cj=await c.json();if(Array.isArray(cj))ACT=cj.length;
 }catch(e){}
 render();doPing()}
async function doPing(){
 PING=null;render();var t=performance.now();
 try{var r=await api("/activity?select=created_at&limit=1");PING=r.ok?Math.round(performance.now()-t):-1}catch(e){PING=-1}
 render()}
function csv(){
 if(!D||!D.length){T("Xog ma jirto");return}
 var k=Object.keys(D[0]),q=function(v){v=v==null?"":(typeof v==="object"?JSON.stringify(v):String(v));return '"'+v.replace(/"/g,'""')+'"'};
 var t=[k.join(",")].concat(D.map(function(r){return k.map(function(x){return q(r[x])}).join(",")})).join("\n");
 dl("abdi-keys-"+new Date().toISOString().slice(0,10)+".csv",t,"text/csv");T("CSV waa la soo dejiyay")}
function pwSheet(){
 var s=sheet('<h3>Change password</h3><label>New password</label><input id="st-p1" type="password" autocomplete="new-password"><label>Confirm</label><input id="st-p2" type="password" autocomplete="new-password"><div class="st-e"></div><button class="st-b p" id="st-go">Update password</button><button class="st-b" id="st-no">Cancel</button>');
 var er=s.querySelector(".st-e");
 s.querySelector("#st-no").onclick=shut;
 s.querySelector("#st-go").onclick=async function(){
  var b=this,p1=s.querySelector("#st-p1").value,p2=s.querySelector("#st-p2").value;er.textContent="";
  if(p1.length<6){er.textContent="Ugu yaraan 6 xaraf";return}
  if(p1!==p2){er.textContent="Labada password isma laha";return}
  var base=String(typeof SB!=="undefined"?SB:"").replace(/\/(rest|auth)\/v1.*$/,"").replace(/\/+$/,"");
  var tok=g("abdi_tok","").replace(/^"|"$/g,"");
  if(!base||!tok){er.textContent="Session lama helin, dib u gal";return}
  b.disabled=true;
  try{
   var r=await fetch(base+"/auth/v1/user",{method:"PUT",headers:{"apikey":(typeof KEY!=="undefined"?KEY:""),"Authorization":"Bearer "+tok,"Content-Type":"application/json"},body:JSON.stringify({password:p1})});
   if(r.ok){shut();T("Password waa la beddelay")}
   else{var j={};try{j=await r.json()}catch(x){}er.textContent=(j.msg||j.error_description||j.message||("Khalad "+r.status)).slice(0,200);b.disabled=false}
  }catch(x){er.textContent=String(x).slice(0,160);b.disabled=false}}}
function defSheet(){
 var dd=g("ab_dd","30"),dv=g("ab_dv","1");
 var o=[1,7,30,90,365].map(function(d){return '<option value="'+d+'"'+(String(d)===dd?" selected":"")+'>'+d+(d===1?" day":" days")+'</option>'}).join("");
 var s=sheet('<h3>Default key</h3><p>Generate waxay u buuxsami doontaa qiimahan.</p><label>Duration</label><select id="st-dd">'+o+'</select><label>Devices</label><input id="st-dv" type="number" min="1" value="'+esc(dv)+'" inputmode="numeric"><button class="st-b p" id="st-go">Save</button><button class="st-b" id="st-no">Cancel</button>');
 s.querySelector("#st-no").onclick=shut;
 s.querySelector("#st-go").onclick=function(){
  sv("ab_dd",s.querySelector("#st-dd").value);sv("ab_dv",String(Math.max(1,parseInt(s.querySelector("#st-dv").value)||1)));
  DEFOK=false;shut();T("Waa la keydiyay");render()}}
async function cleanSheet(){
 if(!D)await loadAll();
 var f=EF();if(!f){T("Expiry column lama helin");return}
 var now=Date.now(),ex=D.filter(function(r){return r.key&&r[f]&&new Date(r[f]).getTime()<now});
 if(!ex.length){T("Key dhacay ma jiro");return}
 var s=sheet('<h3>Delete expired keys</h3><p>'+ex.length+' key oo dhacay ayaa la tirtirayaa. Backup JSON ayaa hore loo soo dejinayaa.</p><div class="st-e"></div><button class="st-b r" id="st-go">Delete '+ex.length+' keys</button><button class="st-b" id="st-no">Cancel</button>');
 var er=s.querySelector(".st-e");
 s.querySelector("#st-no").onclick=shut;
 s.querySelector("#st-go").onclick=async function(){
  var b=this;b.disabled=true;er.textContent="";
  try{
   dl("abdi-expired-backup-"+new Date().toISOString().slice(0,10)+".json",JSON.stringify(ex,null,1),"application/json");
   await new Promise(function(r){setTimeout(r,900)});
   var ks=ex.map(function(r){return r.key});
   for(var i=0;i<ks.length;i+=40){
    var ch=ks.slice(i,i+40).map(encodeURIComponent).join(",");
    var r=await api("/license_keys?key=in.("+ch+")",{method:"DELETE",headers:{"Prefer":"return=minimal"}});
    if(!r.ok){er.textContent="Khalad "+r.status+": "+(await r.text()).slice(0,160);b.disabled=false;return}}
   shut();T(ks.length+" keys waa la tirtiray");loadAll();try{refresh()}catch(x){}
  }catch(x){er.textContent=String(x).slice(0,160);b.disabled=false}}}
function doA(a,t){
 if(a==="pin"){g("ab_pin","")?pinOff():pinOn("Create Passcode")}
 else if(a==="pinc")pinChange();
 else if(a==="lt"){sv("ab_lt",t.getAttribute("data-v"));render()}
 else if(a==="pw")pwSheet();
 else if(a==="snd"){var s=document.querySelector("#v-settings .io-sw");if(s){s.click();setTimeout(render,90)}else T("Sound switch lama helin")}
 else if(a==="def")defSheet();
 else if(a==="csv"){if(D)csv();else loadAll().then(csv)}
 else if(a==="bk"){if(!oldRow("Export backup"))T("Backup lama helin")}
 else if(a==="cl")cleanSheet();
 else if(a==="ca"){if(!oldRow("Clear activity"))T("Clear activity lama helin")}
 else if(a==="ping")doPing();
 else if(a==="lo"){try{logout()}catch(e){}}}
function applyDef(){
 if(DEFOK)return;var dd=g("ab_dd",""),dv=g("ab_dv","");if(!dd&&!dv){DEFOK=true;return}
 var v=document.getElementById("v-keys");if(!v)return;
 var sel=v.querySelector("select"),ins=[].filter.call(v.querySelectorAll("input"),function(i){return i.type==="number"&&i.id!=="kx-ck"});
 if(!sel||!ins.length)return;
 var ok=false;for(var i=0;i<sel.options.length;i++){if(sel.options[i].value===dd||(sel.options[i].text.match(/\d+/)||[])[0]===dd){sel.value=sel.options[i].value;ok=true;break}}
 if(ok)sel.dispatchEvent(new Event("change",{bubbles:true}));
 if(dv){ins[0].value=dv;ins[0].dispatchEvent(new Event("input",{bubbles:true}))}
 DEFOK=true}
var lt0=0;
function tick(){
 var v=document.getElementById("v-settings");
 if(v&&!document.getElementById("ab-st")){
  var c=document.createElement("div");c.id="ab-st";v.insertBefore(c,v.firstChild);
  c.addEventListener("click",function(e){var t=e.target.closest&&e.target.closest("[data-a]");if(t)doA(t.getAttribute("data-a"),t)});
  render()}
 if(v&&v.offsetParent!==null&&Date.now()-lt0>30000){lt0=Date.now();loadAll()}
 applyDef()}
setInterval(tick,1200);setTimeout(tick,700);
})();
/* ===== /SETTINGS HUB JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
