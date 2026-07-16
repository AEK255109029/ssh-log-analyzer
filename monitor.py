import subprocess
import re
from colorama import Fore, Style, init
from utils import get_risk

init(autoreset=True)


def live_monitor():

    print(Fore.CYAN + "=" * 40)
    print(Fore.CYAN + " LIVE SSH MONITOR")
    print(Fore.CYAN + "=" * 40)
    print("Monitoring started...")
    print("Press CTRL+C to stop.\n")

    process = subprocess.Popen(
        ["journalctl", "-u", "ssh", "-f"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    attackers = {}

    try:

        for line in process.stdout:

            if "Failed password" not in line:
                continue

            ip_match = re.search(r"from ([\\da-fA-F:.]+)", line)
            user_match = re.search(
                r"Failed password for (?:invalid user )?(\\S+)",
                line
            )

            ip = ip_match.group(1) if ip_match else "Unknown"
            user = user_match.group(1) if user_match else "Unknown"

            attackers[ip] = attackers.get(ip, 0) + 1
            count = attackers[ip]
            risk = get_risk(count)

            if risk == "HIGH":
                color = Fore.RED
            elif risk == "MEDIUM":
                color = Fore.YELLOW
            else:
                color = Fore.GREEN

            print(color + "=" * 40)
            print(color + f"User     : {user}")
            print(color + f"IP       : {ip}")
            print(color + f"Attempts : {count}")
            print(color + f"Risk     : {risk}")
            print(color + "=" * 40)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        process.terminate()
