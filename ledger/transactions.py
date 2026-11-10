from database import SessionLocal
from models import Transaction
from decimal import Decimal


def get_transactions():
    db = SessionLocal()

    try:
        return db.query(Transaction).all()
    finally:
        db.close()


def create_transaction(
    amount: Decimal,
    from_account: int | None,
    to_account: int | None,
    transaction_type: str
):
    db = SessionLocal()

    transaction = Transaction(
        amount=amount,
        from_account=from_account,
        to_account=to_account,
        type=transaction_type
    )

    try:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return {
            "id": transaction.id,
            "type": transaction.type,
            "amount": transaction.amount,
            "from_account": transaction.from_account,
            "to_account": transaction.to_account
        }

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
