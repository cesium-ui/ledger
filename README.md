# Ledger

A Stripe-inspired financial ledger system built with Python and FastAPI.

Ledger is a learning project focused on backend development, REST APIs, and understanding how financial systems handle money movement.

The project is being developed incrementally, starting with basic account operations and gradually moving towards a more robust financial ledger.

Inspired by [Stripe Engineering — Ledger: Tracking and Validating Money Movement](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement).

## Features

- [x] FastAPI application setup
- [x] API health/status endpoint
- [x] Create accounts
- [x] Retrieve all accounts
- [x] Retrieve an account by ID
- [x] Deposit money
- [x] Withdraw money
- [x] Transfer money between accounts
- [x] Transaction history
- [x] Request validation and HTTP error handling
- [ ] Double-entry bookkeeping
- [ ] PostgreSQL integration
- [ ] Automated testing

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Building REST APIs |
| Pydantic | Request validation |
| Uvicorn | Running the development server |
| Git & GitHub | Version control |

## Getting Started

Follow these steps to run Ledger locally.

### Prerequisites

Make sure you have:

- Python 3.10 or newer
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/cesium-ui/ledger.git
cd ledger
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

The development server should now be running at:

`http://127.0.0.1:8000`

## API Documentation

Ledger uses FastAPI's automatically generated API documentation.

Once the server is running, visit:

| Resource | URL |
|---|---|
| API root | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

You can use Swagger UI to explore endpoints, provide request data, and test API operations directly from your browser.

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Get API information |
| GET | `/accounts` | Retrieve all accounts |
| POST | `/addacc` | Create a new account |
| GET | `/accounts/{account_id}` | Retrieve an account |
| POST | `/accounts/{account_id}/deposit` | Deposit money |
| POST | `/accounts/{account_id}/withdraw` | Withdraw money |
| POST | `/transfer` | Transfer money between accounts |
| GET | `/transactions` | Retrieve transaction history |

## Example Requests

### Create an account

`POST /addacc`

```json
{
  "name": "Alice",
  "currency": "INR"
}
```

### Deposit money

`POST /accounts/1/deposit`

```json
{
  "amount": 1000
}
```

### Withdraw money

`POST /accounts/1/withdraw`

```json
{
  "amount": 500
}
```

### Transfer money

`POST /transfer`

```json
{
  "from_account": 1,
  "to_account": 2,
  "amount": 500
}
```

## Project Structure

```text
Ledger/
├── ledger/
│   ├── __init__.py
│   ├── accounts.py
│   ├── engine.py
│   └── transactions.py
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Current Limitations

Ledger is currently an early-stage prototype.

- Data is stored in memory and resets when the server restarts.
- No database or persistent storage is connected yet.
- Financial amounts currently use floating-point numbers.
- Double-entry bookkeeping has not yet been implemented.
- Automated tests are not yet available.
- Production-level transaction atomicity and concurrency control are not implemented.

## Roadmap

- [x] Basic account management
- [x] Deposits and withdrawals
- [x] Account transfers
- [x] Transaction history
- [ ] Modular backend architecture
- [ ] Double-entry bookkeeping
- [ ] PostgreSQL integration
- [ ] Automated testing with Pytest
- [ ] Transaction atomicity and concurrency control
- [ ] Idempotency
- [ ] Audit trails and reconciliation

## Project Status

- **Version:** 0.1.0
- **Status:** Under active development
- **Purpose:** Learning and experimentation

---

Built as a hands-on exploration of backend engineering and financial infrastructure.
