s = open("bot.py", encoding="utf-8").read()
if "def do_extend" in s:
    print("⚠️ Hore ayaa loo daray")
    raise SystemExit

FUNCS = r'''import threading

def do_extend(chat, key, days):
    sc = schema()
    k = find(key)
    if not k:
        return send(chat, "❌ Key not found.")
    now = datetime.now(timezone.utc)
    e = parse(k.get(sc["exp"]))
    base = e if (e and e > now) else now
    new = base + timedelta(days=days)
    db("/license_keys?key=eq.%s" % urllib.parse.quote(key), "PATCH", {sc["exp"]: new.isoformat()}, "return=minimal")
    log("Key extended +%d days" % days)
    send(chat, "✅ Extended +%d days\n<code>%s</code>\nNew expiry: %s" % (days, key, new.strftime("%d %b %Y")))

def do_expiring(chat, days):
    sc = schema()
    ks = db("/license_keys?select=*&limit=1000")
    now = datetime.now(timezone.utc)
    rows = []
    for k in ks:
        e = parse(k.get(sc["exp"]))
        if e and is_on(k) and now < e <= now + timedelta(days=days):
            rows.append((e, k))
    rows.sort(key=lambda x: x[0])
    if not rows:
        return send(chat, "✅ No keys expiring within %d days." % days, menu())
    t = "⏰ <b>Expiring within %d days</b>\n\n" % days
    send(chat, t + "\n".join("<code>%s</code> · %s" % (k["key"], e.strftime("%d %b")) for e, k in rows[:30]), menu())

def do_expired(chat):
    sc = schema()
    ks = db("/license_keys?select=*&limit=1000")
    now = datetime.now(timezone.utc)
    rows = [k for k in ks if parse(k.get(sc["exp"])) and parse(k.get(sc["exp"])) < now]
    if not rows:
        return send(chat, "✅ No expired keys.", menu())
    send(chat, "🔴 <b>Expired keys (%d)</b>\n\n" % len(rows) + "\n".join("<code>%s</code>" % k["key"] for k in rows[:30]), menu())

def do_free(chat):
    sc = schema()
    ks = db("/license_keys?select=*&limit=1000")
    now = datetime.now(timezone.utc)
    rows = []
    for k in ks:
        e = parse(k.get(sc["exp"]))
        if not k.get("assigned_to") and is_on(k) and not (e and e < now):
            rows.append(k)
    if not rows:
        return send(chat, "No free keys.", menu())
    send(chat, "🟢 <b>Free keys (%d)</b>\n\n" % len(rows) + "\n".join("<code>%s</code>" % k["key"] for k in rows[:30]), menu())

ALERTED = set()

def alerts():
    time.sleep(30)
    while True:
        try:
            sc = schema()
            ks = db("/license_keys?select=*&limit=1000")
            now = datetime.now(timezone.utc)
            soon = []
            for k in ks:
                e = parse(k.get(sc["exp"]))
                if e and is_on(k) and now < e <= now + timedelta(days=2) and k["key"] not in ALERTED:
                    ALERTED.add(k["key"])
                    soon.append((e, k))
            if soon:
                t = "⏰ <b>Keys expiring within 2 days</b>\n\n" + "\n".join("<code>%s</code> · %s" % (k["key"], e.strftime("%d %b %H:%M")) for e, k in soon)
                for a in ADMINS:
                    send(a, t)
        except Exception as ex:
            print("alerts:", ex)
        time.sleep(3600)

'''

BRANCH = r'''    if c == "/extend":
        if len(p) < 3 or not p[2].isdigit():
            return send(chat, "Usage: /extend KEY DAYS\nExample: /extend ABCD-EFGH-IJKL-MNOP 30")
        return do_extend(chat, p[1].upper(), max(1, min(int(p[2]), 3650)))
    if c == "/expiring":
        return do_expiring(chat, int(p[1]) if len(p) > 1 and p[1].isdigit() else 7)
    if c == "/expired":
        return do_expired(chat)
    if c == "/free":
        return do_free(chat)
'''

def rep(src, old, new):
    if old not in src:
        print("❌ Lama helin:", old[:45])
        raise SystemExit
    return src.replace(old, new, 1)

s = rep(s, '"/stats - totals\\n"',
        '"/stats - totals\\n"\n        "/extend KEY DAYS - add days\\n"\n        "/expiring [days] - ending soon\\n"\n        "/expired - expired keys\\n"\n        "/free - unassigned keys\\n"')
s = rep(s, '{"text": "Stats", "callback_data": "s"}]]',
        '{"text": "Stats", "callback_data": "s"}],\n            [{"text": "Expiring", "callback_data": "e"}, {"text": "Free keys", "callback_data": "f"}]]')
s = rep(s, '    elif d == "s":\n        do_stats(chat)\n',
        '    elif d == "s":\n        do_stats(chat)\n    elif d == "e":\n        do_expiring(chat, 7)\n    elif d == "f":\n        do_free(chat)\n')
s = rep(s, '    if c == "/keys":\n        return do_list(chat)\n', BRANCH + '    if c == "/keys":\n        return do_list(chat)\n')
s = rep(s, 'HELP = (', FUNCS + 'HELP = (')
s = rep(s, '    print("✅ Bot running. Ctrl+C to stop.")',
        '    print("✅ Bot running. Ctrl+C to stop.")\n    threading.Thread(target=alerts, daemon=True).start()')
open("bot.py", "w", encoding="utf-8").write(s)
print("✅ La daray")
