import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'SEARCH STUDIO' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_ss')
a='/* ===== KEY SHEET JS ===== */\n(function(){\nvar busy=false;'
if s.count(a)==1: s=s.replace(a,a+'\nwindow.abOpenKey=open;')
else: print('Digniin: Key Sheet lama helin, key rows sheet ma furi doonaan')
css=r'''
/* ===== SEARCH STUDIO ===== */
#v-users .card,#v-users .srch,#v-users .empty,#v-referrals .card,#v-referrals .empty{display:none!important}
#ab-sx .sx-bar{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.10);border-radius:999px;padding:0 16px;height:54px;margin-bottom:12px;-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}
#ab-sx .sx-bar svg{width:20px;height:20px;flex:none;fill:none;stroke:rgba(235,235,245,.55);stroke-width:2;stroke-linecap:round}
#ab-sx #sx-q{flex:1;min-width:0;background:none!important;border:none!important;box-shadow:none!important;padding:0!important;height:100%!important;color:#fff!important;font-size:17px!important;outline:none!important}
#ab-sx #sx-x{display:none;width:24px;height:24px;flex:none;border-radius:50%!important;border:none!important;background:rgba(255,255,255,.28)!important;color:#000!important;font-size:16px;line-height:1;padding:0!important}
#ab-sx .sx-ch{display:flex;gap:8px;overflow-x:auto;margin-bottom:16px}
#ab-sx .sx-ch button{flex:none;padding:9px 18px;border-radius:999px!important;border:1px solid rgba(255,255,255,.12)!important;background:rgba(255,255,255,.07)!important;color:rgba(235,235,245,.65)!important;font-size:15px;font-weight:600}
#ab-sx .sx-ch button.on{background:#0a84ff!important;border-color:#0a84ff!important;color:#fff!important}
#ab-sx .sx-h{font-size:12px;font-weight:600;letter-spacing:.08em;color:rgba(235,235,245,.45);margin:4px 6px 8px}
#ab-sx .sx-l{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.035));border:1px solid rgba(255,255,255,.10);border-radius:26px;padding:2px 16px;margin-bottom:18px;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 30px rgba(0,0,0,.5)}
#ab-sx .sx-r{display:flex;align-items:center;gap:13px;padding:12px 0;border-bottom:.5px solid rgba(255,255,255,.08)}
#ab-sx .sx-r:last-child{border-bottom:none}
#ab-sx .sx-r[data-k]{cursor:pointer}
#ab-sx .sx-i,#ab-sx .sx-av{width:42px;height:42px;flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
#ab-sx .sx-i{border-radius:14px;background:linear-gradient(160deg,rgba(255,255,255,.22),rgba(255,255,255,.07));border:1px solid rgba(255,255,255,.14)}
#ab-sx .sx-i svg{width:20px;height:20px}
#ab-sx .sx-av{border-radius:50%;background:linear-gradient(160deg,#48484a,#1c1c1e);border:1px solid rgba(255,255,255,.14);font-weight:700;font-size:17px}
#ab-sx .sx-m{flex:1;min-width:0}
#ab-sx .sx-m b{display:block;color:#fff;font-size:16px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#ab-sx .sx-m b.mono{font-family:ui-monospace,"SF Mono",Menlo,monospace;letter-spacing:.03em}
#ab-sx .sx-m span{font-size:13px;color:rgba(235,235,245,.5)}
#ab-sx .sx-dot{width:9px;height:9px;border-radius:50%;flex:none}
#ab-sx .sx-b{flex:none;padding:8px 16px;border-radius:999px!important;border:none!important;background:rgba(255,255,255,.12)!important;color:#fff!important;font-size:14px;font-weight:600}
#ab-sx .sx-b.r{color:#ff453a!important}
#ab-sx .sx-em{color:rgba(235,235,245,.45);text-align:center;padding:40px 0;font-size:16px}
#ab-sd .sd-c{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.035));border:1px solid rgba(255,255,255,.10);border-radius:28px;padding:18px;margin-bottom:14px;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 30px rgba(0,0,0,.5)}
#ab-sd .sd-t{font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:rgba(235,235,245,.5);margin-bottom:6px}
#ab-sd label{display:block;font-size:13px;font-weight:600;color:rgba(235,235,245,.5);margin:14px 0 6px}
#ab-sd .sd-g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
#ab-sd input,#ab-sd select{width:100%;box-sizing:border-box}
#ab-sd .sd-ch{display:flex;gap:8px;margin-top:8px}
#ab-sd .sd-ch button{flex:1;padding:10px 0;border-radius:999px!important;background:rgba(255,255,255,.09)!important;color:#fff!important;border:1px solid rgba(255,255,255,.10)!important;font-weight:600}
#ab-sd .sd-ch button.on{background:rgba(10,132,255,.22)!important;border-color:#0a84ff!important;color:#0a84ff!important}
#ab-sd #sd-go{width:100%;margin-top:18px;padding:16px;font-size:17px;font-weight:600;color:#fff!important;background:#0a84ff!important;border:none!important;border-radius:999px!important;box-shadow:0 8px 24px rgba(10,132,255,.35)!important}
#ab-sd #sd-go:disabled{opacity:.55}
#ab-sd .sd-e{color:#ff453a;font-size:13px;margin-top:10px;word-break:break-word}
#ab-sd .sd-k{font-family:ui-monospace,"SF Mono",Menlo,monospace;color:#fff;font-size:16px;letter-spacing:.04em;padding:12px 0;border-bottom:.5px solid rgba(255,255,255,.08)}
#ab-sd .sd-a{display:flex;gap:10px;margin-top:16px}
#ab-sd .sd-a button{flex:1;padding:14px;border-radius:999px!important;border:none!important;font-size:16px;font-weight:600;color:#fff!important;background:rgba(255,255,255,.12)!important}
#ab-sd .sd-a button.p{background:#0a84ff!important}
/* ===== /SEARCH STUDIO ===== */
'''
js=r'''
/* ===== SEARCH STUDIO JS ===== */
(function(){
var K=null,U=null,F="all",lt=0,busy=false,LAST=null;
var KSV='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/></svg>';
function T(m){try{toast(m)}catch(e){}}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function lf(t){var a=document.querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
function fd(t){return new Date(t).toLocaleDateString("en-GB",{day:"numeric",month:"short",year:"numeric"})}
function EF(){if(!K||!K.length)return null;var k=Object.keys(K[0]);for(var i=0;i<k.length;i++){if(/expir|valid_until|ends/i.test(k[i]))return k[i]}return null}
function act(r){if("is_active" in r)return r.is_active!==false;if(typeof r.status==="string")return /^active$/i.test(r.status);if("active" in r)return r.active!==false;return true}
function st(r,f,now){var e=f&&r[f]?new Date(r[f]).getTime():null;if(e&&e<now)return ["exp",e];if(!act(r))return ["off",e];return ["live",e]}
function qv(){var i=document.getElementById("sx-q");return i?i.value.trim().toLowerCase():""}
function draw(){
 var box=document.getElementById("sx-res");if(!box)return;
 if(!K&&!U){box.innerHTML='<div class="sx-em">Loading...</div>';return}
 var q=qv(),f=EF(),now=Date.now(),h="",ks=[],us=[];
 (K||[]).forEach(function(r){
  if(!r.key)return;var s=st(r,f,now);
  if(F==="live"&&s[0]!=="live")return;
  if(F==="exp"&&s[0]!=="exp")return;
  if(F==="free"&&r.assigned_to)return;
  if(q&&r.key.toLowerCase().indexOf(q)<0&&String(r.assigned_to||"").toLowerCase().indexOf(q)<0)return;
  ks.push([r,s])});
 if(F==="all")(U||[]).forEach(function(u){if(!u.username)return;if(q&&u.username.toLowerCase().indexOf(q)<0)return;us.push(u)});
 if(us.length){
  h+='<div class="sx-h">USERS ('+us.length+')</div><div class="sx-l">';
  us.slice(0,15).forEach(function(u){
   var bn=/ban/i.test(u.status||"");
   var sub=[u.is_admin?"Admin":null,bn?"Banned":"Active",u.created_at?fd(u.created_at):null].filter(Boolean).join(" \u00b7 ");
   h+='<div class="sx-r"><div class="sx-av">'+esc(u.username.charAt(0).toUpperCase())+'</div><div class="sx-m"><b>'+esc(u.username)+'</b><span>'+esc(sub)+'</span></div>'+(u.is_admin?'':'<button class="sx-b'+(bn?'':' r')+'" data-u="'+esc(u.username)+'">'+(bn?"Unban":"Ban")+'</button>')+'</div>'});
  h+='</div>'}
 if(ks.length){
  h+='<div class="sx-h">KEYS ('+ks.length+')</div><div class="sx-l">';
  ks.slice(0,30).forEach(function(p){
   var r=p[0],s=p[1],col="#30d158",lab="Active";
   if(s[0]==="exp"){col="#ff453a";lab="Expired \u00b7 "+Math.abs(Math.ceil((s[1]-now)/864e5))+"d ago"}
   else if(s[0]==="off"){col="#8e8e93";lab="Disabled"}
   else if(s[1])lab="Active \u00b7 "+Math.max(0,Math.ceil((s[1]-now)/864e5))+"d left";
   if(r.assigned_to)lab+=" \u00b7 "+r.assigned_to;
   h+='<div class="sx-r" data-k="'+esc(r.key)+'"><div class="sx-i">'+KSV+'</div><div class="sx-m"><b class="mono">'+esc(r.key)+'</b><span>'+esc(lab)+'</span></div><span class="sx-dot" style="background:'+col+'"></span></div>'});
  h+='</div>';
  if(ks.length>30)h+='<div class="sx-em" style="padding:0 0 20px">+'+(ks.length-30)+' more, raadi si aad u yaraysato</div>'}
 if(!us.length&&!ks.length)h='<div class="sx-em">Wax lama helin</div>';
 box.innerHTML=h}
async function load(){
 try{
  var a=await api("/license_keys?select=*&order=created_at.desc&limit=3000");var aj=await a.json();if(Array.isArray(aj))K=aj;
  var b=await api("/profiles?select=username,is_admin,status,created_at&order=created_at.desc&limit=500");var bj=await b.json();if(Array.isArray(bj))U=bj;
  draw()
 }catch(e){}}
function toggleUser(name){
 var v=document.getElementById("v-users");if(!v)return;
 var els=v.querySelectorAll("*"),card=null,i;
 for(i=0;i<els.length;i++){var e=els[i];if(!e.children.length&&e.textContent.trim()===name&&!e.closest("#ab-sx")){card=e.closest(".card")||e.parentNode.parentNode;break}}
 if(!card){T("Sug in yar, Users waa la rarayaa");return}
 var bs=card.querySelectorAll("button"),b=null;
 for(i=0;i<bs.length;i++){if(/^(ban|unban)$/i.test(bs[i].textContent.trim())){b=bs[i];break}}
 if(!b){T("Badhan lama helin");return}
 b.click();setTimeout(function(){lt=0;load()},1600)}
function mkSearch(v){
 var c=document.createElement("div");c.id="ab-sx";
 c.innerHTML='<div class="sx-bar"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><input id="sx-q" type="text" placeholder="Search keys or users" autocomplete="off" autocapitalize="off" spellcheck="false"><button id="sx-x">\u00d7</button></div><div class="sx-ch"><button data-f="all" class="on">All</button><button data-f="live">Active</button><button data-f="exp">Expired</button><button data-f="free">Free</button></div><div id="sx-res"></div>';
 v.insertBefore(c,v.firstChild);
 var inp=c.querySelector("#sx-q"),x=c.querySelector("#sx-x");
 inp.addEventListener("input",function(){x.style.display=inp.value?"block":"none";draw()});
 x.addEventListener("click",function(){inp.value="";x.style.display="none";draw();inp.focus()});
 c.addEventListener("click",function(e){
  var b=e.target.closest&&e.target.closest("button[data-f]");
  if(b){F=b.getAttribute("data-f");c.querySelectorAll("[data-f]").forEach(function(z){z.classList.toggle("on",z===b)});draw();return}
  var u=e.target.closest&&e.target.closest("button[data-u]");
  if(u){toggleUser(u.getAttribute("data-u"));return}
  var r=e.target.closest&&e.target.closest("[data-k]");
  if(r){if(window.abOpenKey)window.abOpenKey(r.getAttribute("data-k"));else T("Key Sheet ma jiro")}});
 draw()}
var CH="ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
function rnd(n){var a=new Uint32Array(n),s="",i;crypto.getRandomValues(a);for(i=0;i<n;i++)s+=CH.charAt(a[i]%CH.length);return s}
function gk(p){var g=p?[p,rnd(4),rnd(4)]:[rnd(4),rnd(4),rnd(4),rnd(4)];return g.join("-")}
function build(sm,key,days,dev){
 var r={},k;for(k in sm){r[k]=sm[k]}
 ["id","created_at","updated_at"].forEach(function(f){delete r[f]});
 var exp=new Date(Date.now()+days*864e5).toISOString();
 Object.keys(r).forEach(function(f){
  var v=r[f];
  if(f==="key"){r[f]=key;return}
  if(f==="assigned_to"||/hwid|device_id|fingerprint|last_|activated|used_at|ban_|banned/i.test(f)){r[f]=Array.isArray(v)?[]:(typeof v==="boolean"?false:null);return}
  if(/device/i.test(f)&&/used|count|current|active/i.test(f)&&typeof v==="number"){r[f]=0;return}
  if(/expir|valid_until|ends/i.test(f)&&(typeof v==="string"||v===null)){r[f]=exp;return}
  if(/^(days|duration|duration_days|validity)$/i.test(f)&&typeof v==="number"){r[f]=days;return}
  if(/device|max_dev/i.test(f)&&typeof v==="number"){r[f]=dev;return}
  if(f==="is_active"||f==="active"){r[f]=true;return}
  if(f==="status"&&typeof v==="string"){r[f]=/^active$/i.test(v)?v:"active"}
 });
 return r}
function msgText(){var L=LAST;return "\ud83d\udd11 Keys ("+L.keys.length+")\n"+L.keys.join("\n")+"\n\n\u23f3 "+L.days+" maalmood \u00b7 \ud83d\udcf1 "+L.dev+" device"+(L.dev>1?"s":"")}
function showRes(){
 var c=document.getElementById("sd-r");if(!c||!LAST)return;
 c.style.display="block";
 c.innerHTML='<div class="sd-t">'+LAST.keys.length+' keys ready</div>'+LAST.keys.map(function(k){return '<div class="sd-k">'+esc(k)+'</div>'}).join("")+'<div class="sd-a"><button id="sd-c">Copy all</button><button class="p" id="sd-s">Share all</button></div>'}
async function gen(){
 if(busy)return;
 var e=document.getElementById("sd-e"),go=document.getElementById("sd-go");
 var p=document.getElementById("sd-p").value.toUpperCase().replace(/[^A-Z0-9]/g,"").slice(0,12);
 var days=+document.getElementById("sd-d").value,dev=Math.max(1,parseInt(document.getElementById("sd-v").value)||1),qty=Math.max(1,Math.min(50,parseInt(document.getElementById("sd-q").value)||1));
 e.textContent="";busy=true;go.disabled=true;go.textContent="Generating...";
 try{
  var q=await api("/license_keys?select=*&order=created_at.desc&limit=1");var qj=await q.json();
  if(!Array.isArray(qj)||!qj.length){e.textContent="Marka hore hal key caadi ah ku samee Keys, Generate";return}
  var set={},keys=[];while(keys.length<qty){var k=gk(p);if(!set[k]){set[k]=1;keys.push(k)}}
  var rows=keys.map(function(k){return build(qj[0],k,days,dev)});
  var r=await api("/license_keys",{method:"POST",headers:{"Content-Type":"application/json","Prefer":"return=minimal"},body:JSON.stringify(rows)});
  if(!r.ok){e.textContent="Khalad "+r.status+": "+(await r.text()).slice(0,200);return}
  LAST={keys:keys,days:days,dev:dev};showRes();T(qty+" keys waa la sameeyay");
  lt=0;try{refresh()}catch(x){}
 }catch(x){e.textContent=String(x).slice(0,200)}
 finally{busy=false;go.disabled=false;go.textContent="Generate"}}
function mkStudio(v){
 var c=document.createElement("div");c.id="ab-sd";
 c.innerHTML='<div class="sd-c"><div class="sd-t">Bulk generate</div><label>Prefix (optional)</label><input id="sd-p" type="text" placeholder="ABDI" maxlength="12" autocomplete="off" autocapitalize="characters"><div class="sd-g2"><div><label>Duration</label><select id="sd-d"><option value="1">1 day</option><option value="7">7 days</option><option value="30" selected>30 days</option><option value="90">90 days</option><option value="365">365 days</option></select></div><div><label>Devices</label><input id="sd-v" type="number" min="1" value="1" inputmode="numeric"></div></div><label>Quantity (max 50)</label><input id="sd-q" type="number" min="1" max="50" value="10" inputmode="numeric"><div class="sd-ch"><button data-n="5">5</button><button data-n="10" class="on">10</button><button data-n="25">25</button><button data-n="50">50</button></div><div class="sd-e" id="sd-e"></div><button id="sd-go">Generate</button></div><div class="sd-c" id="sd-r" style="display:none"></div>';
 v.insertBefore(c,v.firstChild);
 c.addEventListener("click",function(e){
  var n=e.target.closest&&e.target.closest("button[data-n]");
  if(n){document.getElementById("sd-q").value=n.getAttribute("data-n");c.querySelectorAll("[data-n]").forEach(function(z){z.classList.toggle("on",z===n)});return}
  var t=e.target.closest&&e.target.closest("button");if(!t)return;
  if(t.id==="sd-go")gen();
  else if(t.id==="sd-c"&&LAST){try{navigator.clipboard.writeText(msgText()).then(function(){T("Waa la koobiyeeyay")},function(){T("Koobi ma suurtagalin")})}catch(x){T("Koobi ma suurtagalin")}}
  else if(t.id==="sd-s"&&LAST){if(navigator.share){navigator.share({text:msgText()}).catch(function(){})}else{try{navigator.clipboard.writeText(msgText());T("Waa la koobiyeeyay")}catch(x){}}}})}
function tabs(){
 var tb=document.getElementById("tab");if(!tb)return;
 var a=tb.querySelectorAll("*");
 for(var i=0;i<a.length;i++){
  var e=a[i];if(e.children.length)continue;
  var t=e.textContent.trim();
  if(t!=="Users"&&t!=="Referrals")continue;
  var m=t==="Users"?["Search",'<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>']:["Studio",'<path d="M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z"/>'];
  e.textContent=m[0];
  var it=e.parentNode,sv=null;
  while(it&&it!==tb&&!(sv=it.querySelector("svg")))it=it.parentNode;
  if(sv)sv.innerHTML='<g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+m[1]+'</g>'}}
function tick(){
 var vu=document.getElementById("v-users"),vr=document.getElementById("v-referrals");
 if(vu&&!document.getElementById("ab-sx"))mkSearch(vu);
 if(vr&&!document.getElementById("ab-sd"))mkStudio(vr);
 tabs();
 var h=document.querySelector("h1");
 if(h&&!h.children.length){var ht=h.textContent.trim();if(ht==="Users")h.textContent="Search";else if(ht==="Referrals")h.textContent="Studio"}
 if(vu&&vu.offsetParent!==null){
  var s1=lf("Account list");if(s1)s1.textContent="Find any key or user";
  if(Date.now()-lt>25000){lt=Date.now();load()}}
 if(vr&&vr.offsetParent!==null){var s2=lf("Referral codes");if(s2)s2.textContent="Bulk generate and share"}}
setInterval(tick,1200);setTimeout(tick,700);
})();
/* ===== /SEARCH STUDIO JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
