from flask import Flask, render_template, send_file, request

from parser import get_attackers
from statistics import risk_summary, top_attackers, top_users

app = Flask(__name__)


@app.route("/")
def index():

    attackers, users = get_attackers()

    search = request.args.get("search", "").strip()

    if search:
        attackers = {
            ip: count
            for ip, count in attackers.items()
            if search.lower() in ip.lower()
        }

    total = sum(attackers.values())
    unique = len(attackers)

    summary = risk_summary(attackers)

    top_ips = top_attackers(attackers)
    top_user_list = top_users(users)

    # Grafik verileri
    labels = [ip for ip, _, _ in top_ips]
    values = [count for _, count, _ in top_ips]

    return render_template(
        "index.html",
        total=total,
        unique=unique,
        summary=summary,
        attackers=top_ips,
        users=top_user_list,
        labels=labels,
        values=values,
        search=search
    )


@app.route("/download/json")
def download_json():
    return send_file(
        "reports/report.json",
        as_attachment=True,
        download_name="report.json"
    )


@app.route("/download/html")
def download_html():
    return send_file(
        "reports/report.html",
        as_attachment=True,
        download_name="report.html"
    )


@app.route("/download/csv")
def download_csv():
    return send_file(
        "reports/report.csv",
        as_attachment=True,
        download_name="report.csv"
    )


@app.route("/health")
def health():
    return {
        "status": "running",
        "service": "SSH Log Analyzer Dashboard",
        "version": "2.2"
    }


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "index.html",
            total=0,
            unique=0,
            summary={
                "HIGH": 0,
                "MEDIUM": 0,
                "LOW": 0
            },
            attackers=[],
            users=[],
            labels=[],
            values=[],
            search=""
        ),
        404,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
