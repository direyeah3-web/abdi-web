s = open("bot.py").read()
if "PORT" in s:
    print("⚠️ Hore ayaa loo daray")
    raise SystemExit
add = '''
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
'''
i = s.rstrip().rfind("main()")
s = s[:i] + add + "\n" + s[i:]
open("bot.py", "w").write(s)
print("✅ La daray")
