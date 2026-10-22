import re, shutil

shutil.copy("index.html", "index.html.before_sb")
shutil.copy("dashboard.html", "dashboard.html.before_sb")

NEW = r'''const SB="https://qnbiqgntqhzromwnmyth.supabase.co",KEY="sb_publishable_-jVYtd4Psza1wjuBe8g3CQ_kjxRB4lL";
const em=u=>u+"@abdi-app.com";
async function sbPost(path,body){
const r=await fetch(SB+path,{method:"POST",headers:{"apikey":KEY,"Content-Type":"application/json"},body:JSON.stringify(body)});
let j={};try{j=await r.json()}catch(e){}return{ok:r.ok,j:j}}
async function login(){
const u=$("lu").value.trim().toLowerCase(),p=$("lp").value;
if(!u||!p)return flash($("lb"),"Invalid Credentials!","bad",1600);
try{const r=await sbPost("/auth/v1/token?grant_type=password",{email:em(u),password:p});
if(r.ok&&r.j.access_token){
localStorage.setItem("abdi_tok",r.j.access_token);localStorage.setItem("abdi_ref",r.j.refresh_token||"");localStorage.setItem("abdi_cur",u);
flash($("lb"),"Welcome!","ok",700,enter)}
else flash($("lb"),"Invalid Credentials!","bad",1600)}
catch(e){flash($("lb"),"Network error","bad",1600)}}
async function register(){
const u=$("ru").value.trim().toLowerCase(),p=$("rp").value,c=$("rc").value.trim().toUpperCase();
if(!/^[a-z0-9._-]{3,20}$/.test(u))return flash($("rb"),"Username: 3-20 xaraf (a-z, 0-9)","bad",2000);
if(p.length<6)return flash($("rb"),"Password gaaban (6+)","bad",1600);
if(!c)return flash($("rb"),"Referral Code waajib","bad",1600);
try{const r=await sbPost("/auth/v1/signup",{email:em(u),password:p,data:{username:u,referral_code:c}});
if(r.ok){flash($("rb"),"Account Created!","ok",1200,()=>{$("lu").value=u;show("signin")})}
else{const m=String(r.j.msg||r.j.message||r.j.error_description||"");
flash($("rb"),/already|registered|exists/i.test(m)?"Username hore ayuu u jiray":"Referral Code khalad ama Username la qaatay","bad",2200)}}
catch(e){flash($("rb"),"Network error","bad",1600)}}
'''

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

c, n = re.subn(r'async function login\(\)\{.*?(?=function enter\(\))', lambda m: NEW, c, count=1, flags=re.S)
if n != 1:
    print("❌ login/register lama helin, waan joogsaday")
    raise SystemExit

old = 'localStorage.getItem("abdi_cur")?enter():show("welcome")'
if old in c:
    c = c.replace(old, 'localStorage.getItem("abdi_tok")&&localStorage.getItem("abdi_cur")?enter():show("welcome")')
else:
    print("⚠️ auto-login line lama helin")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("✅ index.html waxaa lagu xiray Supabase")

with open("dashboard.html", "r", encoding="utf-8") as f:
    d = f.read()
oldl = 'function logout(){localStorage.removeItem("abdi_cur");location.href="index.html"}'
if oldl in d:
    d = d.replace(oldl, 'function logout(){["abdi_cur","abdi_tok","abdi_ref"].forEach(k=>localStorage.removeItem(k));location.href="index.html"}')
    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(d)
    print("✅ Logout-ka dashboard waa la hagaajiyay")
else:
    print("⚠️ logout dashboard lama helin")
