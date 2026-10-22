import shutil
shutil.copy("dashboard.html", "dashboard.html.before_refs")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()

END = "</script></body></html>"
if "genCode" in d:
    print("⚠️ Referrals hore ayaa loogu daray. Waan joogsaday.")
    raise SystemExit
if END not in d or "function toast" not in d or "function ask" not in d:
    print("❌ dashboard.html qaab lama filayo, waan joogsaday")
    raise SystemExit

JS = r'''
if($("v-referrals")){
const R={rows:[],users:{}};
function rc(){const A="ABCDEFGHJKLMNPQRSTUVWXYZ23456789",b=crypto.getRandomValues(new Uint8Array(6));let s="";for(let i=0;i<6;i++)s+=A[b[i]%32];return "ABDI-"+s}
function rstate(r){return !r.active?"inactive":(r.used_count>=r.max_uses?"full":"active")}
function renderRefs(){const el=$("r-list");
if(!R.rows.length){el.innerHTML='<div class="card empty"><b>Wali code ma jiro</b>Samee kii ugu horreeyay kor ku yaal.</div>';return}
el.innerHTML=R.rows.map(r=>{const s=rstate(r),us=R.users[r.code]||[];
return '<div class="card kc"><div class="kk">'+esc(r.code)+'</div><div class="km"><span class="bd '+(s==="active"?"active":"inactive")+'">'+s+'</span><span>'+r.used_count+' / '+r.max_uses+' la isticmaalay</span></div>'
+(us.length?'<div class="km" style="margin-top:-4px">Users: '+us.map(u=>esc(u)).join(", ")+'</div>':'')
+'<div class="ka"><button data-a="copy" data-id="'+r.id+'">Copy</button><button data-a="toggle" data-id="'+r.id+'">'+(r.active?"Deactivate":"Activate")+'</button><button class="dg" data-a="del" data-id="'+r.id+'">Delete</button></div></div>'}).join("")}
async function genCode(){
let code=$("r-code").value.trim().toUpperCase().replace(/\s+/g,"");
const max=Math.max(1,Math.min(1000,+$("r-max").value||1));
if(!code)code=rc();
if(!/^[A-Z0-9-]{4,24}$/.test(code))return toast("Code: 4-24 xaraf (A-Z, 0-9, -)");
const b=$("r-gen");b.disabled=true;b.textContent="Waa la sameynayaa…";
try{const x=await api("/referral_codes",{method:"POST",body:JSON.stringify({code:code,max_uses:max}),headers:{Prefer:"return=representation"}});
if(x.status===409)toast("Code-kaas hore ayuu u jiray");
else if(!x.ok)toast("Khalad: code lama sameynin");
else{const n=await x.json();R.rows=n.concat(R.rows);renderRefs();$("r-code").value="";toast("Code waa la sameeyay");log("Referral code cusub: "+code);loadOverview()}}
catch(e){if(!(e&&e.message==="auth"))toast("Khalad: isku day mar kale")}
b.disabled=false;b.textContent="Create code"}
async function ract(a,id){const r=R.rows.find(x=>x.id===id);if(!r)return;
if(a==="copy")return copyKey(r.code);
try{
if(a==="toggle"){const na=!r.active;
const x=await api("/referral_codes?id=eq."+id,{method:"PATCH",body:JSON.stringify({active:na})});if(!x.ok)throw 0;
r.active=na;renderRefs();toast(na?"Waa la activate gareeyay":"Waa la deactivate gareeyay")}
if(a==="del"){if(!await ask("Ma hubtaa inaad tirtirto "+r.code+"?"+(r.used_count?" (Users-ka hore ma tirtirmayo)":""),"Delete"))return;
const x=await api("/referral_codes?id=eq."+id,{method:"DELETE"});if(!x.ok)throw 0;
R.rows=R.rows.filter(y=>y.id!==id);renderRefs();toast("Waa la tirtiray");log("Referral code la tirtiray")}
}catch(e){if(!(e&&e.message==="auth"))toast("Khalad: isku day mar kale")}}
async function loadRefs(){$("r-list").innerHTML='<div class="card empty">Loading…</div>';
try{const r=await Promise.all([api("/referral_codes?select=*&order=created_at.desc&limit=500"),api("/profiles?select=username,referral_code&limit=1000")]);
if(!r[0].ok)throw 0;R.rows=await r[0].json();R.users={};
if(r[1].ok)(await r[1].json()).forEach(p=>{if(p.referral_code)(R.users[p.referral_code]=R.users[p.referral_code]||[]).push(p.username)});
renderRefs()}catch(e){if(!(e&&e.message==="auth"))$("r-list").innerHTML='<div class="card empty"><b>Khalad</b>Codes lama soo qaadin.</div>'}}
$("v-referrals").innerHTML='<div class="card"><h3 style="margin:0 0 14px">Create referral code</h3><div class="fg">'
+'<label>Code (ikhtiyaari)<input id="r-code" placeholder="Auto: ABDI-XXXXXX" autocapitalize="characters" autocomplete="off"></label>'
+'<label>Isticmaal ugu badnaan<input id="r-max" type="number" min="1" max="1000" value="1"></label></div>'
+'<button class="pbtn" id="r-gen">Create code</button></div>'
+'<div class="sec"><div id="r-list"></div></div>';
$("r-gen").onclick=genCode;
$("r-list").onclick=e=>{const b=e.target.closest("button");if(b)ract(b.dataset.a,b.dataset.id)};
loadRefs();
}
'''

d = d.replace(END, JS + END, 1)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Referral Codes waa la dhisay")
