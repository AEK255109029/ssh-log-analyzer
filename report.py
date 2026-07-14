from datetime import datetime
import json
import os


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

    print("\n✅ JSON raporu oluşturuldu.")


def save_html(attackers):

    report_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total = sum(attackers.values())
    unique_ips = len(attackers)

    if attackers:
        top_ip = max(attackers, key=attackers.get)
        top_count = attackers[top_ip]
    else:
        top_ip = "-"
        top_count = 0

    html = f"""
<html>
<head>
<title>SSH Log Analyzer Report</title>

<style>

body {{
    font-family: Arial;
    background:#202124;
    color:white;
    padding:30px;
}}

table {{
    border-collapse:collapse;
    width:70%;
}}

th, td {{
    border:1px solid #555;
    padding:10px;
    text-align:center;
}}

th {{
    background:#333;
}}

</style>

</head>

<body>

<h1>SSH Log Analyzer Report</h1>

<p><b>Report Time:</b> {report_time}</p>
<p><b>Total Failed Logins:</b> {total}</p>
<p><b>Unique IPs:</b> {unique_ips}</p>
<p><b>Top Attacker:</b> {top_ip} ({top_count} attempts)</p>

<hr>

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

    os.makedirs("reports", exist_ok=True)

    with open("reports/report.html", "w") as file:
        file.write(html)

    print("✅ HTML raporu oluşturuldu.")
