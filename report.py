from datetime import datetime
import json
import os
import csv


def save_json(attackers):
    os.makedirs("reports", exist_ok=True)

    report = []

    for ip, count in attackers.items():
        report.append({
            "ip": ip,
            "failed_login": count,
            "risk": "HIGH" if count >= 5 else "MEDIUM" if count >= 3 else "LOW"
        })

    with open("reports/report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("✅ JSON raporu oluşturuldu.")


def save_html(attackers):
    os.makedirs("reports", exist_ok=True)

    report_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total = sum(attackers.values())
    unique_ips = len(attackers)

    html = f"""
    <html>
    <head>
        <title>SSH Log Report</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background: #333;
                color: white;
            }}
        </style>
    </head>
    <body>

    <h1>SSH Log Analyzer Report</h1>

    <p><b>Report Time:</b> {report_time}</p>
    <p><b>Total Failed Logins:</b> {total}</p>
    <p><b>Unique IPs:</b> {unique_ips}</p>

    <table>
        <tr>
            <th>IP</th>
            <th>Attempts</th>
            <th>Risk</th>
        </tr>
    """

    for ip, count in attackers.items():

        if count >= 5:
            risk = "HIGH"
        elif count >= 3:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        html += f"""
        <tr>
            <td>{ip}</td>
            <td>{count}</td>
            <td>{risk}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    with open("reports/report.html", "w") as file:
        file.write(html)

    print("✅ HTML raporu oluşturuldu.")


def save_csv(attackers):
    os.makedirs("reports", exist_ok=True)

    with open("reports/report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["IP", "Attempts", "Risk"])

        for ip, count in attackers.items():

            if count >= 5:
                risk = "HIGH"
            elif count >= 3:
                risk = "MEDIUM"
            else:
                risk = "LOW"

            writer.writerow([ip, count, risk])

    print("✅ CSV raporu oluşturuldu.")
