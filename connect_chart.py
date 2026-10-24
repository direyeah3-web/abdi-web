import shutil,sys
f='dashboard.html'
s=open(f,encoding='utf-8').read()
if 'ACT CHART' in s: sys.exit('Hore ayaa loo dhejiyey')
if '</style>' not in s or '</script>' not in s: sys.exit('Struktur khalad')
shutil.copy(f,'dashboard.html.before_chart')
css=r'''
/* ===== ACT CHART ===== */
#ab-chart{margin:4px 0 26px}
#ab-chart .ch-p{display:flex;gap:10px;overflow-x:auto;padding:2px 0 14px}
#ab-chart .ch-p button{flex:none;border:1px solid rgba(255,255,255,.12)!important;background:rgba(255,255,255,.07)!important;color:rgba(235,235,245,.65)!important;padding:11px 22px;border-radius:999px!important;font-size:15px;font-weight:600;-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}
#ab-chart .ch-p button.on{background:rgba(255,255,255,.22)!important;color:#fff!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}
#ab-chart .ch-c{background:linear-gradient(160deg,#232326,#141416);border:1px solid rgba(255,255,255,.10);border-radius:28px;padding:18px 16px 14px;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 10px 30px rgba(0,0,0,.5)}
#ab-chart .ch-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px}
#ab-chart .ch-l{font-size:13px;color:rgba(235,235,245,.5)}
#ab-chart .ch-big{font-size:34px;font-weight:700;letter-spacing:-.02em;color:#fff}
#ab-chart .ch-pv{font-size:14px;color:rgba(235,235,245,.55);margin-left:8px}
#ab-chart .ch-pv b{color:#ff453a;font-weight:600}
#ab-chart .ch-lg{display:flex;flex-direction:column;gap:6px;font-size:13px;color:rgba(235,235,245,.6);margin-top:4px}
#ab-chart .ch-lg i{display:inline-block;width:22px;height:3px;border-radius:2px;background:#fff;vertical-align:middle;margin-right:8px}
#ab-chart .ch-lg i.g{background:rgba(255,255,255,.3);height:2px}
#ab-chart svg{width:100%;height:auto;display:block;overflow:visible}
#ab-chart .ch-x{display:flex;justify-content:space-between;padding:6px 26px 0 6px;font-size:12px;font-weight:600;color:rgba(235,235,245,.4)}
/* ===== /ACT CHART ===== */
'''
js=r'''
/* ===== ACT CHART JS ===== */
(function(){
var N=7,rows=null,lt=0;
function lf(t){var a=document.querySelectorAll("*");for(var i=0;i<a.length;i++){var e=a[i];if(!e.children.length&&e.textContent.trim()===t)return e}return null}
function curve(p,T,B){
 var d="M"+p[0][0]+","+p[0][1];
 for(var i=0;i<p.length-1;i++){
  var p0=p[i-1]||p[i],p1=p[i],p2=p[i+1],p3=p[i+2]||p2;
  var c1y=Math.max(T,Math.min(B,p1[1]+(p2[1]-p0[1])/6)),c2y=Math.max(T,Math.min(B,p2[1]-(p3[1]-p1[1])/6));
  d+=" C"+(p1[0]+(p2[0]-p0[0])/6)+","+c1y+" "+(p2[0]-(p3[0]-p1[0])/6)+","+c2y+" "+p2[0]+","+p2[1];
 }
 return d}
function fmt(v){return String(Math.round(v*10)/10)}
function mk(){
 var h=lf("Recent Activity");if(!h)return null;
 var c=document.getElementById("ab-chart");
 if(!c){
  c=document.createElement("div");c.id="ab-chart";
  c.innerHTML='<div class="ch-p"><button data-n="7">7 Days</button><button data-n="14">14 Days</button><button data-n="30">30 Days</button></div><div class="ch-c"><div class="ch-top"><div><div class="ch-l">Average per day</div><div id="ch-n"></div></div><div class="ch-lg"><span><i></i>Current</span><span><i class="g"></i>Previous</span></div></div><div id="ch-s"></div><div class="ch-x" id="ch-x"></div></div>';
  c.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("[data-n]");if(!b)return;N=+b.getAttribute("data-n");draw()});
 }
 if(c.nextElementSibling!==h)h.parentNode.insertBefore(c,h);
 return c}
function draw(){
 var c=document.getElementById("ab-chart");if(!c||!rows)return;
 c.querySelectorAll("[data-n]").forEach(function(b){b.classList.toggle("on",+b.getAttribute("data-n")===N)});
 var now=new Date();now.setHours(0,0,0,0);
 var start=now.getTime()-(N-1)*864e5,cur=[],prev=[],i;
 for(i=0;i<N;i++){cur.push(0);prev.push(0)}
 rows.forEach(function(x){
  var d=new Date(x.created_at);d.setHours(0,0,0,0);
  var k=Math.round((d.getTime()-start)/864e5);
  if(k>=0&&k<N)cur[k]++;else if(k<0&&k>=-N)prev[k+N]++;
 });
 var sc=0,sp=0;cur.forEach(function(v){sc+=v});prev.forEach(function(v){sp+=v});
 var W=340,H=160,L=6,R=30,T=12,B=148;
 var mx=Math.max(1,Math.max.apply(null,cur),Math.max.apply(null,prev));
 function X(i){return L+(W-L-R)*i/(N-1)}
 function Y(v){return T+(B-T)*(1-v/mx)}
 var pc=cur.map(function(v,i){return [X(i),Y(v)]}),pp=prev.map(function(v,i){return [X(i),Y(v)]});
 var g="";
 for(i=0;i<5;i++){
  var y=T+(B-T)*i/4;
  g+='<line x1="'+L+'" x2="'+(W-R+6)+'" y1="'+y+'" y2="'+y+'" stroke="rgba(255,255,255,.07)"/>';
  if(i==0||i==2||i==4)g+='<text x="'+(W-2)+'" y="'+(y+4)+'" text-anchor="end" fill="rgba(235,235,245,.35)" font-size="11">'+Math.round(mx*(1-i/4))+'</text>';
 }
 var d=curve(pc,T,B),e=pc[N-1];
 var svg='<svg viewBox="0 0 '+W+' '+H+'"><defs><linearGradient id="abg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'+g+
  '<path d="'+d+' L'+X(N-1)+','+B+' L'+X(0)+','+B+' Z" fill="url(#abg)"/>'+
  '<path d="'+curve(pp,T,B)+'" fill="none" stroke="rgba(255,255,255,.3)" stroke-width="2" stroke-linecap="round"/>'+
  '<path d="'+d+'" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'+
  '<circle cx="'+e[0]+'" cy="'+e[1]+'" r="15" fill="rgba(255,255,255,.14)"/><circle cx="'+e[0]+'" cy="'+e[1]+'" r="8" fill="#fff"/></svg>';
 document.getElementById("ch-s").innerHTML=svg;
 document.getElementById("ch-n").innerHTML='<span class="ch-big">'+fmt(sc/N)+'</span><span class="ch-pv">Previous <b>'+fmt(sp/N)+'</b></span>';
 var xs=[0,Math.round((N-1)/3),Math.round(2*(N-1)/3),N-1],xh="";
 xs.forEach(function(k){xh+="<span>"+new Date(start+k*864e5).toLocaleDateString([],{day:"numeric",month:"short"})+"</span>"});
 document.getElementById("ch-x").innerHTML=xh}
async function load(){
 try{
  var r=await api("/activity?select=created_at&created_at=gte."+encodeURIComponent(new Date(Date.now()-62*864e5).toISOString())+"&order=created_at.desc&limit=5000");
  var j=await r.json();
  if(Array.isArray(j)){rows=j;draw()}
 }catch(e){}}
function tick(){
 if(document.hidden)return;
 var c=mk();if(!c)return;
 if(!rows||Date.now()-lt>30000){lt=Date.now();load()}
 else if(!c.querySelector("svg"))draw()}
setInterval(tick,3000);setTimeout(tick,1500);
document.addEventListener("click",function(){setTimeout(tick,400)});
})();
/* ===== /ACT CHART JS ===== */
'''
i=s.rfind('</style>'); s=s[:i]+css+s[i:]
j=s.rfind('</script>'); s=s[:j]+js+s[j:]
open(f,'w',encoding='utf-8').write(s)
print('OK')
