import shutil
shutil.copy("dashboard.html", "dashboard.html.before_live")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-live" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

old1 = 'r.setProperty("--ar",TH[i][1]);r.setProperty("--ac","rgb("+TH[i][1]+")");'
new1 = 'var q=TH[i][1].split(",");r.setProperty("--cr",q[0]);r.setProperty("--cg",q[1]);r.setProperty("--cb",q[2]);'
if old1 in d:
    d = d.replace(old1, new1, 1)
else:
    print("⚠️ theme3 setProperty lama helin (midabka live ma shaqayn karo)")
old2 = "apply(i+1,false);\n"
if old2 in d and "setInterval(function(){apply(i+1,false)}" not in d:
    d = d.replace(old2, "apply(i+1,false);setInterval(function(){apply(i+1,false)},15000);\n", 1)
else:
    print("⚠️ apply interval lama dhejin karin")

CSS = r'''/*abdi-live*/
@property --cr{syntax:"<number>";inherits:true;initial-value:242}
@property --cg{syntax:"<number>";inherits:true;initial-value:92}
@property --cb{syntax:"<number>";inherits:true;initial-value:5}
:root{--ar:var(--cr),var(--cg),var(--cb);--ac:rgb(var(--cr),var(--cg),var(--cb));transition:--cr 2.2s ease,--cg 2.2s ease,--cb 2.2s ease}
#ab-toast#ab-toast{width:auto!important;height:auto!important;min-height:0!important;max-width:90vw!important;margin:0!important;padding:9px 20px 9px 9px!important;box-sizing:border-box!important;right:auto!important;bottom:auto!important}
#ab-act{background:#141414;border:1px solid rgba(255,255,255,.06);border-radius:22px;padding:4px 0 6px;overflow:hidden}
.ac-h{font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#8e8e93;padding:14px 18px 6px}
.ac-r{display:flex;align-items:center;gap:12px;padding:10px 18px}
.ac-r+.ac-r{border-top:1px solid rgba(255,255,255,.05);margin-left:64px;padding-left:0}
.ac-r+.ac-r .ac-i{margin-left:-64px}
.ac-i{width:36px;height:36px;border-radius:11px;display:flex;align-items:center;justify-content:center;flex:none;color:#fff}
.ac-i svg{width:19px;height:19px}
.ac-m{flex:1;min-width:0}
.ac-t{font-size:15px;font-weight:500;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ac-s{font-size:12px;color:#8e8e93;margin-top:2px}
.ac-e{padding:26px;text-align:center;color:#8e8e93;font-size:14px}
'''

JS = r'''
(function(){
var P={
key:'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>',
trash:'<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
link:'<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
dot:'<circle cx="12" cy="12" r="3"/>'};
var svg=function(k){return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+P[k]+'</svg>'};
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function tr(s){
 var m,t=String(s||"").trim();
 if(t==="Key la tirtiray"||t==="Key waa la tirtiray")return "Key deleted";
 if(t==="Referral code la tirtiray")return "Referral code deleted";
 if(m=t.match(/^(\d+) key cusub la sameeyay$/))return m[1]+(m[1]==="1"?" new key created":" new keys created");
 if(m=t.match(/^Referral code cusub: (.+)$/))return "New referral code: "+m[1];
 if(m=t.match(/^Key la siiyay (.+)$/))return "Key assigned to "+m[1];
 if(m=t.match(/^Akoon cusub: (.+)$/))return "New account: "+m[1];
 return t}
function kind(s){
 var x=s.toLowerCase();
 if(/delet|tirtir/.test(x))return ["trash","#ff453a"];
 if(/referral/.test(x))return ["link","var(--ac)"];
 if(/assign|siiyay/.test(x))return ["key","#0a84ff"];
 if(/account|akoon/.test(x))return ["user","#bf5af2"];
 if(/key/.test(x))return ["key","#30d158"];
 return ["dot","#8e8e93"]}
function two(n){return (n<10?"0":"")+n}
function dayKey(d){return d.getFullYear()+"-"+d.getMonth()+"-"+d.getDate()}
function label(d){
 var n=new Date(),y=new Date(Date.now()-864e5);
 if(dayKey(d)===dayKey(n))return "Today";
 if(dayKey(d)===dayKey(y))return "Yesterday";
 return d.toLocaleDateString([],{day:"numeric",month:"short"})}
function when(d){
 var mn=Math.floor((Date.now()-d.getTime())/6e4);
 if(mn<1)return "Just now";
 if(mn<60)return mn+" min ago";
 if(mn<720)return Math.floor(mn/60)+" h ago";
 return two(d.getHours())+":"+two(d.getMinutes())}
var last="",orig=null;
function lf(t){var a=document.querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
async function tick(){
 try{
  var h=lf("Recent Activity");if(!h)return;
  var a=document.getElementById("ab-act");
  if(!a){a=document.createElement("div");a.id="ab-act"}
  if(h.nextElementSibling!==a){
   var b=h.nextElementSibling;
   if(b&&b.classList&&b.classList.contains("card")){orig=b}
   h.parentNode.insertBefore(a,h.nextSibling);
  }
  if(orig)orig.style.display="none";
  var r=await api("/activity?select=message,created_at&order=created_at.desc&limit=30");
  var rows=await r.json();
  if(!Array.isArray(rows))return;
  var sig=JSON.stringify(rows)+Math.floor(Date.now()/6e4);
  if(sig===last)return;last=sig;
  if(!rows.length){a.innerHTML='<div class="ac-e">No activity yet</div>';return}
  var out="",g="";
  rows.forEach(function(x){
   var d=new Date(x.created_at),l=label(d);
   if(l!==g){g=l;out+='<div class="ac-h">'+esc(l)+'</div>'}
   var msg=tr(x.message),k=kind(String(x.message)+" "+msg);
   var sub=l==="Today"?when(d):two(d.getHours())+":"+two(d.getMinutes());
   out+='<div class="ac-r"><span class="ac-i" style="background:'+k[1]+'">'+svg(k[0])+'</span><div class="ac-m"><div class="ac-t">'+esc(msg)+'</div><div class="ac-s">'+esc(sub)+'</div></div></div>';
  });
  a.innerHTML=out;
 }catch(e){}
}
setInterval(tick,8000);
setTimeout(tick,1200);
document.addEventListener("click",function(){setTimeout(tick,350)});
setInterval(function(){
 try{
  if(document.hidden)return;
  var v=document.getElementById("v-overview");
  if(v&&v.offsetParent===null)return;
  if(typeof loadOverview==="function")loadOverview();
 }catch(e){}
},15000);
})();
'''

i = d.rfind("</style>")
d = d[:i] + CSS + d[i:]
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Live waa la dhisay")
