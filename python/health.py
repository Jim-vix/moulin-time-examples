import requests, sys
try:
    r = requests.get("https://moulin-time-jimvix.fly.dev/status", timeout=5)
    print(r.json())
except Exception as e:
    sys.exit(f"health failed: {e}")
