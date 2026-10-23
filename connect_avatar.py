import shutil, os
shutil.copy("dashboard.html", "dashboard.html.before_avatar")
with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
END = "</script></body></html>"
if "abdi-avatar" in d:
    print("⚠️ Hore ayaa loogu daray")
    raise SystemExit
if not os.path.exists("xero.png"):
    print("❌ xero.png ma jiro folderka abdi-web")
    raise SystemExit
if END not in d or "</style>" not in d:
    print("❌ dashboard.html qaab lama filayo")
    raise SystemExit

CSS = r'''/*abdi-avatar*/
.ab-av{background:url(xero.png) center/cover no-repeat #000!important;font-size:0!important;color:transparent!important;border:2px solid rgba(255,255,255,.18)!important;box-shadow:0 0 0 1px rgba(0,0,0,.6)!important;overflow:hidden}
'''
JS = r'''
(function(){
function fix(){
 var a=document.querySelectorAll("*");
 for(var i=0;i<a.length;i++){
  var e=a[i];
  if(e.children.length||e.classList.contains("ab-av"))continue;
  if(e.textContent.trim()!=="A")continue;
  var r=e.getBoundingClientRect();
  if(r.width>=24&&r.width<=70&&r.top<260){e.classList.add("ab-av");return}
 }
}
setInterval(fix,800);fix();
})();
'''
i = d.rfind("</style>")
d = d[:i] + CSS + d[i:]
d = d.replace(END, JS + END)
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ Avatar waa la dhisay")
