# Linux Health Check + Log Backup

A lightweight Linux automation project that generates system health reports and archives them.

## Features
- Generates timestamped system health reports
- Collects uptime, disk usage, memory usage, and load snapshot
- Archives latest report into a `.tar.gz` file
- Rotates old reports (keeps the last 7)

## Technologies Used
- Linux (Ubuntu)
- Python 3
- Bash
- Git & GitHub

## Project Structure

linux-healthcheck/
├── src/
│ └── healthcheck.py
├── scripts/
│ └── run.sh
├── reports/
│ └── .gitkeep
├── README.md
├── .gitignore

## Future Improvements
- Schedule the script using cron
- Add email or Slack alerts for threshold breaches
- Containerise the application with Docker
- Upload reports to cloud storage (e.g. AWS S3)

## Scheduling with cron
This project is designed to run automatically using cron.

Example: run every weekday at 9am
```bash
crontab -e
