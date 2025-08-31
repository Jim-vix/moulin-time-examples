#!/usr/bin/env bash
set -euo pipefail
curl -s https://moulin-time-jimvix.fly.dev/status | jq .
