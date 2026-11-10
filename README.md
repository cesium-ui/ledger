# Ledger

A financial ledger backend built with **Python, FastAPI, and SQLite**.

Ledger is an educational backend project focused on account management, financial transactions, data persistence, and maintaining accurate account balances.

## Features

- Create and retrieve accounts
- Deposit and withdraw funds
- Transfer funds between accounts
- Account balance and currency validation
- Transaction history
- Persistent storage using SQLite
- SQLAlchemy ORM for database operations
- Atomic account-to-account transfers
- Automated API tests using Pytest

## Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Testing:** Pytest
- **Server:** Uvicorn

## Project Structure

```text
Ledger/
├── ledger/
│   ├── accounts.py
│   ├── transactions.py
│   └── engine.py
├── tests/
│   ├── test_api.py
│   └── test_ledger.py
├── main.py
├── routes.py
├── database.py
├── models.py
├── init_db.py
├── seed.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/cesium-ui/ledger.git
cd Ledger
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python init_db.py
```

### 5. Start the server

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## Running Tests

```bash
python -m pytest -v
```

## Database

Ledger uses SQLite for persistent data storage and SQLAlchemy as its ORM.

The database contains:

- **Accounts:** Stores account information, currency, and balances.
- **Transactions:** Records deposits, withdrawals, and transfers.

The database is stored locally in `ledger.db`.

## Project Status

**Version:** 0.2.0

Ledger is an ongoing educational project. The current implementation focuses on persistent storage and reliable financial transaction handling.

Planned improvements include double-entry bookkeeping, stronger transaction integrity, and expanded financial correctness tests.

**Note:** This project is a learning prototype and is not intended for production financial use.