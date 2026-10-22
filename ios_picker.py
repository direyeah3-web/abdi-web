import re, shutil
shutil.copy("dashboard.html", "dashboard.html.before_picker")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()

if "k-dbtn" in d:
    print("⚠️ Picker hore ayaa loogu daray. Waan joogsaday.")
    raise SystemExit

CSS = r'''.sel{width:100%;height:48px;margin-top:6px;border-radius:16px;border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--t);padding:0 14px;font-size:16px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;text-align:left;transition:.2s}
.sel:active{transform:scale(.98);border-color:var(--b)}.sel svg{color:var(--m)}
#sheet{position:fixed;inset:0;z-index:50;display:none;align-items:flex-end;justify-content:center;background:rgba(0,0,0,0);transition:background .3s}
#sheet.on{display:flex}#sheet.show{background:rgba(0,0,0,.55)}
#sheet .sh{width:100%;max-width:480px;margin:0 10px max(10px,env(safe-area-inset-bottom));transform:translateY(110%);transition:transform .4s cubic-bezier(.2,.9,.25,1)}
#sheet.show .sh{transform:none}
.sh .g{background:rgba(44,44,46,.85);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-radius:20px;overflow:hidden;margin-bottom:8px}
.sh .t{text-align:center;color:var(--m);font-size:13px;padding:14px}
.sh button{display:flex;width:100%;justify-content:space-between;align-items:center;padding:17px 22px;background:none;border:0;border-top:1px solid var(--line);color:var(--b);font-size:19px;cursor:pointer;font-family:inherit}
.sh button:active{background:rgba(255,255,255,.1)}.sh button.cur{font-weight:600}
</style>'''

old_sel = re.search(r'<label>Muddo<select id="k-days">.*?</select></label>', d, flags=re.S)
if not old_sel:
    print("❌ Select-ka Muddo lama helin, waan joogsaday")
    raise SystemExit

NEW_SEL = ('<label>Muddo<input type="hidden" id="k-days" value="30">'
           '<button type="button" class="sel" id="k-dbtn"><span id="k-dtxt">30 maalmood</span>'
           '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></button></label>')
d = d[:old_sel.start()] + NEW_SEL + d[old_sel.end():]

JS = r'''function pick(title,opts,cur){return new Promise(res=>{let s=$("sheet");if(!s){s=document.createElement("div");s.id="sheet";document.body.appendChild(s)}
s.innerHTML='<div class="sh"><div class="g"><div class="t">'+esc(title)+'</div>'+opts.map(o=>{const c=String(o[0])===String(cur);return '<button data-v="'+o[0]+'" class="'+(c?"cur":"")+'"><span>'+esc(o[1])+'</span><span>'+(c?"\u2713":"")+'</span></button>'}).join("")+'</div><div class="g"><button class="cl" style="justify-content:center;font-weight:600">Jooji</button></div></div>';
s.classList.add("on");requestAnimationFrame(()=>requestAnimationFrame(()=>s.classList.add("show")));
const done=v=>{s.classList.remove("show");setTimeout(()=>s.classList.remove("on"),380);res(v)};
s.onclick=e=>{const b=e.target.closest("button");if(b)done(b.classList.contains("cl")?null:b.dataset.v);else if(e.target===s)done(null)}})}
const DUR=[["0","Weligeed"],["1","1 maalin"],["7","7 maalmood"],["30","30 maalmood"],["90","90 maalmood"],["365","1 sano"]];
$("k-dbtn").onclick=async()=>{const v=await pick("Muddo",DUR,$("k-days").value);
if(v!==null){$("k-days").value=v;$("k-dtxt").textContent=DUR.find(x=>x[0]===v)[1]}};
$("k-gen").onclick=genKeys;'''

if "$(\"k-gen\").onclick=genKeys;" not in d:
    print("❌ k-gen handler lama helin, waan joogsaday")
    raise SystemExit
d = d.replace('$("k-gen").onclick=genKeys;', JS, 1)
d = d.replace("</style>", CSS, 1)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(d)
print("✅ iOS-style picker waa la dhisay")
