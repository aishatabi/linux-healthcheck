#!/usr/bin/env python3
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")

def run_cmd(cmd: list[str]) -> str:
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return out.strip()
    except subprocess.CalledProcessError as e:
        return f"ERROR running {' '.join(cmd)}:\n{e.output.strip()}"

def bytes_to_gb(b: int) -> str:
    return f"{b / (1024**3):.2f} GB"

def disk_summary() -> str:
    total, used, free = shutil.disk_usage("/")
    return (
        f"Disk (/):\n"
        f"  Total: {bytes_to_gb(total)}\n"
        f"  Used:  {bytes_to_gb(used)}\n"
        f"  Free:  {bytes_to_gb(free)}\n"
    )

def uptime_summary() -> str:
    return f"Uptime:\n  {run_cmd(['uptime'])}\n"

def memory_summary() -> str:
    # Works on Ubuntu via `free -h`
    return f"Memory:\n{run_cmd(['free', '-h'])}\n"

def cpu_load_summary() -> str:
    # Quick snapshot via `top` in batch mode
    return f"CPU/Load (top snapshot):\n{run_cmd(['top', '-b', '-n', '1'])[:800]}\n... (truncated)\n"

def rotate_reports(keep: int = 7) -> list[str]:
    files = sorted(REPORTS_DIR.glob("healthcheck_*.txt"), reverse=True)
    removed = []
    for f in files[keep:]:
        f.unlink(missing_ok=True)
        removed.append(f.name)
    return removed

def main():
    REPORTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = REPORTS_DIR / f"healthcheck_{timestamp}.txt"

    content = []
    content.append(f"Linux Health Check Report - {timestamp}\n")
    content.append("=" * 50 + "\n\n")
    content.append(uptime_summary() + "\n")
    content.append(disk_summary() + "\n")
    content.append(memory_summary() + "\n")
    content.append(cpu_load_summary() + "\n")

    report_path.write_text("".join(content), encoding="utf-8")

    removed = rotate_reports(keep=7)

    print(f"✅ Report saved: {report_path}")
    if removed:
        print(f"🧹 Rotated old reports: {', '.join(removed)}")

if __name__ == "__main__":
    main()
