import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'CONTROL TAB' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_control')
css=r'''
/* ===== CONTROL TAB ===== */
#ab-cc{display:block}
#ab-cc .cc-c{background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.035));border:1px solid rgba(255,255,255,.10);border-radius:28px;padding:18px;margin-bottom:14px;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 30px rgba(0,0,0,.5)}
#ab-cc .cc-t{font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:rgba(235,235,245,.5);margin-bottom:12px}
#ab-cc .cc-top{display:flex;align-items:center;gap:18px}
#ab-cc .cc-top svg{width:116px;height:116px;flex:none}
#ab-cc .cc-lg{display:flex;flex-direction:column;gap:9px;font-size:15px;color:#fff}
#ab-cc .cc-lg i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:10px}
#ab-cc .cc-lg b{float:right;margin-left:18px}
#ab-cc .cc-g{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;justify-items:center;padding:4px 6px}
#ab-cc .cc-g i{width:12px;height:12px;border-radius:50%;background:#fff}
#ab-cc .cc-g i.t{box-shadow:0 0 0 3px rgba(10,132,255,.55)}
#ab-cc .cc-sg{display:flex;background:rgba(255,255,255,.08);border-radius:999px;padding:4px;margin-bottom:8px}
#ab-cc .cc-sg button{flex:1;padding:10px;border:none!important;background:none!important;color:rgba(235,235,245,.6)!important;font-size:15px;font-weight:600;border-radius:999px!important}
#ab-cc .cc-sg button.on{background:rgba(255,255,255,.18)!important;color:#fff!important}
#ab-cc .cc-r{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:13px 0;border-bottom:.5px solid rgba(255,255,255,.08)}
#ab-cc .cc-r:last-child{border-bottom:none}
#ab-cc .cc-k{min-width:0}
#ab-cc .cc-k b{display:block;font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:15px;color:#fff;letter-spacing:.03em;overflow:hidden;text-overflow:ellipsis}
#ab-cc .cc-k span{font-size:13px;color:rgba(235,235,245,.5)}
#ab-cc .cc-x{display:flex;gap:8px;flex:none}
#ab-cc .cc-x button{padding:9px 14px;border-radius:999px!important;border:none!important;background:#0a84ff!important;color:#fff!important;font-size:14px;font-weight:600}
#ab-cc .cc-x button.g{background:rgba(255,255,255,.12)!important}
#ab-cc .cc-em{color:rgba(235,235,245,.45);text-align:center;padding:22px 0;font-size:15px}
#ab-cc .cc-q{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
#ab-cc .cc-q button{display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 6px;border-radius:22px!important;background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.10)!important;color:#fff!important;font-size:13px;font-weight:600}
#ab-cc .cc-q svg{width:24px;height:24px}
/* ===== /CONTROL TAB ===== */
'''
js=r'''
/* ===== CONTROL TAB JS ===== */
(function(){
var D=null,lt=0,L="soon",busy=false;
function T(m){try{toast(m)}catch(e){}}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function EF(){if(!D||!D.length)return null;var k=Object.keys(D[0]);for(var i=0;i<k.length;i++){if(/expir|valid_until|ends/i.test(k[i]))return k[i]}return null}
function ex(r,f){if(!f||!r[f]||typeof r[f]!=="string")return null;var t=new Date(r[f]).getTime();return isNaN(t)?null:t}
function act(r){if("is_active" in r)return r.is_active!==false;if(typeof r.status==="string")return /^active$/i.test(r.status);if("active" in r)return r.active!==false;return true}
function lf(t){var a=document.querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
function view(){var c=document.getElementById("ab-cc");if(c)return c.parentNode;var vs=document.querySelectorAll('[id^="v-"]');for(var i=0;i<vs.length;i++){if(/Maintenance/.test(vs[i].textContent))return vs[i]}return null}
function rel(e,now){var n=Math.ceil((e-now)/864e5);if(n===0)return "today";if(n>0)return "in "+n+" day"+(n>1?"s":"");return Math.abs(n)+" day"+(Math.abs(n)>1?"s":"")+" ago"}
var IC={csv:'<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>',cp:'<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="3"/><path d="M5 15V6a2 2 0 0 1 2-2h9"/></svg>',rf:'<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11a8 8 0 1 0-2.3 5.7M20 4v7h-7"/></svg>'};
function render(){
 var c=document.getElementById("ab-cc");if(!c)return;
 if(!D){c.innerHTML='<div class="cc-c"><div class="cc-em">Loading...</div></div>';return}
 var f=EF(),now=Date.now(),live=0,exd=0,off=0,soon=[],gone=[];
 D.forEach(function(r){var e=ex(r,f),a=act(r);if(e&&e<now){exd++;gone.push([r,e])}else if(!a)off++;else{live++;if(e&&e-now<=7*864e5)soon.push([r,e])}});
 soon.sort(function(a,b){return a[1]-b[1]});gone.sort(function(a,b){return b[1]-a[1]});
 var tot=live+exd+off||1,C=2*Math.PI*44,dash=C*live/tot;
 var ring='<svg viewBox="0 0 110 110"><circle cx="55" cy="55" r="44" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="10"/><circle cx="55" cy="55" r="44" fill="none" stroke="#0a84ff" stroke-width="10" stroke-linecap="round" stroke-dasharray="'+dash+' '+C+'" transform="rotate(-90 55 55)"/><text x="55" y="64" text-anchor="middle" fill="#fff" font-size="28" font-weight="700">'+live+'</text></svg>';
 var t0=new Date();t0.setHours(0,0,0,0);var st=t0.getTime()-27*864e5,cnt=[],i,mx=1;
 for(i=0;i<28;i++)cnt.push(0);
 D.forEach(function(r){if(!r.created_at)return;var d=new Date(r.created_at);d.setHours(0,0,0,0);var k=Math.round((d.getTime()-st)/864e5);if(k>=0&&k<28)cnt[k]++});
 cnt.forEach(function(v){if(v>mx)mx=v});
 var dots="";for(i=0;i<28;i++)dots+='<i class="'+(i===27?"t":"")+'" style="opacity:'+(cnt[i]?(0.3+0.7*cnt[i]/mx):0.12)+'"></i>';
 var list=L==="soon"?soon:gone,lh="";
 if(!f)lh='<div class="cc-em">Expiry column lama helin</div>';
 else if(!list.length)lh='<div class="cc-em">'+(L==="soon"?"Wax dhacaya 7 maalmood gudahood ma jiraan":"Key dhacay ma jiro")+'</div>';
 else list.slice(0,10).forEach(function(p){var r=p[0];if(!r.key)return;lh+='<div class="cc-r"><div class="cc-k"><b>'+esc(r.key)+'</b><span>'+rel(p[1],now)+'</span></div><div class="cc-x"><button data-a="x" data-k="'+esc(r.key)+'" data-d="7" class="g">+7d</button><button data-a="x" data-k="'+esc(r.key)+'" data-d="30">+30d</button></div></div>'});
 c.innerHTML='<div class="cc-c"><div class="cc-top">'+ring+'<div class="cc-lg"><div><i style="background:#0a84ff"></i>Live<b>'+live+'</b></div><div><i style="background:#ff453a"></i>Expired<b>'+exd+'</b></div><div><i style="background:#8e8e93"></i>Disabled<b>'+off+'</b></div></div></div></div>'+
 '<div class="cc-c"><div class="cc-t">Keys created, 28 days</div><div class="cc-g">'+dots+'</div></div>'+
 '<div class="cc-c"><div class="cc-sg"><button data-a="seg" data-v="soon" class="'+(L==="soon"?"on":"")+'">Expiring ('+soon.length+')</button><button data-a="seg" data-v="gone" class="'+(L==="gone"?"on":"")+'">Expired ('+gone.length+')</button></div>'+lh+'</div>'+
 '<div class="cc-q"><button data-a="csv">'+IC.csv+'Export CSV</button><button data-a="cp">'+IC.cp+'Copy live</button><button data-a="rf">'+IC.rf+'Refresh</button></div>'}
async function load(){
 try{var r=await api("/license_keys?select=*&order=created_at.desc&limit=3000");var j=await r.json();if(Array.isArray(j)){D=j;render()}}catch(e){}}
async function ext(key,days){
 if(busy)return;var f=EF();if(!f)return;var r=D.filter(function(x){return x.key===key})[0];if(!r)return;
 busy=true;
 try{
  var cur=ex(r,f)||0,nd=new Date(Math.max(Date.now(),cur)+days*864e5);
  var val=String(r[f]).length===10?nd.toISOString().slice(0,10):nd.toISOString(),b={};b[f]=val;
  var res=await api("/license_keys?key=eq."+encodeURIComponent(key),{method:"PATCH",headers:{"Content-Type":"application/json","Prefer":"return=minimal"},body:JSON.stringify(b)});
  if(res.ok){r[f]=val;T("+"+days+" maalmood");render();try{refresh()}catch(e){}}
  else T("Khalad "+res.status)
 }catch(e){T("Khalad")}
 busy=false}
function csv(){
 if(!D||!D.length){T("Xog ma jirto");return}
 var k=Object.keys(D[0]);
 var q=function(v){v=v==null?"":(typeof v==="object"?JSON.stringify(v):String(v));return '"'+v.replace(/"/g,'""')+'"'};
 var t=[k.join(",")].concat(D.map(function(r){return k.map(function(x){return q(r[x])}).join(",")})).join("\n");
 var u=URL.createObjectURL(new Blob([t],{type:"text/csv"})),a=document.createElement("a");
 a.href=u;a.download="abdi-keys-"+new Date().toISOString().slice(0,10)+".csv";document.body.appendChild(a);a.click();a.remove();T("CSV waa la soo dejiyay")}
function cp(){
 if(!D)return;var f=EF(),now=Date.now();
 var l=D.filter(function(r){var e=ex(r,f);return act(r)&&!(e&&e<now)&&r.key}).map(function(r){return r.key});
 if(!l.length){T("Key live ah ma jiro");return}
 try{navigator.clipboard.writeText(l.join("\n")).then(function(){T(l.length+" keys waa la koobiyeeyay")},function(){T("Koobi ma suurtagalin")})}catch(e){T("Koobi ma suurtagalin")}}
function tick(){
 var v=view();if(!v)return;
 var c=document.getElementById("ab-cc");
 if(!c){c=document.createElement("div");c.id="ab-cc";v.insertBefore(c,v.firstChild);
  c.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("button");if(!b)return;var a=b.getAttribute("data-a");
   if(a==="seg"){L=b.getAttribute("data-v");render()}
   else if(a==="x")ext(b.getAttribute("data-k"),+b.getAttribute("data-d"))
   else if(a==="csv")csv();else if(a==="cp")cp();else if(a==="rf"){lt=0;T("Refreshing");load()}});
  render()}
 v.querySelectorAll(".card,.io-wrap").forEach(function(x){if(!x.closest("#ab-cc"))x.style.display="none"});
 var h=document.querySelector("h1");if(h&&!h.children.length&&h.textContent.trim()==="Loader")h.textContent="Control";
 var s=lf("Maamul loader-ka online");if(s)s.textContent="Quick actions and insights";
 var tb=document.getElementById("tab");if(tb){var a=tb.querySelectorAll("*");for(var i=0;i<a.length;i++){if(!a[i].children.length&&a[i].textContent.trim()==="Loader")a[i].textContent="Control"}}
 if(v.offsetParent!==null&&Date.now()-lt>20000){lt=Date.now();load()}}
setInterval(tick,1200);setTimeout(tick,700);
})();
/* ===== /CONTROL TAB JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
