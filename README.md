# Moulin Time API — Examples

**Landing / Docs:** https://jim-vix.github.io/-moulin-time-site/  
**RapidAPI:** https://rapidapi.com/moulin-time-moulin-time-default/api/moulin-time-api  

Tiny, bot-friendly API for timezone & recurring events.  
**Base URL:** `https://moulin-time-jimvix.fly.dev`  
**Pricing:** Free tier — 1000 calls/month, then €0.0001 per call (metered via Stripe).

---

## Quick examples

### cURL
~~~bash
# Health
curl -s https://moulin-time-jimvix.fly.dev/status

# Meter event (billed via Stripe metering)
curl -s -X POST https://moulin-time-jimvix.fly.dev/debug/meter
~~~

### JavaScript (fetch, Node 18+)
~~~js
// health.js
const res = await fetch("https://moulin-time-jimvix.fly.dev/status");
console.log(await res.json());

// meter.js
await fetch("https://moulin-time-jimvix.fly.dev/debug/meter", { method: "POST" });
~~~

### Python (requests)
~~~python
# health.py
import requests
print(requests.get("https://moulin-time-jimvix.fly.dev/status", timeout=5).json())

# meter.py
import requests
requests.post("https://moulin-time-jimvix.fly.dev/debug/meter", timeout=5)
~~~

---

## Notes
- Free tier: **1000 calls/month**, then **€0.0001 / call** (metered via Stripe).
- No API key for now. Be polite with rate (sleep a bit between calls).
- Docs/Landing: https://jim-vix.github.io/-moulin-time-site/
- RapidAPI: https://rapidapi.com/moulin-time-moulin-time-default/api/moulin-time-api
<!-- EOF -->
