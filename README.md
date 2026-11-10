# Ledger

A financial ledger backend built with **Python, FastAPI, and SQLite**.

### Features
- Account creation and retrieval
- Deposits and withdrawals
- Account-to-account transfers
- Balance and currency validation
- Transaction history
- Persistent storage with SQLAlchemy
- Automated API tests with Pytest

### Tech Stack
Python · FastAPI · SQLAlchemy · SQLite · Pydantic · Pytest

### Setup

```bash
git clone https://github.com/cesium-ui/ledger.git
cd Ledger

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
python init_db.py
uvicorn main:app --reload
```

API documentation: http://127.0.0.1:8000/docs

### Run Tests

```bash
python -m pytest -v
```
### Inspiration

Inspired by Stripe Engineering's article:

[Ledger: Stripe’s system for tracking and validating money movement](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement) — Ilya Ganelin, February 2024.

This project is a simplified implementation inspired by the concepts discussed in the article.
