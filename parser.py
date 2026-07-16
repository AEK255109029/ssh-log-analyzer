import subprocess
import re


def get_attackers(logfile=None):

    if logfile:
        with open(logfile, "r") as file:
            logs = file.read()
    else:
        logs = subprocess.check_output(
            ["journalctl", "-u", "ssh"],
            text=True
        )

    attackers = {}
    users = {}

    for line in logs.splitlines():

        if "Failed password" in line:

            # IP adresini bul
            ip_match = re.search(r"from ([\da-fA-F:.]+)", line)
            if ip_match:
                ip = ip_match.group(1)
                attackers[ip] = attackers.get(ip, 0) + 1

            # Kullanıcı adını bul
            user_match = re.search(
                r"Failed password for (?:invalid user )?(\S+)",
                line
            )

            if user_match:
                user = user_match.group(1)
                users[user] = users.get(user, 0) + 1

    return attackers, users
