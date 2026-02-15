# Linux Health Check + Log Backup

A lightweight Linux ops-style project that generates a system health report and archives it.

## Features
- Generates timestamped health reports (uptime, disk, memory, load snapshot)
- Stores reports in `/reports`
- Archives latest report into `.tar.gz`
- Rotates reports (keeps last 7)

## Requirements
- Linux (tested on Ubuntu)
- Python 3

## Run
```bash
./scripts/run.sh
