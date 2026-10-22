import shutil
shutil.copy("index.html", "index.html.before_dash")

HTML = r'''<!DOCTYPE html><html lang="so"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#000"><title>Dashboard</title>
<style>
:root{--card:rgba(255,255,255,.06);--line:rgba(255,255,255,.1);--t:#f5f5f7;--m:#8e8e93;--b:#0a84ff}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;background:radial-gradient(1200px 600px at 80% -10%,#0b1a33 0,#000 55%) fixed;color:var(--t);font-family:-apple-system,"SF Pro Display",Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{padding:20px 18px 110px;max-width:1100px;margin:auto}
header{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px;gap:10px}
h1{font-size:30px;letter-spacing:-.6px;margin:0}.sub{color:var(--m);font-size:14px;margin-top:4px}
.me{display:flex;gap:8px;align-items:center}
.av{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#0a84ff,#5e5ce6);display:grid;place-items:center;font-weight:600;font-size:14px}
.pill{font-size:11px;color:var(--b);background:rgba(10,132,255,.12);border:1px solid rgba(10,132,255,.3);padding:5px 9px;border-radius:20px}
.out{background:var(--card);border:1px solid var(--line);color:var(--t);border-radius:18px;padding:8px 14px;cursor:pointer;font-size:14px;transition:.2s}
.out:active{transform:scale(.95)}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:18px;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);transition:transform .25s,border-color .25s}
.card:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.2)}
.num{font-size:34px;font-weight:700;letter-spacing:-1px;margin-top:6px}.lab{color:var(--m);font-size:13px}
.empty{text-align:center;padding:38px 16px;color:var(--m)}.empty b{display:block;color:var(--t);font-size:17px;margin:0 0 4px}
.sec{margin-top:18px}.sec h3{font-size:18px;margin:0 0 12px}
.view{display:none}.view.on{display:block;animation:in .4s ease}
@keyframes in{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.nb{flex:1;background:none;border:0;color:var(--m);display:flex;flex-direction:column;align-items:center;gap:3px;padding:8px 0;border-radius:20px;font-size:10px;cursor:pointer;transition:.25s}
.nb svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.nb:active{transform:scale(.92)}.nb.on{color:#fff;background:rgba(255,255,255,.1)}
#tab{position:fixed;left:12px;right:12px;bottom:max(12px,env(safe-area-inset-bottom));display:flex;background:rgba(28,28,30,.72);border:1px solid var(--line);border-radius:26px;padding:6px;backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);z-index:9}
#side{display:none}
@media(min-width:900px){
#side{display:flex;flex-direction:column;gap:4px;position:fixed;top:0;bottom:0;left:0;width:240px;padding:26px 16px;border-right:1px solid var(--line);background:rgba(10,10,12,.6);backdrop-filter:blur(24px)}
.brand{font-size:19px;font-weight:700;padding:0 12px 22px;letter-spacing:-.4px}
#side .nb{flex:none;flex-direction:row;justify-content:flex-start;gap:12px;font-size:15px;padding:11px 12px}
#tab{display:none}main{margin-left:240px;max-width:none;padding:34px 40px}.grid{grid-template-columns:repeat(4,1fr)}}
</style></head><body>
<aside id="side"><div class="brand">Abdi</div></aside>
<main>
<header><div><h1 id="ttl"></h1><div class="sub" id="sub"></div></div>
<div class="me"><span class="pill">Frontend demo</span><div class="av" id="av"></div><button class="out" onclick="logout()">Logout</button></div></header>
<section class="view" id="v-overview">
<div class="grid">
<div class="card"><div class="lab">Total Users</div><div class="num">0</div></div>
<div class="card"><div class="lab">Active Keys</div><div class="num">0</div></div>
<div class="card"><div class="lab">Expired Keys</div><div class="num">0</div></div>
<div class="card"><div class="lab">Activity Today</div><div class="num">0</div></div></div>
<div class="sec"><h3>Recent Activity</h3><div class="card empty"><b>Wax hawl ah ma jiraan</b>Marka backend la xiro, halkan ayaa la arki doonaa.</div></div>
</section>
<div id="views"></div>
</main>
<nav id="tab"></nav>
<script>
const u=localStorage.getItem("abdi_cur");if(!u)location.replace("index.html");
const NAV=[
["overview","Overview","Soo dhawoow, "+u,'<path d="M3 11l9-8 9 8v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z"/>'],
["keys","Keys","Maamul license keys",'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>'],
["users","Users","Liiska akoonnada",'<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>'],
["referrals","Referrals","Referral codes",'<path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1"/>'],
["analytics","Analytics","Tirakoob isticmaal",'<path d="M5 20V10M12 20V4M19 20v-7"/>'],
["settings","Settings","Profile iyo doorbidyo",'<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>']];
const btn=n=>`<button class="nb" data-k="${n[0]}" onclick="go('${n[0]}')"><svg viewBox="0 0 24 24">${n[3]}</svg><span>${n[1]}</span></button>`;
$=i=>document.getElementById(i);
$("side").insertAdjacentHTML("beforeend",NAV.map(btn).join(""));
$("tab").innerHTML=NAV.map(btn).join("");
$("views").innerHTML=NAV.slice(1).map(n=>`<section class="view" id="v-${n[0]}"><div class="card empty"><b>${n[1]}</b>Qaybtan waa la dhisayaa tallaabada xigta.</div></section>`).join("");
$("av").textContent=u[0].toUpperCase();
function go(k){const n=NAV.find(x=>x[0]===k)||NAV[0];
document.querySelectorAll(".view").forEach(v=>v.classList.toggle("on",v.id==="v-"+n[0]));
document.querySelectorAll(".nb").forEach(b=>b.classList.toggle("on",b.dataset.k===n[0]));
$("ttl").textContent=n[1];$("sub").textContent=n[2];if(location.hash!=="#"+n[0])history.replaceState(null,"","#"+n[0]);scrollTo(0,0)}
function logout(){localStorage.removeItem("abdi_cur");location.href="index.html"}
go(location.hash.slice(1));
</script></body></html>'''

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("✅ dashboard.html waa la sameeyay")

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()
old = 'function enter(){$("hn").textContent="Soo dhawoow, "+localStorage.getItem("abdi_cur");show("home")}'
if old in c:
    c = c.replace(old, 'function enter(){location.href="dashboard.html"}')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("✅ Login hadda wuxuu u gudbinayaa dashboard.html")
else:
    print("⚠️ enter() lama helin, index.html lama beddelin")
