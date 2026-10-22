import shutil
shutil.copy("dashboard.html", "dashboard.html.before_users")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()

END = "</script></body></html>"
if "renderUsers" in d:
    print("⚠️ Users hore ayaa loogu daray. Waan joogsaday.")
    raise SystemExit
for need in ("function toast", "function ask", "function pick", "function log"):
    if need not in d:
        print("❌ Waa la waayay:", need, "- waan joogsaday")
        raise SystemExit
if END not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = '.chip{background:rgba(255,255,255,.08);border:1px solid var(--line);color:var(--t);border-radius:12px;padding:6px 10px;font:12px ui-monospace,Menlo,monospace;cursor:pointer}.chip:active{transform:scale(.95)}</style>'

JS = r'''
if($("v-users")){
const U={rows:[],keys:[],q:""};
const uk=id=>U.keys.filter(k=>k.assigned_to===id);
function renderUsers(){const el=$("u-list");
const rows=U.rows.filter(r=>!U.q||r.username.includes(U.q));
if(!U.rows.length){el.innerHTML='<div class="card empty"><b>Wali user ma jiro</b></div>';return}
if(!rows.length){el.innerHTML='<div class="card empty"><b>Waxba lama helin</b>Isku day raadin kale.</div>';return}
el.innerHTML=rows.map(r=>{const ks=uk(r.id);
return '<div class="card kc"><div class="kk">'+esc(r.username)+'</div><div class="km">'
+(r.is_admin?'<span class="bd" style="background:rgba(10,132,255,.15);color:#0a84ff">admin</span>':'')
+'<span class="bd '+(r.status==="active"?"active":"expired")+'">'+r.status+'</span><span>'+new Date(r.created_at).toLocaleDateString([],{day:"numeric",month:"short",year:"numeric"})+'</span></div>'
+(ks.length?'<div class="km" style="margin-top:-4px">'+ks.map(k=>'<button class="chip" data-a="unassign" data-kid="'+k.id+'">'+esc(k.key)+' \u00d7</button>').join("")+'</div>':'<div class="km" style="margin-top:-4px">Key lama siin</div>')
+'<div class="ka"><button data-a="assign" data-id="'+r.id+'">Assign key</button>'
+(r.is_admin?'':'<button class="'+(r.status==="active"?"dg":"")+'" data-a="ban" data-id="'+r.id+'">'+(r.status==="active"?"Ban":"Unban")+'</button>')+'</div></div>'}).join("")}
async function uact(a,id,kid){
try{
if(a==="assign"){const u=U.rows.find(x=>x.id===id);if(!u)return;
const free=U.keys.filter(k=>!k.assigned_to);
if(!free.length)return toast("Ma jiraan keys bannaan. Samee mid Keys-ka.");
const v=await pick("Key u dooro "+u.username,free.map(k=>[k.id,k.key]),null);if(v===null)return;
const x=await api("/license_keys?id=eq."+v,{method:"PATCH",body:JSON.stringify({assigned_to:id})});if(!x.ok)throw 0;
U.keys.find(k=>k.id===v).assigned_to=id;renderUsers();toast("Key waa la siiyay");log("Key la siiyay "+u.username)}
if(a==="unassign"){const k=U.keys.find(x=>x.id===kid);if(!k)return;
if(!await ask("Ka qaad "+k.key+" user-kan?","Ka qaad"))return;
const x=await api("/license_keys?id=eq."+kid,{method:"PATCH",body:JSON.stringify({assigned_to:null})});if(!x.ok)throw 0;
k.assigned_to=null;renderUsers();toast("Waa laga qaaday")}
if(a==="ban"){const u=U.rows.find(x=>x.id===id);if(!u||u.is_admin)return;
const ns=u.status==="active"?"banned":"active";
if(ns==="banned"&&!await ask("Ma ban gareynaysaa "+u.username+"?","Ban"))return;
const x=await api("/profiles?id=eq."+id,{method:"PATCH",body:JSON.stringify({status:ns})});if(!x.ok)throw 0;
u.status=ns;renderUsers();toast(ns==="banned"?"Waa la ban gareeyay":"Waa la unban gareeyay");log(u.username+(ns==="banned"?" la ban gareeyay":" la unban gareeyay"))}
}catch(e){if(!(e&&e.message==="auth"))toast("Khalad: isku day mar kale")}}
async function loadUsers(){$("u-list").innerHTML='<div class="card empty">Loading…</div>';
try{const r=await Promise.all([api("/profiles?select=id,username,is_admin,status,created_at&order=created_at.desc&limit=1000"),api("/license_keys?select=id,key,assigned_to&limit=1000")]);
if(!r[0].ok||!r[1].ok)throw 0;U.rows=await r[0].json();U.keys=await r[1].json();renderUsers()}
catch(e){if(!(e&&e.message==="auth"))$("u-list").innerHTML='<div class="card empty"><b>Khalad</b>Users lama soo qaadin.</div>'}}
$("v-users").innerHTML='<input class="srch" id="u-q" placeholder="Raadi user…" autocomplete="off"><div id="u-list"></div>';
$("u-q").oninput=e=>{U.q=e.target.value.trim().toLowerCase();renderUsers()};
$("u-list").onclick=e=>{const b=e.target.closest("button");if(b)uact(b.dataset.a,b.dataset.id,b.dataset.kid)};
loadUsers();
}
'''

d = d.replace("</style>", CSS, 1)
d = d.replace(END, JS + END, 1)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Users waa la dhisay")
