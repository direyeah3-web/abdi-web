import shutil
import os

# ==========================================
# 1. QAYBTA CLOUDFLARE WORKER (Backend)
# ==========================================
worker_code = """
export default {
  async fetch(request, env) {
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, HEAD, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    const url = new URL(request.url);

    // 1. Abuurista Key-ga (Generate)
    if (url.pathname === '/generate' && request.method === 'POST') {
      try {
        const body = await request.json();
        const duration = body.duration; // Tusaale: '1 Day'
        const newKey = "ABDI-VIP-" + Math.random().toString(36).substring(2, 8).toUpperCase();
        
        let expiryDate = new Date();
        if (duration === '1 Day') expiryDate.setDate(expiryDate.getDate() + 1);
        else if (duration === '7 Days') expiryDate.setDate(expiryDate.getDate() + 7);
        else if (duration === '30 Days') expiryDate.setDate(expiryDate.getDate() + 30);
        else if (duration === '1 Year') expiryDate.setFullYear(expiryDate.getFullYear() + 1);

        // Kaydi KV (Database-ka Cloudflare)
        const keyData = {
            status: "unused",
            duration: duration,
            expiresAt: expiryDate.toISOString()
        };

        await env.MY_KEYS.put(newKey, JSON.stringify(keyData));

        return new Response(JSON.stringify({ status: true, key: newKey, expiresAt: expiryDate }), { 
            headers: { ...corsHeaders, "Content-Type": "application/json" } 
        });
      } catch (e) {
        return new Response(JSON.stringify({ status: false, error: e.message }), { headers: corsHeaders });
      }
    }

    // 2. Hubinta Key-ga (Verify) - Loader-ka ayaa wacaya
    if (url.pathname === '/verify' && request.method === 'POST') {
      try {
        const body = await request.json();
        const userKey = body.key;

        const keyDataStr = await env.MY_KEYS.get(userKey);
        
        if (!keyDataStr) {
            return new Response(JSON.stringify({ status: false, message: "Key not found" }), { headers: corsHeaders });
        }

        const keyData = JSON.parse(keyDataStr);
        
        // Hubi Expiry
        const now = new Date();
        const expiry = new Date(keyData.expiresAt);

        if (now > expiry) {
            return new Response(JSON.stringify({ status: false, message: "Key expired" }), { headers: corsHeaders });
        }

        return new Response(JSON.stringify({ status: true, message: "Key is valid", expiresAt: keyData.expiresAt }), { headers: corsHeaders });

      } catch (e) {
        return new Response(JSON.stringify({ status: false, error: e.message }), { headers: corsHeaders });
      }
    }

    return new Response(JSON.stringify({ status: false, reason: "Route not found" }), { headers: corsHeaders });
  }
};
"""

with open('cloudflare_worker.js', 'w', encoding='utf-8') as f:
    f.write(worker_code)

print("✅ cloudflare_worker.js waa la abuuray!")

# ==========================================
# 2. CUSBOONAYSII DASHBOARD-KA (Frontend)
# ==========================================
if os.path.exists('dashboard.html'):
    shutil.copy('dashboard.html', 'dashboard_real_keys_backup.html')
    
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # Waxaan u beddelaynaa generateKeys si uu ula xiriiro Worker-ka
    old_js = """
        function generateKeys() {
            const qty = parseInt(document.getElementById('key-quantity').value);
            let keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
            
            for (let i = 0; i < qty; i++) {
                const randomStr = Math.random().toString(36).substring(2, 8).toUpperCase();
                keys.push({
                    id: Date.now() + i,
                    key: `ABDI-VIP-${randomStr}`,
                    duration: selectedDuration,
                    status: 'unused',
                    date: new Date().toLocaleDateString()
                });
            }
            
            localStorage.setItem('abdi_keys', JSON.stringify(keys));
            closeModal();
            loadLicenses();
            showToast(`${qty} Key(s) generated successfully!`, 'success');
        }
    """

    new_js = """
        async function generateKeys() {
            const qty = parseInt(document.getElementById('key-quantity').value);
            const btn = document.querySelector('.modal-gen-btn');
            
            btn.innerText = "Generating...";
            btn.disabled = true;

            // HALKAN ku beddel link-ga Worker-kaaga cusub
            const workerUrl = 'https://YOUR_WORKER_URL.workers.dev/generate';

            try {
                for (let i = 0; i < qty; i++) {
                    const response = await fetch(workerUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ duration: selectedDuration })
                    });
                    
                    const data = await response.json();
                    
                    if (data.status) {
                        // Key-ga dhabta ah ee Worker-ka ka yimid ayaan kaydinaynaa
                        let keys = JSON.parse(localStorage.getItem('abdi_keys')) || [];
                        keys.push({
                            id: Date.now() + i,
                            key: data.key,
                            duration: selectedDuration,
                            status: 'unused',
                            date: new Date().toLocaleDateString()
                        });
                        localStorage.setItem('abdi_keys', JSON.stringify(keys));
                    }
                }
                
                closeModal();
                loadLicenses();
                showToast(`${qty} Key(s) generated successfully!`, 'success');
                
            } catch (error) {
                showToast('Failed to connect to Worker. Check URL.', 'error');
            } finally {
                btn.innerText = "GENERATE NOW";
                btn.disabled = false;
            }
        }
    """

    if old_js in c:
        c = c.replace(old_js, new_js)
        print("✅ Dashboard-ka waa lagu xidhay Worker-ka.")
    else:
        print("⚠️ Qoraalka JavaScript-ka lama helin. Waxaa laga yaabaa in koodhkaagu yara duwan yahay.")

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(c)
