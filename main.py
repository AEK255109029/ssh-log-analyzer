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

attackers = get_attackers(args.file)

print(Fore.CYAN + "=" * 35)
print(Fore.CYAN + "      SSH LOG ANALYZER")
print(Fore.CYAN + "=" * 35)

total = sum(attackers.values())

print(f"\nToplam Başarısız Giriş: {total}\n")

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
