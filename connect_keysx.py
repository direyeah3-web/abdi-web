import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'KEYS X' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_keysx')
css=r'''
/* ===== KEYS X ===== */
#ab-kx{display:flex;gap:12px;padding:14px!important}
#ab-kx button{flex:1;padding:15px 10px!important;border-radius:999px!important;font-size:16px!important;font-weight:600!important}
#ab-kx .kx-a{background:#0a84ff!important;color:#fff!important;border:none!important;box-shadow:0 8px 24px rgba(10,132,255,.35)!important}
#ab-kx .kx-d{background:rgba(255,69,58,.14)!important;color:#ff453a!important;border:1px solid rgba(255,69,58,.35)!important}
#kx-o{position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);display:flex;align-items:flex-end}
.kx-s{width:100%;max-height:88%;overflow:auto;background:#1c1c1e;border-radius:30px 30px 0 0;border:1px solid rgba(255,255,255,.10);border-bottom:none;padding:10px 20px calc(env(safe-area-inset-bottom,0px) + 24px);animation:kxUp .32s cubic-bezier(.2,.8,.2,1)}
@keyframes kxUp{from{transform:translateY(100%)}to{transform:none}}
.kx-g{width:40px;height:5px;border-radius:3px;background:rgba(255,255,255,.25);margin:4px auto 16px}
.kx-s h3{font-size:22px;margin:0 0 6px;color:#fff}
.kx-s p{color:rgba(235,235,245,.6);font-size:15px;margin:0 0 14px;line-height:1.4}
.kx-s label{display:block;font-size:13px;font-weight:600;color:rgba(235,235,245,.5);margin:12px 0 6px}
.kx-s input,.kx-s select{width:100%;box-sizing:border-box}
.kx-s .kx-b{width:100%;margin-top:18px;padding:16px;border:none;border-radius:999px;font-size:17px;font-weight:600;color:#fff;background:#0a84ff}
.kx-s .kx-b.r{background:#ff453a}
.kx-s .kx-b.x{background:rgba(255,255,255,.1);margin-top:10px}
.kx-s .kx-e{color:#ff453a;font-size:13px;margin-top:12px;word-break:break-word}
/* ===== /KEYS X ===== */
'''
js=r'''
/* ===== KEYS X JS ===== */
(function(){
function lf(t,root){var a=(root||document).querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
function T(m){try{toast(m)}catch(e){}}
function close(){var o=document.getElementById("kx-o");if(o)o.remove()}
function sheet(h){close();var o=document.createElement("div");o.id="kx-o";o.innerHTML='<div class="kx-s"><div class="kx-g"></div>'+h+'</div>';o.addEventListener("click",function(e){if(e.target===o)close()});document.body.appendChild(o);return o.firstChild}
function err(el,m){var e=el.querySelector(".kx-e");if(e)e.textContent=m}
function JH(){return {"Content-Type":"application/json","Prefer":"return=minimal"}}
function build(sm,key,days,dev){
 var r={},k;for(k in sm){r[k]=sm[k]}
 ["id","created_at","updated_at"].forEach(function(f){delete r[f]});
 var exp=new Date(Date.now()+days*864e5).toISOString();
 Object.keys(r).forEach(function(f){
  var v=r[f];
  if(f==="key"){r[f]=key;return}
  if(f==="assigned_to"||/hwid|device_id|fingerprint|last_|activated|used_at|ban_|banned/i.test(f)){r[f]=Array.isArray(v)?[]:(typeof v==="boolean"?false:null);return}
  if(/device/i.test(f)&&/used|count|current|active/i.test(f)&&typeof v==="number"){r[f]=0;return}
  if(/expir|valid_until|ends/i.test(f)&&(typeof v==="string"||v===null)){r[f]=exp;return}
  if(/^(days|duration|duration_days|validity)$/i.test(f)&&typeof v==="number"){r[f]=days;return}
  if(/device|max_dev/i.test(f)&&typeof v==="number"){r[f]=dev;return}
  if(f==="is_active"||f==="active"){r[f]=true;return}
  if(f==="status"&&typeof v==="string"){r[f]=/^active$/i.test(v)?v:"active"}
 });
 return r}
function done(){close();try{refresh()}catch(e){}}
function custom(){
 var s=sheet('<h3>Custom key</h3><p>Qor key-ga aad rabto.</p><label>Key</label><input id="kx-k" placeholder="ABDI-VIP-0001" autocapitalize="characters" autocomplete="off"><label>Duration</label><select id="kx-d"><option value="7">7 days</option><option value="30" selected>30 days</option><option value="90">90 days</option><option value="365">365 days</option></select><label>Devices</label><input id="kx-v" type="number" min="1" value="1"><div class="kx-e"></div><button class="kx-b" id="kx-go">Create key</button><button class="kx-b x" id="kx-no">Cancel</button>');
 var inp=s.querySelector("#kx-k");
 inp.addEventListener("input",function(){inp.value=inp.value.toUpperCase().replace(/[^A-Z0-9\-_]/g,"")});
 s.querySelector("#kx-no").onclick=close;
 s.querySelector("#kx-go").onclick=async function(){
  var b=this,key=inp.value.trim(),days=+s.querySelector("#kx-d").value,dev=Math.max(1,parseInt(s.querySelector("#kx-v").value)||1);
  if(key.length<4){err(s,"Key-gu waa inuu ugu yaraan 4 xaraf noqdaa");return}
  b.disabled=true;err(s,"");
  try{
   var d=await api("/license_keys?select=key&key=eq."+encodeURIComponent(key));
   var dj=await d.json();
   if(Array.isArray(dj)&&dj.length){err(s,"Key-gan hore ayuu u jiray");b.disabled=false;return}
   var q=await api("/license_keys?select=*&order=created_at.desc&limit=1");
   var qj=await q.json();
   if(!Array.isArray(qj)||!qj.length){err(s,"Marka hore hal key ku samee Generate, si qaab-dhismeedka loo ogaado");b.disabled=false;return}
   var r=await api("/license_keys",{method:"POST",headers:JH(),body:JSON.stringify(build(qj[0],key,days,dev))});
   if(r.ok){T("Key waa la sameeyay");done()}
   else{err(s,"Khalad "+r.status+": "+(await r.text()).slice(0,220));b.disabled=false}
  }catch(e){err(s,String(e).slice(0,200));b.disabled=false}
 }}
function delall(){
 var s=sheet('<h3>Delete all keys</h3><p id="kx-c">Waa la tirtirayaa dhammaan keys-ka. Backup ayaa hore loo soo dejinayaa.</p><label>Qor DELETE si aad u xaqiijiso</label><input id="kx-t" placeholder="DELETE" autocapitalize="characters" autocomplete="off"><div class="kx-e"></div><button class="kx-b r" id="kx-go">Delete all</button><button class="kx-b x" id="kx-no">Cancel</button>');
 s.querySelector("#kx-no").onclick=close;
 s.querySelector("#kx-go").onclick=async function(){
  var b=this;
  if(s.querySelector("#kx-t").value.trim().toUpperCase()!=="DELETE"){err(s,"Qor DELETE");return}
  b.disabled=true;err(s,"");
  try{
   var a=await api("/license_keys?select=*");
   var aj=await a.json();
   if(!Array.isArray(aj)){err(s,"Backup lama sameyn karo, waa la joojiyay");b.disabled=false;return}
   if(!aj.length){err(s,"Keys ma jiraan");b.disabled=false;return}
   var bl=new Blob([JSON.stringify(aj,null,1)],{type:"application/json"}),u=URL.createObjectURL(bl),l=document.createElement("a");
   l.href=u;l.download="abdi-keys-backup-"+new Date().toISOString().slice(0,10)+".json";document.body.appendChild(l);l.click();l.remove();
   await new Promise(function(r){setTimeout(r,900)});
   var r=await api("/license_keys?key=not.is.null",{method:"DELETE",headers:{"Prefer":"return=minimal"}});
   if(r.ok){T(aj.length+" keys waa la tirtiray");done()}
   else{err(s,"Khalad "+r.status+": "+(await r.text()).slice(0,220));b.disabled=false}
  }catch(e){err(s,String(e).slice(0,200));b.disabled=false}
 }}
function mk(){
 var v=document.getElementById("v-keys");if(!v||document.getElementById("ab-kx"))return;
 var h=lf("Generate keys",v);var c=h&&h.closest(".card");if(!c)return;
 var x=document.createElement("div");x.id="ab-kx";x.className="card";
 x.innerHTML='<button class="kx-a" id="kx-a">+ Custom key</button><button class="kx-d" id="kx-d">Delete all</button>';
 x.querySelector("#kx-a").onclick=custom;x.querySelector("#kx-d").onclick=delall;
 c.parentNode.insertBefore(x,c.nextSibling)}
setInterval(mk,1500);setTimeout(mk,800);
})();
/* ===== /KEYS X JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
