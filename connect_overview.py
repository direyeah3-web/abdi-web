import shutil
shutil.copy("dashboard.html", "dashboard.html.before_ov")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()

def rep(old, new, must=False):
    global d
    if old in d:
        d = d.replace(old, new, 1)
        return True
    print("⚠️ lama helin:", old[:45])
    if must:
        raise SystemExit
    return False

rep('const u=localStorage.getItem("abdi_cur");if(!u)location.replace("index.html");',
    'const u=localStorage.getItem("abdi_cur");if(!u||!localStorage.getItem("abdi_tok"))location.replace("index.html");')
rep('<span class="pill">Frontend demo</span>', '<span class="pill" id="pill">Live</span>')
rep('<div class="lab">Total Users</div><div class="num">0</div>', '<div class="lab">Total Users</div><div class="num" id="s-users">–</div>')
rep('<div class="lab">Active Keys</div><div class="num">0</div>', '<div class="lab">Active Keys</div><div class="num" id="s-active">–</div>')
rep('<div class="lab">Expired Keys</div><div class="num">0</div>', '<div class="lab">Expired Keys</div><div class="num" id="s-expired">–</div>')
rep('<div class="lab">Activity Today</div><div class="num">0</div>', '<div class="lab">Activity Today</div><div class="num" id="s-today">–</div>')
rep('<div class="card empty"><b>Wax hawl ah ma jiraan</b>Marka backend la xiro, halkan ayaa la arki doonaa.</div>',
    '<div class="card" id="act"><div class="empty">Loading…</div></div>')
rep('</style>', '.row{display:flex;justify-content:space-between;gap:12px;padding:12px 4px;border-bottom:1px solid var(--line);font-size:14px}.row:last-child{border:0}.row span:last-child{color:var(--m);white-space:nowrap;font-size:12px}</style>')

JS = r'''
const SB="https://qnbiqgntqhzromwnmyth.supabase.co",KEY="sb_publishable_-jVYtd4Psza1wjuBe8g3CQ_kjxRB4lL";
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
async function refresh(){const rt=localStorage.getItem("abdi_ref");if(!rt)return false;
try{const r=await fetch(SB+"/auth/v1/token?grant_type=refresh_token",{method:"POST",headers:{apikey:KEY,"Content-Type":"application/json"},body:JSON.stringify({refresh_token:rt})});
const j=await r.json();if(r.ok&&j.access_token){localStorage.setItem("abdi_tok",j.access_token);localStorage.setItem("abdi_ref",j.refresh_token||rt);return true}}catch(e){}return false}
async function api(path,opt,retry){opt=opt||{};
const h=Object.assign({apikey:KEY,Authorization:"Bearer "+localStorage.getItem("abdi_tok"),"Content-Type":"application/json"},opt.headers||{});
const r=await fetch(SB+"/rest/v1"+path,Object.assign({},opt,{headers:h}));
if(r.status===401){if(!retry&&await refresh())return api(path,opt,true);logout();throw new Error("auth")}
return r}
async function count(q){const r=await api("/"+q,{method:"HEAD",headers:{Prefer:"count=exact"}});
return parseInt((r.headers.get("content-range")||"").split("/")[1])||0}
async function loadOverview(){
try{
const me=await(await api("/profiles?select=is_admin&username=eq."+encodeURIComponent(u))).json();
if(!me[0]||!me[0].is_admin){document.querySelector("main").innerHTML='<div class="card empty"><b>Ma tihid admin</b>Akoonkan ma laha oggolaansho.<br><br><button class="out" onclick="logout()">Logout</button></div>';return}
const now=new Date().toISOString(),d0=new Date();d0.setHours(0,0,0,0);
const r=await Promise.all([
count("profiles?select=id"),
count("license_keys?select=id&status=eq.active&or=(expires_at.is.null,expires_at.gt."+now+")"),
count("license_keys?select=id&expires_at=lt."+now),
count("activity?select=id&created_at=gte."+d0.toISOString())]);
["s-users","s-active","s-expired","s-today"].forEach((id,i)=>$(id).textContent=r[i]);
const rows=await(await api("/activity?select=message,created_at&order=created_at.desc&limit=8")).json();
$("act").innerHTML=rows.length?rows.map(x=>'<div class="row"><span>'+esc(x.message)+'</span><span>'+new Date(x.created_at).toLocaleString([],{day:"numeric",month:"short",hour:"2-digit",minute:"2-digit"})+'</span></div>').join(""):'<div class="empty"><b>Wax hawl ah ma jiraan</b></div>';
}catch(err){if(err.message!=="auth"){$("pill").textContent="Offline";$("act").innerHTML='<div class="empty"><b>Khalad</b>Xogta lama soo qaadin. Isku day mar kale.</div>'}}}
loadOverview();
'''
rep('go(location.hash.slice(1));', 'go(location.hash.slice(1));' + JS, must=True)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Overview waa lagu xiray Supabase")
