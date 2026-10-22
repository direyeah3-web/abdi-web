
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
