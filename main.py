import argparse
from colorama import Fore, Style, init

from parser import get_attackers
from report import save_json, save_html, save_csv
from utils import get_risk
from monitor import live_monitor

init(autoreset=True)

parser = argparse.ArgumentParser(description="SSH Log Analyzer")

parser.add_argument(
    "--json",
    action="store_true",
    help="Generate JSON report"
)

parser.add_argument(
    "--html",
    action="store_true",
    help="Generate HTML report"
)

parser.add_argument(
    "--csv",
    action="store_true",
    help="Generate CSV report"
)

parser.add_argument(
    "--file",
    type=str,
    help="Analyze a custom log file"
)

parser.add_argument(
    "--live",
    action="store_true",
    help="Live SSH monitoring"
)

args = parser.parse_args()

# Live monitoring mode
if args.live:
    live_monitor()
    exit()

# Analyze logs
attackers, users = get_attackers(args.file)

print(Fore.CYAN + "=" * 45)
print(Fore.CYAN + "          SSH LOG ANALYZER")
print(Fore.CYAN + "=" * 45)

total = sum(attackers.values())
unique_ips = len(attackers)

print(f"\nTotal Failed Logins : {total}")
print(f"Unique IPs          : {unique_ips}")

# Attack Summary
print(Fore.CYAN + "\n===== Attack Summary =====")

if attackers:

    top_ip = max(attackers, key=attackers.get)
    top_count = attackers[top_ip]
    risk = get_risk(top_count)

    print(f"Top Attacker : {top_ip}")
    print(f"Attempts     : {top_count}")
    print(f"Risk         : {risk}")

else:
    print("No failed login attempts found.")

# Targeted Users
print(Fore.CYAN + "\n===== Targeted Users =====")

if users:

    for user, count in sorted(users.items(),
                              key=lambda x: x[1],
                              reverse=True):

        print(f"{user:<20} {count}")

else:
    print("No targeted users found.")

# Attacker List
print(Fore.CYAN + "\n===== Attacker IPs =====")

if attackers:

    for ip, count in sorted(attackers.items(),
                            key=lambda x: x[1],
                            reverse=True):

        risk = get_risk(count)

        if risk == "HIGH":
            color = Fore.RED
        elif risk == "MEDIUM":
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        print(color + f"IP       : {ip}")
        print(color + f"Attempts : {count}")
        print(color + f"Risk     : {risk}")
        print(Style.RESET_ALL + "-" * 45)

else:
    print("No attacker IPs found.")

# Reports
if args.json:
    save_json(attackers)

if args.html:
    save_html(attackers)

if args.csv:
    save_csv(attackers)
