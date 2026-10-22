import shutil
shutil.copy("dashboard.html", "dashboard.html.before_dock")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-dock" in d:
    print("⚠️ Dock hore ayaa loogu daray")
    raise SystemExit
if 'id="tab"' not in d or 'id="side"' not in d or END not in d:
    print("❌ #tab ama #side lama helin")
    raise SystemExit

# dami dock-kii hore ee khaldanaa
d = d.replace("setInterval(()=>{try{dock();ov()}", "setInterval(()=>{try{ov()}")

CSS = r'''/*abdi-dock*/
#side{display:none!important}
.ab-wrap{display:block!important;grid-template-columns:none!important}
#side~*:not(#tab){margin-left:0!important;width:100%!important;max-width:100%!important;box-sizing:border-box!important;padding-bottom:130px!important}
#tab{display:flex!important;flex-direction:row!important;position:fixed!important;left:10px!important;right:10px!important;top:auto!important;bottom:calc(10px + env(safe-area-inset-bottom,0px))!important;width:auto!important;height:auto!important;margin:0!important;padding:6px!important;gap:2px!important;border-radius:32px!important;z-index:9000!important;background:rgba(30,30,40,.55)!important;backdrop-filter:blur(34px) saturate(190%)!important;-webkit-backdrop-filter:blur(34px) saturate(190%)!important;border:1px solid rgba(255,255,255,.16)!important;box-shadow:0 14px 40px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.2)!important;overflow:hidden}
#tab>*{flex:1 1 0!important;min-width:0!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:3px!important;padding:8px 2px!important;margin:0!important;border:0!important;border-radius:24px!important;background:transparent!important;font-size:10px!important;font-weight:600!important;text-align:center;color:rgba(255,255,255,.6)!important;overflow:hidden;box-shadow:none!important}
#tab svg{width:22px!important;height:22px!important;margin:0!important}
#tab>.ab-on{background:rgba(255,255,255,.16)!important;color:#fff!important;box-shadow:inset 0 1px 0 rgba(255,255,255,.25)!important}
html.ab-light #tab{background:rgba(255,255,255,.6)!important}
'''

JS = r'''
(function(){
const t=document.getElementById("tab"),s=document.getElementById("side");
if(!t||!s)return;
s.parentElement.classList.add("ab-wrap");
function mark(el){Array.prototype.forEach.call(t.children,c=>c.classList.remove("ab-on"));if(el)el.classList.add("ab-on")}
t.addEventListener("click",e=>{let n=e.target;while(n&&n.parentElement!==t)n=n.parentElement;if(n)mark(n)});
setTimeout(()=>{
const cur=Array.prototype.find.call(t.children,c=>/(^|\s)(on|active|act|sel|cur)(\s|$)/.test(c.className))||t.children[0];
mark(cur);
},400);
})();
'''

d = d.replace("</style>", CSS + "</style>", 1)
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Dock waa la dhisay")
