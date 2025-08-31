import requests, sys
try:
    r = requests.post("https://moulin-time-jimvix.fly.dev/debug/meter", timeout=5)
    print(r.text)
except Exception as e:
    sys.exit(f"meter failed: {e}")
