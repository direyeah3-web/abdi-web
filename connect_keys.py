import shutil
shutil.copy("dashboard.html", "dashboard.html.before_keys")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()

if "genKeys" in d:
    print("⚠️ Keys hore ayaa loogu daray. Waan joogsaday.")
    raise SystemExit

END = "</script></body></html>"
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo, waan joogsaday")
    raise SystemExit

CSS = r'''.fg{display:grid;grid-template-columns:1fr;gap:12px;margin-bottom:14px}@media(min-width:600px){.fg{grid-template-columns:repeat(3,1fr)}}
.fg label{display:block;color:var(--m);font-size:13px}
.fg input,.fg select,.srch{width:100%;height:48px;margin-top:6px;border-radius:16px;border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--t);padding:0 14px;font-size:16px;outline:0}
.srch{margin:0 0 12px}.fg input:focus,.fg select:focus,.srch:focus{border-color:var(--b)}
.fg option{background:#1c1c1e}
.pbtn{width:100%;height:50px;border:0;border-radius:25px;background:var(--b);color:#fff;font-size:16px;font-weight:600;cursor:pointer;transition:.2s}
.pbtn:active{transform:scale(.97)}.pbtn:disabled{opacity:.5}
.kc{margin-bottom:10px}.kk{font-family:ui-monospace,Menlo,monospace;font-size:16px;letter-spacing:.5px;word-break:break-all}
.km{display:flex;gap:10px;flex-wrap:wrap;color:var(--m);font-size:12px;margin:8px 0 12px;align-items:center}
.bd{padding:3px 9px;border-radius:12px;font-size:11px;font-weight:600;text-transform:capitalize}
.bd.active{background:rgba(48,209,88,.15);color:#30d158}.bd.inactive{background:rgba(255,255,255,.1);color:#aaa}.bd.expired{background:rgba(255,69,58,.15);color:#ff453a}
.ka{display:flex;gap:8px}.ka button{flex:1;height:40px;border-radius:14px;border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--t);font-size:14px;cursor:pointer;transition:.2s}
.ka button:active{transform:scale(.95)}.ka .dg{color:#ff453a}
#mod{position:fixed;inset:0;background:rgba(0,0,0,.6);backdrop-filter:blur(6px);display:none;align-items:center;justify-content:center;z-index:30;padding:20px}
#mod.on{display:flex}#mod .card{max-width:340px;width:100%;background:#1c1c1e}
#toast{position:fixed;left:50%;top:max(16px,env(safe-area-inset-top));transform:translate(-50%,-90px);background:#2c2c2e;color:#fff;border:1px solid var(--line);padding:11px 18px;border-radius:22px;font-size:14px;z-index:40;transition:.35s;max-width:90%}
#toast.on{transform:translate(-50%,0)}
</style>'''

JS = r'''
if($("v-keys")){
const K={rows:[],q:""};
function toast(m){let t=$("toast");if(!t){t=document.createElement("div");t.id="toast";document.body.appendChild(t)}t.textContent=m;t.classList.add("on");clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove("on"),2400)}
function ask(msg,ok){return new Promise(res=>{let m=$("mod");if(!m){m=document.createElement("div");m.id="mod";document.body.appendChild(m)}
m.innerHTML='<div class="card"><p style="margin:0 0 18px;font-size:16px">'+esc(msg)+'</p><div class="ka"><button id="m-no">Jooji</button><button class="dg" id="m-ok">'+esc(ok)+'</button></div></div>';
m.classList.add("on");const done=v=>{m.classList.remove("on");res(v)};$("m-no").onclick=()=>done(false);$("m-ok").onclick=()=>done(true)})}
function mk(){const A="ABCDEFGHJKLMNPQRSTUVWXYZ23456789",b=crypto.getRandomValues(new Uint8Array(16));let s="";for(let i=0;i<16;i++){s+=A[b[i]%32];if(i%4===3&&i<15)s+="-"}return s}
function st(k){return(k.expires_at&&new Date(k.expires_at)<new Date())?"expired":k.status}
function log(m){api("/activity",{method:"POST",body:JSON.stringify({message:m})}).catch(()=>{})}
async function copyKey(k){try{await navigator.clipboard.writeText(k)}catch(e){const t=document.createElement("textarea");t.value=k;document.body.appendChild(t);t.select();try{document.execCommand("copy")}catch(_){}t.remove()}toast("Waa la koobiyeeyay")}
function renderKeys(){const el=$("k-list");
const rows=K.rows.filter(r=>!K.q||r.key.includes(K.q));
if(!K.rows.length){el.innerHTML='<div class="card empty"><b>Wali key ma jiraan</b>Samee kii ugu horreeyay kor ku yaal.</div>';return}
if(!rows.length){el.innerHTML='<div class="card empty"><b>Waxba lama helin</b>Isku day raadin kale.</div>';return}
el.innerHTML=rows.map(r=>{const s=st(r);
return '<div class="card kc"><div class="kk">'+esc(r.key)+'</div><div class="km"><span class="bd '+s+'">'+s+'</span><span>'+(r.expires_at?new Date(r.expires_at).toLocaleDateString([],{day:"numeric",month:"short",year:"numeric"}):"Weligeed")+'</span><span>'+r.device_limit+' aalad</span></div>'
+'<div class="ka"><button data-a="copy" data-id="'+r.id+'">Copy</button><button data-a="toggle" data-id="'+r.id+'">'+(r.status==="active"?"Deactivate":"Activate")+'</button><button class="dg" data-a="del" data-id="'+r.id+'">Delete</button></div></div>'}).join("")}
async function act(a,id){const r=K.rows.find(x=>x.id===id);if(!r)return;
if(a==="copy")return copyKey(r.key);
try{
if(a==="toggle"){const ns=r.status==="active"?"inactive":"active";
const x=await api("/license_keys?id=eq."+id,{method:"PATCH",body:JSON.stringify({status:ns})});if(!x.ok)throw 0;
r.status=ns;renderKeys();toast(ns==="active"?"Waa la activate gareeyay":"Waa la deactivate gareeyay");loadOverview()}
if(a==="del"){if(!await ask("Ma hubtaa inaad tirtirto "+r.key+"?","Delete"))return;
const x=await api("/license_keys?id=eq."+id,{method:"DELETE"});if(!x.ok)throw 0;
K.rows=K.rows.filter(y=>y.id!==id);renderKeys();toast("Waa la tirtiray");log("Key la tirtiray");loadOverview()}
}catch(e){if(!(e&&e.message==="auth"))toast("Khalad: isku day mar kale")}}
async function genKeys(){
const days=+$("k-days").value,dev=Math.max(1,Math.min(100,+$("k-dev").value||1)),qty=Math.max(1,Math.min(50,+$("k-qty").value||1));
const b=$("k-gen");b.disabled=true;b.textContent="Waa la sameynayaa…";
const exp=days?new Date(Date.now()+days*864e5).toISOString():null;
const body=Array.from({length:qty},()=>({key:mk(),expires_at:exp,device_limit:dev}));
try{const x=await api("/license_keys",{method:"POST",body:JSON.stringify(body),headers:{Prefer:"return=representation"}});
if(!x.ok)throw 0;const n=await x.json();K.rows=n.concat(K.rows);renderKeys();toast(qty+" key waa la sameeyay");log(qty+" key cusub la sameeyay");loadOverview()}
catch(e){if(!(e&&e.message==="auth"))toast("Khalad: key lama sameynin")}
b.disabled=false;b.textContent="Generate"}
async function loadKeys(){$("k-list").innerHTML='<div class="card empty">Loading…</div>';
try{const x=await api("/license_keys?select=*&order=created_at.desc&limit=500");if(!x.ok)throw 0;K.rows=await x.json();renderKeys()}
catch(e){if(!(e&&e.message==="auth"))$("k-list").innerHTML='<div class="card empty"><b>Khalad</b>Keys lama soo qaadin.</div>'}}
$("v-keys").innerHTML='<div class="card"><h3 style="margin:0 0 14px">Generate keys</h3><div class="fg">'
+'<label>Muddo<select id="k-days"><option value="0">Weligeed</option><option value="1">1 maalin</option><option value="7">7 maalmood</option><option value="30" selected>30 maalmood</option><option value="90">90 maalmood</option><option value="365">1 sano</option></select></label>'
+'<label>Aaladaha (devices)<input id="k-dev" type="number" min="1" max="100" value="1"></label>'
+'<label>Tirada<input id="k-qty" type="number" min="1" max="50" value="1"></label></div>'
+'<button class="pbtn" id="k-gen">Generate</button></div>'
+'<div class="sec"><input class="srch" id="k-q" placeholder="Raadi key…" autocomplete="off"><div id="k-list"></div></div>';
$("k-gen").onclick=genKeys;
$("k-q").oninput=e=>{K.q=e.target.value.trim().toUpperCase();renderKeys()};
$("k-list").onclick=e=>{const b=e.target.closest("button");if(b)act(b.dataset.a,b.dataset.id)};
loadKeys();
}
'''

d = d.replace("</style>", CSS, 1)
d = d.replace(END, JS + END, 1)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Key Management waa la dhisay")
