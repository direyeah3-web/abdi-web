import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'IOS WIDGETS' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_widgets')
css=r'''
/* ===== IOS WIDGETS ===== */
#v-overview .km{display:none!important}
#ab-iw{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:2px 0 26px;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}
#ab-iw .iw-w{position:relative;border-radius:30px;padding:16px 18px;background:linear-gradient(160deg,rgba(255,255,255,.10),rgba(255,255,255,.035));border:1px solid rgba(255,255,255,.11);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 10px 30px rgba(0,0,0,.5);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);color:#fff;min-width:0;transition:box-shadow .2s}
#ab-iw .iw-w.s{min-height:158px;display:flex;flex-direction:column;justify-content:space-between}
#ab-iw .iw-w.w{grid-column:1/-1;min-height:128px;display:flex;align-items:center;gap:18px}
#ab-iw .iw-big{font-size:44px;font-weight:700;letter-spacing:-.03em;line-height:1;font-variant-numeric:tabular-nums;color:#fff}
#ab-iw .iw-b{min-width:0}
#ab-iw .iw-b b{display:block;font-size:17px;font-weight:600;color:#fff;margin-top:4px}
#ab-iw .iw-b span{display:block;font-size:13px;color:rgba(235,235,245,.5);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#ab-iw .iw-b span.m{font-family:ui-monospace,"SF Mono",Menlo,monospace}
#ab-iw .iw-r{width:54px;height:54px;display:block}
#ab-iw .iw-dots{display:grid;grid-template-columns:repeat(7,10px);gap:8px 10px;flex:none}
#ab-iw .iw-dots i{width:10px;height:10px;border-radius:50%;background:#fff}
#ab-iw .iw-bars{display:flex;align-items:flex-end;gap:7px;height:62px;margin-left:auto;flex:none}
#ab-iw .iw-bars i{width:13px;border-radius:7px;background:rgba(255,255,255,.28);min-height:6px}
#ab-iw .iw-bars i.t{background:#fff}
#ab-iw .iw-x{display:none;position:absolute;top:-8px;left:-8px;width:28px;height:28px;border-radius:50%!important;border:none!important;background:rgba(72,72,74,.96)!important;color:#fff!important;font-size:20px;line-height:1;padding:0!important;z-index:3;box-shadow:0 2px 8px rgba(0,0,0,.5)}
#ab-iw.edit .iw-x{display:block}
#ab-iw.edit .iw-w{animation:iwJ .22s infinite alternate;touch-action:none}
@keyframes iwJ{from{transform:rotate(-.7deg)}to{transform:rotate(.7deg)}}
#ab-iw.edit .iw-w.drag{animation:none;transform:scale(1.05);z-index:4;box-shadow:0 22px 50px rgba(0,0,0,.85)}
#ab-iw .iw-add{display:none;min-height:158px;border-radius:30px;border:1.5px dashed rgba(255,255,255,.22);align-items:center;justify-content:center;font-size:40px;font-weight:300;color:rgba(235,235,245,.55);cursor:pointer}
#ab-iw .iw-add.has,#ab-iw.edit .iw-add{display:flex}
#ab-iw .iw-bar{display:none;grid-column:1/-1;justify-content:flex-end}
#ab-iw.edit .iw-bar{display:flex}
#ab-iw .iw-bar button{padding:9px 22px;border-radius:999px!important;border:none!important;background:#0a84ff!important;color:#fff!important;font-size:15px;font-weight:600}
#iw-o{position:fixed;inset:0;z-index:99996;background:rgba(0,0,0,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);display:flex;align-items:flex-end}
#iw-o .ss{width:100%;background:#1c1c1e;border-radius:30px 30px 0 0;border:1px solid rgba(255,255,255,.10);border-bottom:none;padding:10px 20px calc(env(safe-area-inset-bottom,0px) + 22px);animation:kxUp .32s cubic-bezier(.2,.8,.2,1)}
#iw-o .ss-g{width:40px;height:5px;border-radius:3px;background:rgba(255,255,255,.25);margin:4px auto 16px}
#iw-o h3{font-size:22px;margin:0 0 12px;color:#fff}
#iw-o button{width:100%;margin-top:10px;padding:15px;border:none;border-radius:999px;font-size:17px;font-weight:600;color:#fff;background:rgba(255,255,255,.12)}
#iw-o button.p{background:#0a84ff}
#iw-o p{color:rgba(235,235,245,.55);margin:0 0 6px}
/* ===== /IOS WIDGETS ===== */
'''
js=r'''
/* ===== IOS WIDGETS JS ===== */
(function(){
var DEF=["live","users","grid","soon","activity","expired"];
var NAMES={live:"Live keys",users:"Users",grid:"Keys created",soon:"Expiring soon",activity:"Activity",expired:"Expired"};
var SIZE={live:"s",users:"s",expired:"s",grid:"w",soon:"w",activity:"w"};
var S={K:null,nu:null,banned:0,act:null};
var editing=false,drag=null,timer=null,sx=0,sy=0,swallow=0,lastSwap=0,lt=0,el=null;
function g(k,d){try{var v=window.localStorage.getItem(k);return v==null?d:v}catch(e){return d}}
function sv(k,v){try{window.localStorage.setItem(k,v)}catch(e){}}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function cfg(){
 try{var j=JSON.parse(g("ab_iw","null"));
  if(j&&Array.isArray(j.order)&&Array.isArray(j.hidden)){
   DEF.forEach(function(d){if(j.order.indexOf(d)<0)j.order.push(d)});
   j.order=j.order.filter(function(d){return DEF.indexOf(d)>=0});
   j.hidden=j.hidden.filter(function(d){return DEF.indexOf(d)>=0});return j}}catch(e){}
 return {order:DEF.slice(),hidden:[]}}
function save(c){sv("ab_iw",JSON.stringify(c))}
function EF(){if(!S.K||!S.K.length)return null;var k=Object.keys(S.K[0]);for(var i=0;i<k.length;i++){if(/expir|valid_until|ends/i.test(k[i]))return k[i]}return null}
function isOn(r){if("is_active" in r)return r.is_active!==false;if(typeof r.status==="string")return /^active$/i.test(r.status);if("active" in r)return r.active!==false;return true}
function calc(){
 if(!S.K)return null;
 var f=EF(),now=Date.now(),live=0,ex=0,soon=[],t0=new Date();t0.setHours(0,0,0,0);
 var st=t0.getTime()-27*864e5,cnt=[],mx=1,t28=0,i;
 for(i=0;i<28;i++)cnt.push(0);
 S.K.forEach(function(r){
  var e=f&&r[f]?new Date(r[f]).getTime():null;
  if(e&&e<now)ex++;
  else if(isOn(r)){live++;if(e&&e-now<=7*864e5&&r.key)soon.push([r.key,Math.max(0,Math.ceil((e-now)/864e5))])}
  if(r.created_at){var d=new Date(r.created_at);d.setHours(0,0,0,0);var k=Math.round((d.getTime()-st)/864e5);if(k>=0&&k<28){cnt[k]++;t28++}}});
 soon.sort(function(a,b){return a[1]-b[1]});
 cnt.forEach(function(v){if(v>mx)mx=v});
 return {live:live,ex:ex,tot:S.K.length,soon:soon,cnt:cnt,mx:mx,t28:t28}}
function ring(p,n){
 var C=2*Math.PI*21;
 return '<svg class="iw-r" viewBox="0 0 52 52"><circle cx="26" cy="26" r="21" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="5"/><circle cx="26" cy="26" r="21" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-dasharray="'+(C*p)+' '+C+'" transform="rotate(-90 26 26)"/><text x="26" y="31.5" text-anchor="middle" fill="#fff" font-size="'+(String(n).length>2?13:17)+'" font-weight="600">'+n+'</text></svg>'}
function body(id){
 var C=calc(),i;
 if(id==="users")return '<div><div class="iw-big">'+(S.nu==null?"-":S.nu)+'</div></div><div class="iw-b"><b>Users</b><span>'+(S.banned?S.banned+" banned":"all good")+'</span></div>';
 if(!C)return '<div class="iw-b"><b>'+NAMES[id]+'</b><span>Loading...</span></div>';
 if(id==="live")return '<div>'+ring(C.tot?C.live/C.tot:0,C.live)+'</div><div class="iw-b"><b>Live keys</b><span>of '+C.tot+' total</span></div>';
 if(id==="expired")return '<div><div class="iw-big">'+C.ex+'</div></div><div class="iw-b"><b>Expired</b><span>'+(C.ex?"need renewal":"none")+'</span></div>';
 if(id==="grid"){
  var d="";for(i=0;i<28;i++)d+='<i style="opacity:'+(C.cnt[i]?(0.35+0.65*C.cnt[i]/C.mx):0.13)+'"></i>';
  return '<div class="iw-dots">'+d+'</div><div class="iw-b" style="margin-left:auto;text-align:right"><div class="iw-big">'+C.t28+'</div><b>Keys created</b><span>Last 28 days</span></div>'}
 if(id==="soon"){
  var l="";C.soon.slice(0,2).forEach(function(p){l+='<span class="m">'+esc(p[0])+' \u00b7 '+(p[1]===0?"today":p[1]+"d")+'</span>'});
  return '<div class="iw-big">'+C.soon.length+'</div><div class="iw-b" style="flex:1"><b>Expiring soon</b>'+(l||'<span>All clear for 7 days</span>')+'</div>'}
 if(id==="activity"){
  var a=S.act||[0,0,0,0,0,0,0],mx=1,b="";a.forEach(function(v){if(v>mx)mx=v});
  a.forEach(function(v,k){b+='<i class="'+(k===6?"t":"")+'" style="height:'+Math.max(6,Math.round(62*v/mx))+'px"></i>'});
  return '<div class="iw-b"><div class="iw-big">'+a[6]+'</div><b>Activity today</b><span>Last 7 days</span></div><div class="iw-bars">'+b+'</div>'}
 return ""}
function render(){
 if(!el)return;
 var c=cfg(),h='<div class="iw-bar"><button id="iw-done">Done</button></div>';
 c.order.forEach(function(id){if(c.hidden.indexOf(id)>=0)return;h+='<div class="iw-w '+SIZE[id]+'" data-id="'+id+'"><button class="iw-x" data-x="'+id+'">\u2212</button>'+body(id)+'</div>'});
 h+='<div class="iw-add'+(c.hidden.length?" has":"")+'" id="iw-add">+</div>';
 el.innerHTML=h}
function shut(){var o=document.getElementById("iw-o");if(o)o.remove()}
function sheet(){
 shut();var c=cfg(),o=document.createElement("div");o.id="iw-o";
 var l=c.hidden.length?c.hidden.map(function(id){return '<button data-r="'+id+'">+ '+NAMES[id]+'</button>'}).join(""):'<p>Dhammaan widgets waa muuqdaan.</p>';
 o.innerHTML='<div class="ss"><div class="ss-g"></div><h3>Add widget</h3>'+l+'<button data-reset="1">Reset layout</button><button class="p" data-close="1">Close</button></div>';
 o.addEventListener("click",function(e){
  if(e.target===o||(e.target.closest&&e.target.closest("[data-close]"))){shut();return}
  var r=e.target.closest&&e.target.closest("[data-r]");
  if(r){var c2=cfg(),id=r.getAttribute("data-r");c2.hidden=c2.hidden.filter(function(x){return x!==id});c2.order=c2.order.filter(function(x){return x!==id});c2.order.push(id);save(c2);shut();render();return}
  if(e.target.closest&&e.target.closest("[data-reset]")){save({order:DEF.slice(),hidden:[]});shut();render()}});
 document.body.appendChild(o)}
function commit(){
 var ids=[].map.call(el.querySelectorAll(".iw-w"),function(w){return w.getAttribute("data-id")}),c=cfg();
 c.hidden.forEach(function(h){if(ids.indexOf(h)<0)ids.push(h)});
 c.order=ids;save(c)}
function enter(w){
 editing=true;el.classList.add("edit");swallow=Date.now();
 try{if(navigator.vibrate)navigator.vibrate(14)}catch(e){}
 if(w){drag=w;w.classList.add("drag")}}
function exit(){editing=false;el.classList.remove("edit");if(drag){drag.classList.remove("drag");drag=null}render()}
function attach(){
 el.addEventListener("contextmenu",function(e){e.preventDefault()});
 el.addEventListener("touchstart",function(e){
  var w=e.target.closest&&e.target.closest(".iw-w");if(!w)return;
  var t=e.touches[0];sx=t.clientX;sy=t.clientY;
  if(editing){if(e.target.closest(".iw-x"))return;drag=w;w.classList.add("drag");return}
  clearTimeout(timer);timer=setTimeout(function(){timer=null;enter(w)},480)},{passive:true});
 el.addEventListener("touchmove",function(e){
  var t=e.touches[0];
  if(timer&&(Math.abs(t.clientX-sx)>10||Math.abs(t.clientY-sy)>10)){clearTimeout(timer);timer=null}
  if(editing&&drag){
   e.preventDefault();
   var x=document.elementFromPoint(t.clientX,t.clientY),o=x&&x.closest&&x.closest(".iw-w");
   if(o&&o!==drag&&Date.now()-lastSwap>160){
    var ws=[].slice.call(el.querySelectorAll(".iw-w")),a=ws.indexOf(drag),b=ws.indexOf(o);
    el.insertBefore(drag,a<b?o.nextSibling:o);lastSwap=Date.now()}}},{passive:false});
 function end(){clearTimeout(timer);timer=null;if(drag){drag.classList.remove("drag");drag=null;commit()}}
 el.addEventListener("touchend",end);el.addEventListener("touchcancel",end);
 el.addEventListener("click",function(e){
  if(Date.now()-swallow<650)return;
  if(e.target.closest("#iw-done")){exit();return}
  var x=e.target.closest("[data-x]");
  if(x){var id=x.getAttribute("data-x"),c=cfg();if(c.hidden.indexOf(id)<0)c.hidden.push(id);save(c);render();return}
  if(e.target.closest("#iw-add"))sheet()})}
async function load(){
 try{
  var a=await api("/license_keys?select=*&order=created_at.desc&limit=3000"),aj=await a.json();if(Array.isArray(aj))S.K=aj;
  var b=await api("/profiles?select=status&limit=2000"),bj=await b.json();
  if(Array.isArray(bj)){S.nu=bj.length;S.banned=bj.filter(function(p){return /ban/i.test(p.status||"")}).length}
  var t0=new Date();t0.setHours(0,0,0,0);var st=t0.getTime()-6*864e5;
  var c=await api("/activity?select=created_at&created_at=gte."+encodeURIComponent(new Date(st).toISOString())+"&limit=5000"),cj=await c.json();
  if(Array.isArray(cj)){var arr=[0,0,0,0,0,0,0];cj.forEach(function(r){var d=new Date(r.created_at);d.setHours(0,0,0,0);var k=Math.round((d.getTime()-st)/864e5);if(k>=0&&k<7)arr[k]++});S.act=arr}
 }catch(e){}
 if(!editing)render()}
function tick(){
 var v=document.getElementById("v-overview");if(!v)return;
 if(!document.getElementById("ab-iw")){
  var km=v.querySelector(".km");if(!km)return;
  var p=km.parentNode,all=p!==v&&[].every.call(p.children,function(x){return x.classList.contains("km")});
  if(all)p.style.display="none";
  var anchor=all?p:km;
  el=document.createElement("div");el.id="ab-iw";
  anchor.parentNode.insertBefore(el,anchor);
  attach();render();lt=0}
 if(v.offsetParent!==null&&!editing&&Date.now()-lt>30000){lt=Date.now();load()}}
setInterval(tick,1200);setTimeout(tick,700);
})();
/* ===== /IOS WIDGETS JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
