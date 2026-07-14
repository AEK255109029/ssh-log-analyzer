# SSH Log Analyzer

A Python-based security tool that analyzes SSH logs and detects failed login attempts.

## Features

- SSH failed login detection
- Attacker IP extraction
- Login attempt counting
- Risk level classification
- JSON report generation
- HTML report generation

## Technologies

- Python 3
- Linux
- journalctl
- Regex
- Colorama

## Installation

```bash
git clone https://github.com/USERNAME/ssh-log-analyzer.git
cd ssh-log-analyzer

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
