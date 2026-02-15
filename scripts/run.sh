#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

./src/healthcheck.py

latest_report=$(ls -t reports/healthcheck_*.txt | head -n 1)
archive_name="${latest_report%.txt}.tar.gz"

tar -czf "$archive_name" "$latest_report"

echo "📦 Archived: $archive_name"
