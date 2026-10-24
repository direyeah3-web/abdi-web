import os, json, secrets, time, urllib.request, urllib.parse, urllib.error
from datetime import datetime, timedelta, timezone

def load_env():
    if os.path.exists(".env"):
        for l in open(".env", encoding="utf-8"):
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
load_env()
TOKEN = os.environ.get("BOT_TOKEN", "")
SB = os.environ.get("SUPABASE_URL", "").rstrip("/")
SK = os.environ.get("SUPABASE_SERVICE_KEY", "")
ADMINS = {int(x) for x in os.environ.get("ADMIN_IDS", "").split(",") if x.strip().isdigit()}

def http(url, method="GET", data=None, headers=None):
    req = urllib.request.Request(url, method=method, headers=headers or {})
    if data is not None:
        req.data = json.dumps(data).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            body = r.read().decode()
            return r.status, (json.loads(body) if body else None)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()

def db(path, method="GET", data=None, prefer=None):
    h = {"apikey": SK, "Authorization": "Bearer " + SK}
    if prefer:
        h["Prefer"] = prefer
    s, b = http(SB + "/rest/v1" + path, method, data, h)
    if s >= 300:
        raise Exception("DB %s: %s" % (s, str(b)[:250]))
    return b

def tg(method, **p):
    s, b = http("https://api.telegram.org/bot%s/%s" % (TOKEN, method), "POST", p)
    return b if isinstance(b, dict) else {}

def send(chat, text, kb=None):
    p = {"chat_id": chat, "text": text, "parse_mode": "HTML"}
    if kb:
        p["reply_markup"] = {"inline_keyboard": kb}
    tg("sendMessage", **p)

def menu():
    return [[{"text": "1 day", "callback_data": "g:1"}, {"text": "7 days", "callback_data": "g:7"}, {"text": "30 days", "callback_data": "g:30"}],
            [{"text": "Last keys", "callback_data": "l"}, {"text": "Stats", "callback_data": "s"}]]

def schema():
    rows = db("/license_keys?select=*&limit=1")
    s = rows[0] if rows else {}
    def pick(c, d):
        for x in c:
            if x in s:
                return x
        return d
    return {
        "exp": pick(["expires_at", "expiry", "expires", "expire_at", "expiry_date", "expires_on"], "expires_at"),
        "dev": pick(["max_devices", "devices", "device_limit", "max_device"], "max_devices"),
        "bool": ("is_active" in s and "status" not in s)}

def gen_key():
    a = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "-".join("".join(secrets.choice(a) for _ in range(4)) for _ in range(4))

def log(msg):
    try:
        db("/activity", "POST", {"message": msg})
    except Exception:
        pass

def make(days, dev, qty):
    sc = schema()
    exp = (datetime.now(timezone.utc) + timedelta(days=days)).isoformat()
    rows = []
    for _ in range(qty):
        r = {"key": gen_key(), sc["exp"]: exp, sc["dev"]: dev}
        if sc["bool"]:
            r["is_active"] = True
        else:
            r["status"] = "active"
        rows.append(r)
    db("/license_keys", "POST", rows, "return=minimal")
    log("%d key cusub la sameeyay" % qty)
    return [r["key"] for r in rows], sc

def find(k):
    r = db("/license_keys?key=eq.%s&select=*" % urllib.parse.quote(k))
    return r[0] if r else None

def parse(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None

def is_on(k):
    return (k.get("status") == "active") if "status" in k else (k.get("is_active") is not False)

def state(k, sc):
    e = parse(k.get(sc["exp"]))
    if e and e < datetime.now(timezone.utc):
        return "🔴 expired"
    return "🟢 active" if is_on(k) else "⚪ inactive"

def info(k, sc):
    e = parse(k.get(sc["exp"]))
    return ("<code>%s</code>\nStatus: %s\nExpires: %s\nDevices: %s\nAssigned: %s" % (
        k["key"], state(k, sc), e.strftime("%d %b %Y") if e else "-",
        k.get(sc["dev"], "-"), "yes" if k.get("assigned_to") else "no"))

def set_state(key, on):
    sc = schema()
    body = {"is_active": on} if sc["bool"] else {"status": "active" if on else "inactive"}
    db("/license_keys?key=eq.%s" % urllib.parse.quote(key), "PATCH", body, "return=minimal")

def do_gen(chat, days, dev, qty):
    keys, sc = make(days, dev, qty)
    t = "✅ %d key(s) created · %d days · %d device(s)\n\n" % (qty, days, dev)
    send(chat, t + "\n".join("<code>%s</code>" % k for k in keys), menu())

def do_list(chat):
    sc = schema()
    rows = db("/license_keys?select=*&order=created_at.desc&limit=10")
    if not rows:
        return send(chat, "No keys yet.", menu())
    send(chat, "\n".join("%s  <code>%s</code>" % (state(k, sc).split()[0], k["key"]) for k in rows), menu())

def do_stats(chat):
    sc = schema()
    ks = db("/license_keys?select=*&limit=1000")
    now = datetime.now(timezone.utc)
    exp = [k for k in ks if parse(k.get(sc["exp"])) and parse(k.get(sc["exp"])) < now]
    act = [k for k in ks if is_on(k) and k not in exp]
    free = [k for k in ks if not k.get("assigned_to")]
    send(chat, "📊 <b>Stats</b>\nTotal: %d\nActive: %d\nExpired: %d\nUnassigned: %d" % (len(ks), len(act), len(exp), len(free)), menu())

HELP = ("🔑 <b>Abdi Key Bot</b>\n\n"
        "/gen [days] [devices] [qty] - create keys\n"
        "/keys - last 10 keys\n"
        "/key KEY - key info\n"
        "/on KEY - activate\n"
        "/off KEY - deactivate\n"
        "/del KEY - delete\n"
        "/stats - totals\n"
        "/myid - your Telegram ID")

def handle(chat, uid, text):
    p = text.split()
    if not p:
        return
    c = p[0].split("@")[0].lower()
    if c == "/myid":
        return send(chat, "Your ID: <code>%s</code>" % uid)
    if uid not in ADMINS:
        return send(chat, "⛔ Not authorized.")
    if c in ("/start", "/help"):
        return send(chat, HELP, menu())
    if c == "/gen":
        n = [int(x) for x in p[1:4] if x.isdigit()]
        days = n[0] if len(n) > 0 else 30
        dev = n[1] if len(n) > 1 else 1
        qty = n[2] if len(n) > 2 else 1
        days = max(1, min(days, 3650)); dev = max(1, min(dev, 100)); qty = max(1, min(qty, 50))
        return do_gen(chat, days, dev, qty)
    if c == "/keys":
        return do_list(chat)
    if c == "/stats":
        return do_stats(chat)
    if c in ("/key", "/on", "/off", "/del"):
        if len(p) < 2:
            return send(chat, "Usage: %s KEY" % c)
        key = p[1].upper()
        k = find(key)
        if not k:
            return send(chat, "❌ Key not found.")
        sc = schema()
        if c == "/key":
            return send(chat, info(k, sc))
        if c == "/on":
            set_state(key, True)
            return send(chat, "✅ Activated\n" + "<code>%s</code>" % key)
        if c == "/off":
            set_state(key, False)
            return send(chat, "⏸ Deactivated\n" + "<code>%s</code>" % key)
        return send(chat, "Delete <code>%s</code>?" % key,
                    [[{"text": "Yes, delete", "callback_data": "d:" + key}, {"text": "Cancel", "callback_data": "x"}]])
    send(chat, "Unknown command. /help")

def handle_cb(cb):
    chat = cb["message"]["chat"]["id"]
    uid = cb["from"]["id"]
    tg("answerCallbackQuery", callback_query_id=cb["id"])
    if uid not in ADMINS:
        return
    d = cb.get("data", "")
    if d.startswith("g:"):
        do_gen(chat, int(d[2:]), 1, 1)
    elif d == "l":
        do_list(chat)
    elif d == "s":
        do_stats(chat)
    elif d.startswith("d:"):
        db("/license_keys?key=eq.%s" % urllib.parse.quote(d[2:]), "DELETE", None, "return=minimal")
        log("Key la tirtiray")
        send(chat, "🗑 Deleted.")
    elif d == "x":
        send(chat, "Cancelled.")

def main():
    if not (TOKEN and SB and SK):
        print("❌ .env is incomplete")
        return
    print("✅ Bot running. Ctrl+C to stop.")
    off = 0
    while True:
        try:
            r = tg("getUpdates", offset=off, timeout=30)
            for u in r.get("result", []):
                off = u["update_id"] + 1
                try:
                    if "callback_query" in u:
                        handle_cb(u["callback_query"])
                    elif "message" in u and "text" in u["message"]:
                        m = u["message"]
                        handle(m["chat"]["id"], m["from"]["id"], m["text"])
                except Exception as e:
                    print("err:", e)
                    try:
                        chat = (u.get("message") or u["callback_query"]["message"])["chat"]["id"]
                        send(chat, "⚠️ Error: " + str(e)[:300])
                    except Exception:
                        pass
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("loop:", e)
            time.sleep(3)


import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
    def do_HEAD(self):
        self.send_response(200); self.end_headers()
    def log_message(self, *a):
        pass
def serve():
    HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "10000"))), H).serve_forever()
threading.Thread(target=serve, daemon=True).start()

main()
