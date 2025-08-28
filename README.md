

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  [![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org)

# Chaos Engineering & DR Automation

AWS FIS experiments, RTO checks, and dashboards.

## Run (pseudo)
```
terraform init && terraform apply
python rto_check.py
```

## Architecture
![Architecture](architecture.png)

## Environment
Copy `.env.template` to `.env` and fill secret keys.


## Detailed Architecture

Refer to `architecture_detailed.png` for the full high-level architecture and `*_detailed.drawio` for editable source.


## Polished Architecture

See `architecture_polished.png` for a polished diagram.

