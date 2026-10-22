import shutil
shutil.copy("dashboard.html", "dashboard.html.before_theme2")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-theme2" in d:
    print("⚠️ Theme2 hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = r'''/*abdi-theme2*/
html{background:#000!important}
body{background:transparent!important}
.ab-blob{position:fixed;border-radius:50%;filter:blur(70px);z-index:-1;pointer-events:none;opacity:.55;animation:abFloat 16s ease-in-out infinite alternate}
.ab-b1{width:340px;height:340px;background:#0a84ff;top:-90px;right:-90px}
.ab-b2{width:300px;height:300px;background:#bf5af2;bottom:12%;left:-110px;animation-delay:-5s}
.ab-b3{width:260px;height:260px;background:#ff375f;top:42%;right:-120px;opacity:.32;animation-delay:-9s}
@keyframes abFloat{from{transform:translate(0,0) scale(1)}to{transform:translate(-40px,50px) scale(1.18)}}
.ab-side{position:fixed!important;left:10px!important;right:10px!important;top:auto!important;bottom:calc(10px + env(safe-area-inset-bottom,0px))!important;width:auto!important;height:auto!important;min-height:0!important;padding:6px!important;margin:0!important;border-radius:32px!important;z-index:9000!important;background:rgba(30,30,40,.55)!important;backdrop-filter:blur(34px) saturate(190%)!important;-webkit-backdrop-filter:blur(34px) saturate(190%)!important;border:1px solid rgba(255,255,255,.16)!important;box-shadow:0 14px 40px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.2)!important;display:block!important;overflow:hidden}
.ab-nav{display:flex!important;flex-direction:row!important;gap:2px!important;margin:0!important;padding:0!important;width:100%!important}
.ab-ni{flex:1 1 0!important;min-width:0;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center;gap:3px!important;padding:8px 2px!important;border-radius:24px!important;font-size:10px!important;font-weight:600;text-align:center;overflow:hidden}
.ab-ni svg{width:22px!important;height:22px!important;margin:0!important}
.ab-app{display:block!important;grid-template-columns:none!important}
.ab-app>*:not(.ab-side){margin-left:0!important;width:100%!important;max-width:100%!important;box-sizing:border-box!important;padding-bottom:140px!important}
h1{font-size:34px!important;font-weight:800!important;letter-spacing:-.03em!important}
.ab-live{background:#000!important;color:#30d158!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:999px!important;padding:5px 12px 5px 22px!important;position:relative;font-weight:700}
.ab-live:before{content:"";position:absolute;left:9px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:#30d158;box-shadow:0 0 8px #30d158;animation:abPulse 1.6s infinite}
@keyframes abPulse{50%{opacity:.25}}
.ab-ic{position:absolute;top:12px;right:12px;width:30px;height:30px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:16px;box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 4px 12px rgba(0,0,0,.4)}
.ab-rel{position:relative}
.ab-ai{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:9px;margin-right:10px;font-size:14px;background:rgba(255,255,255,.1);vertical-align:middle}
#ab-qa{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0}
#ab-qa button{padding:16px 10px;border:0;border-radius:20px;color:#fff;font-weight:700;font-size:15px;cursor:pointer}
#ab-qa .q1{background:linear-gradient(135deg,#3aa0ff,#0a84ff);box-shadow:0 10px 26px rgba(10,132,255,.45)}
#ab-qa .q2{background:linear-gradient(135deg,#bf5af2,#8e44ec);box-shadow:0 10px 26px rgba(191,90,242,.4)}
#ab-snd{bottom:calc(104px + env(safe-area-inset-bottom,0px))!important}
#ab-lt{position:fixed;right:14px;bottom:calc(158px + env(safe-area-inset-bottom,0px));width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.18);background:rgba(30,30,36,.6);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);color:#fff;font-size:20px;z-index:9999}
html.ab-light{filter:invert(1) hue-rotate(180deg)}
html.ab-light img,html.ab-light video{filter:invert(1) hue-rotate(180deg)}
'''

JS = r'''
(function(){
const $$=(s,r)=>Array.prototype.slice.call((r||document).querySelectorAll(s));
const lf=t=>$$("*").filter(e=>!e.children.length&&e.textContent.trim()===t);
["ab-b1","ab-b2","ab-b3"].forEach(c=>{const x=document.createElement("div");x.className="ab-blob "+c;document.body.appendChild(x)});
let docked=false;
function dock(){
if(docked)return;
const names=["Overview","Keys","Users","Referrals","Analytics","Settings"];
const items=names.map(n=>lf(n)[0]).filter(Boolean);
if(items.length<4)return;
let a=items[0];
while(a&&!items.every(i=>a.contains(i)))a=a.parentElement;
if(!a)return;
let s=a;
while(s.parentElement&&s.parentElement!==document.body&&s.parentElement.getBoundingClientRect().width<innerWidth*0.5)s=s.parentElement;
if(s.parentElement===document.body)return;
Array.prototype.slice.call(s.children).forEach(c=>{if(!c.contains(a)&&!a.contains(c)&&c!==a){if(!items.some(i=>c.contains(i)))c.style.display="none"}});
a.classList.add("ab-nav");
items.forEach(i=>{let n=i;while(n.parentElement&&n.parentElement!==a)n=n.parentElement;n.classList.add("ab-ni")});
s.classList.add("ab-side");
s.parentElement.classList.add("ab-app");
docked=true;
}
function go(n){const e=lf(n)[0];if(e)e.click();window.scrollTo({top:0,behavior:"smooth"})}
const defs={"Total Users":["👥","#0a84ff"],"Active Keys":["🔑","#30d158"],"Expired Keys":["⌛","#ff9f0a"],"Activity Today":["⚡","#bf5af2"]};
function count(el,to){
const from=0,t0=performance.now(),dur=900;
function step(t){const p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3),v=Math.round(from+(to-from)*e);el.textContent=v;el.dataset.last=String(v);if(p<1)requestAnimationFrame(step)}
requestAnimationFrame(step);
}
function rel(raw){
const m=raw.match(/(\d+)\s+(\w+),?\s+(\d+):(\d+)/);if(!m)return null;
const t=new Date(m[1]+" "+m[2]+" "+new Date().getFullYear()+" "+m[3]+":"+m[4]).getTime();
if(isNaN(t))return null;
const mn=Math.floor((Date.now()-t)/6e4);
if(mn<1)return "hadda";
if(mn<60)return mn+" daqiiqo ka hor";
const h=Math.floor(mn/60);
if(h<24)return h+" saac ka hor";
return Math.floor(h/24)+" maalin ka hor";
}
function ico(m){
const s=m.toLowerCase();
if(s.includes("tirtir"))return "🗑️";
if(s.includes("referral"))return "🔗";
if(s.includes("key"))return "🔑";
if(s.includes("akoon")||s.includes("user"))return "👤";
return "•";
}
function ov(){
let first=null;
Object.keys(defs).forEach(k=>{
const el=lf(k)[0];if(!el)return;
const card=el.parentElement;
if(!first)first=card;
if(!card.dataset.ab){card.dataset.ab="1";card.classList.add("ab-rel");
const b=document.createElement("span");b.className="ab-ic";b.textContent=defs[k][0];b.style.background="linear-gradient(135deg,"+defs[k][1]+",rgba(255,255,255,.25))";card.appendChild(b)}
const num=$$("*",card).filter(e=>!e.children.length&&/^\d+$/.test(e.textContent.trim()))[0];
if(num&&num.textContent!==num.dataset.last){const to=parseInt(num.textContent,10);num.dataset.last="";count(num,to)}
});
if(first&&!document.getElementById("ab-qa")){
const g=first.parentElement;
g.insertAdjacentHTML("afterend",'<div id="ab-qa"><button class="q1" data-go="Keys">🔑 Generate key</button><button class="q2" data-go="Referrals">🔗 Create code</button></div>');
$$("#ab-qa button").forEach(b=>b.onclick=()=>go(b.dataset.go));
}
const h=lf("Recent Activity")[0];
if(h){
const box=h.nextElementSibling;
if(box)$$("*",box).filter(e=>e.children.length===2&&/\d+\s+\w+,?\s+\d+:\d+/.test(e.lastElementChild.textContent)||(e.children.length===2&&e.lastElementChild.dataset&&e.lastElementChild.dataset.raw)).forEach(r=>{
const msg=r.firstElementChild,tm=r.lastElementChild;
if(!msg.dataset.ic){msg.dataset.ic="1";const s=document.createElement("span");s.className="ab-ai";s.textContent=ico(msg.textContent);msg.insertBefore(s,msg.firstChild)}
if(!tm.dataset.raw&&/\d+:\d+/.test(tm.textContent)){tm.dataset.raw=tm.textContent;tm.title=tm.textContent}
if(tm.dataset.raw){const x=rel(tm.dataset.raw);if(x&&tm.textContent!==x)tm.textContent=x}
});
}
const lv=lf("Live")[0];if(lv)lv.classList.add("ab-live");
}
const lt=document.createElement("button");lt.id="ab-lt";
const setL=()=>{let l=false;try{l=localStorage.getItem("abdi_light")==="1"}catch(e){}document.documentElement.classList.toggle("ab-light",l);lt.textContent=l?"☀️":"🌙"};
lt.onclick=()=>{let l=false;try{l=localStorage.getItem("abdi_light")==="1";localStorage.setItem("abdi_light",l?"0":"1")}catch(e){}setL()};
document.body.appendChild(lt);setL();
setInterval(()=>{try{dock();ov()}catch(e){}},900);
})();
'''

d = d.replace("</style>", CSS + "</style>", 1)
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Theme2 waa la dhisay")
