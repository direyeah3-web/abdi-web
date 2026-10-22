import shutil
shutil.copy("dashboard.html", "dashboard.html.before_set")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "renderSettings" in d:
    print("⚠️ Settings hore ayaa loogu daray")
    raise SystemExit
for need in ("function toast", "function api", "async function refresh"):
    if need not in d:
        print("❌ Waa la waayay:", need)
        raise SystemExit
if END not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = '.st-i{width:100%;box-sizing:border-box;margin-top:10px;padding:13px;border-radius:14px;border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--t);font-size:15px}.st-b{width:100%;margin-top:12px;padding:13px;border:0;border-radius:14px;background:#0a84ff;color:#fff;font-weight:600;font-size:15px;cursor:pointer}.st-d{background:#ff453a}</style>'

JS = r'''
if($("v-settings")){
const S=$("v-settings");
const E=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const hd=()=>({apikey:KEY,Authorization:"Bearer "+localStorage.getItem("abdi_tok"),"Content-Type":"application/json"});
const putPw=pw=>fetch(SB+"/auth/v1/user",{method:"PUT",headers:hd(),body:JSON.stringify({password:pw})});
function renderSettings(){
S.innerHTML='<div class="card"><b>Profile</b><div class="km" style="margin-top:8px">Username: <span style="font-family:ui-monospace,monospace">'+E(u)+'</span></div></div>'
+'<div class="card" style="margin-top:12px"><b>Beddel password</b><input id="st-p1" type="password" placeholder="Password cusub" class="st-i"><input id="st-p2" type="password" placeholder="Ku celi password-ka" class="st-i"><button id="st-pw" class="st-b">Cusboonaysii password</button></div>'
+'<div class="card" style="margin-top:12px"><b>Backup</b><div class="km" style="margin-top:6px">Soo dejiso data-ga oo JSON ah</div><button id="st-ex" class="st-b">Export JSON</button></div>'
+'<div class="card" style="margin-top:12px"><b>Activity log</b><div class="km" style="margin-top:6px">Tirtir dhammaan hawlaha la diiwaangeliyay</div><button id="st-cl" class="st-b st-d">Clear activity</button></div>';
$("st-pw").onclick=async()=>{
const a=$("st-p1").value,b=$("st-p2").value;
if(a.length<6)return toast("Password-ku waa inuu ahaadaa 6+ xaraf");
if(a!==b)return toast("Labada password isma waafaqaan");
try{
let r=await putPw(a);
if(r.status===401&&await refresh())r=await putPw(a);
if(r.ok){toast("Password waa la beddelay");$("st-p1").value="";$("st-p2").value=""}
else{const j=await r.json().catch(()=>({}));toast(j.msg||j.message||"Ma suurtagalin")}
}catch(e){toast("Error")}};
$("st-ex").onclick=async()=>{
try{
const o={};
for(const t of ["license_keys","profiles","referral_codes","activity"]){o[t]=await(await api("/"+t+"?select=*&limit=10000")).json()}
const bl=new Blob([JSON.stringify(o,null,2)],{type:"application/json"});
const a=document.createElement("a");
a.href=URL.createObjectURL(bl);
a.download="abdi-backup-"+new Date().toISOString().slice(0,10)+".json";
document.body.appendChild(a);a.click();a.remove();
toast("Backup waa la soo dejiyay");
}catch(e){toast("Error")}};
$("st-cl").onclick=async()=>{
if(!confirm("Dhammaan activity log-ka ma tirtiraa?"))return;
try{
const r=await api("/activity?created_at=not.is.null",{method:"DELETE",headers:{Prefer:"return=minimal"}});
toast(r.ok?"Activity waa la tirtiray":"Ma suurtagalin (ogolaansho la'aan)");
}catch(e){toast("Error")}};
}
let was=false;
const chk=()=>{const v=getComputedStyle(S).display!=="none"&&S.offsetParent!==null;if(v&&!was)renderSettings();was=v};
new MutationObserver(chk).observe(S,{attributes:true,attributeFilter:["class","style","hidden"]});
document.addEventListener("click",()=>setTimeout(chk,80));
chk();
}
'''

d = d.replace("</style>", CSS, 1)
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Settings waa la dhisay")
