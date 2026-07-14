# 🔐 SSH Log Analyzer

A Python-based cybersecurity tool that analyzes SSH logs, detects failed login attempts, identifies attacker IP addresses, and generates security reports in JSON and HTML formats.

---

## ✨ Features

- 🔍 Detect failed SSH login attempts
- 🌐 Extract attacker IP addresses
- 📊 Count login attempts per IP
- ⚠️ Risk level classification (LOW / MEDIUM / HIGH)
- 📄 Generate JSON reports
- 🌍 Generate HTML reports
- 🎨 Colored terminal output

---

## 🛠 Technologies

- Python 3
- Linux
- journalctl
- Regular Expressions (Regex)
- Colorama

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/AEK255109029/ssh-log-analyzer.git
cd ssh-log-analyzer
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the analyzer:

```bash
python3 main.py
```

Generate JSON report:

```bash
python3 main.py --json
```

Generate HTML report:

```bash
python3 main.py --html
```

---

## 📸 Example Output

```text
===================================
        SSH LOG ANALYZER
===================================

Total Failed Logins: 2

IP: ::1
Attempts: 2
Risk: LOW
```

---

## 📁 Project Structure

```text
ssh-log-analyzer/
│
├── main.py
├── parser.py
├── report.py
├── reports/
│   ├── report.json
│   └── report.html
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 Future Improvements

- Brute Force Detection
- Live SSH Log Monitoring
- CSV Report Generation
- Graphical Statistics
- Web Dashboard (Flask)
- Email Alert System
- Support for `/var/log/auth.log`

---

## 👨‍💻 Author

**Ali Ekber Kartal**

GitHub: https://github.com/AEK255109029

---

## 📄 License

This project is licensed under the MIT License.
