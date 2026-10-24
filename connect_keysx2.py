import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'KEYS X2' in s: sys.exit('Hore ayaa loo dhejiyey')
o1='''x.innerHTML='<button class="kx-a" id="kx-a">+ Custom key</button><button class="kx-d" id="kx-d">Delete all</button>';'''
o2='''x.querySelector("#kx-a").onclick=custom;x.querySelector("#kx-d").onclick=delall;'''
if s.count(o1)!=1 or s.count(o2)!=1: sys.exit('Anchor lama helin (KEYS X ma jiro?)')
shutil.copy(f,'dashboard.html.before_keysx2')
s=s.replace(o1,'''x.innerHTML='<button class="kx-d" id="kx-d">Delete all</button>';''')
s=s.replace(o2,'''x.querySelector("#kx-d").onclick=delall;''')
css=r'''
/* ===== KEYS X2 ===== */
#kx-ce{color:#ff453a;font-size:13px;margin-top:8px;word-break:break-word}
#kx-ck{font-family:ui-monospace,"SF Mono",Menlo,monospace!important;letter-spacing:.04em}
/* ===== /KEYS X2 ===== */
'''
js=r'''
/* ===== KEYS X2 JS ===== */
(function(){
function lf(t,root){var a=(root||document).querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
function T(m){try{toast(m)}catch(e){}}
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
function mk(){
 var v=document.getElementById("v-keys");if(!v||document.getElementById("kx-ck"))return;
 var h=lf("Generate keys",v);var c=h&&h.closest(".card");if(!c)return;
 var ins=c.querySelectorAll("input");if(!ins.length)return;
 var last=ins[ins.length-1];
 var lb=document.createElement("label");lb.id="kx-cl";lb.textContent="Custom key (optional)";
 var inp=document.createElement("input");inp.id="kx-ck";inp.type="text";inp.placeholder="Madhan = auto key";inp.autocomplete="off";inp.autocapitalize="off";inp.spellcheck=false;
 var er=document.createElement("div");er.id="kx-ce";
 last.insertAdjacentElement("afterend",lb);lb.insertAdjacentElement("afterend",inp);inp.insertAdjacentElement("afterend",er)}
async function make(card,inp,er){
 var key=inp.value.trim();
 var all=Array.prototype.slice.call(card.querySelectorAll("input")).filter(function(i){return i.id!=="kx-ck"});
 var dev=Math.max(1,parseInt(all[0]&&all[0].value)||1),qty=Math.max(1,parseInt(all[1]&&all[1].value)||1);
 var sel=card.querySelector("select"),days=30;
 if(sel){if(/^\d+$/.test(sel.value))days=+sel.value;else{var m=(sel.options[sel.selectedIndex].text||"").match(/\d+/);if(m)days=+m[0]}}
 er.textContent="";
 if(key.length<3){er.textContent="Key-gu waa inuu ugu yaraan 3 xaraf noqdaa";return}
 if(qty>1){er.textContent="Custom key waa hal key. Quantity ka dhig 1";return}
 try{
  var d=await api("/license_keys?select=key&key=eq."+encodeURIComponent(key));
  var dj=await d.json();
  if(Array.isArray(dj)&&dj.length){er.textContent="Key-gan hore ayuu u jiray";return}
  var q=await api("/license_keys?select=*&order=created_at.desc&limit=1");
  var qj=await q.json();
  if(!Array.isArray(qj)||!qj.length){er.textContent="Marka hore hal key caadi ah ku samee Generate";return}
  var r=await api("/license_keys",{method:"POST",headers:{"Content-Type":"application/json","Prefer":"return=minimal"},body:JSON.stringify(build(qj[0],key,days,dev))});
  if(r.ok){inp.value="";T("Key waa la sameeyay");try{refresh()}catch(e){}}
  else er.textContent="Khalad "+r.status+": "+(await r.text()).slice(0,200)
 }catch(e){er.textContent=String(e).slice(0,200)}}
document.addEventListener("click",function(e){
 var b=e.target.closest&&e.target.closest("button");if(!b)return;
 var inp=document.getElementById("kx-ck");if(!inp)return;
 var card=inp.closest(".card");if(!card||!card.contains(b))return;
 if(b.textContent.trim().toLowerCase()!=="generate")return;
 if(!inp.value.trim())return;
 e.preventDefault();e.stopImmediatePropagation();
 make(card,inp,document.getElementById("kx-ce"))
},true);
setInterval(mk,1200);setTimeout(mk,700);
})();
/* ===== /KEYS X2 JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
