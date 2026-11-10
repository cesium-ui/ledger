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

### Status
Educational project : currently focused on persistent storage and reliable financial transactions. Not intended for production use.