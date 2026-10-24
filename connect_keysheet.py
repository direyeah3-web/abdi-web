import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'KEY SHEET' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_keysheet')
css=r'''
/* ===== KEY SHEET ===== */
#ks-o{position:fixed;inset:0;z-index:99998;background:rgba(0,0,0,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);display:flex;align-items:flex-end;transition:opacity .2s}
#ks-o.out{opacity:0}
#ks-o .ks{width:100%;max-height:90%;overflow:auto;background:#1c1c1e;border-radius:30px 30px 0 0;border:1px solid rgba(255,255,255,.10);border-bottom:none;padding:10px 20px calc(env(safe-area-inset-bottom,0px) + 22px);animation:ksUp .34s cubic-bezier(.2,.8,.2,1)}
@keyframes ksUp{from{transform:translateY(100%)}to{transform:none}}
#ks-o .ks-g{width:40px;height:5px;border-radius:3px;background:rgba(255,255,255,.25);margin:4px auto 16px}
#ks-o .ks-k{font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:22px;font-weight:700;color:#fff;letter-spacing:.04em;word-break:break-all}
#ks-o .ks-p{display:inline-block;margin:10px 0 6px;padding:5px 13px;border-radius:999px;font-size:13px;font-weight:600;background:rgba(48,209,88,.16);color:#30d158}
#ks-o .ks-p.r{background:rgba(255,69,58,.16);color:#ff453a}
#ks-o .ks-p.o{background:rgba(255,255,255,.12);color:rgba(235,235,245,.6)}
#ks-o .ks-i{background:rgba(255,255,255,.06);border-radius:20px;padding:4px 16px;margin:10px 0 16px}
#ks-o .ks-r{display:flex;justify-content:space-between;gap:12px;padding:13px 0;border-bottom:.5px solid rgba(255,255,255,.08);font-size:16px;color:#fff}
#ks-o .ks-r:last-child{border-bottom:none}
#ks-o .ks-r span{color:rgba(235,235,245,.5)}
#ks-o .ks-r b{font-weight:600;text-align:right}
#ks-o .ks-l{font-size:13px;font-weight:600;color:rgba(235,235,245,.5);margin:6px 0 8px;letter-spacing:.02em}
#ks-o .ks-x{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px}
#ks-o button{border:none;border-radius:999px;padding:14px 8px;font-size:16px;font-weight:600;color:#fff;background:rgba(255,255,255,.12)}
#ks-o button:active{transform:scale(.96)}
#ks-o .ks-x button{background:rgba(10,132,255,.18);color:#0a84ff}
#ks-o textarea{width:100%;box-sizing:border-box;min-height:104px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.10);border-radius:18px;padding:14px;color:#fff;font-size:16px;font-family:inherit;resize:none}
#ks-o .ks-b{display:flex;gap:10px;margin-top:12px}
#ks-o .ks-b button{flex:1}
#ks-o .ks-b .pr{background:#0a84ff;box-shadow:0 8px 24px rgba(10,132,255,.35)}
.kc{cursor:pointer}
/* ===== /KEY SHEET ===== */
'''
js=r'''
/* ===== KEY SHEET JS ===== */
(function(){
var busy=false;
function T(m){try{toast(m)}catch(e){}}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function close(){var o=document.getElementById("ks-o");if(o){o.classList.add("out");setTimeout(function(){o.remove()},200)}}
function find(r,re,num){var k=Object.keys(r);for(var i=0;i<k.length;i++){if(re.test(k[i])&&(!num||typeof r[k[i]]==="number"))return k[i]}return null}
function fd(t){return new Date(t).toLocaleDateString("en-GB",{day:"numeric",month:"short",year:"numeric"})}
function act(r){if("is_active" in r)return r.is_active!==false;if(typeof r.status==="string")return /^active$/i.test(r.status);if("active" in r)return r.active!==false;return true}
function msg(r,EF,DF){
 var l=["🔑 Key-gaaga:",r.key];
 if(EF&&r[EF])l.push("","⏳ Dhacaya: "+fd(r[EF]));
 if(DF&&r[DF])l.push("📱 Devices: "+r[DF]);
 l.push("","Mahadsanid! 🙏");return l.join("\n")}
function render(r){
 var o=document.getElementById("ks-o");if(!o)return;
 var EF=find(r,/expir|valid_until|ends/i),DF=find(r,/^(devices|max_devices|device_limit|max_dev\w*)$/i,true)||find(r,/device/i,true);
 var now=Date.now(),e=EF&&r[EF]?new Date(r[EF]).getTime():null,gone=e&&e<now,on=act(r);
 var pill=gone?'<span class="ks-p r">Expired</span>':(on?'<span class="ks-p">Active</span>':'<span class="ks-p o">Disabled</span>');
 var rel="";if(e){var n=Math.ceil((e-now)/864e5);rel=n>=0?" ("+n+"d left)":" ("+Math.abs(n)+"d ago)"}
 var rows="";
 if(EF)rows+='<div class="ks-r"><span>Expires</span><b>'+(e?fd(e)+rel:"-")+'</b></div>';
 if(DF)rows+='<div class="ks-r"><span>Devices</span><b>'+esc(r[DF])+'</b></div>';
 if(r.assigned_to)rows+='<div class="ks-r"><span>Assigned to</span><b>'+esc(r.assigned_to)+'</b></div>';
 if(r.created_at)rows+='<div class="ks-r"><span>Created</span><b>'+fd(r.created_at)+'</b></div>';
 o.innerHTML='<div class="ks"><div class="ks-g"></div><div class="ks-k">'+esc(r.key)+'</div>'+pill+'<div class="ks-i">'+rows+'</div>'+
 (EF?'<div class="ks-l">EXTEND</div><div class="ks-x"><button data-d="7">+7d</button><button data-d="30">+30d</button><button data-d="90">+90d</button></div>':'')+
 '<div class="ks-l">MESSAGE</div><textarea id="ks-m">'+esc(msg(r,EF,DF))+'</textarea><div class="ks-b"><button id="ks-c">Copy</button><button class="pr" id="ks-s">Share</button></div></div>';
 o.querySelectorAll("[data-d]").forEach(function(b){b.onclick=function(){ext(r,EF,+b.getAttribute("data-d"))}});
 o.querySelector("#ks-c").onclick=function(){var t=o.querySelector("#ks-m").value;try{navigator.clipboard.writeText(t).then(function(){T("Waa la koobiyeeyay")},function(){T("Koobi ma suurtagalin")})}catch(x){T("Koobi ma suurtagalin")}};
 o.querySelector("#ks-s").onclick=function(){var t=o.querySelector("#ks-m").value;if(navigator.share){navigator.share({text:t}).catch(function(){})}else{try{navigator.clipboard.writeText(t);T("Waa la koobiyeeyay")}catch(x){}}}}
async function ext(r,EF,days){
 if(busy||!EF)return;busy=true;
 try{
  var cur=r[EF]?new Date(r[EF]).getTime():0,nd=new Date(Math.max(Date.now(),cur)+days*864e5);
  var val=String(r[EF]||"").length===10?nd.toISOString().slice(0,10):nd.toISOString(),b={};b[EF]=val;
  var res=await api("/license_keys?key=eq."+encodeURIComponent(r.key),{method:"PATCH",headers:{"Content-Type":"application/json","Prefer":"return=minimal"},body:JSON.stringify(b)});
  if(res.ok){r[EF]=val;T("+"+days+" maalmood");render(r);try{refresh()}catch(e){}}else T("Khalad "+res.status)
 }catch(e){T("Khalad")}
 busy=false}
function keyOf(card){
 var a=card.querySelectorAll("*");
 for(var i=0;i<a.length;i++){var e=a[i];if(e.children.length||e.closest("button"))continue;
  var t=e.textContent.trim();
  if(t.length>=4&&t.length<=60&&!/\s/.test(t)&&!/^(active|expired|inactive|disabled|copy|delete|deactivate|activate)$/i.test(t))return t}
 return null}
async function open(key){
 var o=document.getElementById("ks-o");if(o)o.remove();
 o=document.createElement("div");o.id="ks-o";o.addEventListener("click",function(e){if(e.target===o)close()});document.body.appendChild(o);
 try{
  var r=await api("/license_keys?select=*&key=eq."+encodeURIComponent(key)+"&limit=1");var j=await r.json();
  if(Array.isArray(j)&&j.length)render(j[0]);else{close();T("Key lama helin")}
 }catch(e){close();T("Khalad")}}
document.addEventListener("click",function(e){
 var c=e.target.closest&&e.target.closest("#v-keys .kc, .kc");if(!c)return;
 if(e.target.closest("button,a,input,select,textarea"))return;
 var k=keyOf(c);if(k)open(k)});
})();
/* ===== /KEY SHEET JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
