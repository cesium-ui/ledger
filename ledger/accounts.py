from database import SessionLocal
from models import Account, Transaction
from decimal import Decimal
#accounts = [
#    {"id": 1,
#    "name": "Alice",
#    "currency": "INR",
#    "balance": 10000},
#    {"id": 2,
#    "name": "Bob",
#    "currency": "INR",
#    "balance": 5000
#    }
#]

def create_account(name: str,currency: str):
    db = SessionLocal()
    acc = Account(name=name,
    currency=currency,
    balance=Decimal("0.00"))
    try:
        db.add(acc)
        db.commit()
        db.refresh(acc)
    except:
        db.rollback()
        raise
    finally:
        db.close()
    return {
    "id": acc.id,
    "name": acc.name,
    "currency": acc.currency,
    "balance": acc.balance
}

def get_account(account_id: int):
    db = SessionLocal()
    try:
        a = db.query(Account).filter(Account.id == account_id).first()
        return a
    finally:
        db.close()

def get_all_accounts():
    db = SessionLocal()
    try:
        return db.query(Account).all()
    finally:
        db.close()

def withdraw(account_id: int,amount: Decimal):
    db = SessionLocal()
    try:
        a = db.query(Account).filter(Account.id == account_id).first()
        if a is None:
            return None
        a.balance -= amount
        db.commit()
        db.refresh(a)
    except:
        db.rollback()
        raise
    finally:
        db.close()
    return{
        "id": a.id,
        "name": a.name,
        "currency": a.currency,
        "balance": a.balance}

def deposit(account_id: int,amount: Decimal):
    db = SessionLocal()
    try:
        a = db.query(Account).filter(Account.id == account_id).first()
        if a is None:
            return None
        a.balance += amount
        db.commit()
        db.refresh(a)
    except:
        db.rollback()
        raise
    finally:
        db.close()
    return{
        "id": a.id,
        "name": a.name,
        "currency": a.currency,
        "balance": a.balance}

def transfer_account(from_id: int, to_id: int, amount: Decimal):
    db = SessionLocal()

    try:
        sender = db.query(Account).filter(Account.id == from_id).first()
        receiver = db.query(Account).filter(Account.id == to_id).first()

        if sender is None or receiver is None:
            return None

        if amount <= 0:
            raise ValueError("Invalid amount")

        if from_id == to_id:
            raise ValueError("Source and receiver cannot be the same")

        if sender.currency != receiver.currency:
            raise ValueError("Cannot transfer between different currencies")

        if sender.balance < amount:
            raise ValueError("Insufficient balance")

        sender.balance -= amount
        receiver.balance += amount

        transaction = Transaction(
            amount=amount,
            from_account=from_id,
            to_account=to_id,
            type="transfer"
        )

        db.add(transaction)
        db.commit()

        db.refresh(sender)
        db.refresh(receiver)

        return {
            "from_account": {
                "id": sender.id,
                "name": sender.name,
                "balance": sender.balance
            },
            "to_account": {
                "id": receiver.id,
                "name": receiver.name,
                "balance": receiver.balance
            }
        }

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()