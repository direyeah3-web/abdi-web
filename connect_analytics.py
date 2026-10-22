import shutil
shutil.copy("dashboard.html", "dashboard.html.before_an")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "loadAnalytics" in d:
    print("⚠️ Analytics hore ayaa loogu daray")
    raise SystemExit
for need in ("function toast", "function api"):
    if need not in d:
        print("❌ Waa la waayay:", need)
        raise SystemExit
if END not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = '.an-g{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}.an-s{background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:16px;padding:14px}.an-s small{display:block;opacity:.6;font-size:12px;margin-bottom:4px}.an-s b{font-size:26px}.an-bars{display:flex;align-items:flex-end;gap:8px;height:130px}.an-b{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;font-size:11px}.an-b i{display:block;width:100%;background:#0a84ff;border-radius:6px 6px 0 0;min-height:2px;margin:3px 0}</style>'

JS = r'''
if($("v-analytics")){
const A=$("v-analytics");
const E=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const arr=x=>Array.isArray(x)?x:[];
const f1=(o,l)=>{for(const k of l)if(o[k]!=null)return o[k];return null};
const fd=t=>new Date(t).toLocaleDateString([],{day:"numeric",month:"short"});
async function loadAnalytics(){
A.innerHTML='<div class="card empty"><b>Analytics</b>Waa la soo rarayaa...</div>';
try{
const j=async p=>arr(await(await api(p)).json());
const [keys,users,refs,acts]=await Promise.all([
j("/license_keys?select=*&order=created_at.desc&limit=1000"),
j("/profiles?select=id,username,is_admin,status,created_at&limit=1000"),
j("/referral_codes?select=*&limit=1000"),
j("/activity?select=message,created_at&order=created_at.desc&limit=1000")]);
const now=Date.now(),wk=now+7*864e5;
const ex=k=>{const v=f1(k,["expires_at","expiry","expires","expire_at","expiry_date","expires_on"]);return v?new Date(v).getTime():null};
const on=k=>(k.status?k.status==="active":k.is_active!==false);
const expd=k=>{const e=ex(k);return e!==null&&e<now};
const active=keys.filter(k=>on(k)&&!expd(k));
const expired=keys.filter(expd);
const free=keys.filter(k=>!k.assigned_to);
const soon=keys.filter(k=>{const e=ex(k);return on(k)&&e!==null&&e>=now&&e<=wk}).sort((a,b)=>ex(a)-ex(b));
const used=refs.reduce((s,r)=>s+(Number(f1(r,["used","uses","used_count","times_used"]))||0),0);
const banned=users.filter(x=>x.status!=="active").length;
const days=[];
for(let i=6;i>=0;i--){const dd=new Date();dd.setHours(0,0,0,0);dd.setDate(dd.getDate()-i);days.push({d:dd,n:0})}
acts.forEach(a=>{const t=new Date(a.created_at);t.setHours(0,0,0,0);const x=days.find(y=>y.d.getTime()===t.getTime());if(x)x.n++});
const mx=Math.max(1,...days.map(x=>x.n));
const st=(l,v)=>'<div class="an-s"><small>'+l+'</small><b>'+v+'</b></div>';
A.innerHTML='<div class="an-g">'+st("Keys guud",keys.length)+st("Active",active.length)+st("Expired",expired.length)+st("Aan la siin",free.length)+st("Users",users.length)+st("Banned",banned)+st("Referral la isticmaalay",used)+st("Referral codes",refs.length)+'</div>'
+'<div class="card"><b>Hawlaha 7 maalmood</b><div class="an-bars" style="margin-top:14px">'+days.map(x=>'<div class="an-b">'+x.n+'<i style="height:'+Math.round(x.n/mx*70)+'px"></i><span>'+x.d.toLocaleDateString([],{weekday:"short"})+'</span></div>').join("")+'</div></div>'
+'<div class="card" style="margin-top:12px"><b>Keys dhacaya 7 maalmood gudahood</b>'+(soon.length?soon.map(k=>'<div class="km" style="margin-top:8px"><span style="font-family:ui-monospace,monospace">'+E(k.key)+'</span> · '+fd(ex(k))+'</div>').join(""):'<div class="km" style="margin-top:8px">Midna ma dhacayo</div>')+'</div>';
}catch(e){A.innerHTML='<div class="card empty"><b>Error</b>Data lama helin.</div>'}
}
let was=false;
const chk=()=>{const v=getComputedStyle(A).display!=="none"&&A.offsetParent!==null;if(v&&!was)loadAnalytics();was=v};
new MutationObserver(chk).observe(A,{attributes:true,attributeFilter:["class","style","hidden"]});
document.addEventListener("click",()=>setTimeout(chk,80));
chk();
}
'''

d = d.replace("</style>", CSS, 1)
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Analytics waa la dhisay")
