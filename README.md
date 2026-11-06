# Ledger

A financial ledger backend built with **Python and FastAPI**.

### Features
- Account creation and retrieval
- Deposits and withdrawals
- Account-to-account transfers
- Balance and currency validation
- Transaction history
- Automated API testing with Pytest

### Tech Stack
Python · FastAPI · Pydantic · Uvicorn · Pytest

### Setup

```bash
git clone https://github.com/cesium-ui/ledger
cd Ledger

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload
```

API documentation: `http://127.0.0.1:8000/docs`

### Run Tests

```bash
python -m pytest -v
```

### Project Structure

```text
Ledger/
├── ledger/
├── tests/
├── main.py
├── routes.py
├── requirements.txt
└── README.md
```

### Status

`v0.1.0` — Educational prototype using in-memory storage. Not intended for production financial transactions.
