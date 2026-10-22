import shutil
shutil.copy("dashboard.html", "dashboard.html.before_theme")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-theme" in d:
    print("⚠️ Theme hore ayaa loogu daray")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = r'''/*abdi-theme*/
:root{--ios:#0a84ff;--ios2:#5ac8fa;--glass:rgba(255,255,255,.07)}
html,body{font-family:-apple-system,"SF Pro Display","SF Pro Text",system-ui,Roboto,sans-serif!important;-webkit-font-smoothing:antialiased;-webkit-tap-highlight-color:transparent}
body{background:radial-gradient(900px 500px at 85% -10%,rgba(10,132,255,.28),transparent 60%),radial-gradient(700px 500px at -10% 110%,rgba(191,90,242,.22),transparent 60%),#000!important;background-attachment:fixed!important}
aside,nav,.side,.sidebar,.sb{background:rgba(20,20,26,.55)!important;backdrop-filter:blur(30px) saturate(180%);-webkit-backdrop-filter:blur(30px) saturate(180%);border-color:rgba(255,255,255,.08)!important}
.card{background:linear-gradient(145deg,rgba(255,255,255,.10),rgba(255,255,255,.03))!important;backdrop-filter:blur(26px) saturate(180%);-webkit-backdrop-filter:blur(26px) saturate(180%);border:1px solid rgba(255,255,255,.13)!important;border-radius:26px!important;box-shadow:0 12px 32px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.14)}
.an-s{background:linear-gradient(145deg,rgba(255,255,255,.10),rgba(255,255,255,.03))!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:22px!important;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);box-shadow:inset 0 1px 0 rgba(255,255,255,.12)}
.an-s b{background:linear-gradient(180deg,#fff,#9fd0ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.an-b i{background:linear-gradient(180deg,#5ac8fa,#0a84ff)!important;box-shadow:0 0 16px rgba(10,132,255,.7);border-radius:8px 8px 3px 3px!important}
button,.chip,select,input,a,[data-a]{transition:transform .22s cubic-bezier(.3,1.7,.5,1),filter .2s,box-shadow .25s,background .25s;-webkit-tap-highlight-color:transparent}
button:active,.chip:active,[data-a]:active{transform:scale(.93)!important;filter:brightness(1.25)}
button{border-radius:16px}
.st-b,button[class*=pri],button[class*=gen],button[class*=btn]:not(.dg){background:linear-gradient(180deg,#3aa0ff,#0a84ff)!important;color:#fff!important;box-shadow:0 8px 22px rgba(10,132,255,.45),inset 0 1px 0 rgba(255,255,255,.35)}
.st-d,.dg{background:linear-gradient(180deg,#ff6a60,#ff453a)!important;color:#fff!important;box-shadow:0 8px 22px rgba(255,69,58,.4),inset 0 1px 0 rgba(255,255,255,.3)}
input,select,textarea{background:rgba(255,255,255,.07)!important;border:1px solid rgba(255,255,255,.12)!important;border-radius:16px!important;color:#fff}
input:focus,select:focus,textarea:focus{outline:0!important;border-color:var(--ios)!important;box-shadow:0 0 0 4px rgba(10,132,255,.28)!important}
.bd{border-radius:999px!important;backdrop-filter:blur(10px);font-weight:600}
.chip{border-radius:999px!important;background:rgba(255,255,255,.09)!important;backdrop-filter:blur(10px)}
.view{animation:abIn .5s cubic-bezier(.2,.9,.2,1) both}
.card{animation:abIn .55s cubic-bezier(.2,.9,.2,1) both}
@keyframes abIn{from{opacity:0;transform:translateY(16px) scale(.97)}to{opacity:1;transform:none}}
h1,h2{letter-spacing:-.02em}
::-webkit-scrollbar{width:0;height:0}
#ab-snd{position:fixed;right:14px;bottom:calc(14px + env(safe-area-inset-bottom,0px));width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.18);background:rgba(30,30,36,.6);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);color:#fff;font-size:20px;z-index:9999;box-shadow:0 8px 24px rgba(0,0,0,.5)}
'''

JS = r'''
(function(){
const AC=window.AudioContext||window.webkitAudioContext;let ctx=null;
const on=()=>{try{return localStorage.getItem("abdi_snd")!=="0"}catch(e){return true}};
function tone(f1,f2,dur,vol,type,delay){
if(!on()||!AC)return;
try{
if(!ctx)ctx=new AC();
if(ctx.state==="suspended")ctx.resume();
const t=ctx.currentTime+(delay||0),o=ctx.createOscillator(),g=ctx.createGain();
o.type=type||"sine";o.frequency.setValueAtTime(f1,t);o.frequency.exponentialRampToValueAtTime(f2,t+dur);
g.gain.setValueAtTime(0.0001,t);g.gain.exponentialRampToValueAtTime(vol,t+.008);g.gain.exponentialRampToValueAtTime(0.0001,t+dur);
o.connect(g);g.connect(ctx.destination);o.start(t);o.stop(t+dur+.02);
}catch(e){}}
const tick=()=>{tone(1500,900,.05,.07,"sine");try{on()&&navigator.vibrate&&navigator.vibrate(7)}catch(e){}};
const good=()=>{tone(660,660,.12,.07,"sine");tone(990,990,.18,.07,"sine",.09)};
const SEL="button,a,select,input,.chip,[data-a],[data-v],li,nav div,aside div,.nav *";
document.addEventListener("pointerdown",e=>{const t=e.target.closest&&e.target.closest(SEL);if(t&&t.id!=="ab-snd")tick()},true);
try{const _t=toast;toast=function(){good();return _t.apply(this,arguments)}}catch(e){}
const b=document.createElement("button");b.id="ab-snd";
const set=()=>{b.textContent=on()?"🔊":"🔇"};set();
b.onclick=()=>{try{localStorage.setItem("abdi_snd",on()?"0":"1")}catch(e){}set();if(on())good()};
document.body.appendChild(b);
})();
'''

d = d.replace("</style>", CSS + "</style>", 1)
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Theme waa la dhisay")
