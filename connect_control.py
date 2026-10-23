import shutil
shutil.copy("dashboard.html", "dashboard.html.before_ctl")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()

END = "</script></body></html>"
if "loadCtl" in d:
    print("⚠️ Loader tab hore ayaa loogu daray. Waan joogsaday.")
    raise SystemExit
for need in ("function toast", "function ask", "function log", "const esc=", "async function api("):
    if need not in d:
        print("❌ Waa la waayay:", need, "- waan joogsaday")
        raise SystemExit
if END not in d or '["analytics","Analytics"' not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

NAV_NEW = '["control","Loader","Maamul loader-ka online",\'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>\'],\n'
d = d.replace('["analytics","Analytics"', NAV_NEW + '["analytics","Analytics"', 1)

CSS = r'''.lb{display:block;color:var(--m);font-size:13px;margin:12px 0}
.ta{width:100%;margin-top:6px;border-radius:16px;border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--t);padding:12px 14px;font:16px -apple-system,Inter,system-ui,sans-serif;outline:0;resize:vertical}
.ta:focus{border-color:var(--b)}
.swr{display:flex;justify-content:space-between;align-items:center;gap:12px}
.sw{position:relative;width:54px;height:32px;border-radius:16px;border:0;background:#39393d;cursor:pointer;transition:.25s;flex:none}
.sw::after{content:"";position:absolute;top:3px;left:3px;width:26px;height:26px;border-radius:50%;background:#fff;transition:.25s}
.sw.on{background:#30d158}.sw.on::after{transform:translateX(22px)}
</style>'''

JS = r'''
if($("v-control")){
const C={cfg:null,ann:[],cr:[]};
const val=i=>$(i).value.trim();
const tf=s=>new Date(s).toLocaleString([],{day:"numeric",month:"short",hour:"2-digit",minute:"2-digit"});
const okUrl=s=>s===""||/^https:\/\/\S+$/.test(s);
function fail(e){if(!(e&&e.message==="auth"))toast("Khalad: isku day mar kale")}
async function patchCfg(p){p.updated_at=new Date().toISOString();
const x=await api("/app_config?id=eq.1",{method:"PATCH",body:JSON.stringify(p)});if(!x.ok)throw 0;Object.assign(C.cfg,p)}
function renderAnn(){const el=$("c-ann");
if(!C.ann.length){el.innerHTML='<div class="card empty"><b>Wali fariin ma jirto</b></div>';return}
el.innerHTML=C.ann.map(a=>'<div class="card kc"><div class="kk" style="font-family:inherit;letter-spacing:0">'+esc(a.title)+'</div>'
+(a.body?'<div class="km" style="white-space:pre-wrap;font-size:13px">'+esc(a.body)+'</div>':"")
+'<div class="km"><span class="bd '+(a.active?"active":"inactive")+'">'+(a.active?"live":"hidden")+'</span><span>'+tf(a.created_at)+'</span></div>'
+'<div class="ka"><button data-a="atoggle" data-id="'+a.id+'">'+(a.active?"Hide":"Show")+'</button><button class="dg" data-a="adel" data-id="'+a.id+'">Delete</button></div></div>').join("")}
function renderCr(){const el=$("c-cr");
if(!C.cr.length){el.innerHTML='<div class="card empty"><b>Crash ma jiro</b>Wax khalad ah lama soo sheegin.</div>';return}
el.innerHTML='<div class="card">'+C.cr.map(r=>'<div class="row"><span>'+esc((r.message||"(no message)").slice(0,140))+'<br><span style="color:var(--m);font-size:12px">v'+esc(r.app_version==null?"?":r.app_version)+" \u00b7 "+esc(String(r.device_id).slice(0,8))+'</span></span><span>'+tf(r.created_at)+'</span></div>').join("")+'</div>'}
function drawCtl(){const c=C.cfg;
$("v-control").innerHTML=
'<div class="card"><div class="swr"><div><h3 style="margin:0">Maintenance</h3><div class="lab">Marka ON, app-ku wuu joogsanayaa</div></div><button class="sw'+(c.maintenance?" on":"")+'" id="c-sw" aria-label="Maintenance"></button></div>'
+'<label class="lb">Fariinta users-ka<textarea class="ta" id="c-msg" rows="3" maxlength="300">'+esc(c.maintenance_msg)+'</textarea></label>'
+'<button class="pbtn" id="c-savemsg">Save message</button></div>'
+'<div class="card sec"><h3 style="margin:0 0 12px">Version &amp; Links</h3><div class="fg">'
+'<label>Latest version<input id="c-lv" type="number" min="1" value="'+esc(c.latest_version)+'"></label>'
+'<label>Min version (la khasbayo update)<input id="c-mv" type="number" min="1" value="'+esc(c.min_version)+'"></label>'
+'<label>Update link (download)<input id="c-url" value="'+esc(c.update_url||"")+'" placeholder="https://..."></label>'
+'<label>Support link<input id="c-sup" value="'+esc(c.support_url||"")+'" placeholder="https://t.me/..."></label></div>'
+'<button class="pbtn" id="c-savev">Save</button></div>'
+'<div class="card sec"><h3 style="margin:0 0 12px">Announcements</h3><div class="fg"><label>Cinwaan<input id="c-at" maxlength="80"></label></div>'
+'<label class="lb">Qoraal<textarea class="ta" id="c-ab" rows="3" maxlength="500"></textarea></label><button class="pbtn" id="c-post">Post</button></div>'
+'<div class="sec" id="c-ann"></div>'
+'<div class="sec"><div class="swr" style="margin-bottom:12px"><h3 style="margin:0">Crash reports</h3><button class="out" id="c-clr">Clear</button></div><div id="c-cr"></div></div>';
renderAnn();renderCr();
$("c-sw").onclick=async()=>{const on=!C.cfg.maintenance;
if(on&&!await ask("Shid maintenance? App-ka users-ka dhammaan wuu joogsanayaa.","Shid"))return;
try{await patchCfg({maintenance:on,maintenance_msg:val("c-msg")||C.cfg.maintenance_msg});$("c-sw").classList.toggle("on",on);toast(on?"Maintenance ON":"Maintenance OFF");log("Maintenance "+(on?"ON":"OFF"))}catch(e){fail(e)}};
$("c-savemsg").onclick=async()=>{const m=val("c-msg");if(!m)return toast("Qor fariinta");
try{await patchCfg({maintenance_msg:m});toast("Fariinta waa la keydiyay")}catch(e){fail(e)}};
$("c-savev").onclick=async()=>{const lv=+val("c-lv"),mv=+val("c-mv"),url=val("c-url"),sup=val("c-sup");
if(!(Number.isInteger(lv)&&Number.isInteger(mv)&&lv>=1&&mv>=1))return toast("Version waa inuu noqdaa tiro (1+)");
if(mv>lv)return toast("Min version ma noqon karo ka weyn Latest");
if(!okUrl(url)||!okUrl(sup))return toast("Link-ku waa inuu ku bilaabmaa https://");
try{await patchCfg({latest_version:lv,min_version:mv,update_url:url||null,support_url:sup||null});toast("Waa la keydiyay");log("App version/links la cusboonaysiiyay")}catch(e){fail(e)}};
$("c-post").onclick=async()=>{const t=val("c-at"),b=val("c-ab");if(!t)return toast("Geli cinwaan");
try{const x=await api("/announcements",{method:"POST",body:JSON.stringify({title:t,body:b}),headers:{Prefer:"return=representation"}});if(!x.ok)throw 0;
C.ann=(await x.json()).concat(C.ann);$("c-at").value="";$("c-ab").value="";renderAnn();toast("Waa la dhigay");log("Announcement: "+t)}catch(e){fail(e)}};
$("c-ann").onclick=async e=>{const b=e.target.closest("button");if(!b)return;const a=C.ann.find(x=>x.id===b.dataset.id);if(!a)return;
try{
if(b.dataset.a==="atoggle"){const x=await api("/announcements?id=eq."+a.id,{method:"PATCH",body:JSON.stringify({active:!a.active})});if(!x.ok)throw 0;a.active=!a.active;renderAnn()}
if(b.dataset.a==="adel"){if(!await ask("Tirtir fariintan?","Delete"))return;const x=await api("/announcements?id=eq."+a.id,{method:"DELETE"});if(!x.ok)throw 0;C.ann=C.ann.filter(y=>y.id!==a.id);renderAnn();toast("Waa la tirtiray")}
}catch(err){fail(err)}};
$("c-clr").onclick=async()=>{if(!C.cr.length)return;if(!await ask("Tirtir dhammaan crash reports?","Clear"))return;
try{const x=await api("/crash_reports?id=gt.0",{method:"DELETE"});if(!x.ok)throw 0;C.cr=[];renderCr();toast("Waa la nadiifiyay")}catch(e){fail(e)}}}
async function loadCtl(){$("v-control").innerHTML='<div class="card empty">Loading…</div>';
try{const r=await Promise.all([api("/app_config?select=*&id=eq.1"),api("/announcements?select=*&order=created_at.desc&limit=50"),api("/crash_reports?select=*&order=created_at.desc&limit=30")]);
if(!r.every(x=>x.ok))throw 0;
const cf=await r[0].json();if(!cf[0])throw 0;C.cfg=cf[0];C.ann=await r[1].json();C.cr=await r[2].json();drawCtl()}
catch(e){if(!(e&&e.message==="auth"))$("v-control").innerHTML='<div class="card empty"><b>Khalad</b>Xogta lama soo qaadin.</div>'}}
loadCtl();
}
'''

d = d.replace("</style>", CSS, 1)
d = d.replace(END, JS + END, 1)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Loader tab waa la dhisay")
