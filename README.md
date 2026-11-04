# Ledger

A Stripe-inspired financial ledger system built with Python and FastAPI.

Ledger is a learning project focused on understanding backend development, REST APIs, and financial transaction systems.

## Current Features

* [x] FastAPI application setup
* [x] API health/status endpoint
* [x] Create accounts
* [x] Retrieve all accounts
* [x] Retrieve an account by ID
* [x] Deposit money into accounts
* [x] HTTP error handling and request validation
* [ ] Withdrawals
* [ ] Account-to-account transfers
* [ ] Double-entry bookkeeping
* [ ] Transaction history
* [ ] PostgreSQL integration
* [ ] Automated testing

## Tech Stack

* **Language:** Python
* **Framework:** FastAPI
* **Validation:** Pydantic
* **Server:** Uvicorn

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ledger.git
cd ledger
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the development server

```bash
uvicorn main:app --reload
```

### 4. Explore the API

Once the server is running:

* API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint                         | Description           |
| ------ | -------------------------------- | --------------------- |
| GET    | `/`                              | API information       |
| GET    | `/accounts`                      | Retrieve all accounts |
| POST   | `/addacc`                        | Create a new account  |
| GET    | `/accounts/{account_id}`         | Retrieve an account   |
| POST   | `/accounts/{account_id}/deposit` | Deposit money         |

## Current Limitations

This is an early-stage prototype.

* Account data is stored in memory.
* Data resets when the server restarts.
* Financial amounts currently use floating-point numbers.
* Transactions are not yet implemented using double-entry bookkeeping.
* No persistent database is connected.

These limitations will be addressed as development progresses.

## Project Roadmap

The long-term goal is to build a reliable financial ledger system incorporating:

1. Account management
2. Deposits and withdrawals
3. Account transfers
4. Double-entry bookkeeping
5. Transaction consistency and atomicity
6. Idempotency
7. PostgreSQL persistence
8. Automated testing
9. Concurrency control
10. Audit trails and reconciliation

## Status

**Version:** 0.1.0
**Development:** In Progress
