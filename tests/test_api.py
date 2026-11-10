from fastapi.testclient import TestClient
from main import app
import pytest
from ledger.transactions import get_transactions
from database import SessionLocal
from models import Account as DBAccount
from decimal import Decimal
from models import Transaction as DBTransaction

client = TestClient(app)

@pytest.fixture
def sample_data():
    return {
        "name": "Charlie",
        "currency": "INR"
    }

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "Ledger"

def test_get_account(reset_accounts):
    response = client.get("/accounts/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["currency"] == "INR"
    assert response.json()["balance"] == 10000

def test_create_account(sample_data,reset_accounts):
    response = client.post("/addacc",
    json=sample_data)
    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["name"] == "Charlie"
    assert response.json()["currency"] == "INR"
    assert response.json()["balance"] == 0

@pytest.fixture
def reset_accounts():
    db=SessionLocal()
    try:
        db.query(DBAccount).delete()
        db.add_all([
            DBAccount(
                name="Alice",
                currency="INR",
                balance=Decimal("10000.00")
            ),
            DBAccount(
                name="Bob",
                currency="INR",
                balance=Decimal("5000.00")
            )
        ])
        db.commit()
        yield
    finally:
        db.query(DBAccount).delete()
        db.commit()
        db.close()

@pytest.fixture
def reset_transactions():
    db = SessionLocal()

    try:
        db.query(DBTransaction).delete()
        db.commit()
        yield
    finally:
        db.query(DBTransaction).delete()
        db.commit()
        db.close()

def test_deposit(reset_accounts,reset_transactions):
    response = client.post("/accounts/1/deposit",
    json={"amount":500})
    assert response.status_code == 200
    assert response.json()["balance"] == 10500
    assert len(get_transactions()) == 1

def test_withdraw(reset_accounts, reset_transactions):
    response = client.post("/accounts/1/withdraw",
    json={"amount":500})
    assert response.status_code == 200
    assert response.json()["balance"] == 9500
    assert len(get_transactions()) == 1
    
def test_transfer(reset_accounts, reset_transactions):
    response = client.post("/transfer",
    json={"from_account": 1,
        "to_account": 2,
        "amount":500})
    alice = client.get("/accounts/1")
    bob = client.get("/accounts/2")
    assert response.status_code == 200
    assert alice.json()["balance"] == 9500
    assert bob.json()["balance"] == 5500
    assert len(get_transactions()) == 1
    

def test_get_transactions(reset_accounts, reset_transactions):
    client.post(
        "/accounts/1/deposit",
        json={"amount": 500}
    )
    response = client.get("/transactions")
    assert len(get_transactions()) == 1
    assert len(response.json()) == 1
    assert response.json()[0]["type"] == "deposit"
    assert response.json()[0]["amount"] == 500

def test_withdraw_insufficient_funds(reset_accounts, reset_transactions):
    response = client.post("/accounts/1/withdraw",
    json = {"amount":15000})
    alice = client.get("/accounts/1")
    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0

def test_deposit_invalid_amount(reset_accounts, reset_transactions):
    response = client.post("/accounts/1/deposit",
    json = {"amount":-500})
    alice = client.get("/accounts/1")
    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0

def test_deposit_zero_amount(reset_accounts, reset_transactions):
    response = client.post("/accounts/1/deposit",
    json = {"amount":0})
    alice = client.get("/accounts/1")
    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0

def test_transfer_insufficient_funds(reset_accounts, reset_transactions):
    response = client.post("/transfer",
    json={"from_account": 1,
        "to_account": 2,
        "amount":15000})
    alice = client.get("/accounts/1")
    bob = client.get("/accounts/2")
    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert bob.json()["balance"] == 5000
    assert len(get_transactions()) == 0

def test_transfer_same_account(reset_accounts, reset_transactions):
    response = client.post("/transfer",
    json={"from_account": 1,
        "to_account": 1,
        "amount":500})
    alice = client.get("/accounts/1")
    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0
    assert response.json()["detail"] == "Source and receiver cannot be the same"

def test_transfer_invalid_destination(reset_accounts, reset_transactions):
    response = client.post("/transfer", json={
        "from_account": 1,
        "to_account": 999,
        "amount": 500
    })

    alice = client.get("/accounts/1")

    assert response.status_code == 404
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0

def test_transfer_currency_mismatch(reset_accounts, reset_transactions):
    db = SessionLocal()

    alice = db.query(DBAccount).filter(DBAccount.id == 1).first()
    alice.currency = "USD"
    db.commit()
    db.close()

    response = client.post("/transfer", json={
        "from_account": 1,
        "to_account": 2,
        "amount": 500
    })

    alice = client.get("/accounts/1")
    bob = client.get("/accounts/2")

    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert bob.json()["balance"] == 5000
    assert len(get_transactions()) == 0

def test_withdraw_invalid_account(reset_accounts, reset_transactions):
    response = client.post(
        "/accounts/999/withdraw",
        json={"amount": 500}
    )

    assert response.status_code == 404
    assert len(get_transactions()) == 0

def test_withdraw_invalid_amount(reset_accounts, reset_transactions):
    response = client.post(
        "/accounts/1/withdraw",
        json={"amount": -500}
    )

    alice = client.get("/accounts/1")

    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0

def test_withdraw_zero_amount(reset_accounts, reset_transactions):
    response = client.post(
        "/accounts/1/withdraw",
        json={"amount": 0}
    )

    alice = client.get("/accounts/1")

    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert len(get_transactions()) == 0

def test_deposit_invalid_account(reset_accounts, reset_transactions):
    response = client.post(
        "/accounts/999/deposit",
        json={"amount": 500}
    )

    assert response.status_code == 404
    assert len(get_transactions()) == 0

def test_transfer_invalid_amount(reset_accounts, reset_transactions):
    response = client.post("/transfer", json={
        "from_account": 1,
        "to_account": 2,
        "amount": -500
    })

    alice = client.get("/accounts/1")
    bob = client.get("/accounts/2")

    assert response.status_code == 400
    assert alice.json()["balance"] == 10000
    assert bob.json()["balance"] == 5000
    assert len(get_transactions()) == 0