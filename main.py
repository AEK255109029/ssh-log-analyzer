import argparse
from parser import get_attackers
from report import save_json, save_html
from colorama import Fore, Style, init

init(autoreset=True)

parser = argparse.ArgumentParser(description="SSH Log Analyzer")

parser.add_argument(
    "--json",
    action="store_true",
    help="JSON raporu oluştur"
)

parser.add_argument(
    "--html",
    action="store_true",
    help="HTML raporu oluştur"
)

parser.add_argument(
    "--file",
    type=str,
    help="Analiz edilecek log dosyası"
)

args = parser.parse_args()

attackers, users = get_attackers(args.file)

print(Fore.CYAN + "=" * 35)
print(Fore.CYAN + "      SSH LOG ANALYZER")
print(Fore.CYAN + "=" * 35)

total = sum(attackers.values())
unique_ips = len(attackers)

print(f"\nToplam Başarısız Giriş: {total}")
print(f"Benzersiz IP Sayısı   : {unique_ips}\n")

if attackers:
    top_ip = max(attackers, key=attackers.get)
    top_count = attackers[top_ip]

    print(Fore.CYAN + "===== Attack Summary =====")
    print(f"Top Attacker : {top_ip}")
    print(f"Attempts     : {top_count}")

    if top_count >= 5:
        print(Fore.RED + "Status       : 🚨 BRUTE FORCE DETECTED")
    elif top_count >= 3:
        print(Fore.YELLOW + "Status       : Suspicious Activity")
    else:
        print(Fore.GREEN + "Status       : Normal")

    print(Fore.CYAN + "=" * 35)

print(Fore.CYAN + "\n===== Targeted Users =====\n")

for user, count in users.items():
    print(f"{user:<15} : {count} attempts")

print(Fore.CYAN + "=" * 35)

for ip, count in attackers.items():

    if count >= 5:
        color = Fore.RED
        risk = "HIGH"
    elif count >= 3:
        color = Fore.YELLOW
        risk = "MEDIUM"
    else:
        color = Fore.GREEN
        risk = "LOW"

    print(f"{color}IP: {ip}")
    print(f"{color}Deneme: {count}")
    print(f"{color}Risk: {risk}")
    print(Style.RESET_ALL + "-" * 35)

if args.json:
    save_json(attackers)

if args.html:
    save_html(attackers)






