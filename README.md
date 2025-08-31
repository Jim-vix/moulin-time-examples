# Moulin Time API — Examples

**Landing / Docs:** https://jim-vix.github.io/-moulin-time-site/  
**RapidAPI:** https://rapidapi.com/moulin-time-moulin-time-default/api/moulin-time-api  

Tiny, bot-friendly API for timezone & recurring events.  
**Base URL:** `https://moulin-time-jimvix.fly.dev`

---

## Quick examples

### cURL
```bash
# Health
curl -s https://moulin-time-jimvix.fly.dev/status

# Meter event (billed via Stripe metering)
curl -s -X POST https://moulin-time-jimvix.fly.dev/debug/meter
- Docs/Landing: https://jim-vix.github.io/-moulin-time-site/
- RapidAPI: https://rapidapi.com/moulin-time-moulin-time-default/api/moulin-time-api
