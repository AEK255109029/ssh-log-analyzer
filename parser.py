import subprocess
import re

def get_attackers():
    logs = subprocess.check_output(
        ["journalctl", "-u", "ssh"],
        text=True
    )

    attackers = {}

    for line in logs.split("\n"):
        if "Failed password" in line:
            ip = re.search(r"from ([\da-fA-F:]+)", line)

            if ip:
                ip = ip.group(1)
                attackers[ip] = attackers.get(ip, 0) + 1

    return attackers
