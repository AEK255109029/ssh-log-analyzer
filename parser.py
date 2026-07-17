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

    for line in logs.split("\n"):

        if "Failed password" in line:

            ip_match = re.search(r"from ([\da-fA-F:.]+)", line)
            user_match = re.search(r"for (invalid user )?(\S+)", line)

            if ip_match:
                ip = ip_match.group(1)
                attackers[ip] = attackers.get(ip, 0) + 1

            if user_match:
                username = user_match.group(2)
                users[username] = users.get(username, 0) + 1

    return attackers, users
